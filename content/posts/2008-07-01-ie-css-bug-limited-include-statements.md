---
title: "IE CSS Bug: Limited @include Statements"
date: "2008-07-01T14:57:14"
slug: "ie-css-bug-limited-include-statements"
url: "/2008/07/01/ie-css-bug-limited-include-statements/"
wp_id: 939
categories: ["Browser", "CSS"]
tags: []
author: "jesper"
---

I found out that Internet explorer only interprets 32 @include statements in CSS for a webpage. The rest is silently ignored.

Tested with IE7. Has anybody tried this with IE8?

For more info see:

[Internet Explorer issue - maximum of 32 CSS @import](http://www.agum.com/web/2008/03/11/internet-explorer-issue-maximum-of-32-css-import/ "Agnum.com: Internet Explorer issue - maximum of 32 CSS @import")

PS. Silent ignorance is just about the worst form for ignorance when coding. The least they could do was to display an error in the error console.
