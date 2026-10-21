# URL parity with the original justaddwater.dk

| Old (WordPress) | New (Hugo) | Status |
|---|---|---|
| `/YYYY/MM/DD/slug/` posts, pages (`/about-the-authors/` ...) | same, from front matter `url:` | preserved |
| `/wp-content/uploads/...` | `static/wp-content/uploads/...` | preserved |
| `/category/<slug>/`, `/tag/<slug>/`, `/category/` | same (`[permalinks.term]` in hugo.toml) | preserved |
| `/category/<slug>/page/N/`, `/page/N/` | same paths, but Hugo `pagerSize = 20` so contents differ | preserved (paging differs) |
| `/feed/` (original 301s to feedburner) | `/feed/index.xml` served at `/feed/`; also `/category/<x>/feed/`, `/tag/<x>/feed/` | preserved |
| `/feed.xml`, `/rss/`, `/comments/feed/` | 301 -> `/feed/` | redirected (no comments feed) |
| `/category/eventsseminars/`, `justaddwaterdk`, `testing-2`, `webstandards`; tag `virkdk` | `/category/events/`, `justaddwater.dk`, `testing`, `web-standards`; tag `virk.dk` | redirected (Hugo slugs follow term names, not WP nicenames) |
| `/category/<parent>/<child>/` (webstandards, eventsseminars) | `/category/<child>/` (flat) | redirected |
| `/category/books|odd|uncategorized/`, unused tags | `/category/` | no posts; 302 / dropped |
| `/?p=ID` | permalink via `static/_redirects` query rules (Netlify/CF Pages) | redirected (453 rules) |
| `/archive` | `/archive/` | redirected |
| `/sitemap.xml`, `/robots.txt` | emitted by Hugo | preserved |
| `.../function.file-exists/` attachment pages, WP 404s from the mirror log, `/wp-json`, `/wp-admin`, `/comments/feed/` content | none | dropped |

Known mismatch: hugo.toml `[outputs]` leave `section`/`taxonomy` without RSS. `public/robots.txt` has no `Sitemap:` line (needs `layouts/robots.txt`, theme agent).

## Verification

    hugo --gc && docs/verify-urls.sh     # every front-matter url: has public/<url>/index.html
    curl -sI http://justaddwater.dk/<path> # compare with public/<path>

`_redirects` is only honoured by Netlify / Cloudflare Pages; `hugo server` ignores it.
