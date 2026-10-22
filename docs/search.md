# Search (Pagefind)

Client-side, fully static search using [Pagefind](https://pagefind.app) (MIT), pinned in `package.json` (`pagefind` 1.5.2, binary in `node_modules/.bin/pagefind`).

## What is indexed
Only the 440 posts. `layouts/_default/single.html` puts `data-pagefind-body` on `<div class="post">` when `.Type` is `posts`. Because at least one page has that attribute, Pagefind skips every page without it: home, `/category/`, `/tag/`, `/author/`, date archives, `/all-posts/`, `/archive/`, fixed pages and `/search/`.
- Comments are rendered after `.post` (partial `comments.html`), so they are not indexed.
- The "posted by ... filed under" box has `data-pagefind-ignore`.
- Metadata: `title` (from the h2), `date` (hidden span, `YYYY-MM-DD`). Filters: `category`, `year`.
- Pagefind warns about `/wp-content/uploads/*.html` files having no `<html>` element; harmless (they are not indexed).

## Build
- Production: `bin/build` (rm -rf public, `hugo --gc`, `pagefind --site public`). Hosting build command: `bin/build`, publish dir `public` (run `yarn install` first).
- Dev: `hugo server` serves from memory, so no index exists. `bin/dev reindex` builds the site to `tmp/search-site`, runs Pagefind there and writes the bundle to `static/pagefind/` (git-ignored), which hugo serves as `/pagefind/`. `bin/dev start` builds it if missing, `bin/dev restart` always rebuilds. Re-run `bin/dev reindex` after content changes (layout/CSS changes need nothing).
- `bin/build` removes `site/pagefind` before indexing so a dev bundle copied from `static/` never ends up stale.

## UI
`/search/` (`content/search.md`, layout `layouts/_default/search.html`) uses the Pagefind Default UI (`/pagefind/pagefind-ui.js`), reads `?q=`, and is `noindex`. The sidebar form (`#searchform`) is a GET form to `/search/` with `name="q"`. The old WordPress `/?s=term` redirects there through `static/_redirects` (Netlify query rule; Cloudflare Pages ignores query strings in rules, `hugo server` ignores `_redirects` entirely).

## Changing scope
- Index another page type: add `data-pagefind-body` for that type in its layout.
- Exclude a part: `data-pagefind-ignore`. Add a filter/meta: `data-pagefind-filter="name[attr]"` / `data-pagefind-meta`.
- Pagefind 1.5 offers a newer Component UI; the Default UI still works. Upgrade: `yarn add -D pagefind@<version>`, then `bin/build` and check the indexed page count (440).
