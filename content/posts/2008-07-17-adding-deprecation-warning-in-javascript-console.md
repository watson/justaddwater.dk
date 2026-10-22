---
title: "Adding Deprecation Warning in JavaScript Console"
date: "2008-07-17T13:10:49"
slug: "adding-deprecation-warning-in-javascript-console"
url: "/2008/07/17/adding-deprecation-warning-in-javascript-console/"
wp_id: 940
categories: ["Code", "JavaScript"]
tags: ["JavaScript"]
author: "jesper"
---

I used this quick trick today to help me clean up and refactor some javascript functions today:

    if ("console" in window)
      console.warn('DEPRECATED function call to '+ arguments.callee
      +'\nCalled by:\n'+ arguments.callee.caller );

Which results in a fine deprecation warning in the console:\
[{{< img src=`/wp-content/uploads/2008/07/firebug-javascript-caller-callee-debugger-warning.png` alt=`` title=`firebug-javascript-caller-callee-debugger-warning` class=`alignnone size-full wp-image-941` width=`500` height=`249` >}}](http://justaddwater.dk/wp-content/uploads/2008/07/firebug-javascript-caller-callee-debugger-warning.png)

There is plenty of space for improvement here. Feel free to use or tamper ... but please post any alternative suggestions here as a comment.
