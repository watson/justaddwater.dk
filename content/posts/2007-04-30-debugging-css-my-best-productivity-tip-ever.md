---
title: "Debugging CSS: My Best Productivity Tip Ever"
date: "2007-04-30T00:07:26"
slug: "debugging-css-my-best-productivity-tip-ever"
url: "/2007/04/30/debugging-css-my-best-productivity-tip-ever/"
wp_id: 590
categories: ["Code", "CSS", "Errors", "Productivity", "Web Development"]
tags: []
---

Firebug keeps surprising me. I've recently been working on code for several web designs and this little trick helped me to understand existing HTML and CSS much faster. Just to give an example I use our Justaddwater RSS feed page (but could be any page).

Before you start, [get Firebug](http://www.getfirebug.com/) for Firefox (if you haven't got it already).

1.  \
2.  Press F12 and the Firebug window appears below in the browser window
    \
3.  Start the HTML inspector and mouse over any element, you want to learn about.\
    [![firebug-css-tip-start-html-inspector-thumb.png](/wp-content/uploads/2007/04/firebug-css-tip-start-html-inspector-thumb.png)](/wp-content/uploads/2007/04/firebug-css-tip-start-html-inspector.png "firebug-css-tip-start-html-inspector.png")
    \
4.  Now, you can see the HTML, the hierachy,and the CSS rules. For me it has been very useful, that overridden CSS rules are marked with strikethrough text. That's a very handy information when CSS specificity plays in with a trick or two.
    \
5.  Press escape to stop inspector mode, and move mouse down to CSS rules.
    \
6.  Mouse over the CSS rules reveal a small icon to toggle the line. See screenshot animation below.
    

![firebug-css-bugfix-toggle.gif](/wp-content/uploads/2007/04/firebug-css-bugfix-toggle.gif)

This trick will probably completely replace my use of "edit CSS" in [Webdeveloper toolbar](https://addons.mozilla.org/en-US/firefox/addon/60 "Web developer toolbar Firefox Add-on"), the nifty [CSSViewer add-on](https://addons.mozilla.org/en-US/firefox/addon/2104 "CSSViewer Firefox Add-on"), and the [mouseover DOM inspector](http://slayeroffice.com/tools/modi/v2.0/modi_help.html "Slayeroffice: Modi2 (mouse over DOM inspector) by Steve Chipmann") bookmarklet.

Related info:

- \
- Justaddwater: [Web developer’s collection of browser tool](/2005/11/30/web-developers-collection-of-browser-tools/ "Permanent Link: Web developer’s collection of browser tools") (November 2005)
  \
- [Firebug keyboard shortcuts](http://www.getfirebug.com/keyboard.html)
  \
