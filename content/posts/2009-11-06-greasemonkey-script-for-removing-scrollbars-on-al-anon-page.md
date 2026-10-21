---
title: "Greasemonkey Script For Removing Scrollbars on Al-Anon Page"
date: "2009-11-06T12:49:45"
slug: "greasemonkey-script-for-removing-scrollbars-on-al-anon-page"
url: "/2009/11/06/greasemonkey-script-for-removing-scrollbars-on-al-anon-page/"
wp_id: 1235
categories: ["Personal"]
tags: []
---

I have recently discovered an alcoholic in my family. And in order to deal with that, a friend pointed me to Al-Anon which has material and publications to help relatives.

The angle for this blog, however, is that i wrote this small script to remove scrollbars and remove menu when printing page. The script works on the Danish pages <http://al-anon.dk/>

*wwwal-anondk_no_inline_s.user.js — [gist on GitHub](https://gist.github.com/227952)*

``` javascript
// ==UserScript==
// @name           www.al-anon.dk Remove inline scroll so that page content prints properly
// @namespace      http://userscripts.org/users/103819
// @description    remove scroll from al-anon pages
// @include        http://al-anon.dk/*
// @require        http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js
// ==/UserScript==

$('#framen').css({'height': 'auto', width: 'auto'});
$('<style media="print">#menu {display: none;}</style>').appendTo('head');
```

I have published a few notes via [my Facebook Status](http://www.facebook.com/jesperronn) about the incident (in Danish).
