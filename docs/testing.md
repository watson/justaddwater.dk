# Testing

## Checks

| Check | Command |
|---|---|
| URL parity | `hugo --gc && sh docs/verify-urls.sh` (every front-matter `url:` has a page in `public/`) |
| Build and search | `bin/build` (prints indexed page count, expected 440) |
| Visual | `bin/screenshot --all`, then `bin/compare` |

## Visual comparison

- `bin/screenshot` takes 800 px full-page shots of the 41 paths in `bin/screenshot-pages.txt` into `screenshots/dev/` (needs `bin/dev start`) and `screenshots/orig/` (live site). Append new pages at the end.
- `bin/compare` builds a pixelpilot review of the two folders (`~/src/dotfiles/bin/pixelpilot`, override with `PIXELPILOT`).
- `bin/compare --report [--only a,b] [--fail-above PCT]` prints per page: sizes, height delta, % differing pixels, per-100px bands. Diffs go to `tmp/pixelpilot-report`.
- `bin/compare --shoot` retakes everything first (~40 s).

## Known remaining differences

| Difference | Effect |
|---|---|
| Original has a "Leave a Reply" form, here "Comments are closed." | about 250 px shorter pages, bands differ from the comments down |
| Page 30 (make-wordpress-editor-less-evil): comment list | Hugo shows all comments, the original only a paged subset (4496 px original vs 10830 px Hugo), about 60% differing |
| Page 35 (change-history-of-svn-repository) | height differs by 707 px, about 33% differing |
| Footer says "powered by Hugo" | text differs |
| Contact form on `/contact-us/` missing | not rebuilt |
| Paging: Hugo `pagerSize = 20` | `/page/N/` contents differ |
| No comments feed | `/comments/feed/` redirects to `/feed/` |

About half of the 41 pages differ by more than 1% (mostly 4-27%, from the reply form and small height drifts). Run `bin/compare --report` for current numbers.
