---
title: "How to make a dry-run with svn update"
date: "2008-04-29T19:24:50"
slug: "how-to-make-a-dry-run-with-svn-update"
url: "/2008/04/29/how-to-make-a-dry-run-with-svn-update/"
wp_id: 924
categories: ["justaddwater.dk"]
tags: ["subversion"]
author: "jesper"
---

Quick Subversion trick:

I asked at the office today if anyone could figure out a method for doing a dry-run to see what files would be updated if you do an "svn update" from repository.

My colleague Mads came up with this:

> `jesper:test_project jesper$ svn merge --dry-run -r BASE:HEAD .`\
> `U app/helpers/application_helper.rb`\
> `U app/controllers/reports_controller.rb`\
> `A app/views/layouts/formula.html.erb`\
> `U app/views/overview/index.html.erb`\
> `U app/views/overview/_sidebar.html.erb`\
> `U app/views/reports/index.html.erb`\
> `A app/views/reports/_sidebar.html.erb`\
> `U app/views/reports/new.html.erb`\
> `U app/views/reports/start.html.erb`\
> `C log/development.log`\
> `U public/stylesheets/app.css`

Brilliant! Now I can see which files will conflict or update before I pull newest version from repository. Now added as an alias:

`alias svnupdry='svn merge --dry-run -r BASE:HEAD .'`

I took a brief look at the Git manual. There is apparently no flag on 'git pull' that does a dry-run. Anyone knows if the same thing is possible with Git?
