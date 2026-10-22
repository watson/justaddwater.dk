---
title: "Ruby on Rails as rapid prototyping tool"
date: "2006-04-12T00:16:45"
slug: "rails-prototyping"
url: "/2006/04/12/rails-prototyping/"
wp_id: 221
categories: ["Best of Justaddwater", "Businesscase", "Code", "Prototyping", "Ruby on Rails"]
tags: []
author: "jesper"
technorati: ["prototyping", "html", "ruby on rails", "business case", "capgemini", "productivity"]
---

Ruby on Rails might be the perfect match as a prototyping tool. It delivers consistent productivity gains compared to any other prototyping tool. Very few lines of code makes it easy to change. Here is why we use it at work as our preferred prototyping tool.

First time I heard about Ruby on Rails was when David Heinemeier Hansson, Jason Fried and Ryan Singer presented the "[Building of Basecamp](http://www.37signals.com/workshop-062504.php "37 signals: The building of Basecamp workshop")" workshop in Denmark June 2005. Basecamp was the project that sparked the development of the Ruby on Rails framework.

I recognize the reaction that Deane of gadgetopia describes:

> So what was the biggest shock of the Basecamp seminar? Finding out that it was written in [Ruby](http://www.ruby-lang.org/en/). Yeah, that’s right — that Japanese language that you thought no one was using. They’ve apparently put together a Web development framework for it which they’re releasing to open-source.
>
> (from [www.gadgetopia.com](http://www.gadgetopia.com/post/2530 "Gadgetopia.com: Basecamp and Ruby") June 25, 2004)

I was immediately interested in the possibility of using Rails as a productivity tool, where in some cases a Rails application can be developed up to ten times faster than a similar Java or .Net application. Very promising.

### Prototyping satisfaction survey

I've tried a lot of different prototyping tools: Paper, Photoshop, Powerpoint, Dreamweaver, HTML. Until Rails I was perfectly happy with HTML prototypes: I consider them easy to maintain, fast to produce, possible to search and replace during development.

My experience goes pretty well with the 2002 GUUUI survey where 52 people replied on their preferred prototyping tool and their satisfaction with it (people preferring HTML were the most happy with their tool).

<table cellspacing="1" cellpadding="2" border="0" class="article">
<tr>
<td class="smallCopy" colspan="5"><span class="bold">"I'm perfectly happy with the prototyping tool I'm using"</span></td>
</tr>
<tr>
<td class="smallCopy"></td>
<td align="center" class="smallCopy">Strongly disagree</td>
<td align="center" class="smallCopy">Mildly disagree</td>
<td align="center" class="smallCopy">Neither agree nor disagree</td>
<td align="center" class="smallCopy">Mildly agree</td>
<td align="center" class="smallCopy">Strongly agree</td>
</tr>
<tr>
<td bgcolor="#f0f0f2" class="smallCopy">All replies (52 replies)</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">7.5%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">37.7%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">15.1%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">32.1%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">7.5%</td>
</tr>
<tr>
<td class="smallCopy">Using a visual or text based HTML tool (15  		 replies)</td>
<td valign="top" align="center" class="smallCopy">6.7%</td>
<td valign="top" align="center" class="smallCopy">20.0%</td>
<td valign="top" align="center" class="smallCopy">6.7%</td>
<td valign="top" align="center" class="smallCopy">60.0%</td>
<td valign="top" align="center" class="smallCopy">6.7%</td>
</tr>
<tr>
<td bgcolor="#f0f0f2" class="smallCopy">Using a diagramming tool  		 (13 replies)</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">7.7%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">76.9%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">7.7%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">0.0%</td>
<td valign="top" bgcolor="#f0f0f2" align="center" class="smallCopy">7.7%</td>
</tr>
<tr>
<td class="smallCopy">Using a graphic design tool (10 replies)</td>
<td valign="top" align="center" class="smallCopy">10.0%</td>
<td valign="top" align="center" class="smallCopy">20.0%</td>
<td valign="top" align="center" class="smallCopy">20.0%</td>
<td valign="top" align="center" class="smallCopy">50.0%</td>
<td valign="top" align="center" class="smallCopy">0.0%</td>
</tr>
</table>

Source [2002 GUUUI survey](http://www.guuui.com/issues/01_03_02.php "GUUUI - Results from a survey of web prototyping tools usage") on prototyping tools.

### Enter ruby on Rails

One thing I miss in HTML prototyping is the lack of real data. For instance, a user enters a date on one page. On the next page, the date is hardcoded. Chances are that users at a user test enter values that are different from what I hardcoded on the screen. Here Rails is perfect. In stead of building screens, we build the application front-end.

At my work in Capgemini Denmark, we have used Rails for some months at work projects and it has proven to deliver:

- Very high fidelity prototypes that can use real data. The high fidelity give much better findings in usability testing.
- Consistent productivity gains compared to any other prototyping tool.
- Very few lines of code makes it easy to change prototype.
- Doesn't have to be thrown away after building prototype.

Consider the fact that Rails can actually live on in the application development. I believe that Rails is a perfect match for making rapid prototype development. Also this approach is what Garret Dimon invented "**just build it**", and it fits like a glove with the agile approach of the guys at 37signals.

Whats your thoughts on this? What tools would you use for prototyping?

- Digital Web Magazine: [Just Build It: HTML Prototyping and Agile Development](http://www.digital-web.com/articles/just_build_it_html_prototyping_and_agile_development/)
- Garrett Dimon: [AJAX & DOM Scripting: Just Build It](http://www.garrettdimon.com/archives/ajax-dom-scripting-just-build-it)
- 37signals: [Getting Real, Step 1: No Functional Spec](http://www.37signals.com/svn/archives/001050.php)
- Particletree: [A Designer's Guide to Prototyping Ajax](http://particletree.com/features/a-designers-guide-to-prototyping-ajax/ "A Designer's Guide to Prototyping Ajax")
- GUUI: [2002 survey on prototyping tools](http://www.guuui.com/issues/01_03_02.php "GUUUI - Results from a survey of web prototyping tools usage")
