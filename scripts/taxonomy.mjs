// Shared by the generator and the plain-Node MCP server.
export function flattenCategories(categories, parent = '') {
  return categories.flatMap(node => {
    const path = parent ? `${parent}/${node.id}` : node.id;
    return [{ ...node, path, parent }, ...flattenCategories(node.subcategories ?? [], path)];
  });
}

export const withinClassification = (path, ancestor) => path === ancestor || path.startsWith(`${ancestor}/`);

export function serviceClassifications(service) {
  return service.catalog?.classifications?.length ? service.catalog.classifications : [service.category];
}

export function inClassification(service, path) {
  return serviceClassifications(service).some(value => withinClassification(value, path));
}

export function classificationLabel(categories, path, zh = false) {
  const nodes = flattenCategories(categories);
  return path.split('/').map((id, index, parts) => {
    const node = nodes.find(n => n.path === parts.slice(0, index + 1).join('/'));
    return node ? (zh ? node.name_zh ?? node.name : node.name) : id;
  }).join(' / ');
}

export function classificationCapabilities(categories, path, descendants = false) {
  return flattenCategories(categories)
    .filter(node => withinClassification(path, node.path) || (descendants && withinClassification(node.path, path)))
    .flatMap(node => node.capabilities ?? []);
}
