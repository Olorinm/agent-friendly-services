// Offline checks against the saved task; this does not verify payable prices,
// market completeness, operating carriers or inventory with an airline.
// Usage: node scripts/verify-flight-smoke.mjs <run.json> [<run.json> ...]
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as yaml from 'js-yaml';

export function checkOffer(offer, input) {
  const tripIssues = [], quoteIssues = [];
  const check = (ok, issue) => { if (!ok) tripIssues.push(issue); };
  check(input.origin_airports.includes(offer.origin), 'origin');
  check(offer.destination === input.destination_airport, 'destination');
  check(offer.stops === input.max_stops, 'stops');
  check(offer.cabin?.toLowerCase() === input.cabin, 'cabin');
  check(typeof offer.flight === 'string' && offer.flight.length > 0, 'flight_number');
  const local = value => typeof value === 'string' && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$/.test(value);
  check(local(offer.departure) && offer.departure.slice(0, 10) === input.departure_date, 'departure_date');
  check(local(offer.arrival) && offer.arrival.slice(0, 10) === input.departure_date, 'arrival_date');
  check(local(offer.departure) && offer.departure.slice(11) >= `${input.departure_local.from}:00`
    && offer.departure.slice(11) < `${input.departure_local.until}:00`, 'departure_window');
  check(local(offer.arrival) && offer.arrival.slice(11) < `${input.arrival_local_before}:00`
    && offer.arrival > offer.departure, 'arrival_window');
  if (offer.currency !== input.currency) quoteIssues.push('currency');
  if (!(typeof offer.price === 'number' && Number.isFinite(offer.price) && offer.price > 0)) quoteIssues.push('price');
  for (const key of ['adults', 'children', 'infants']) {
    if (offer.passengers?.[key] !== input[key]) quoteIssues.push(`unconfirmed_${key}`);
  }
  return { ...offer, trip_issues: tripIssues, quote_issues: quoteIssues,
    flight_details_match: tripIssues.length === 0, quote_conditions_match: quoteIssues.length === 0 };
}

export function verifyRun(run, fallbackTask = undefined) {
  const task = run.task ?? fallbackTask;
  if (!task || task.id !== run.task_id) throw new Error('Task identity missing or mismatched');
  if (!['kiwi', 'ignav'].includes(run.service)) throw new Error('Unsupported response format');
  return { task_id: task.id, service: run.service, route: run.route,
    assurance: 'saved-response checks only; not a payable-price or market-coverage pass',
    calls: run.calls.map(call => {
      const kiwi = run.service === 'kiwi';
      const body = kiwi ? call.response?.structuredContent : call.response;
      if (call.error || call.response?.isError || body?.error || !Array.isArray(body?.itineraries)) {
        return { status: 'error_or_missing_response', error: call.error ?? body?.error ?? 'Missing usable response' };
      }
      const offers = body.itineraries.map(itinerary => {
        const segments = itinerary.outbound?.segments ?? [];
        const first = segments[0], last = segments.at(-1);
        const offer = kiwi ? {
          flight: first?.flightNumber, origin: first?.from, destination: last?.to,
          departure: first?.departureTime, arrival: last?.arrivalTime,
          cabin: itinerary.outbound?.cabinClass, stops: segments.length - 1,
          passengers: body.passengers, price: itinerary.price, currency: body.currency,
        } : {
          flight: first?.marketing_carrier_code && first?.flight_number
            ? first.marketing_carrier_code + first.flight_number : null,
          origin: first?.departure_airport, destination: last?.arrival_airport,
          departure: first?.departure_time_local, arrival: last?.arrival_time_local,
          cabin: itinerary.cabin_class, stops: segments.length - 1,
          passengers: null, price: itinerary.price?.amount, currency: itinerary.price?.currency,
        };
        return checkOffer(offer, task.inputs);
      });
      return { started_at: call.started_at, elapsed_ms: call.elapsed_ms,
        origin: call.arguments?.flyFrom ?? call.request?.origin,
        status: offers.length ? 'offers_inspected' : 'no_offers_returned_unverified', offers,
        matching_flight_details: offers.filter(o => o.flight_details_match).length,
        matching_quote_conditions: offers.filter(o => o.flight_details_match && o.quote_conditions_match).length };
    }) };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  const task = yaml.load(fs.readFileSync(path.join(root, 'data/experiments/tasks/travel-flights.yaml'), 'utf8'));
  if (process.argv.length < 3) throw new Error('Provide one or more saved run JSON files; no network requests are made.');
  for (const file of process.argv.slice(2)) {
    const result = verifyRun(JSON.parse(fs.readFileSync(file, 'utf8')), task);
    console.log(JSON.stringify({ file, ...result }, null, 2));
  }
}
