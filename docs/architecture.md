# Architecture

## Pipeline

    bin/mirror -> bin/sanitize-export -> bin/export-to-hugo
                                      -> bin/export-excerpts
                  bin/copy-uploads    -> hugo --gc -> pagefind   (bin/build)

| Step | Input | Output |
|---|---|---|
| `bin/mirror` | live site | `mirror/` (safety copy, source of uploads) |
| `bin/sanitize-export` | `export/raw-justaddwater.xml` (git-ignored) | `export/justaddwater.sanitized.xml` (no emails/IPs/drafts) |
| `bin/export-to-hugo` | sanitized XML (needs pandoc, ~7 min) | `content/posts`, `content/pages`, `data/comments/<slug>.json` |
| `bin/export-excerpts` | raw XML | `data/excerpts.json` |
| `bin/copy-uploads` | `mirror/` | `static/wp-content/uploads/` |
| `bin/build` | all of the above | `public/` incl. Pagefind index |

## Generated vs hand-written

| Generated, overwritten on re-run | Hand-written |
|---|---|
| `content/posts/*.md`, `content/pages/*.md` | `content/all-posts.md`, `content/search.md` |
| `data/comments/*.json`, `data/excerpts.json` | `content/archives/_content.gotmpl` (year, month, author archives) |
| `static/wp-content/uploads/` | `data/authors.yaml`, `layouts/`, `assets/`, `static/_redirects` |

The converter deletes nothing. After `rm -rf content data`, restore hand-written files from git. Permalinks come from each file's `url:` front matter; `author:` is jesper, thomas or luis.

## Layouts

`layouts/_default/`: `baseof`, `single`, `list`, `terms`, `archive`, `datearchive`, `search`. Also `_markup/render-image.html` (width/height, srcset), `shortcodes/img.html`, `robots.txt`.

| Partial | Role |
|---|---|
| `sidebar`, `archive-nav`, `date-nav` | sidebar per page type, prev/next links |
| `post-short`, `post-archive`, `archive-lists` | list entries, `/archive/` lists |
| `comments`, `commentcount`, `commentlink` | static comments and counts |
| `excerpt`, `img`, `ordinal-date` | helpers |
| `tx`, `tt` | texturize |

## Rules

- Texturize: `tx.html` is a wptexturize clone (curly quotes, `NxN`, dashes, ellipsis; text nodes only, never in `pre`/`code`). `tt.html` does the same for plain-text titles.
- Excerpts: hand-written one from `data/excerpts.json`, else the first 55 words plus `[&hellip;]`, with inline code keeping its backticks, as WordPress did.
- Comments: sorted by date; more than 100 shows only the newest page of 100 (oldest first within it), like WordPress.
- Gists: embedded statically from `export/gists/<id>.json`, fetched from the GitHub API once and cached.
- Search: only posts carry `data-pagefind-body` (`docs/search.md`).
