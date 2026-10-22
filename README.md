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
- Video embeds in **21 posts**, all using native YouTube players, including
  nine owner-approved replacement uploads across twelve posts.
  Original player dimensions are preserved.
- **61 legacy code examples in 19 articles** displayed as code, plus **14 files
  from 12 GitHub gist embeds** saved locally. Quotes, command-line hyphens and
  literal HTML tags are preserved without executing the examples. Ten further
  paragraph-style examples have corrected code punctuation and formatting;
  literal `<object>` and `<a>` examples no longer consume IE7 article text.
- Two missing accessibility images recovered from an old site backup, repaired
  Beermat/presentation links, and a local copy of the previously broken external
  mullet illustration.
- Local, working versions of the table-height and undo demonstrations, plus the
  interactive CSS button example. The undo example is an adaptation of Aza
  Raskin's archived 2007 demo, with attribution; Done resets it locally.
- **26 working bookmarklets** across the two toolbox downloads and cookie editor.
  Their scripts, styles and grid image are local. The original SlayerOffice
  notices are retained; its retired PHP source viewer has a browser-only replacement.
- A local MP3 and native audio player for the Copenhagen Ruby Brigade podcast,
  recovered from the publisher and linked from the article and both transcripts.
- Local topic indexes replace retired Technorati destinations. Original WordPress
  `/tag/` archives and feed scopes are unchanged. Known mistyped article URLs
  redirect to their canonical posts, including the original GWT plugin redirect.
- A public-content export in `data/content.json` and recovery reports in `data/`.

Some local files already returned 404, and some external images could not be
retrieved during capture. **167 of 187 external image references** were recovered
and stored locally. Unavailable images have a small placeholder and retain their
original URL in a `data-original-url` attribute. The obsolete FeedBurner icon is
replaced with a local RSS icon. Reports identify unrecovered resources and the
fetch errors for possible recovery from backups. This repair pass restored 82
additional image references, including all 29 Google menu screenshots. Nineteen
external image references still have no usable recovered file; their URLs and
affected articles are listed in `data/ui-repair-report.json`. The twentieth
unrecovered external reference is the FeedBurner icon already replaced locally.

Video players depend on external services. Approved alternatives restore Jeff
Sutherland's Scrum Tuning talk (two posts), Mary Poppendieck's Competing on the
Basis of Speed, Barry Schwartz's Google TechTalk, the SmartLunch OIOREST
presentation, the motivation clip, Monty Python's Spam sketch, Michael Wesch's
Web 2.0 film (two posts), and Aza Raskin's Rapid Prototyping talk. The two Mojiti
replacements explain that their original comment/annotation or transcription
layers are unavailable; the article screenshot and complete written transcript
remain. The original Danish Scrum presentation was recovered from the Internet
Archive and re-uploaded to YouTube by the site owner, restoring both posts that
embedded the same Google Video recording.
The original capture remains unchanged in `data/content.json`;
`data/video-players.json` records each migration and approved alternative.
YouTube's supported `hl`, `fs` and `rel` parameters are retained; Flash-only
`border`, `wmode` and script-access settings are dropped. The Google Video
subtitle preference on the Barry Schwartz talk maps to `cc_load_policy=1`. See the
[YouTube player documentation](https://developers.google.com/youtube/player_parameters)
for current parameter behavior (including the changed meaning of `rel=0`).

Legacy tracking scripts and WordPress runtime scripts are removed. The two
reviewed JavaScript demonstrations use a small local script. Restored bookmarklets
execute only when the visitor invokes them; other code examples are inert text.
Browser security policies can still restrict bookmarklets on unrelated websites.
Browser-only demo controls remain active without submission
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
2.0 markup: small “Technorati Tags:” text, now linked to local `/topics/` indexes.
`data/ui-repairs.json` records the additional code, URL, audio and bookmarklet
repairs. Recovered bookmarklet originals are kept in
`data/recovered-assets/bookmarklets/`; their deployed adaptations use local
dependencies. `data/external-images.json` records source URLs and checksums for
recovered images.
The original captured article markup remains in `data/content.json`.

The database dump, WordPress configuration and unreviewed historical content are
not included in this repository. Rebuilds use only the selected public material
in `data/recovery.json` and `data/recovered-assets/`. The owner approved restoring
comments #27244 (the archive pingback) and #58286 (Jesper's source attribution)
on 22 October 2026. The other three historical comments and four historical pages
reviewed alongside them remain excluded.

`scripts/verify.py` checks that the full text of every exported post/page is
preserved, all public comment IDs appear in HTML, local navigation and asset
references resolve, RSS and sitemap XML parse, and pages do not contain
unreviewed executable scripts or dynamic forms. The exact reviewed bookmarklet
URLs are allowlisted only on their three original download pages, and all
recovered bookmarklet dependencies are verified against recorded checksums.
It verifies that archived form controls are
disabled and have an associated notice. It also checks background images in external
stylesheets, style attributes and embedded style blocks, rejecting remote CSS
dependencies. The deployment workflow runs these checks before publishing.
RSS checks cover feed paths, article footer links, scoped entries, original
comment timestamps and IDs, and links back into the deployed archive.
Expected article text is checked independently of the converter's cleanup rules,
so the same accidental deletion cannot be hidden on both sides of the comparison.
Recovered examples are checked character-for-character against their recorded
sources, and recovered assets and repaired aliases are checked for byte identity.
Video markup is compared with the original public export and explicit migration
records, including retained nested Flash players and their parameters. Tests
independently check migrated video IDs, dimensions and supported options against
the original export; playback availability is not required.

To test a project URL prefix:

```sh
.venv/bin/python scripts/prepare_pages.py --base-path /justaddwater.dk
.venv/bin/python scripts/verify.py --site _site --base-path /justaddwater.dk
```

## Compare the archive with the original capture

The independent auditor checks **every URL in `.cache/capture.json`**, including
HTML downloads, assets and failed captures. It does not import the converter's
cleanup code. Exact recovery records explain known changes; unexpected prose,
missing comments, changed links, broken local targets, fragment links, differing
downloads, malformed feeds and remaining legacy UI problems are reported.
Both versions receive health checks, so a bug faithfully copied from WordPress
can still appear as an inherited problem.

```sh
.venv/bin/pip install -r requirements-audit.txt
.venv/bin/python scripts/audit.py
```

Open `.cache/audit/index.html` for a filterable report and per-URL text/resource
diffs. `.cache/audit/report.json` contains all results, evidence and coverage.
The report is local and excluded from Git and the published site. A fresh clone
needs the original `.cache/` capture to perform these comparisons; the script
reports missing evidence rather than silently accepting it.
`data/audit-summary.json` records the first complete run, its coverage and the
confirmed items needing review. The auditor reports findings without editing
the archived site.

For screenshots, pixel differences and Chromium health checks on **all captured
HTML pages**:

```sh
npm ci
npx playwright install chromium
.venv/bin/python scripts/audit.py --browser
```

Alternatively, use an installed Chrome with
`--browser-executable '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'`.
The browser runs in isolated contexts with network requests intercepted and
served from local files. Uncaptured dependencies and external players are blocked
and listed. Clone HTML uses GitHub Pages' UTF-8 response charset; original
responses retain their captured content types. Recovered external images are labeled as reconstructed dependencies;
they are not presented as original response snapshots. No forms are submitted.
This offline pass cannot determine whether a third-party video currently plays.
Controls are inspected, not exercised; existing demo interaction checks remain
separate. The runner uses Playwright's
[context routing](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)
and [page screenshots](https://playwright.dev/docs/api/class-page#page-screenshot).

Screenshots use a 1280 × 900 viewport and extend to the page's full height, capped
at 50,000 pixels. Horizontal overflow and any cap are explicit findings. JPEG
screenshots are compared at 480-pixel width with a 45/255 luminance tolerance;
more than 1% differing pixels creates a visual review item. This is a prioritizing
signal: intentional repairs and missing replay dependencies also change pixels.
The raw text diff and original/clone screenshots remain available even for
expected changes. Browser results are resumable and invalidated by changes to
HTML, dependency bytes, configuration, browser version or the runner.

Useful options:

- `--match '/2007/09/27/'` or `--limit 10`: a clearly labeled partial run.
- `--site _site --base-path /justaddwater.dk`: audit the deployment build.
- `--browser-workers 4`: control browser concurrency (default 3, maximum 8).
- `--report-only`: rebuild the HTML/JSON report from saved evidence.
- `--refresh`: fetch originals with two GET workers into a separate `live/`
  snapshot and report changes since capture. The original cache is never replaced.
- `--fail-on-unexplained`: return a nonzero status for unexplained differences.

Unexplained findings require investigation; they are not automatically declared
regressions. Generated clone-only pages are listed separately, and `verify.py`
continues to check their links and expected content. The comparison is optional
and is not part of deployment CI, which must work without the private capture
cache or the original server.

## Licensing

See [LICENSE.md](LICENSE.md). The original theme explicitly carries a GPL notice.
Articles, comments, third-party media and individually licensed projects retain
their existing notices; this repository does not impose one license on them all.
