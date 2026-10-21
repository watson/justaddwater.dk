---
title: "IE 7, web standards and CSS support"
date: "2006-08-28T09:29:04"
slug: "ie-7-web-standards-and-css-support"
url: "/2006/08/28/ie-7-web-standards-and-css-support/"
wp_id: 384
categories: ["Browser", "CSS", "User Interface", "Web Development", "Web Standards"]
tags: []
author: "jesper"
technorati: ["internet explorer", "ie 7", "microsoft", "browser", "css", "standalone", "web standards", "strict mode", "quirks mode"]
---

The Internet Explorer team is preparing to ship the next major version of the world's most popular browser. The IE team has written an update on which CSS bugfixes that will make it into the final release.

### Update of existing CSS on websites

Before we get to that rather long list, I feel it's important to know what will change from the web developer's point of view. The update list is a must read to anybody responsible for a website rendered in web standards mode (so called "[strict mode](http://www.quirksmode.org/css/quirksmode.html "Peter Paul koch: CSS: Quirks mode and strict mode")"). For IE7 backwards compatibility, changes are not applied in quirksmode.

Personally and professionally I've been using strict mode for a long time (as it made IE6 pages look more like Firefox pages), and that means that I probably have to check my previous pages with IE7, at least to make sure that they don't rely on any of the bugs mentioned below.

To sum it up your pages are probably safe and renders the same way in IE7 as in IE6 in the following situations:

- If they render in quirks mode
- If they render in strict mode but don't rely on the bugs below to filter out information from IE

So the safest thing is probably to check existing CSS files for use of the bugs that the IE team fixed in IE7.

### CSS bugs fixed

On IE blog, the following list of [CSS bugs that IE7 will fix](http://blogs.msdn.com/ie/archive/2006/08/22/712830.aspx "IEBlog: Details on our CSS changes for IE7"):

> **Here is the list of CSS features and changes for IE7:**
>
> **Bugs we fixed**
>
> - All bugs on [positioniseverything.net](http://www.positioniseverything.net/explorer.html) except the “escaping floats” bug (which is planned for the future)
>   - [Peekaboo Bug](http://www.positioniseverything.net/explorer/peekaboo.html)
>   - [Internet Explorer and Expanding Box Problem](http://www.positioniseverything.net/explorer/expandingboxbug.html)
>   - [Quirky Percentages](http://www.positioniseverything.net/explorer/percentages.html)
>   - [Line-height bug](http://www.positioniseverything.net/explorer/lineheightbug.html)
>   - [Border Chaos](http://www.positioniseverything.net/explorer/border-chaos.html)
>   - [Disappearing List-Background bug](http://www.positioniseverything.net/explorer/ie-listbug.html)
>   - [Guillotine Bug](http://www.positioniseverything.net/explorer/guillotine.html)
>   - [Unscrollable Content bug](http://www.positioniseverything.net/explorer/unscrollable.html)
>   - [Duplicate Characters Bug](http://www.positioniseverything.net/explorer/dup-characters.html)
>   - [IE and Italics](http://www.positioniseverything.net/explorer/italicbug-ie.html)
>   - [Doubled Float-Margin bug](http://www.positioniseverything.net/explorer/doubled-margin.html)
>   - [Duplicate Indent bug](http://www.positioniseverything.net/explorer/floatIndent.html)
>   - [Three pixel text jog](http://www.positioniseverything.net/explorer/threepxtest.html)
>   - [Creeping Text bug](http://www.positioniseverything.net/explorer/creep.html)
>   - [Missing First letter bug](http://www.positioniseverything.net/explorer/firstletter.html)
>   - [Phantom box bug](http://www.positioniseverything.net/explorer/inlinelist.html)
>
> **Details on some of the other bugs (from sources other than the positioniseverything.net list) that we fixed:**
>
> - Overflow now works correctly! (That means boxes do not automatically grow any more.)
> - Parser bugs: \* html, \_property and /\*\*/ comment bug
> - Select control: CSS style-able and not always on top
> - Auto-sizing of absolute positioned element with width:auto and right & left (great for 3 column layouts)
> - Addressed many relative positioning issues
> - Addressed many absolute positioned issues
> - % calculations for height/width for abs positioned elements <http://channel9.msdn.com/ShowPost.aspx?PostID=191182>
> - \< ?xml\> prolog no longer causes quirks mode
> - HTML element truly independent of the Body (now gets its own width, height etc.)
> - 1 px dotted borders no longer render as dashed
> - Bottom margin bug on hover does not collapse margins
> - Several negative margin issues fixed
> - Recalc issues including relative positioning and/or negative margins are fixed now
> - CLSID attribute of
>   tag no longer limited to 128 characters
> - :first-letter whitespace bug described in <http://blogs.msdn.com/ie/archive/2005/09/02/460115.aspx> fixed
> - Descendant selector now works properly for grand children when combined with other selectors
> - First-line and first-letter now applies when there is no space between word :first-line and opening brace {
> - Pseudo-classes now are working as expected if selector is excluded
> - The :link selector works now for anchor tag with href set to bookmark
> - Addressed !important issues
> - PositionIsEverything [piefecta-rigid](http://www.positioniseverything.net/piefecta-rigid.html).htm now works
> - List-item whitespace bug fixed
> - Fixed Absolutely [Buggy](http://positioniseverything.net/abs_relbugs.html) II
> - Absolute positioned elements now use always correct containing block for positioning and size information
> - Nested block elements now respect all overflow declarations (hidden, scroll, etc)
> - Fixed the opposing offset problem (absolute positioned element whit all four top, bottom left and right are present)
> - tags nested within LI elements will no longer add extra bottom margin when hover occurs
> - We no longer lose the image aspect ratio on refresh
> - Cleaned up our ident parsing according to CSS2.1 rules
> - Fixed parsing bugs for multi- class selectors and class selectors that are combined with id selectors
> - And many more
>
> **We also extended our existing implementations to comply with W3C specifications:**
>
> - Enable :hover on all elements not just on
> - Background-attachment: fixed works on all elements – so [Eric Meyer’s complexspiral demo](http://meyerweb.com/eric/css/edge/complexspiral/glassy.html) works
> - Improved
>   fallback
>
> **Finally, we added new features from CSS2.1:**
>
> - Min/max width/height support (also for images, which did not work in IE7b2)
> - Transparent borders
> - Fixed positioning support
> - Selectors: first-child, adjacent, attribute, child
>   - A couple of CSS 3 attribute selectors: prefix, suffix and substring since we were working already in the code base (also the general sibling selector)
> - Alpha channel PNG support (Not a CSS feature but too important for designers to not call it out)

### Web standards support: Web development Nirvana

The better support of web standards is a major leap forward to web developers and website responsibles. This is a step towards "web development Nirvana" where a website only has to be written in one way. No browser specific hacks or quirks are needed in web development nirvana, because all browsers (eventually) understand HTML and CSS the same way.

However, even IE7 web standards support is a giant improvement over IE6, there are still a long way to go before we can acheive that ultimate goal. According to Nate Koecheley of Yahoo!, there are currently over 10,000 different combinations browser versions and operating systems (see [Golden nuggets for describing browser support](/2006/04/11/golden-nuggets-for-describing-browser-support/ "Permanent Link to Golden nuggets for describing browser support")). So there is still plenty of work for anybody who understands browser quirks, bugs, hacks and anomalies of different browsers on different platforms.

### Test IE7 and IE6 side by side

I have previously written about how to run [IE7 beta side by side with IE6](/2006/02/03/ie7-beta-running-side-by-side-with-ie6/ "Permanent Link to IE7 beta running side by side with IE6"). But according to Jon Galloway (inventor of the trick), this only works up to [before IE7 Beta 3](http://weblogs.asp.net/jgalloway/archive/2005/12/28/434132.aspx "Jon Galloway: IE7 Standalone Launch Script"). But the good thing is that he is working on an update.

I hope to learn that somebody are able to "flip around" this solution (so that we can get IE 6 to run as standalone in the same way as IE3, IE4, IE5, IE5.5). Please let us know if you already know how to do that trick.

**Update: [All IE Browsers Standalone On Same PC](/2006/09/28/all-ie-browsers-standalone-on-same-pc/ "Justaddwater.dk: All IE Browsers Standalone On Same PC") (September 28, 2006) solves the problem.**
