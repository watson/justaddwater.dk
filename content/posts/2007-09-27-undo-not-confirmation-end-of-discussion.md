---
title: "Undo — Not Confirmation — End of Discussion"
date: "2007-09-27T09:19:36"
slug: "undo-not-confirmation-end-of-discussion"
url: "/2007/09/27/undo-not-confirmation-end-of-discussion/"
wp_id: 718
categories: ["Usability", "User experience"]
tags: []
---

Asa Raskin has made a really useful example of how to implement undo easily in user interfaces. Here's the example file (linked directly to a page at his company Humanized). Try deleting some items and then press undo.

[Embedded content: http://humanized.com/weblog/images/resources/undo/todo.html](http://humanized.com/weblog/images/resources/undo/todo.html)

Note how there is no confirmation when you delete and the items can come back pressing undo.

I really like this approach, and have long been pushing for a similar approach in projects I have worked with recently.

Now, there is a constant resistance (usually from a technical perspective), when discussing undo. And in the project I have worked in, none of them eventually decided to have undo. Here are the reasons I have heard from customers deciding not to implement undo:

1.  Afraid of high technical costs
2.  Prioritized new functionality higher than undo
3.  Did not acknowledge the importance of undo from a user perspective
4.  Did not acknowledge the annoyance of having to confirm the action over and over

In case you missed the A List Apart article by Asa, go read his brilliant "Never use a warning when you mean undo". I could not agree more.

More info:\
Alistapart: [Never Use a Warning When You Mean Undo](http://www.alistapart.com/articles/neveruseawarning/)\
Humanized: [Undo Made Easy with Ajax (Part 1)](http://humanized.com/weblog/2007/09/14/undo-made-easy-with-ajax-part-1/) and [part 1.5](http://humanized.com/weblog/2007/09/21/undo-made-easy-with-ajax-part-15/)
