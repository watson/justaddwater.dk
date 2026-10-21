---
title: "How to limit table cell height (GMail style)"
date: "2006-03-11T17:49:01"
slug: "how-to-limit-table-cell-height-gmail-style"
url: "/2006/03/11/how-to-limit-table-cell-height-gmail-style/"
wp_id: 176
categories: ["Code", "CSS", "Web Standards"]
tags: []
author: "jesper"
---

I just sent this to the [CSS-D discussion list](http://archivist.incutio.com/viewlist/css-discuss/71697 "CSS-D: How to limit table cell height (GMail style)")

> Hope you can help me with this. I want to limit a table cell height to only one line of text. My example below does not work - any height on td is simply ignored if content is long.
>
> Problem here (according to for instance [http://annevankesteren.nl/2004/01/css-tables](http://annevankesteren.nl/2004/01/css-tables) ) is that CSS specification requires table cell to expand to a minimum height of the containing content.
>
> So my question is: How is this solved in for instance GMail where content i only one line high (and additional overflowing content is hidden). Please share your thoughts on this, and if you could point me to any information on how to solve this.
>
> ``` html
> < !DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
> <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
> <head>
> <title></title>
> <style type="text/css">
> table{
> width:300px;
> border:1px dashed red;
> }
> td{
> vertical-align: top;
> background-color: #dfc;
> height: 10px; /* table cell does not obey this height */
> }
> </style>
> </head>
>
> <body>
> <p>I want table row to be the height of 1 text line.</p>
> <table>
> <tr>
> <td>1. start cell not much content</td>
> <td>2. second cell has insanely long content that I know will always wrap</td>
> </tr>
> </table>
> </body>
> </html>
> ```
>
> Any help appreciated,\
> Jesper
>
> -- Jesper Rønn-Jensen Capgemini Danmark A/S [http://justaddwater.dk/](/) (weblog)

[Example page - not working](/wp-content/uploads/2006/03/fixed-table-cells-notworking.html)

I'll post the results here as I find out how Google GMail does the trick. Please share any tricks that you know of here. Oh, for your information, solution must work in Internet Explorer...

*UPDATE: Now working!* Thanks to the information at [BlakeMS blog](http://www.blakems.com/archives/000077.html "BlakeMS.com: Using text-overflow"), I now got it working (no Javascript necessary).

> Now this works the same with table cells. See below and note that you must set table to have the table-layout: fixed property for it to work.
>
> ``` css
> .tbl {
>     table-layout:fixed;
>     border-top: 5px solid #333;
>     border-collapse: collapse;
>     background: #fff;
>      }
> .tbl td {
>     border-bottom: 1px dashed #333;
>     padding: 2px 5px;
>     text-overflow:ellipsis;
>     overflow:hidden;
>     white-space:nowrap;
>  } 
> ```

Note that he also adds `white-space:nowrap`. Otherwise it won't work. [Example page - working](/wp-content/uploads/2006/03/fixed-table-cells-working.html)
