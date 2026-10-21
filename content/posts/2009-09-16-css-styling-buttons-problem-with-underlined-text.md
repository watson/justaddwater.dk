---
title: "CSS Styling Buttons Problem with Underlined Text"
date: "2009-09-16T10:32:56"
slug: "css-styling-buttons-problem-with-underlined-text"
url: "/2009/09/16/css-styling-buttons-problem-with-underlined-text/"
wp_id: 1141
categories: ["CSS", "Web Development", "Web Standards"]
tags: ["button", "CSS", "HTML", "input", "Web Standards"]
---

I ran into the challenge the other day to style a\<button\> element to make it look like a link (with underline and everything).

Unfortunately, the \<button\> element does not react to text-decoration: underline;

But according to [a discussion at the CSS Creator forum](http://csscreator.com/node/25902 "CSS Forum: [Solved?] Doctype prevents underline in button input"), there is a way out:

> I was just messing around with it and for some reason this doesn't work:\
> `input {text-decoration:underline;}`\
> but this does:\
> `input {text-decoration:underline;float:left;}`\
> and\
> `input{text-decoration:underline;display:block;}`\
> and\
> `input{text-decoration:underline;position:absolute;}`
>
> Don't ask me... I can't explain this one.

Interesting!

I ended up implementing it as `display:inline-block;` which also works fine. Here is my final rules for styling buttons as links

> .clickable, button.tertiary, input.tertiary{\
>   color: #339;\
>   text-decoration: underline;\
>   display: inline-block; /\* else underline won't work \*/\
>   cursor: pointer;\
>   border: none;\
>   background-color: transparent;\
>   font-size: 1em;\
>   padding: 0;\
> }\
> .clickable:hover, button.tertiary:hover, input.tertiary:hover{\
>   text-decoration: underline;\
>   color: #669;\
> }
