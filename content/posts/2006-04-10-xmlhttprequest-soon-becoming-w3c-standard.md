---
title: "XMLHttpRequest soon becoming W3C standard"
date: "2006-04-10T18:01:25"
slug: "xmlhttprequest-soon-becoming-w3c-standard"
url: "/2006/04/10/xmlhttprequest-soon-becoming-w3c-standard/"
wp_id: 220
categories: ["AJAX", "Browser", "JavaScript", "Web Standards", "XML"]
tags: []
author: "thomas"
---

I just found out ([via BorkWeb](http://borkweb.com/story/xmlhttprequest-object-w3c-working-draft "BorkWeb: XMLHttpRequest Object W3C Working Draft")) that the W3C is looking to standardizing the XMLHttpRequest object which is the foundation for all AJAX based applications.

Today this object is implemented by all the major browsers. But because there is no standard dictating how this object should behave, the implementations are a bid different. That in turn means that web-developers the world over have to deal with browser compatibility issues (and we all remember to good old days of web-development in the 90's right?).

Currently the W3C have [a "first draft" of the standard ready](http://www.w3.org/TR/XMLHttpRequest/ "The XMLHttpRequest Object - W3C Working Draft 05 April 2006") for the public to take a look at.

From the draft:

> The XMLHttpRequest object is implemented today, in some form, by many popular Web browsers. Unfortunately the implementations are not completely interoperable. The goal of this specification is to document a minimum set of interoperable features based on existing implementations, allowing Web developers to use these features without platform-specific code. In order to do this, only features that are already implemented are considered. In the case where there is a feature with no interoperable implementations, the authors have specified what they believe to be the most correct behavior.
