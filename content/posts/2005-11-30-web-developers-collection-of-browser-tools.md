---
title: "Web developer's collection of browser tools"
date: "2005-11-30T16:03:03"
slug: "web-developers-collection-of-browser-tools"
url: "/2005/11/30/web-developers-collection-of-browser-tools/"
wp_id: 29
categories: ["AJAX", "CSS", "JavaScript", "Links", "Web Standards"]
tags: []
author: "jesper"
---

With the release of Firefox 1.5, I thought it's time to make a round up on the tools and plugins that makes my everyday work faster, more efficient. Here are some of my favorite tools for Firefox and a few for Internet Explorer.

### FireFox extensions

[HTML validator](http://users.skynet.be/mgueury/mozilla/) (based on Tidy) — Validates all pages I visit and shows an icon based on the result. Discreet, unobtrusive and very effective in showing that pages are valid. One note, though: HTML Tidy seems to be more strict than the ordinary [HTML validator](http://validator.w3.org/check), so a valid page sometimes shows errors. I see it this way: If this plugin validates, the code validates!

[Live HTTP Headers](http://livehttpheaders.mozdev.org/) — Good tool for debugging AJAX calls and a good tool to learn about other interesting webservices. Turn it on and visit Google Maps. It will show all about the calls your browser makes to the webserver. Also, it shows what HTTP headers your browser send, and what it recieves.

[IE view](http://ieview.mozdev.org/) — Right click a page to show the page in IE.

[Screen grab!](http://andy.5263.org/screengrab/) — Easy screenshots of your browser window (requires Java). It works very good for me, as I do a lot of prototyping work and print screenshots.

[Add N Edit Cookies](http://addneditcookies.mozdev.org/) — I like [View Cookies](http://www.bitstorm.org/extensions/view-cookies/) more, but this one can also edit the cookie value.

[Adblock](http://adblock.mozdev.org/) — I have a disability: It's the opposite of banner blindness: Banner distraction. I'm sometimes so distracted by banner ads that I cannot read text. Adblock removes annoying banner ads. Recently I also started using [Adblock Filterset.G Updater](https://addons.mozilla.org/extensions/moreinfo.php?id=1136)

[Slim Extension List](http://v2studio.com/k/moz/) — Collapses extension list and makes it easier to see what extensions I have.

[Web developer toolbar](http://chrispederick.com/work/webdeveloper/) — Impressive collection of web developer tools. See below for details.

### Web developer toolbar for Firefox

This is an impressive collection of tools. Easy to turn on/off JavaScript, CSS, images, Java. You can mark deprecated elements, show ID and class details and much, much more. The [web developer toolbar](http://chrispederick.com/work/webdeveloper/) website has more details, I just want to point out these few keyboard shortcuts I use:

- CTRL-SHIFT-E: CSS live edit
- CTRL-SHIFT-A: HTML validator of local file
- CTRL-SHIFT-S: Toggle CSS stylesheets on/off

Unfortunately, Display ID and class details has no keyboard shortcut (probably the feature I use the most). I must say that the developers has done a good work for accessibility by implementing keyboard shortcuts. Nice!

### IE developer toolbar

Via the [IE blog](https://blogs.msdn.com/ie/archive/2005/09/16/469686.aspx) I learned about the IE developer Toolbar. It's like web developer toolbar for Firefox, only smaller (less functions). It has a DOM inspector, though, which is kind of cool when I sometimes see that Firefox and IE DOM models differ.

### Fiddler HTTP header viewer for IE

[Fiddler](http://www.fiddlertool.com/fiddler/) is a power tool for Internet Explorer and is fantastic for debugging. Its like Live HTTP Headers for Firefox and in addition it has the ability to view the content of the HTTP packets. Indispensable for debugging, but last time I used it, it lacked support of https protocol. So I couldn't debug on websites with secure login. Hope they fix this in a future release. Heres an [article on using Fiddler as a debugging tool](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnwebgen/html/IE_IntroFiddler.asp).

### Bookmarklets

In addition to this, I have installed some bookmarklets in my browser. Bookmarklets are also called Favelets. Basically, it's a URL made of JavaScript.

Some bookmarklets for investigating the webpage\
Steve Chipman working for AOL has a good collection. [Slayeroffice favelet suite](http://slayeroffice.com/?c=/content/tools/suite.html), [mouseover DOM inspector](http://slayeroffice.com/tools/modi/v2.0/modi_help.html), and [page info](/wp-admin/post.php?action=edit&post=29) are my favorites.\
Jesse Ruderman has an impressive [collection of bookmarklets](http://www.squarefree.com/bookmarklets/). Some of them are already included in Web Developer Toolbar. My favorites are [JavaScript Shell](http://www.squarefree.com/shell/), [View javascript variables](http://www.squarefree.com/bookmarklets/webdevel.html#view_variables), [computed CSS Style](http://www.squarefree.com/bookmarklets/webdevel.html#computed_styles). As a side node I suggested some impovements to Javascript Shell which Jesse [added to the current version](http://www.squarefree.com/2005/10/30/javascript-shell-14/).

One final bookmarklet. I made my own **cookie editor**. Its limited to your current domain and shows all cookies as a list. You can edit both the name and the value. A link is available on my [bookmarklet page](http://visitjesper.homeip.net/bookmarklets.html) on VisitJesper, my personal website. It works both in Firefox and IE.

Other tools worth a mention:\
[Drip IE leak detector](http://www.outofhanwell.com/ieleak/) — I know about this tool and will definately try it out next time I'm about to hunt memory leaks in JavaScript.\
[CSS Vista](http://www.sitevista.com/cssvista/) from the [SiteVista](http://www.sitevista.com/) team. A tool where you can live-edit CSS and view the result simultaneously in Firefox and IE.

### Read more and give feedback

If you want more, there is a good presentation about [Rapid web development and testing with Firefox](http://lesliefranke.com/index.php/2005/08/22/rapid-web-development-and-testing-with-mozilla-firefox/). Please share with me, what tools you use in webdevelopment, and why.

Technorati tags: [firefox](http://technorati.com/tag/firefox) [extension](http://technorati.com/tag/extension) [webdeveloper](http://technorati.com/tag/webdeveloper)[webdevelopment](http://technorati.com/tag/webdevelopment) [ie](http://technorati.com/tag/ie) [microsoft](http://technorati.com/tag/microsoft) [webstandards](http://technorati.com/tag/webstandards) [cssvista](http://technorati.com/tag/cssvista) [sitevista](http://technorati.com/tag/sitevista) [fiddler](http://technorati.com/tag/fiddler) [bookmarklet](http://technorati.com/tag/bookmarklet) [favelet](http://technorati.com/tag/favelet)
