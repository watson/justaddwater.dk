---
title: "Sharepoint 2007, Accessibility, and Impossible UI Customization"
date: "2008-01-20T20:51:53"
slug: "sharepoint-2007-accessibility-and-impossible-ui-customization"
url: "/2008/01/20/sharepoint-2007-accessibility-and-impossible-ui-customization/"
wp_id: 866
categories: ["Accessibility", "Web Development", "Web Standards"]
tags: []
---

Emil Stenström's recent "[Sharepoint 2007 from an interface developer’s view](http://friendlybit.com/css/sharepoint-2007-from-an-interface-developers-view/)" is definitely worth reading if you care about webstandards, accessibility and decent frontend code in general.\
Here are some of the quotes that really stand out in an excellent article that i really recommend you read before picking your web development platform.

> One major problem is that you still need javascript enabled for many of the accessibility features. Enabling “Accessibility mode”, among other things, makes dropdown menus appear as new windows (popups) instead of dynamically writing HTML to the page. And this is after they “fixed” it.

> Except from core.js, the javascript is spread out all over the place. As usual in many CMS:es, javascript is not treated as a real programming language, so there’s no structuring whatsoever. Sometimes it’s script tags, sometimes inline, sometimes external mini files, and most often automatically generated code. It’s a real mess, and is a big reason for the HTML size being so large. Many of the scripts do not work in browsers other than IE, which means you really need IE to properly use the admin interface.

> The problem is that the system is built so that all of those “out of the box” features are hard to customize. Things like changing how the wiki renders, is really hard. Often it’s easier to rebuild that feature from scratch, than customizing what Sharepoint ships.

Keep an eye out for Emil, as he promises more posts as the project moves on. It's good that people like him write about the ups and downs of development frameworks. And also valuable to share the possible workaround and best solutions -- even when it is formulated like here:

> **Sharepoint 2007, is beyond repair when it comes to interface customization**, and you should do everything in your power to avoid working with it. If I can give one interface developer the arguments to convince a customer to pick another system, this article was worth it.

Read more:

- Emil Stenström: [Sharepoint 2007 from an interface developer’s view](http://friendlybit.com/css/sharepoint-2007-from-an-interface-developers-view/)
- Justaddwater: [Sharepoint Meets Web Standards](/2007/06/04/sharepoint-meets-web-standards/ "Permanent Link to Sharepoint Meets Web Standards") (June 2007)
