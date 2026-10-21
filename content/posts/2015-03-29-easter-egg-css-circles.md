---
title: "Easter egg CSS circles"
date: "2015-03-29T19:49:11"
slug: "easter-egg-css-circles"
url: "/2015/03/29/easter-egg-css-circles/"
wp_id: 1747
categories: ["Code", "CSS"]
tags: []
author: "jesper"
---

We are approaching easter, and I couldn't resist to make eggs on the project I am working on these days:

Now:

 

[![screenshot-with-easter-eggs](/wp-content/uploads/2015/03/screenshot-with-easter-eggs-300x222.png)](/wp-content/uploads/2015/03/screenshot-with-easter-eggs.png)

Before

 

 

[![screenshot-without-easter-eggs](/wp-content/uploads/2015/03/screenshot-without-easter-eggs-300x194.png)](/wp-content/uploads/2015/03/screenshot-without-easter-eggs.png)

 

The trick is really easy. CSS border radius can be applied in ellipsis shapes. Each corner has a  vertical and a horizontal radius. So you really just have to change the vertical radius of each corner like this:

 

[![Screen Shot 2015-03-27 at 09.59.44](/wp-content/uploads/2015/03/Screen-Shot-2015-03-27-at-09.59.44-300x99.png)](/wp-content/uploads/2015/03/Screen-Shot-2015-03-27-at-09.59.44.png)

And voila, the 60% and 40% vertical radius will do the trick.

 

I can highly recommend this really interesting presentation from Lea Verou on border-radius. It's 14 minutes and highly worth the time.

 

https://www.youtube.com/watch?v=JSaMl2OKjfQ

 

Also, CSS Tricks has a collection of pre-cooked css shapes for inspiration: [CSS-Tricks.com:ShapesOfCSS](https://css-tricks.com/examples/ShapesOfCSS)
