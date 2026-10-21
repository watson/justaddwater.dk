---
title: "Shorthand to clean up installed Rubygems (but don't cleanup Rails)"
date: "2009-05-29T09:57:23"
slug: "shorthand-to-clean-up-installed-rubygems-but-dont-cleanup-rails"
url: "/2009/05/29/shorthand-to-clean-up-installed-rubygems-but-dont-cleanup-rails/"
wp_id: 1098
categories: ["Ruby on Rails", "Web Development"]
tags: ["rails", "Ruby on Rails", "Rubygems"]
---

I trimmed my installed Rubygems on my local development machine. The command "`sudo gem cleanup`" is just for that.

Only problem: What about my older Rails apps that require a specific version of Rails, ActiveRecord, etc.?

My solution:

> `gem list --no-versions | grep -v "^active" | grep -v "^action" | grep -v "^rails$" | xargs sudo gem cleanup {}`

Any suggestions on how to make it even simpler?
