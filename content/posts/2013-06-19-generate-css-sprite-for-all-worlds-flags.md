---
title: "Generate CSS sprite for all world's flags"
date: "2013-06-19T13:46:24"
slug: "generate-css-sprite-for-all-worlds-flags"
url: "/2013/06/19/generate-css-sprite-for-all-worlds-flags/"
wp_id: 1594
categories: ["justaddwater.dk"]
tags: []
author: "jesper"
---

Recently i worked on a project, which had to use flag icons for all flags in the world. The implementation looked like this:

css file:

.

 

 

In order to reduce the number of HTTP requests, I wanted to change it to using CSS sprites instead.

 

CSS file now has changed to lines like this:

.er_16{ background-position: -20px 0; }\
.es_16{ background-position: -20px -20px; }\
.et_16{ background-position: -20px -40px; }\
.fi_16{ background-position: -20px -60px; }

 

\> Generation of sprite: http://spritegen.website-performance.org/

\> \* Upload zip file with flags (in my case all the 16x16 px flags)\
\> \* ignore duplicate images\
\> \* build direction vertical\
\> \* offset 4px (since the images are 16x14, this will make a 20-20 grid)\
\> \* background/transparency colour: \#ffffff\
\> \* output format: PNG\
\> \* Compress Image with OptiPNG: YES\
\> \* Number of colours: True colour\
\> \* css suffix: \_16 (to indicate 16px icons)

 

Oh, before creatign the zip file, I removed all countries not matching a two-letter code.

cd 16/

find . -type f -name '???????\*' \|xargs -I{} rm {}

This would remove countries named "\_African Union.png", "\_United Nations.png", "Olimpic Movement.png"  and similar.

 

 

For the following sizes of flags, I used these offset values:

16px, offset 4px will make a 20px grid

24px, offset 6px will make a 30px grid

32px, offset 8px will make a 40pxgrid

48px, offset 2px will make a 50px grid

64px, offset 6px will make a 70px grid

128px, offset 2px will make a 130px grid
