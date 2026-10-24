# Gap analysis: origin/main vs hugosite-jrj

Date: 2026-10-24. Source: a read-only subagent comparison of the two committed `site/` trees and main's live site (`https://watson.github.io/justaddwater.dk/`). Figures come from the agent's own commands and were not independently re-run. The branches share no history.

Sizes: main `site/` 2724 pages, 129 MB; hugosite-jrj 991 pages, 66 MB.

## Gaps in main that hugosite-jrj fills

| Item | main | hugosite-jrj |
|---|---|---|
| Search | substring match over a 1.1 MB `search.json`, no ranking, filters or paging | Pagefind: posts only, newest/relevance sort, year/category filters, URL sync, load more, `/?s=` redirect |
| Mobile | no viewport meta, no `@media` rules found | viewport meta, rules at max-width 740px |
| Output size | 129 MB | 66 MB, one minified CSS file |
| Pipeline and docs | Python scripts | `bin/build`, `bin/dev`, `bin/check-site`, docs set, comments plan (`docs/comments-plan.md`) |
| Visual comparison | `audit_browser.mjs`, no committed set | `bin/screenshot`, `bin/compare`, 45 pages orig vs dev |

## Gaps in hugosite-jrj that main fills (ranked)

| # | Gap | Evidence | Effort |
|---|---|---|---|
| 1 | 201 of 2778 comments not in the pages: newest 100 only, no `comment-page-N` | wordpress-plugins 100/142, google-analytics-trick 100/101, archive 1; main serves `comment-page-1..3` | S-M |
| 2 | No `404.html` | missing in `site/`; main has it | S |
| 3 | Old-URL redirects do not work on GitHub Pages (`_redirects` ignored) | hugosite-jrj 8 meta-refresh pages vs main 210; main handles `?p=`, `?page_id=`, `?attachment_id=`, `?page=`, `?paged=` in the browser via `archive-assets/routes.json`; 7 "article has moved" stubs | M |
| 4 | No deploy workflow, tests or content validator on the branch | main: `pages.yml`, 9 `test_*.py`, `verify.py`, `migration_report.py --check` | M |
| 5 | No per-article comment feeds | main 894 `.../feed/index.xml` plus `/comments/feed/` | M |
| 6 | Video embeds: iframes on 1 page vs 40 (not diffed per post) | `youtube` 7 vs 42 pages | M |
| 7 | 571 hotlinked remote images (340 are the FeedBurner icon) | main 0; `data/external-images.json` recovered 174 of 193 | M |
| 8 | Attachment pages, `/topics/` indexes, original category/tag trees | main ~1027 `/topics/*`, ~50 attachment pages, `/category/eventsseminars/...` | S-M |
| 9 | `/page/N/` uses 20 per page, original used 10 | `pagerSize = 20` | S |
| 10 | Migration report and provenance data; 6 more comments (2784 vs 2778) | `/migration-report/`, `data/migration-report.json` | M |

## Fidelity (agent's own measurement, to reconcile)

800 px shots of 13 pages per site against hugosite-jrj's committed `screenshots/orig`, naive per-pixel diff: main 0.02-0.14% on posts and category pages, hugosite-jrj 4.7-15%; home 0.49% (main) vs 0.19%; archive 1.33 vs 0.75. hugosite-jrj's own `bin/compare` (pixelpilot) reports lower numbers on the same pages (for example 6.09% on the netbank post), so the methods differ. Main appears to capture the original HTML closely; hugosite-jrj rebuilds the theme.

## Not checked

Main's feed contents against the original, per-page parity with the live original, accessibility beyond `lang` and `alt`, page weight per page. Neither site uses `srcset`.
