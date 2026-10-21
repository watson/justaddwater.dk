---
title: "Print CSS Background Logo Hack"
date: "2009-09-29T11:08:58"
slug: "print-css-background-logo-hack"
url: "/2009/09/29/print-css-background-logo-hack/"
wp_id: 1163
categories: ["Code", "CSS", "Web Development"]
tags: ["CSS", "hack", "webdevelopment"]
author: "jesper"
---

I learned this nice little hack to bypass the standard browser setting that normally prevents background images from being printed.

The hack makes use of converting the background-image to a list item with an image.

    /* Hack, to trick the browser to print another logo 
       Unfortunetaly, Firefox on Windows doesn't show logo on print 
        — see Mozilla bug 133490 for further details */
    #header {
      display: list-item; 
      list-style-image: url(../images/logo_print.gif); 
      list-style-position: inside;
        margin: 0 !important;
      padding: 0 !important;
        height: 50pt;
    }

This way, you don't have to fall back to inserting an image tag in your HTML for the logo. Instead, just have an a element that contains the corporate logo text, and nothing all.
