---
title: "3 column CSS layout equal height solved"
date: "2005-11-16T13:18:33"
slug: "3-column-css-layout-equal-height-solved"
url: "/2005/11/16/3-column-css-layout-equal-height-solved/"
wp_id: 10
categories: ["CSS", "Web Standards"]
tags: []
---

Recently the CSS hackers at Position is Everything posted an indepth article "[In search of the one true layout](http://positioniseverything.net/articles/onetruelayout/)". After a couple of reads, it seems that this is the future way of making 3-column page layout. In fact, it can be used for any number of columns.

Eric Meyer thinks this is so good and that "[There's a new \[CSS\] sherif in town](http://meyerweb.com/eric/thoughts/2005/11/01/layout-revolution/ "Eric Meyer blog post: Layout Revolution")".

The idea is to float the columns next to each other directly. Usually this gives you columns of different heights. But here's the brilliant idea: Apply a large `padding-bottom` and an equal large *negative* `margin-bottom`. That's is it! Of course, there are still a few browser quirks to deal with (but they are few compared to previous methods I've been using).

So, it's time for me to forget the previous layout techniques I've been using: Forget all about [faux columns](http://www.alistapart.com/articles/fauxcolumns/), [redmelon](http://www.redmelon.net/tstme/3cols2/) negative margin layout, Eric Costello's [The holy grail](http://glish.com/css/7.asp), and Doug Bowman's [liquid bleach](http://www.stopdesign.com/log/2004/09/03/liquid-bleach.html). Even time to forget the ugly [voice-family hack](http://tantek.com/CSS/Examples/boxmodelhack.html), I hope I'll never use it again.

What's that to do with usability? Well, less CSS hacking gives me more time for usability work! OK, 'nuff said. I think I [read the article](http://positioniseverything.net/articles/onetruelayout/) once more!

Technorati tags: [css](http://technorati.com/tag/css)
