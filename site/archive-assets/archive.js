/* Static archive navigation and local search; no analytics or network services. */
(() => {
  'use strict';
  const root = new URL('../', document.currentScript.src);
  const local = (path) => new URL(path.replace(/^\//, ''), root);
  const params = new URLSearchParams(location.search);
  const legacyID = params.get('p') || params.get('page_id') || params.get('attachment_id');

  if (legacyID) {
    fetch(local('/archive-assets/routes.json'))
      .then((response) => response.json())
      .then((routes) => {
        if (routes[legacyID]) {
          const destination = local(routes[legacyID]);
          destination.hash = location.hash;
          location.replace(destination);
        }
      })
      .catch(() => {});
  }

  const footer = document.querySelector('#footer');
  if (footer) {
    const note = document.createElement('p');
    note.className = 'archive-note archive-footer-note';
    note.append('Static archive · ');
    const link = document.createElement('a');
    link.href = local('/search/');
    link.textContent = 'Search the archive';
    note.append(link);
    // Keep the original footer's fixed-height background intact. The archive
    // note sits on the surrounding page background, outside the theme panel.
    (document.getElementById('page') || footer).after(note);
  }

  const query = params.get('s') || '';
  const input = document.getElementById('archive-query');
  if (!input && query) {
    const destination = local('/search/');
    destination.searchParams.set('s', query);
    location.replace(destination);
    return;
  }
  if (!input) return;
  input.value = query;
  const status = document.getElementById('search-status');
  const results = document.getElementById('search-results');
  if (!query.trim()) {
    status.textContent = 'Enter a word or phrase to search all posts and pages.';
    return;
  }
  status.textContent = 'Searching…';
  fetch(local('/archive-assets/search.json'))
    .then((response) => {
      if (!response.ok) throw new Error('Search index unavailable');
      return response.json();
    })
    .then((posts) => {
      const terms = query.toLocaleLowerCase().trim().split(/\s+/);
      const matches = posts.filter((post) => {
        const text = `${post.title} ${post.text}`.toLocaleLowerCase();
        return terms.every((term) => text.includes(term));
      });
      status.textContent = `${matches.length} result${matches.length === 1 ? '' : 's'} for “${query}”`;
      for (const post of matches) {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = local(post.url);
        link.textContent = post.title;
        const date = document.createElement('small');
        date.textContent = ` — ${post.date}`;
        const excerpt = document.createElement('p');
        excerpt.textContent = post.text.slice(0, 220) + (post.text.length > 220 ? '…' : '');
        item.append(link, date, excerpt);
        results.append(item);
      }
    })
    .catch(() => {
      status.textContent = 'Search could not load. Please try again or browse the archive.';
    });
})();
