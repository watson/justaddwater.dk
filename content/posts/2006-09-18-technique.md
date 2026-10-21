---
title: "Technique — locating problems in HTML"
date: "2006-09-18T22:37:19"
slug: "technique"
url: "/2006/09/18/technique/"
wp_id: 393
categories: ["CSS", "HTML", "justaddwater.dk", "Web Development", "Web Standards"]
tags: []
---

Technique for using the toolbox: Locating problems in HTML.

I decided to make a little toolbox that's easy to apply on web pages, when investigating problems with web pages. Basically, it's the tools I used when investigating the case I described in "[Why web standards matter (case study)](/2006/06/29/webstandards-case-study/)"

I split this into two posts. This is the second part. The first one is about the [toolbox](/2006/09/18/toolbox).

### Web standards investigation technique

The case study shwoed a page in big trouble and the problem turned out to be a combination of different things that led to the guidelines:

- Avoid JavaScript (where appropriate)
- Remove HTML errors and warnings
- Remove elements without content

The following steps can be used on any page to assess if the page is likely to benefit from a rework. Of course I cannot guarantee that the investigation technique can find the root to trouble on any page. And it's not likely that this checklist can replace a thorough investigation (which you'll probably end up with in some cases).

However it might be a good starting point if something is not working or going wrong.

[JavaScript errors](#technique1)\
[HTML errors and warnings](#technique2)\
[Total code weight](#technique3)\
[Content to markup ratio](#technique4)\
[Number of `img` elements](#technique5)\
[Number of `table` elements (used for layout)](#technique6)\
[Total number of elements in the DOM](#technique7)

1. JavaScript errors  
JavaScript errors are important to get rid of as errors in JavaScript prevent your code from running. The Firebug extension for Firefox comes in handy, as it shows a little icon on the statusbar. It's normally a green checkmark (but converts to a red icon and displays the number of JavaScript errors. A click shows the Firebug console with additional information on each error. Goal is to have 0 JavaScript errors.

A little more on JavaScript should be avoided (where appropriate): JavaScript is perfectly OK to use for adding functionality to your page. But, you should probably not use it for things like making a print version of you page (use CSS), or render stuff on your page during load (`document.write`).

2. HTML errors and warnings  
HTML errors and warnings will in most cases lead to browser misinterpretation of your web page (because web standards only describe what to do when HTML is correct). HTML Validator (based on Tidy) comes in handy here: It shows an icon in the status bar. The icon is a green checkmark that changes to a warning icon whenever errors are present (and there is a setting that shows you both the icon and text about how many warnings.

The error messages are mostly good, letting you know exactly where the problem is in the HTML source.

Its realistic to aim for 0 HTML errors and warnings (but on a rare occation there can be reasons for leaving a few warnings in).

3. Total code weight  
The "page info" bookmarklet tells you total code weight. In general, this number should be as low as possible because that means sending fewer bytes to the client, making code easier to interpret for the browser.

Ideally,

4. Content to markup ratio  
Also from the "page info" bookmarklet. The relation between size of content compared to entire footprint of HTML page. The higher ratio the better.

In my experience, pages designed using tables and transparent images for layout has a content/markup ratio around 10-20%. Removing tables and unnecessary pixels easily bring the ratio up on the better side of 50%.

Of course, the exact ratio to aim for is depending on the type of page: The more content-heavy, the better the ratio.

5. Number of `img` elements  
Count number of images with bookmarlet "#img". The number itself should respond approximately to the number of images providing content on the page. Use it to assess if there are transparent images or other images that don't convey any content to the user.

6. Number of `table` elements (used for layout)  
Count number with bookmarklet "#table". Use it to assess if tables are used for layout. Tables should only be used for tabular content. Also, the other bookmarklet "Number table rows" is sometimes handy to count the number of rows used.

7. Total number of elements in the DOM  
Count total number of elements in DOM with the bookmarklet "#elements". In the case study, I had a page with 27,000 DOM nodes (and that was asking for trouble).

All in all, these numbers can hint problems in your page and make it easier to guess what to do about it. I'm using this to estimate which pages to change (and which could be left).

### Summary

These are the basic techniques that have been helpful for me when investigating web standards related issues in web pages. The technique here is complimented with the page describing the [toolbox for locating problems in HTML](/2006/09/18/toolbox).

Related reading:

- [toolbox for locating problems in HTML](/2006/09/18/toolbox)
- [Why web standards matter (case study)](/2006/06/29/webstandards-case-study/)
