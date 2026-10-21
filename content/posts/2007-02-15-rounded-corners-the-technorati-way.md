---
title: "Rounded Corners the Technorati Way"
date: "2007-02-15T12:01:05"
slug: "rounded-corners-the-technorati-way"
url: "/2007/02/15/rounded-corners-the-technorati-way/"
wp_id: 550
categories: ["Code", "CSS", "HTML", "Web Standards"]
tags: []
---

It's been a while where web standards don't get the attention it deserves on this blog. In that spirit, here's a behind-the-scenes view on how Technorati makes rounded corners on a faded background.

![Technorati screenshot of box with rounded corners on faded background (showing Justaddwater Ranks no. 9980 on Technorati)](/wp-content/uploads/2007/02/technorati-rounded-corner-justadwater-rank-9980-mini.png)

I remember Eric Meyer mentioned this solution back at a workshop in 2005 (before he could actually tell that it was for Technorati — the redesign was unveiled a few days later).

### Technique

HTML for the box:

``` html
<div class="bloginfo-summary boxc">
  <h2>..</h2>
  <ul>
    <li>..</li>
    ..
  </ul>
  <b class="cn tr"></b>
  <b class="cn br"></b>
  <b class="cn tl"></b>
  <b class="cn bl"></b>
</div>
```

The HTML is then styled with the following CSS:

``` css
div.bloginfo-summary {background:
  url(http://static.technorati.com/static/css/img/bg/fade-lightgreen.png) repeat-x;
  float:left;margin-bottom:20px;padding:10px;width:690px}
/* Large radius image backgrounds */
.boxc {position:relative;}
.boxc b.cn { height: 10px; width: 10px; background:
 url(http://static.technorati.com/static/css/img/corners/white.png) no-repeat;
 position:absolute;
 }
.boxc b.tl {top: -1px; left: -1px; background-position: top left;}
.boxc b.tr {top: -1px; right: -1px; background-position: top right;}
.boxc b.bl {bottom: -1px; left: -1px; background-position: bottom left;}
.boxc b.br {bottom: -1px; right: -1px; background-position: bottom right;}

/* IE Filters */
    * html .boxc b.bl {bottom:-2px}
    * html .boxc b.br {bottom:-2px}
    * html .boxc b.cn {background-image:
       url(http://static.technorati.com/static/css/img/corners/white.gif);
       line-height: 1px;
       font-size: 1px;
      }
```

So, graphically displayed, the `<b>` elements are actually positioned in each corner with no content:

![Technorati screenshot of box with rounded corners on faded background showing HTML elements](/wp-content/uploads/2007/02/technorati-rounded-corner-html-tags-mini.png)

Note that the background-image for the faded box is one thin sliced faded image:\
![technorati faded background slice](http://static.technorati.com/static/css/img/bg/fade-lightgreen.png)

The corners is made with only one image that's positioned differently depending on which corner it's in. The image is actually a transparent circle on white background.

![technorati rounded corner image](http://static.technorati.com/static/css/img/corners/white.gif) shown on dark background for clarity.

So I [included the final example on a separate page](/wp-content/uploads/2007/03/technorati-style-rounded-corners.html "Example page: technorati-style rounded corners") (because the Wordpress editor doesn't let me add the HTML code precisely as it's required)

[example page: technorati-style rounded corners](/wp-content/uploads/2007/03/technorati-style-rounded-corners.html "Example page: technorati-style rounded corners")

More info\
Eric Meyer: [Technorati Redesigns](http://meyerweb.com/eric/thoughts/2005/06/21/technorati-redesigns/) (June 2005)\
Smileycat: [CSS Rounded Corners Roundup](http://www.smileycat.com/miaow/archives/000044.html)
