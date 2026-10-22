---
title: "The IE PNG fix vs. Accessibility"
date: "2006-11-06T14:08:45"
slug: "the-ie-png-fix-vs-accessibility"
url: "/2006/11/06/the-ie-png-fix-vs-accessibility/"
wp_id: 437
categories: ["Accessibility", "JavaScript", "Web Development"]
tags: []
author: "thomas"
technorati: ["Internet Explorer", "IE", "IE6", "IE7", "png fix", "images", "accessibility", "screen reader", "JAWS", "DOM", "HTML", "JavaScript", "web development"]
---

It is no secret that all versions of Internet Explorer on Windows prior to version 7.0 has a flaw in its PNG renderer. The flaw basically involves the rendering of the alpha transparency and means that the images cannot fade nicely into the background.

### The IE PNG bug explained

In the screenshots below you can see the same image as it is seen in Internet Explorer 6 and Internet Explorer 7 <small>(Gray border added around the edge of the screenshot for your viewing pleasure)</small>:

![Screenshot of IE6 png bug](/wp-content/uploads/2006/11/png-alpha-trans2.png "Screenshot of IE6 png bug")\
<small>PNG alpha transparency bug as seen in IE6</small>

![Screenshot of IE6 png bug fixed](/wp-content/uploads/2006/11/png-alpha-trans-fixed2.png "Screenshot of IE6 png bug fixed")\
<small>No PNG alpha transparency bug as seen in IE7</small>

Instead of showing what is truly behind the image all IE renderer's prior to IE 7 just shows an ugly, bluish/gray background color.

### The solution and a new problem

Several people have found solutions to this problem. Most noticeably is [the fix by Bob Osola](http://homepage.ntlworld.com/bobosola/ "The PNG problem in Windows Internet Explorer") where I have also borrowed the above examples.

**There is one problem though with these kind of fixes, and that problem is accessibility.**

The idea is that you embed a piece of JavaScript in your webpage that, just before the images are displayed, runs through the DOM and replaces any img element that display a PNG image with a span element. What's special about this span element is that it has a style attribute with a special IE-only filter called:

`DXImageTransform.Microsoft.AlphaImageLoader`

This filter then renders the original image inside the span element and the user sees the image as if it was just a regular img element.

But what about screen readers? Will they still recognize this as a regular image? Some may say that screen readers don't use JavaScript anyway and therefore never gets their DOM changed. But the most popular screen reader of them all for Windows called [JAWS](http://www.freedomscientific.com/fs_products/software_jaws.asp) is just a regular Windows program running next to the browser and just reads whatever code the browser holds.

**Does anybody have any thoughts or experience with this? Am I for example right in my assumption that JAWS actually reads the generated code? And will that in fact be a problem? Please drop a comment with your thoughts.**

<ins>Update 2006-11-06 19:10 (CET)</ins>\
To better understand the accessibility implications, here is an update to clarify what Bob Osolas fix actually does. Take this example of a regular img element:

`<img src="`**`/images/sunset.png`**`" align="`**`left`**`" alt="`**`Sunset over New York`**`" width="`**`654`**`" height="`**`321`**`" id="`**`img421`**`" class="`**`largeimage`**`" style="`**`border: 1px solid black`**`" />`

That is then translated into this span element:

`<span id="`**`img421`**`" class="`**`largeimage`**`" title="`**`Sunset over New York`**`" style="width:`**`654`**`px; height:`**`321`**`px; float:`**`left`**`; display:inline-block; `**`border: 1px solid black`**`; filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='`**`/images/sunset.png`**`', sizingMethod='scale');"></span>`

In turn if the original img element is wrapped in an a element (i.e. is linkable) the following css is also added to the style attribute of the span element:

`cursor:hand;`
