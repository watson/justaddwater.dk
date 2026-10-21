---
title: "Creating Passionate Users website printing problems solved in CSS"
date: "2006-09-11T22:22:12"
slug: "passionate-users-printing"
url: "/passionate-users-printing/"
wp_id: 388
categories: []
tags: []
---

*Letter to Kathy Sierra dated August 22nd, 2006, where I discovered some problems with printing pages from her blog: [Creating Passionate Users](http://headrush.typepad.com/ "Kathy Sierra blog: Creating Passionate Users").*

*This is a sidebar story to the blog post "[See you at RailsConf, Europe this Thursday](/2006/09/11/railsconf-europe "Justaddwater.dk: See you at RailsConf, Europe this Thursday")"\*

------------------------------------------------------------------------

Hi Kathy. I really enjoy your passionate articles on the blog. I just found out that I had big problems printing your articles, as I want to use one of your articles as inspiration for a workshop.Print preview in Firefox shows the problem: The main article is printed on a page for itself (but has a "overflow:hidden" rule applied), which means that the article and all comments are ony given one page of print. Besides, left and right column are both printed on separate pages (which for me was a waste of paper: I want the article).I had a look at the HTML + CSS and found the problem. This added at the bottom of your CSS file should sort the problem:

> @media print{\
> \#center{\
> margin: 2em;\
> width: 90%;\
> overflow: auto;\
> }\
> \#left{display:none}\
> \#right{display:none}\
> }

If you want to use it, please do so. Let me know if you have any other questions.\
I'll appreciate if you'll link to my blog at [http://justaddwater.dk/](//) if you find it appropriate.

Kind regards,\
Jesper

PS besides this, I also think you should add you logo to the print pages. Let me know if i can help you with that.\
PPS. I'm attending RailsConf, and looking forward to see you presenting :)

--

--\
Jesper Rønn-Jensen\
Capgemini Danmark A/S\
Oernegaardsvej 16\
DK - 2820 Gentofte\
Denmark\
Blog: [http://justaddwater.dk/](/)
