# Plan (later): limited commenting

Status: not started. Today all 2778 comments are static and read-only (`data/comments/*.json`, `layouts/partials/comments.html`), and every post says "Comments are closed." This plan is for opening a small, moderated door again without adding a server.

## Goal and scope

- Keep the 2005-2016 archive closed. Old comments stay as they are.
- Allow comments only where they are wanted: new posts, plus a hand-picked set of old ones (opt-in per post with `comments: true` in the front matter).
- No spam, no tracking, no database of our own to run or patch.
- Old and new comments must not get mixed up: the static list stays on top, the new thread sits below under its own heading ("New comments").

## Options compared

| Option | How it works | Spam / moderation | Fits GitHub Pages | Downsides |
|---|---|---|---|---|
| **Giscus** (recommended) | One GitHub Discussion per post, embedded via script | Commenters need a GitHub login, which stops almost all spam; moderate in GitHub; lock or delete threads | Yes, needs a public repo with Discussions enabled | Readers without a GitHub account cannot comment; the audience of an old usability blog is probably fine with that |
| Utterances | Same idea with GitHub issues | Same | Yes | Issues are cluttered; Giscus is the better successor |
| Staticman or a form to a function | A form opens a pull request with a comment file | Review and merge each comment; honeypot/captcha | Yes, with a small hosted function | Needs a function host and a token; most moving parts |
| Cusdis / Remark42 / similar | Small hosted widget or self-hosted server | Built-in moderation, anonymous comments possible | Yes (widget) | Hosted service we depend on, or a server we would have to maintain |
| E-mail a reply | "Reply by e-mail" link, comments added by hand | Fully manual | Yes | Slow, but zero infrastructure; good enough as the very first step |
| Disqus and other ad-based | Third-party script | Heavy tracking | Yes | Against the goal (privacy, GDPR banner) |

Recommendation: **Giscus**. It is free, has no server, uses GitHub's spam protection through the login, and keeps comments in the open source repo's Discussions, next to the code. If anonymous comments turn out to matter, add Cusdis later.

## How it would work

1. Enable Discussions on the repo; create a category "Comments" (announcement type: only maintainers create threads, giscus creates them).
2. Install the giscus GitHub app on the repo; get `data-repo-id` and `data-category-id` from giscus.app.
3. Add `layouts/partials/giscus.html` with the script tag, `data-mapping="pathname"` (one thread per URL), `data-reactions-enabled="0"`, `data-loading="lazy"`, `data-lang="en"`, theme `light` (to match Kubrick).
4. In `comments.html`: after the static list, `{{ if .Params.comments }}` render the heading and the partial; otherwise keep "Comments are closed." only for posts without an opt-in.
5. Default off. New posts get `comments: true` from an archetype (`archetypes/posts.md`); old posts opt in by hand.
6. Style the iframe container to the theme's `#comments` width (pixel check with `bin/compare`, since the old pages must not change: `comments: true` is absent there, so diffs stay unchanged).
7. Pagefind: the giscus iframe is outside `data-pagefind-body`, so comments are not indexed; keep it that way.

## Moderation and house rules

- Add a short comment policy under the form (be civil, no ads, comments may be removed).
- Turn on GitHub's "block users" and restrict the Discussions category to authenticated users (default).
- Close threads after N months by locking the discussion (manual, or a small scheduled GitHub Action that locks threads older than 12 months).
- Keep a copy: a scheduled Action can export Discussions to JSON in the repo, so the comments live on if GitHub is ever abandoned. Fits the existing `data/comments/*.json` format, so they can be rendered statically later.

## Privacy and legal

- giscus loads from `giscus.app` and GitHub: only on posts with `comments: true`, loaded lazily (after the reader scrolls there), so the rest of the site stays third-party free.
- Mention it on a short privacy page (the site already has a privacy page: update the text there).
- Existing comments: names and URLs were published already; no new personal data is collected by us.

## Open decisions

1. Is a GitHub login acceptable, or are anonymous comments required (then Cusdis or a form-to-PR flow)?
2. Opt-in set of old posts: none, or a "best of" list (the category "Best of Justaddwater" exists).
3. Where the new comments appear relative to the old ones (below, with its own heading, as proposed).
4. Who moderates, and a notification path (GitHub notifications and e-mail are enough).

## Work items

1. Decide the points above; make the repo public (see `docs/hosting.md`).
2. Giscus partial, front matter flag, archetype, theme styling.
3. Policy text and privacy page update.
4. Optional: locking and export Actions.
5. Test on one new post before enabling on any old post.
