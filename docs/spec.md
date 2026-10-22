# Specification

What the site must do. Details live in the linked docs.

## Requirements

| Area | Requirement |
|---|---|
| URL parity | Every URL of justaddwater.dk keeps working, by same path or 301. Map: `docs/urls.md`. Check: `docs/verify-urls.sh` |
| Redirects | Legacy feeds, renamed category/tag slugs, `/?p=ID`, `/?s=term`, `/archive` in `static/_redirects` (Netlify / Cloudflare Pages syntax) |
| Content | 440 posts and the fixed pages, with original date, slug, categories, tags, author |
| Media | `/wp-content/uploads/...` served at the same paths |
| Feed | RSS at `/feed/`, plus `/category/<x>/feed/` and `/tag/<x>/feed/` |
| Comments | Static, read-only, WordPress markup; no form, pages say "Comments are closed." Later option: `docs/comments-plan.md` |
| Search | Client-side Pagefind over posts, `/search/`. See `docs/search.md` |
| Authors | Per-author sidebars and archives as on the original. See `docs/authors.md` |
| Fidelity | Looks like the original Kubrick-based `jaw` theme at 800 px width |
| Hosting | Static files only, HTTPS. Plan: `docs/hosting.md` |

## Page types

| Type | URL |
|---|---|
| Home | `/`, `/page/N/` (5 posts per page) |
| Post | `/YYYY/MM/DD/slug/` |
| Fixed page | `/about-the-authors/`, `/contact-us/`, `/privacy/`, `/blogtools/`, ... |
| Category, tag | `/category/<slug>/`, `/tag/<slug>/`, `/category/` (+ `/page/N/`, 20 per page) |
| Author | `/author/<slug>/` (jesper, luis; thomas 404s as on the original) |
| Year, month archive | `/YYYY/`, `/YYYY/MM/` |
| Archive | `/archive/` (month and category lists) |
| All posts | `/all-posts/` (new, not on the original) |
| Search | `/search/` (new, noindex) |

## Out of scope

New comments, a contact form, a comments feed, section pages.
