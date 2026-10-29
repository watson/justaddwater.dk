/* Local filtering of the public, server-rendered migration record. */
(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const matches = (row, input) => input.value.toLocaleLowerCase().trim().split(/\s+/)
    .every(term => row.dataset.search.includes(term));
  const filter = (selector, predicate, countId, emptyId, noun) => {
    const rows = [...document.querySelectorAll(selector)];
    let count = 0;
    for (const row of rows) {
      row.hidden = !predicate(row);
      if (!row.hidden) count++;
    }
    byId(countId).textContent = `${count} of ${rows.length} ${noun} shown`;
    byId(emptyId).hidden = count !== 0;
  };
  const update = () => {
    filter('.change', row => matches(row, byId('change-query')) &&
      (!byId('change-kind').value || row.dataset.categories.split(' ').includes(byId('change-kind').value)) &&
      (byId('shared-changes').checked || row.dataset.shared !== 'true'), 'change-count', 'changes-empty', 'changes');
    filter('.page-row', row => matches(row, byId('page-query')) &&
      (byId('page-copies').checked || row.dataset.primary === 'true'), 'page-count', 'pages-empty', 'pages');
    filter('.resource', row => matches(row, byId('resource-query')) &&
      (!byId('resource-kind').value || row.dataset.kind === byId('resource-kind').value), 'resource-count', 'resources-empty', 'resources');
  };
  for (const input of document.querySelectorAll('.filters input,.filters select')) {
    input.addEventListener('input', update);
    input.addEventListener('change', update);
  }
  const reveal = () => {
    const target = byId(decodeURIComponent(location.hash.slice(1)));
    if (!target) return;
    if (target.hidden) {
      for (const input of document.querySelectorAll('.filters input[type=search],.filters select')) input.value = '';
      byId('shared-changes').checked = true;
      update();
    }
    if (target.tagName === 'DETAILS') target.open = true;
    target.scrollIntoView({block:'start'});
  };
  window.addEventListener('hashchange', reveal);
  update();
  if (location.hash) reveal();
})();
