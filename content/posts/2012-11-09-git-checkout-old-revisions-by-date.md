---
title: "Git checkout old revisions by date"
date: "2012-11-09T23:24:06"
slug: "git-checkout-old-revisions-by-date"
url: "/2012/11/09/git-checkout-old-revisions-by-date/"
wp_id: 1658
categories: ["Code"]
tags: ["git"]
author: "jesper"
---

I wanted to do some code stats for a repository. This line checks out old revisions by date and shows code stats:

    git checkout `git rev-list -n 1 --before="2012-03-01" master`

Then, I ran cloc to count lines of code:

    cloc .

Its really easy to register the point in time as a git branch so that you can get back and count lines of code later:

    git co -b 2012-03

You can always verify latest revision like so:

    Git log -1

The combination of git and cloc makes it really simple to keep history of codebase changes.
