# Search (Pagefind)

Client-side, fully static search using [Pagefind](https://pagefind.app) (MIT), pinned in `package.json` (`pagefind` 1.5.2, binary in `node_modules/.bin/pagefind`).

## What is indexed
Only the 440 posts. `layouts/_default/single.html` puts `data-pagefind-body` on `<div class="post">` when `.Type` is `posts`. Because at least one page has that attribute, Pagefind skips every page without it: home, `/category/`, `/tag/`, `/author/`, date archives, `/all-posts/`, `/archive/`, fixed pages and `/search/`.
- Comments are rendered after `.post` (partial `comments.html`), so they are not indexed.
- The "posted by ... filed under" box has `data-pagefind-ignore`.
- Metadata: `title` (from the h2), `date` (`YYYY-MM-DD`), `excerpt` (HTML from `partials/excerpt.html`, same as the front page), `author` (first name), `short` (`Jan 2`), `comments` (count). All set through hidden spans with `data-pagefind-meta="name[data-v]"` in `single.html`. Filters: `category`, `year`.
- Pagefind warns about `/wp-content/uploads/*.html` files having no `<html>` element; harmless (they are not indexed).

## Build
- Production: `bin/build` (rm -rf public, `hugo --gc`, `pagefind --site public`). Hosting build command: `bin/build`, publish dir `public` (run `yarn install` first).
- Dev: `hugo server` serves from memory, so no index exists. `bin/dev reindex` builds the site to `tmp/search-site`, runs Pagefind there and writes the bundle to `static/pagefind/` (git-ignored), which hugo serves as `/pagefind/`. `bin/dev start` builds it if missing, `bin/dev restart` always rebuilds. Re-run `bin/dev reindex` after content changes (layout/CSS changes need nothing).
- `bin/build` removes `site/pagefind` before indexing so a dev bundle copied from `static/` never ends up stale.

## UI
`/search/` (`content/search.md`, layout `layouts/_default/search.html`, `noindex`) imports `/pagefind/pagefind.js` (JS API, no Default UI) and renders each hit with the same markup and classes as `partials/post-short.html` (title, byline, date, comment line, stored excerpt, "Continue reading"), so the front-page CSS applies. Results come 10 at a time ("Load more results"); order is Pagefind relevance (the original sorted by date). The year and category facets sit in a collapsed `<details>` "Filter results" (small type, inline lists; counts are computed with one cheap search per value because Pagefind only returns counts for filters it is given). The result container gets `data-ready="1"` when rendered; `bin/screenshot` waits for it.
- URL state: `?q=...&year=2009&category=Usability`. New searches and filter clicks use `history.pushState`, the initial state is read from the URL (so a reload restores it), `popstate` re-runs the search.
- The sidebar form (`#searchform`) is a GET form to `/search/` with `name="q"`.
- Old WordPress URL `/?s=term`: the home page head (`baseof.html`, only for `.IsHome`) has a tiny inline script that, when `s=` is present, does `location.replace('/search/?q=' + encodeURIComponent(term))`. This is what works on GitHub Pages and `hugo server`. `static/_redirects` keeps the Netlify rule `/ s=:term /search/?q=:term 301` (harmless elsewhere).

## Changing scope
- Index another page type: add `data-pagefind-body` for that type in its layout.
- Exclude a part: `data-pagefind-ignore`. Add a filter/meta: `data-pagefind-filter="name[attr]"` / `data-pagefind-meta`.
- Pagefind 1.5 offers a newer Component UI; the Default UI still works. Upgrade: `yarn add -D pagefind@<version>`, then `bin/build` and check the indexed page count (440).

## Sorting

Radio buttons "Newest" (default) and "Relevance". Newest uses Pagefind's `sort: {date: "desc"}` on the `date` sort key set in `single.html`; relevance is Pagefind's ranking. The URL carries `&sort=relevance` only for relevance, so a reload keeps the choice.
