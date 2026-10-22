# Hosting plan: jaw-static on GitHub Pages

Project name: **jaw-static** (jaw = justaddwater). Proposal: a public, open source GitHub repo `jaw-static`, published with GitHub Pages on the custom domain `justaddwater.dk`. No server, no PHP, no patching: it works out of the box and is free for public repos.

## Why GitHub Pages fits

- Static files only, which is exactly what `hugo` + `pagefind` produce (`site/`, about 65 MB, uploads 48 MB).
- HTTPS with an automatic certificate for the custom domain (fixes the "Not secure" problem of today's HTTP-only site).
- Deploys from `git push` through GitHub Actions; the history is the backup.
- Limits (published site 1 GB, 100 MB per file, about 100 GB/month soft bandwidth, 10 builds/hour) are far above what a 2016 archive needs.
- Search works as is: Pagefind is client-side, no server needed (`docs/search.md`).

## What GitHub Pages cannot do (and what we do about it)

| Need | Netlify/Cloudflare | GitHub Pages | Plan |
|---|---|---|---|
| `static/_redirects` (494 old-URL rules) | supported | **ignored** | Generate redirects as Hugo `aliases` (small HTML pages with meta refresh + canonical link). Needs a converter from `_redirects`, see steps. |
| `/?s=term` -> `/search/?q=term` (query string rule) | Netlify only | no | Small script in `index.html`: if `location.search` has `s=`, go to `/search/?q=`. |
| Custom 404 | yes | yes: `404.html` at the root | Add `layouts/404.html` (currently missing). |
| `/feed/` | file | file | Already a static file (`/feed/index.xml`); verify that `/feed/` serves it. |
| Response headers, real 301s | yes | no | Accept: aliases are 200 + meta refresh. Search engines treat that as a redirect; the canonical link carries the signal. |

If real 301s ever matter, the fallback is Cloudflare Pages or Netlify (the `_redirects` file is kept for that reason, and `docs/urls.md` documents all mappings).

## Repo hygiene before making it public

- [ ] Rename the local folder and GitHub repo to `jaw-static`.
- [ ] Keep `export/raw-justaddwater.xml` out of the repo and of its history (it is git-ignored; check with `git log --all -- export/raw-justaddwater.xml`, which is empty today). Back it up privately.
- [x] `export/justaddwater.sanitized.xml` is git-ignored and removed from history (regenerate with `bin/sanitize-export`). `data/comments/*.json` holds commenter names, URLs and text, already public on the site; e-mails and IPs are stripped.
- [ ] `.git` is about 326 MB (mostly screenshot history). Fine for GitHub, but consider squashing/ignoring `screenshots/` before publishing; the user already rewrote history once, so this is cheap now and expensive later.
- [ ] Add a `LICENSE` (code: MIT) and a `README` for the code. Decide the content licence separately (e.g. CC BY-NC-SA), since the posts and comments are people's own writing.
- [ ] The theme is a port of the original WordPress theme (`reference/original-theme/`); keep its licence notice.

## Build and deploy (GitHub Actions)

`.github/workflows/pages.yml`, trigger: push to `main`.

1. Checkout, setup Hugo (pin the version used here, v0.168) and Node.
2. `yarn install --frozen-lockfile`
3. `bin/build` (clean `hugo --gc`, then `pagefind --site site`).
4. `sh docs/verify-urls.sh` as a gate (`missing=0`).
5. `actions/upload-pages-artifact` with `site/` (or, as on origin/main, only `site/` is published, so it can also be committed and deployed without a build step), then `actions/deploy-pages`.
6. Repo settings: Pages source = GitHub Actions. Custom domain `justaddwater.dk`, "Enforce HTTPS".

`static/CNAME` containing `justaddwater.dk` (or set only in the settings, which is enough with Actions deploys).

## DNS cutover

1. Test on `https://<user>.github.io/jaw-static/` first; set a temporary `baseURL` for that build only so assets resolve. Better: test on a subdomain, e.g. `new.justaddwater.dk` CNAME to `<user>.github.io`, with the real `baseURL`.
2. Lower the TTL on the current records to 300 s a day ahead.
3. Apex `justaddwater.dk`: four `A` records (185.199.108.153, .109.153, .110.153, .111.153) and four `AAAA` (2606:50c0:8000::153 ... 8003::153); check GitHub's docs for the current list before changing.
4. `www`: `CNAME` to `<user>.github.io`; GitHub redirects `www` to the apex.
5. Wait for the certificate (minutes to an hour), tick "Enforce HTTPS".
6. Run `bin/screenshot --host https://justaddwater.dk` style checks and `docs/verify-urls.sh` against the live site (the script needs a host option; not yet there).
7. Submit sitemap/check Search Console; keep the old server read-only for 30 days, then shut it down.

## Open points to decide

1. GitHub account/org that owns the repo (personal or an org).
2. Public from day one, or private until the redirect work is done (GitHub Pages on a private repo needs a paid plan).
3. Licence for the content.
4. Whether the redirect-as-aliases conversion should be generated at build time from `static/_redirects` (one source of truth, recommended) or by hand.
5. A sitemap (`sitemap.xml`) and `robots.txt` sitemap line: robots.txt exists, check that the sitemap is generated.

## Work items (in order)

1. `layouts/404.html`.
2. `bin/redirects-to-aliases` (or a Hugo template) producing alias pages from `_redirects`; add the `?s=` script; extend `verify-urls.sh` to follow alias pages.
3. `.github/workflows/pages.yml`.
4. Repo hygiene list above, rename to `jaw-static`.
5. Dry run on a test subdomain, then DNS cutover.
