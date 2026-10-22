---
title: "CSS Fun: Flag Deprecated HTML Tags"
date: "2009-01-08T11:47:14"
slug: "css-fun-flag-deprecated-html-tags"
url: "/2009/01/08/css-fun-flag-deprecated-html-tags/"
wp_id: 990
categories: ["CSS", "Web Development", "Web Standards"]
tags: ["css webdevelopment deprecated html validation"]
author: "jesper"
---

Here is a little fun CSS snippet that helped me identify deprecated HTML on a recent project. Put these lines into the CSS file of your website:

> \
> `/* Watch out for invalid/deprecated HTML in CMS */`\
> `b{font-size: x-large; background-color: fuchsia; color: yellow; font-weight: normal;}`\
> `i{font-size: x-large; background-color: lime; color: blue; font-style: normal}`\
> `font{background-color: aqua; color: red}`\
> `b,i,font{text-decoration: blink;}`

[{{< img src=`/wp-content/uploads/2009/01/blink-and-flag-deprecated-font-b-i-tags.gif` alt=`` title=`blink-and-flag-deprecated-font-b-i-tags` class=`alignnone size-full wp-image-991` width=`249` height=`165` >}}](/wp-content/uploads/2009/01/blink-and-flag-deprecated-font-b-i-tags.gif)

This was really useful for identifying dirty HTML that was generated from a Microsoft-based CMS.

Coloring and blinking text makes the editors aware that something is wrong. Two major advantages for this approach:

- Instant attention on HTML validation errors (also for non-developers)
- Developers spend less time on hunting down invalid HTML that constantly sneaks into the web application.

These lines may also be useful to you -- unless you are able to guard your HTML before it's inserted in your application (something that was not possible at this project).
