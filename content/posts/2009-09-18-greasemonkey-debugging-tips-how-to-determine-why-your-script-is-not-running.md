---
title: "Greasemonkey Debugging Tips: How to Determine Why your Script Is Not Running"
date: "2009-09-18T22:27:03"
slug: "greasemonkey-debugging-tips-how-to-determine-why-your-script-is-not-running"
url: "/2009/09/18/greasemonkey-debugging-tips-how-to-determine-why-your-script-is-not-running/"
wp_id: 1144
categories: ["Web Development"]
tags: ["greasemonkey", "Web Development"]
author: "jesper"
---

After running into some trouble with getting a Greasemonkey to work, I just wanted to share this list with you of things to look out for when your Greasemonkey script does not seem to run. What are the common pitfalls you see around. I'll gladly add them here.

I am trying to get a Greasemonkey script to run on a page. But it does not. How do you debug scripts?\
What are the smallest possible baby-steps to start a new Greasemonkey script?

----------

You can alert a message:

alert('hello from Greasemonkey')

if this does not work, you probably need to check if your included sites match the current URL.

For instance, I had to change from

// @include        http://www.lavpriskoekken.dk/shop/\*

to

// @include        http://\*lavpriskoekken.dk/shop/\*

----------

You can write logs everywhere in your scripts to get better traces of what if being done in them:

GM_log("Hello, World!");

If this does not work, check your settings in Firebug console. Set checkmark at:\
\* Show Chrome Errors\
\* Show Chrome Messages

http://wiki.greasespot.net/GM%5Flog

More info: http://wiki.greasespot.net/Greasemonkey%5FManual%3AOther%5FUseful%5FTools#JavaScript%5FConsole

----------

Problem with @require statements:

Adding a line in your config like this:\
// @require        http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.js

makes you able to use jQuery directly. Test it like so:\
alert(jQuery.toString() );

if that does not work, then you have probably added the @require statement after installing/creating the script. Try to uninstall the script, and then reinstall it again.
