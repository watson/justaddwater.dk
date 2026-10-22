# justaddwater.dk

Static archive of justaddwater.dk, a blog about usability, web standards, and web
development by Jesper Rønn-Jensen and Thomas Watson Steen, with guest contributions.

The archive preserves the original theme, published articles and pages, dated
permalinks, comments, author/category/tag/date archives, images and downloads.
It runs without PHP, WordPress, a database, or a build-time connection to the
original host.

## What is included

- **440 posts and 10 pages**, captured from the public site on 22 October 2026.
- **2,219 public API comments**, all preserved as read-only content. The rendered
  pages contain **2,782 comment and trackback entries** in total.
- **548 public media records.** WordPress advertises 572, but returns 548 across
  all API pages. Images and downloads discovered in HTML and CSS are also copied,
  including files not listed in the media library.
- The original site layout, plus local search, RSS feeds, a sitemap and a 404 page.
- Original video players in **21 posts**, including YouTube, Vimeo and legacy
  Flash embeds, with their original URLs, dimensions and player parameters.
- A public-content export in `data/content.json` and recovery reports in `data/`.

Some local files already returned 404, and some external images could not be
retrieved during capture. **84 of 187 external image references** were recovered
and stored locally. Unavailable images have a small placeholder and retain their
original URL in a `data-original-url` attribute. The obsolete FeedBurner icon is
replaced with a local RSS icon. Reports identify unrecovered resources and the
fetch errors for possible recovery from backups.

Video players depend on their original external services; obsolete or unavailable
players are preserved even if they no longer play.

Legacy tracking scripts, WordPress runtime scripts, other executable embeds and
comment submission forms are removed. Code examples remain text, and downloadable
examples remain files. CSS-demo controls remain visible without submitting forms.
Historical comments retain their original authorship and
links. This is a public static capture, **not** a database backup: drafts, private
posts, unpublished media and server-side files are not included.

## Preview locally

```sh
python3 -m http.server 8000 --directory site
```

Open <http://localhost:8000>. Use an HTTP server, rather than opening HTML files
directly, so search can load its local JSON index.

## GitHub Pages

The workflow publishes only `site/`, using `scripts/prepare_pages.py` to support
both the repository's project URL and a future custom domain. The workflow
installs the Python dependencies for validation and never contacts the old
WordPress server.

In the repository's **Settings → Pages**, choose **GitHub Actions** as the source.
Pushes to `main` and manual workflow runs deploy the archive.

For a custom domain, verify ownership in GitHub, set `justaddwater.dk` in the Pages
settings, and then update the apex and `www` DNS records at one.com. Changing DNS
or the original hosting account is a separate cutover. The current apex A record
has a 12-hour TTL; reduce it ahead of a planned switch. The workflow automatically
uses the custom domain's root path after another deployment.

## Reproduce the capture

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/archive.py inventory
.venv/bin/python scripts/archive.py capture
.venv/bin/python scripts/external_images.py
.venv/bin/python scripts/archive.py build
.venv/bin/python scripts/verify.py
```

Capturing uses only public GET requests, with four concurrent requests and bounded
timeouts. Raw responses are cached in `.cache/`, which is excluded from Git. Keep
that cache for repeatable local rebuilding; move it aside to make a fresh capture.
External-image results are cached separately in `data/external-images.json`.
HTML is parsed using the browser's HTML5 rules to preserve formatting in the
original WordPress markup, including mismatched inline tags. Literal form tags
inside legacy `[code]` examples are escaped before parsing so they cannot swallow
the surrounding article text.

`scripts/verify.py` checks that the full text of every exported post/page is
preserved, all public comment IDs appear in HTML, local navigation and asset
references resolve, RSS and sitemap XML parse, and pages do not contain legacy
executable scripts or dynamic forms. It also checks background images in external
stylesheets, style attributes and embedded style blocks, rejecting remote CSS
dependencies. The deployment workflow runs these checks before publishing.
Expected article text is checked independently of the converter's cleanup rules,
so the same accidental deletion cannot be hidden on both sides of the comparison.
Video markup is compared directly with the original public export, including
nested Flash players and their parameters; playback availability is not required.

To test a project URL prefix:

```sh
python3 scripts/prepare_pages.py --base-path /justaddwater.dk
.venv/bin/python scripts/verify.py --site _site --base-path /justaddwater.dk
```

## Licensing

See [LICENSE.md](LICENSE.md). The original theme explicitly carries a GPL notice.
Articles, comments, third-party media and individually licensed projects retain
their existing notices; this repository does not impose one license on them all.
