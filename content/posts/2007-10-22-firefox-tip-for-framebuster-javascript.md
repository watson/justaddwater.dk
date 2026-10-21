---
title: "Firefox Tip For Framebuster JavaScript"
date: "2007-10-22T13:30:06"
slug: "firefox-tip-for-framebuster-javascript"
url: "/2007/10/22/firefox-tip-for-framebuster-javascript/"
wp_id: 748
categories: ["Browser", "JavaScript", "Web Development"]
tags: ["JavaScript"]
---

I have for long been struggling with an internal legacy application that wraps the content page in a frameset. Very annoying because I have spent some time to reverse engineer a poor-mans API to the application.

Problem: An inline "reverse" framebuster script that makes sure that everything is nicely(?) wrapped in the frameset. As you see it's included inline in the HTML.

``` javascript


  url = "application_url";
  if (parent.frames[0]) {
    if (parent.frames[0].name != 'FrameMain') {
      document.location.replace(url);
    }
  }else{
    document.location.replace(url);
  }
```

One thing is I never understood the thing about putting everything in a frameset. In this case, I have not been able to change the code. But as I have to use the application every now and then, the big question is:

**How to change or remove the inline JavaScript, and make sure the framebuster is ignored?**

I did not think this was possible until I got this answer from "esquifit" in the [Greasemonkey user goup](http://groups.google.com/group/greasemonkey-users):

> You do not need GM nor Opera for this task. Firefox comes with a\
> built-in capability for allowing/disallowing access to\
> properties/methods of DOM Objects on a per-site basis. It is called\
> Configurable Security Policies (CAPS) and it is described in \[1\].\
> Further examples and explanations are provided for example in \[2\] and\
> \[3\].\
> A short guide assuming the simplest case:\
> 1\) Close Firefox\
> 2\) Locate your profile folder \[4\]\
> 3\) Locate the file user.js within this folder. If it does not exist,\
> create it with a \*text\* editor (Notepad, vim, etc.), not with a 'word\
> processor' (MS Word, OpenOffice.org, Wordpad, etc.)\
> 4\) Add the following lines to user.js:\
> user_pref("capability.policy.policynames", "noframebuster");\
> user_pref("capability.policy.noframebuster.sites",\
> "[http://www.annoying-site.com](http://www.annoying-site.com/)");\
> user_pref("capability.policy.noframebuster.Location.replace", "noAccess");\
> Of course, you will have to replace the domain with the one you want to prevent from redirecting your frames.

Find the entire discussion here:

- \
- Greasemonkey users group: "[How to ignore framebuster script](http://groups.google.com/group/greasemonkey-users/browse_thread/thread/42a64be1aa31e1d8/76df7564697e076a#76df7564697e076a)"
  \
