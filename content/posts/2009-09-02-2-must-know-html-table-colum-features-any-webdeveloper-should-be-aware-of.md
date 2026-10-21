---
title: "2 Must-Know HTML Table Colum Features Any Webdeveloper Should Be Aware Of"
date: "2009-09-02T15:23:49"
slug: "2-must-know-html-table-colum-features-any-webdeveloper-should-be-aware-of"
url: "/2009/09/02/2-must-know-html-table-colum-features-any-webdeveloper-should-be-aware-of/"
wp_id: 1135
categories: ["HTML", "Web Standards"]
tags: ["HTML", "tables", "Web Development", "Web Standards"]
---

I was reading up on the good old HTML specification and discovered a feature I had always wanted -- and it's already there:\
Creating widths of columns that will work like percentages, but will also pay attention to any small, fixed-width columns.

Take a look at HTML's proportional widths and amount alignment features.

Look at this from HTML specification of \<COL\> elements:

> Authors may specify column widths in three ways:
>
> **Fixed**  
> A fixed width specification is given in pixels (e.g., ` width`="30"). A fixed-width specification enables incremental rendering.
>
> **Percentage**  
> A percentage specification (e.g., `width`="20%") is based on the percentage of the horizontal space available to the table (between the current left and right margins, including floats). Note that this space does not depend on the table itself, and thus percentage specifications enable incremental rendering.
>
> **Proportional**  
> Proportional specifications (e.g., `width`="3\*") refer to portions of the horizontal space *required* by a table. If the table width is given a fixed value via the `width` attribute of the [`TABLE`](http://www.w3.org/TR/html4/struct/tables.html#edef-TABLE) element, user agents may render the table incrementally even with proportional columns.However, if the table does not have a fixed width, user agents must receive all table data before they can determine the horizontal space required by the table. Only then may this space be allotted to proportional columns.

Proportional widths! Nice. This means that you can create tables like this example (i have swapped the original HTML4 style to lowercase XHTML):

> Once the (visual) user agent has received the table's data: the available horizontal space will be alloted by the user agent as follows: First the user agent will allot 30 pixels to columns one and two. Then, the minimal space required for the third column will be reserved. **The remaining horizontal space will be divided into six equal portions (since 2\* + 1\* + 3\* = 6 portions)**. Column four (2\*) will receive two of these portions, column five (1\*) will receive one, and column six (3\*) will receive three.
>
> \<table\>\
> \<colgroup\>\
>   \<col width="30"/\>\
> \<colgroup\>\
>   \<col width="30"/\>\
>   \<col width="0\*"/\>\
>   \<col width="2\*"/\>\
> \<colgroup align="center"\>\
>   \<col width="1\*"/\>\
>   \<col width="3\*" align="char" char=":"/\>\
> \<thead\>\
> \<tr\>\<td\> ...\
> ...rows...\
> \</table\>

This leaves me with one big question: How is browser support for \<col width="2\*"\> ????

BONUS: Did you notice the little align feature 'align="char" char=":" ' so that you can correctly align your decimal amounts? I was not aware of that either!

More info in W3C's HTML4 specification "[Calculating the widths of columns](http://www.w3.org/TR/html4/struct/tables.html#h-11.2.4.4)"
