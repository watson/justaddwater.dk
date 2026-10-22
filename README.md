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
  pages contain **2,784 comment and trackback entries** in total, including two
  owner-approved comments recovered from the 2007 database backup.
- **548 public media records.** WordPress advertises 572, but returns 548 across
  all API pages. Images and downloads discovered in HTML and CSS are also copied,
  including files not listed in the media library.
- The original site layout, plus local search, RSS feeds, a sitemap and a 404 page.
- Article comment feeds and category, tag and author feeds retain their original
  `/…/feed/` paths and scope. Feed item links use the deployed archive address;
  original RSS IDs and comment timestamps are preserved.
  The original RSS and Atom aliases for the Web Standards category also work.
- Original video players in **21 posts**, including YouTube, Vimeo and legacy
  Flash embeds, with their original URLs, dimensions and player parameters.
- **61 legacy code examples in 19 articles** displayed as code, plus **14 files
  from 12 GitHub gist embeds** saved locally. Quotes, command-line hyphens and
  literal HTML tags are preserved without executing the examples.
- Two missing accessibility images recovered from an old site backup, repaired
  Beermat/presentation links, and a local copy of the previously broken external
  mullet illustration.
- Local, working versions of the table-height and undo demonstrations, plus the
  interactive CSS button example. The undo example is an adaptation of Aza
  Raskin's archived 2007 demo, with attribution; Done resets it locally.
- A public-content export in `data/content.json` and recovery reports in `data/`.

Some local files already returned 404, and some external images could not be
retrieved during capture. **85 of 187 external image references** were recovered
and stored locally. Unavailable images have a small placeholder and retain their
original URL in a `data-original-url` attribute. The obsolete FeedBurner icon is
replaced with a local RSS icon. Reports identify unrecovered resources and the
fetch errors for possible recovery from backups.

Video players depend on their original external services; obsolete or unavailable
players are preserved even if they no longer play.

Legacy tracking scripts and WordPress runtime scripts are removed. The two
reviewed JavaScript demonstrations use a small local script; other code examples
are inert text. Browser-only demo controls remain active without submission
notices or server requests. Contact/comment forms and the three old Capgemini
search forms copied into map examples retain their visible controls, with all
fields and buttons disabled and a highlighted notice that submissions are closed.
Their submission endpoints and hidden runtime fields are removed; archive search
stays active. Code examples remain text, and downloadable examples remain files.
Historical comments retain their original authorship and
links. This is a public static capture, **not** a database backup: drafts, private
posts, unpublished media and server-side files are not included.

## Preview locally

```sh
python3 scripts/serve.py --directory site --port 8000
```

Open <http://localhost:8000>. Use an HTTP server, rather than opening HTML files
directly, so search can load its local JSON index. The preview server also serves
`index.xml` at feed directory URLs, matching GitHub Pages. Feeds contain XML
directly, without an HTML redirect or an `index.xml` suffix in their public URLs.

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
Original public comment RSS fields are captured in `data/comment-feeds.json`;
this retains pingbacks omitted by the public comments API. Original post feed IDs
are saved separately in `data/post-feed-ids.json`. To refresh these
snapshots after capturing the site, run `.venv/bin/python scripts/capture_feeds.py`
before rebuilding. The capture accepts only comments already present in the
reviewed archive. Article feeds retain WordPress's ten most recent responses,
including the two owner-approved recoveries where applicable; articles without
responses have valid empty feeds.
HTML is parsed using the browser's HTML5 rules to preserve formatting in the
original WordPress markup, including mismatched inline tags. Literal form tags
inside legacy `[code]` examples are escaped before parsing so they cannot swallow
the surrounding article text.
Known `[code]` shortcodes are escaped before HTML parsing, so example form,
table, style and script tags remain visible code and cannot consume article text
or change the page. `data/recovery.json` records the selected public snippets,
asset checksums, original paths, gist revisions and demo provenance. It preserves
later CSS edits where the public article differs from the older database.
Two malformed `[tags]…[tags]` lists are rendered with the original SimpleTags
2.0 markup: small “Technorati Tags:” text and the original Technorati tag links.
The original captured article markup remains in `data/content.json`.

The database dump, WordPress configuration and unreviewed historical content are
not included in this repository. Rebuilds use only the selected public material
in `data/recovery.json` and `data/recovered-assets/`. The owner approved restoring
comments #27244 (the archive pingback) and #58286 (Jesper's source attribution)
on 22 October 2026. The other three historical comments and four historical pages
reviewed alongside them remain excluded.

`scripts/verify.py` checks that the full text of every exported post/page is
preserved, all public comment IDs appear in HTML, local navigation and asset
references resolve, RSS and sitemap XML parse, and pages do not contain legacy
executable scripts or dynamic forms. It verifies that archived form controls are
disabled and have an associated notice. It also checks background images in external
stylesheets, style attributes and embedded style blocks, rejecting remote CSS
dependencies. The deployment workflow runs these checks before publishing.
RSS checks cover feed paths, article footer links, scoped entries, original
comment timestamps and IDs, and links back into the deployed archive.
Expected article text is checked independently of the converter's cleanup rules,
so the same accidental deletion cannot be hidden on both sides of the comparison.
Recovered examples are checked character-for-character against their recorded
sources, and recovered assets and repaired aliases are checked for byte identity.
Video markup is compared directly with the original public export, including
nested Flash players and their parameters; playback availability is not required.

To test a project URL prefix:

```sh
.venv/bin/python scripts/prepare_pages.py --base-path /justaddwater.dk
.venv/bin/python scripts/verify.py --site _site --base-path /justaddwater.dk
```

## Licensing

See [LICENSE.md](LICENSE.md). The original theme explicitly carries a GPL notice.
Articles, comments, third-party media and individually licensed projects retain
their existing notices; this repository does not impose one license on them all.
