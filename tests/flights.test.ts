import test from 'node:test';
import assert from 'node:assert/strict';
import { checkOffer, verifyRun } from '../scripts/verify-flight-smoke.mjs';

const input = { origin_airports: ['PEK', 'PKX'], destination_airport: 'YNT',
  departure_date: '2026-09-25', max_stops: 0, cabin: 'economy',
  departure_local: { from: '08:00', until: '12:00' }, arrival_local_before: '14:00',
  currency: 'CNY', adults: 2, children: 0, infants: 0 };
const offer = { origin: 'PEK', destination: 'YNT', flight: 'TEST123',
  departure: '2026-09-25T08:00:00', arrival: '2026-09-25T09:00:00', stops: 0,
  cabin: 'economy', passengers: { adults: 2, children: 0, infants: 0 }, price: 1000, currency: 'CNY' };

test('flight checks enforce exclusive noon/arrival boundaries and the requested date', () => {
  assert.equal(checkOffer(offer, input).flight_details_match, true);
  for (const patch of [
    { departure: '2026-09-25T12:00:00', arrival: '2026-09-25T13:00:00' },
    { arrival: '2026-09-25T14:00:00' },
    { departure: '2026-09-26T08:00:00', arrival: '2026-09-26T09:00:00' },
    { departure: undefined }, { stops: 1 }, { cabin: 'business' },
  ]) assert.equal(checkOffer({ ...offer, ...patch }, input).flight_details_match, false);
});

test('valid flight details cannot hide wrong currency or unconfirmed passenger count', () => {
  const checked = checkOffer({ ...offer, passengers: null, currency: 'USD' }, input);
  assert.equal(checked.flight_details_match, true);
  assert.equal(checked.quote_conditions_match, false);
  assert(checked.quote_issues.includes('currency'));
  assert(checked.quote_issues.includes('unconfirmed_adults'));
});

test('an empty or error response cannot become a task pass', () => {
  const task = { id: 'synthetic', inputs: input };
  const run = { task_id: task.id, service: 'kiwi', route: 'search-mcp', task,
    calls: [{ response: { structuredContent: { itineraries: [] } } },
      { response: { isError: true, structuredContent: { itineraries: [] } } }] };
  assert.equal(verifyRun(run).calls[0].status, 'no_offers_returned_unverified');
  assert.equal(verifyRun(run).calls[1].status, 'error_or_missing_response');
});
