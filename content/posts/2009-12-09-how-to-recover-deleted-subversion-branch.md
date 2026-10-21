---
title: "How To Recover Deleted Subversion Branch"
date: "2009-12-09T16:33:48"
slug: "how-to-recover-deleted-subversion-branch"
url: "/2009/12/09/how-to-recover-deleted-subversion-branch/"
wp_id: 1257
categories: ["Code", "Web Development"]
tags: []
---

I recently deleted a branch from our (svn) code repository. Did you know that it's the general recommendation to delete a branch after a merge to ensure that nobody commits to it. (see [svnmerge wiki](http://www.orcaware.com/svn/wiki/Svnmerge.py#Merging_development_branches_back_to_trunk) for more on that advice)

Svn checkout, svn info, etc. all fail when you try to access the deleted branch immediately:

> \
> \$ HOST=https://repository.com/repos_path\
> \$ svn log --limit=3 \$HOST/portal/branches/VA1-12\
> svn: '/svn/repos_path/!svn/bc/8881/portal/branches/VA1-12' path not found\
> 

But the interesting thing is that we need to add a so-called peg revision, denoted by the @ after the URL:

> \
> \$ svn log --limit=3 \$HOST/portal/branches/VA1-12@8800\
> \
> ------------------------------------------------------------------------\
> r8774 \| jronn \| 2009-11-23 11:30:40 +0100 (Mon, 23 Nov 2009) \| 3 lines\
> \
> Max height in search results (indberetninger): 34px is 2 lines for a total of max 4 lines.\
> \
> Also converted spaces to tabs and removed trailing whitespace for consistency\
> ------------------------------------------------------------------------\
> r8769 \| jronn \| 2009-11-17 17:01:25 +0100 (Tue, 17 Nov 2009) \| 1 line\
> \
> Horizontal train first-shot with new image files\
> ------------------------------------------------------------------------\
> r8768 \| jronn \| 2009-11-17 17:01:21 +0100 (Tue, 17 Nov 2009) \| 1 line\
> \
> Removed image files having not been used for a long time\
> ------------------------------------------------------------------------\
> 

And to recover the deleted branch (for instance by checking out a copy):

> \
> \$ svn co \$HOST/portal/branches/VA1-12@8800 va112

More info on [peg revisions in svn book](http://svnbook.red-bean.com/nightly/en/svn.advanced.pegrevs.html)
