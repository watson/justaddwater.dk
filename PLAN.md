# justaddwater.dk 2026 update: plan

## Current state (probed 2026-10-21)

| Fact | Finding |
|---|---|
| Platform | WordPress 5.1.27, custom theme `jaw`, one plugin (`nofollow-case-by-case`) |
| Runtime | PHP 5.2.17 on Apache (end of life since 2011) |
| HTTPS | Broken. Port 443 refuses connections, and `www` redirects to plain `http://` |
| Content | 440 posts (2005-10 to 2016-11), 13 pages, 72 categories, 149 tags, 572 media items, 2219 comments |
| Biggest topics | Usability (136), justaddwater.dk meta (103), Web Development, Code, Blogging, Web Standards, Rails, Accessibility |
| Activity | No new posts since 2016-11, so this is an archive |
| Wayback | Captures exist (e.g. 2024-12-18), which is a fallback source for content |

The site is a public archive on an unsupported stack with no TLS. It is the likeliest thing here to get compromised, and browsers flag it as "Not secure".

## Goal (proposed, to confirm)

Preserve 20 years of content and URLs, drop the maintenance and security burden, and make it readable on modern devices. Optionally relaunch it with new writing.

## Recommended approach: freeze WordPress into a static site

1. **Back up everything first.** Export the database, `wp-content/uploads` and the theme over FTP/SSH. Run `wget --mirror` as a second copy. Check Wayback as a third.
2. **Export content** to Markdown with front matter, using the WP REST API (reachable today) or WXR. Keep the slug, date, categories, tags and comments for each post.
3. **Pick a static generator.** Hugo is the default pick (fast, single binary, good taxonomy support). Astro is the alternative if you want components.
4. **Preserve URLs.** Match the existing permalink structure exactly, and add a redirect map for anything that moves. Keep `/feed/` (RSS) alive.
5. **Comments.** Render the 2219 comments as static read-only HTML under each post, and add no new comments (or Giscus if you want them back).
6. **Design.** A new responsive theme with readable typography, dark mode, and basic accessibility (the blog covered the topic, so it should pass). Optionally keep a nod to the old `jaw` look.
7. **Media.** Move the 572 uploads over, add alt text where it is missing, and fix dead embeds and links (a link-check pass).
8. **Hosting and TLS.** Cloudflare Pages, Netlify or GitHub Pages with automatic HTTPS. Point DNS at it and keep the old host running until verified.
9. **Cutover.** Lower the TTL, switch DNS, then check Search Console, redirects, feed and sitemap. Keep the old server read-only for 30 days, then shut it down.

## Alternative options

- **Upgrade in place:** move to PHP 8.x and current WordPress, then re-theme. Keeps editing but needs ongoing patching, so I'd avoid it for an archive.
- **Relaunch as an active blog:** the same static setup, plus new posts. It can be done after the migration.

## Milestones

1. Backups and a content inventory (including a list of dead links)
2. Export to Markdown, with a spot check of 20 posts
3. Generator skeleton with URL parity
4. Theme and comments
5. QA (link check, redirects, feed, Lighthouse) and cutover

## Open questions for you

- Where is the site hosted, and do you have FTP/SSH or a database dump?
- Static archive only, or do you want to write new posts?
- Keep comments visible, or drop them?
- Keep Danish and English as they are, or should something be translated or pruned (e.g. the spam-tagged posts, outdated tech tips)?
- Any hosting preference or budget?
- Is Google Analytics or ad revenue still involved?

## Hosting

Project name: jaw-static. Hosting plan (GitHub Pages, public repo): see `docs/hosting.md`. Later option for limited, moderated commenting: `docs/comments-plan.md`.

## Local files

- `bin/mirror`: wget mirror of the live site into `mirror/` (gitignored).
- `export/`: put the WordPress XML export (Tools → Export → All content) here, e.g. `export/justaddwater.WordPress.xml`.

- Search: client-side Pagefind over posts only (`bin/build`, `bin/dev reindex`, `/search/`); see `docs/search.md`.
