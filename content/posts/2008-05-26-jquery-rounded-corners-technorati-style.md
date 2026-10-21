---
title: "JQuery Rounded Corners (Technorati Style)"
date: "2008-05-26T17:11:14"
slug: "jquery-rounded-corners-technorati-style"
url: "/2008/05/26/jquery-rounded-corners-technorati-style/"
wp_id: 929
categories: ["justaddwater.dk"]
tags: []
author: "jesper"
technorati: ["technorati", "round", "corners", "jquery", "unobtrusive", "javascript", "library", "github"]
---

If you ever use [rounded corners the Technorati way](/2007/02/15/rounded-corners-the-technorati-way/), here is some additional code I created recently.

Usually I add four non-semantic elements to each corner of a div box to round:\
HTML for the box:

``` html
<div class="round">
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

Well, what if you could just write:

``` html
<div class="round">
...
</div>
```

So that the round corners magic was separated semantically away from the HTML code?. This is how you can do it.

The trick is to add the b-elements with jquery. This way i'll append the rounded corners as an extra bonus for enhanced clients understanding javascript.

Create a file named roundcorners.js

``` javascript
// Add rounded corners to all div elements with class="round"
// Adds corners the "technorati way", described on
// http://justaddwater.dk/2007/02/15/rounded-corners-the-technorati-way/
// requires you to set class="round" on div or similar elements
// also works on images, which it wraps in a div element to add the
// necessary content
var round_corners = function(){
 var str = '<b class="cn tl"></b><b class="cn tr"></b><b class="cn bl"></b><b class="cn br"></b>';
  $('.round').addClass("boxc").append(str);
};

$(document).ready( function(){round_corners();});
```

Create a file named roundcorners.css:

``` css
.boxc {
padding:0px;
position:relative;
}
.boxc b.cn {
background:transparent url(roundwhite.png) no-repeat scroll 0%;
height:10px;
position:absolute;
width:10px;
}
.boxc b.tl {
background-position:left top;
left:-1px;
top:-1px;
}
.boxc b.tr {
background-position:right top;
right:-1px;
top:-1px;
}
.boxc b.bl {
background-position:left bottom;
bottom:-1px;
left:-1px;
}
.boxc b.br {
background-position:right bottom;
bottom:-1px;
right:-1px;
}
* html .boxc b.bl {
bottom:-2px;
}
* html .boxc b.br {
bottom:-2px;
}
* html .boxc b.cn {
background-image:url(roundwhite.gif);
font-size:1px;
line-height:1px;
}
```

Put the two image files in the same directory as roundcorners.css:\
[roundwhite.png](http://static.technorati.com/static/css/img/corners/white.png), [roundwhite.gif](http://static.technorati.com/static/css/img/corners/white.gif)

Now in your HTML file header, add references to load JQuery, the css and js file:

``` html
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="roundcorners.js"></script>
<link type="text/css" rel="stylesheet" href="roundcorners.css"></link>
```

Finally, add css class "round" to any div on your page.

I put the code up on Github =\> [jesperronn/jquery-round-corners](http://github.com/jesperronn/jquery-round-corners/tree) . Looking forward to patches and improvements :)\
I would also like a modification that can do the same but works with prototype. Has anybody seen something that does that?
