---
title: "Count number of jobs in Hudson"
date: "2012-06-14T11:42:53"
slug: "count-number-of-jobs-in-hudson"
url: "/2012/06/14/count-number-of-jobs-in-hudson/"
wp_id: 1596
categories: ["Web Development"]
tags: ["hudson", "JavaScript", "jenkins"]
author: "jesper"
---

I wanted to count the number of jobs running on a Hudson server (continuous integration) at work.

 

This javascript counts the number of lines in the table with all jobs:

 

document.getElementById("projectstatus").children\[0\].children.length

 

Or save this as a browser toolbar bookmarklet:

Name: #HudsonJobs\
 javascript:(function(e){alert(document.getElementById("projectstatus").children\[0\].children.length);e.preventDefault()})()

This line finds the table with id="projectstatus", and counts the TR elements inside of it's TBODY.

At work it said 445 lines, including the table header.

 

Which means that this hudson server has configured 444 jobs.

 

That's insane!

 

How many jobs are on your Hudson servers?

 

(I am currently relying on the html structure for Hudson version 2.1.2. It may work for other versions as well)
