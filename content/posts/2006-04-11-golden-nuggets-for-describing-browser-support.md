---
title: "Golden nuggets for describing browser support"
date: "2006-04-11T13:06:50"
slug: "golden-nuggets-for-describing-browser-support"
url: "/2006/04/11/golden-nuggets-for-describing-browser-support/"
wp_id: 168
categories: ["Accessibility", "Browser"]
tags: []
author: "jesper"
---

[Yahoo! Developer Network: Graded Browser Support](http://developer.yahoo.net/yui/articles/gbs/gbs.html)

Super article by Nate Koechley of Yahoo!. He has done an excellent job for describing Yahoo!'s different grades of browser support. For those of you who wonder why not all browsers get the same code. They do. They just interpret it differently. This is what makes front-end web development so hard.

> Support does not mean that everybody gets the same thing. Expecting two users using different browser software to have an identical experience fails to embrace or acknowledge the heterogeneous essence of the Web. In fact, requiring the same experience for all users creates a barrier to participation. Availability and accessibility of content should be our key priority.
>
> Consider television. At the core: TV distributes information. A hand-cranked emergency radio is capable of receiving television audio transmissions. It would be counter-productive to prevent access to this content, even though it’s a fringe experience.
>
> Some viewers still have black-and-white televisions. Broadcasting only in black-and-white — the “lowest common denominator” approach — ensures a shared experience but benefits no one. Excluding the black-and-white television owners — the “you must be this tall to ride” approach — provides no benefit either.
>
> An appropriate support strategy allows every user to consume as much visual and interactive richness as their environment can support. This approach—commonly referred to as *progressive enhancement* — builds a rich experience on top of an accessible core, without compromising that core.

I really like this comparison to TV. What he touches here is actually **user experience**. No web content provider is in control of the customers' user experience. Your web page is seen in different ways beyond your control. Your web page is used in more ways than you can imagine.

Web content providers need to focus on delivering user experience that just works. Browser support is a technical thing that shouldn't be an obstackle. In stead focus should be on providing every browser a decent user experience — In short: Your site should work best with JavaScript and CSS in recent browsers; **Your site should be able to function with a screenreader or a text based browser, with JavaScript disabled, and should be possible to understand with CSS disabled.**
