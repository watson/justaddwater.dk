---
title: "Internal Apps In Firefox"
date: "2009-09-23T12:28:46"
slug: "internal-apps-in-firefox"
url: "/2009/09/23/internal-apps-in-firefox/"
wp_id: 1152
categories: ["Accessibility", "Browser", "capgemini"]
tags: ["Accessibility", "capgemini", "firefox", "greasemonkey", "login", "workaround"]
---

This post is probably highly irrelevant unless you work at Capgemini and want to use the [internal nordic applications](http://applications.capgemini.se/) in Firefox.

Read on if you want to access systems like CTR (time reporting), Event calendar, Skills database, PDR, Project forms or similar applications in Firefox.

Problem is that the systems are not accessible at all if you're not logged in. The reason is some extremely malformed HTML. Here is the entire content of the HTML page sent out:

> \<!-- CFIF (#Cookie.CFId# LT 10000) --\>\
> \<!-- CFLOCATION URL="/applikationer/Login/CleanUp.cfm" Addtoken="NO" --\>\
> \<!-- /CFIF ---\>
>
> \<HTML\>\
> \<HEAD\>\
> \<TITLE\>CTR System\</TITLE\>\
> \</HEAD\>
>
> \<!-- No Cookie --\>
>
> \<FORM Name="ssoRedirect" Method="Post" Action="https://sso.capgemini.com/gate.asp"\>\
> \<INPUT Type = "hidden" Name="calling_url" Value="http://applications.capgemini.se/Applications/CTR/CTR.cfm?"\>\
> \<INPUT Type = "hidden" Name="server_identifier" Value="applications.capgemini.se"\>\
> \</FORM\>
>
> \<SCRIPT Language="javascript"\>\
> document.forms\['ssoRedirect'\].submit()\
> \</SCRIPT\>

Several problems here: Content outside of HTML element. No body element. No end HTML tag. And the most critical that triggers this particular problem: The form element and the SCRIPT element are outside the body.

IE has an interpretation of this illegal structure: It creates a body element and fills in the SCRIPT and FORM tag into them.

Firefox guesses differently. It moves the FORM element to the body as well, but the SCRIPT element is put in the HEAD section. The consequence is that the form submit happens before the FORM element is rendered. And it gives a JavaScript error that the form is not found.

I wrote a Greasemonkey script that essentially posts the form again (and Greasemonkey is not triggered until DOM is loaded).

Install greasemonkey script:

[capinternal_systems_login_nordic_apps.user.js](/wp-content/uploads/2009/09/capinternal_systems_login_nordic_apps.user.js) (version 1.0 created 2009-09-23)

If you want to improve on it or add more for more internal systems, feel free to fork this gist on Github <http://gist.github.com/191896>
