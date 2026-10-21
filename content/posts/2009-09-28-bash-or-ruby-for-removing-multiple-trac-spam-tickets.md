---
title: "Bash or Ruby for removing multiple Trac Spam Tickets"
date: "2009-09-28T11:21:32"
slug: "bash-or-ruby-for-removing-multiple-trac-spam-tickets"
url: "/2009/09/28/bash-or-ruby-for-removing-multiple-trac-spam-tickets/"
wp_id: 1159
categories: ["justaddwater.dk"]
tags: []
author: "jesper"
---

I had to clean up a public Trac ticket db where anonymous tickets are allowed. I had to issue commands like this:

    trac-admin . ticket remove 58

I keep forgetting the shell syntax for doing a loop over numbers. But actually a ruby script was just right for the task:

    ruby -e "(49..75).each{|i| %x(sudo -u www-data trac-admin . ticket remove #{i})}"

This shows some of my reasons to love Ruby: Very intuitive syntax. And faster than to lookup bash syntax.
