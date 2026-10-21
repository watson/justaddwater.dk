---
title: "HTML use and abuse in one billion webpages"
date: "2006-01-27T00:05:04"
slug: "html-use-and-abuse-in-one-billion-webpages"
url: "/2006/01/27/html-use-and-abuse-in-one-billion-webpages/"
wp_id: 116
categories: ["Web Standards"]
tags: []
author: "jesper"
technorati: ["google code", "web standards", "web developer", "html", "IE7"]
---

Google posted a very interesting study with regards to web standards. As new browsers get better and better support for web standards, our awareness is raised to make sure web applications also support the future browsers (such as Internet Explorer 7.

> **How do developers use HTML?** - 20/Jan/2006
>
> As part of our work with the [WHAT working group](http://www.whatwg.org/), who are writing proposals for a new version of HTML, we have done some research into what aspects of HTML authors are using today. We took a sample of slightly over a **billion** documents, and looked at what elements were used on the most pages, what class names were used on the most pages, and so forth. [The results are quite interesting](http://code.google.com/webstats/index.html)!

I think the study underplays their focus on webstandards. It's not really explicitly mentioned. But I guess this is to make the study interesting for the big part of web developers that (still) don't care about webstandards.

Here's one of the more abusive examples from the study. It's the `body ` element and which attributes that are used (and abused) with it;\
[![Screenshot body element and attributes small size](/wp-content/uploads/2006/01/screenshot%20body%20element%20small.png)](/?attachment_id=122 "Screenshot body element and attributes original size")

> Of the top twenty most-used attributes on `body`, fourteen are purely presentational. Of the remaining six, three are event handlers; of these, `onload` is the most common by a significant margin; then we have `onunload` and `oncontextmenu`, both used on a small fraction of the pages in the sample. One area of future study would be to see what these attributes are used for: is `onunload` used mostly by Web applications for legitimate purposes, or is it used more by hostile sites to show pop-unders? Is `oncontextmenu` used for good purposes, or to cancel the showing of the context menu?
>
> \[...\]
>
> The presentational attributes provide us with some interesting insights. For example, the four IE-specific margin attributes (`topmargin`, `rightmargin`, `bottommargin`, and `leftmargin`) are not all specified the same number of times. People care about the top margin most of all, then about the left margin, then the right margin, and then the bottom margin. This is borne out by the Netscape-specific margin attributes, which are in the same order: `marginheight` first, then `marginwidth`.
>
> \[...\]
>
> One conclusion one can draw from the spread of attributes used on the `body` element is that **authors don't care about what the specifications say. Of these top twenty attributes, nine are completely invalid, and five have been deprecated for nearly eight years**, half the lifetime of the Web so far.

See it all on [Google Code: Web Authoring Statistics](http://code.google.com/webstats/ "Google Code")
