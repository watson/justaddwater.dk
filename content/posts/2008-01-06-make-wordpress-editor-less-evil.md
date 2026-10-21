---
title: "Make Wordpress Editor Less Evil"
date: "2008-01-06T19:26:01"
slug: "make-wordpress-editor-less-evil"
url: "/2008/01/06/make-wordpress-editor-less-evil/"
wp_id: 854
categories: ["Usability", "WordPress"]
tags: []
author: "thomas"
---

This Friday, Jesper and I had a chat about things we don't like about the current WordPress WYSIWYG editor. In particular when trying to write code examples in our posts:

> **Jesper:** One change I really would appreciate in the next Wordpress would be the ability to shift wysiwyg/code editor directly on the edit page
>
> (Now we have to change it on the user prefs page)
>
> **Thomas:** now = today
>
> **Jesper:** aggreed! the sooner the better!
>
> I would like always to put my setting to wysiwyg off and turn it on when editing a post individually. Too often I have burnt my fingers and messed up posts containing code, blockquotes or formatted whitespace
>
> If the control were moved to the edit page I could easily write wysiwyg when needed and avoid it when it would mess up my post
>
> **Thomas:** Yes... it should be possible to tell WordPress that a given post should always open with WYSIWYG off (or on) whenever it is edited... dismissing the default settings
>
> **Jesper:** exactly!
>
> wysiwyg MUST be off by default because it's darn destructive! (at least in the current versions of the wysiwyg editors)
>
> **Thomas:** I wonder if there exists some WP plugins out there that do this already
>
> **Jesper:** Good question!
>
> **Thomas:** ... or even better doesn't mess up custom code or HTML
>
> (I mean... hacks WP so it doesn't)
>
> **Jesper:** I hate the double/single quotes that WP replaces.
>
> All code examples stop working unless the author manually replaces:
>
> '(single quote) with \&#039;
>
> "(double quote) with \&quot;
>
> **Thomas:** I think that there is a simple solution to the quote issue... it must be fairly simple to change that
>
> \*searching for a fix\*
>
> Sent at 11:04 PM on Friday
>
> **Thomas:** hmmm it seems to be hard to find
>
> Is the problem that you write a regular quote and WordPress translates it into a html entity or the other way around?
>
> **Jesper:** The problem is when posting code snippets, HTML or JavaScript for instance. The regular quote (double quote) is automatically translated to the angled double quotes -- the same illness as Word does by default.
>
> It's an illness, in my opinion.
>
> Leave it up to the user to actively change my text
>
> Don't spoil my code snippets by default.
>
> Making normal quotes in normal text pretty is just not a great tradeoff ...
>
> **Thomas:** depends... the quotes them selves look great when wrapping sentences - but doesn't work for code - I agree

After this chat I did some googling and found - as I expected - that we are not alone when it comes to the angled quote issue. The quote replacement is actually called "Smart Quotes" in WordPress, and there is a good discussion on the topic over at [WordPress Support](http://wordpress.org/support/topic/125038 "Please give us the option to turn of smart 'quotes'").

I also found a very good blog-article on the subject by Aaron Russell called "[Trials and tribulations of using WordPress to display code syntax](http://www.milienzo.com/2007/09/06/trials-and-tribulations-of-using-wordpress-to-display-code-syntax/)".

### What we want...

The most optimal solution would be a WordPress plugin that simply disables smart quotes inside \<code\>...\</code\> blocks. To top it of it should also escape the &, \> and \< characters.

### Can you help?

Do you know any plugins that actually do what we would like? Any settings we overlook in WordPress? If not, I guess we will have to convince somebody into changing a future WordPress version.
