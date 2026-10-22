# jaw-static

Static Hugo archive of the WordPress blog justaddwater.dk (jaw = justaddwater): 440 posts, 10 pages, about 2800 comments, 2005-2016. The theme is pixel-matched to the original, and every old URL is kept.

## Quick start

    yarn install                          # pagefind, playwright, pngjs
    npx playwright install chromium       # once, for bin/screenshot
    bin/dev start                         # http://localhost:1313
    bin/build                             # production build into site/

Needs Hugo; pandoc only for re-running `bin/export-to-hugo`.

## Commands (`bin/<name> --help` for details)

| Command | Purpose |
|---|---|
| `bin/dev` | start, stop, restart, status, reindex of the Hugo dev server |
| `bin/build` | `hugo --gc` then Pagefind index into `site/` |
| `bin/check-site` | verify that the committed `site/` matches the sources |
| `bin/mirror` | wget mirror of the live site into `mirror/` (git-ignored) |
| `bin/scan` | flag suspicious files and links in the mirror and comments |
| `bin/sanitize-export` | commit-safe copy of the raw WordPress XML export |
| `bin/export-to-hugo` | sanitized XML to `content/` and `data/comments/` |
| `bin/export-excerpts` | hand-written excerpts to `data/excerpts.json` |
| `bin/copy-uploads` | mirror uploads to `static/wp-content/uploads/` |
| `bin/screenshot` | full-page screenshots of dev and original |
| `bin/compare` | compare the two screenshot folders in pixelpilot |

## Directory map

| Path | Content |
|---|---|
| `content/` | posts, pages (generated), hand-written all-posts, archives, search |
| `data/` | comments, excerpts, authors |
| `layouts/` | templates, partials, shortcodes, image render hook |
| `assets/`, `static/` | theme CSS and images; uploads, `_redirects`, dev Pagefind bundle |
| `export/` | WordPress XML (raw and sanitized are git-ignored), cached gists |
| `reference/` | original jaw theme CSS and images |
| `screenshots/` | `orig/` and `dev/` comparison images |
| `docs/` | documentation |
| `site/` | generated site (committed; GitHub Pages publishes it) |
| `mirror/`, `tmp/`, `logs/` | generated, git-ignored |

## Docs

- `docs/spec.md`: requirements
- `docs/architecture.md`: pipeline and structure
- `docs/testing.md`: verification and known differences
- `docs/urls.md`, `docs/search.md`, `docs/authors.md`, `docs/hosting.md`, `docs/comments-plan.md`
- `PLAN.md`: original migration plan
