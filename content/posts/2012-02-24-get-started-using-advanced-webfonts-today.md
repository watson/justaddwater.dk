---
title: "Get started using advanced web fonts today"
date: "2012-02-24T17:00:05"
slug: "get-started-using-advanced-webfonts-today"
url: "/2012/02/24/get-started-using-advanced-webfonts-today/"
wp_id: 1580
categories: ["Web Development", "Web Standards"]
tags: ["Web Development", "webdevelopment", "webfonts"]
---

I saw this example on [a blog today](http://uxcampcph.org/):

[![](/wp-content/uploads/2012/02/web-font-example.png "web-font-example")](/wp-content/uploads/2012/02/web-font-example.png)

Studying the code, it turns out this is just [clever use of Google's font api](https://developers.google.com/webfonts/docs/getting_started). What you essentially do is to add this to your \<HEAD\> element:

```
<!-- Google Fonts --> 
<link href='http://fonts.googleapis.com/css?family=Cabin Sketch:bold' rel='stylesheet' type='text/css' /> 
<style type="text/css" media="screen"> 
  h1 { font-family: 'Cabin Sketch', arial, serif; } 
  .entry-title { 
    font-family:'Cabin Sketch'; 
  } 
</style>
```

Now the stylesheet referenced takes care of the rest. It's as simple as that!

## Browser support

The best part of this, is that it works for all modern browsers, and also for old IE versions (down to IE6).

From [googles FAQ](https://developers.google.com/webfonts/faq):

> **What browsers are supported?**
>
> The Google Web Fonts API is compatible with the following browsers:
>
> - Google Chrome: version 4.249.4+
> - Mozilla Firefox: version: 3.5+
> - Apple Safari: version 3.1+
> - Opera: version 10.5+
> - Microsoft Internet Explorer: version 6+
>
> **Does the Google Web Fonts API work on mobile devices?**
>
> The Google Web Fonts API works reliably on the vast majority of modern mobile operating systems, including Android 2.2+ and iOS 4.2+ (iPhone, iPad, iPod). Support for earlier iOS versions is limited.

 

 

## Bandwidth considerations

One word of caution: Think twice before adding a lot of extra bytes to your web application. You should only add assets to it if it *really makes a difference for your end users!*

 

```
```
