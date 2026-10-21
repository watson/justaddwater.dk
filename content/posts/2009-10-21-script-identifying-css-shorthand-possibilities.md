---
title: "Script identifying CSS shorthand possibilities"
date: "2009-10-21T14:29:17"
slug: "script-identifying-css-shorthand-possibilities"
url: "/2009/10/21/script-identifying-css-shorthand-possibilities/"
wp_id: 1211
categories: ["Code", "CSS"]
tags: ["Code", "CSS"]
author: "jesper"
---

For my own convenience I created this script to identify css files where colors like \#aaaaaa can be rewritten in the short form \#aaa

(saves bandwith, but can also make it easier to identify similar colors)

    grep -nE '#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3' **/*.css

output from a random project:

    css/actions.css:19:  color: #000000;
    css/actions.css:38:  color: #000000 !important;
    css/actions.css:53:  color: #ffffff !important;
    css/admin.css:90:   color: #cccccc;
    css/admin.css:94:   color: #aaaaaa !important;
