---
title: "Design Guide or HTML Markup Guide"
date: "2008-02-08T13:47:41"
slug: "design-guide-or-html-markup-guide"
url: "/2008/02/08/design-guide-or-html-markup-guide/"
wp_id: 861
categories: ["Web Development", "Web Standards"]
tags: ["htmlguide", "Productivity", "Web Standards"]
author: "jesper"
technorati: ["web standards", "webstandards", "html", "guide", "xhtml", "css", "consistency", "tdc", "erhvervs- og selskabsstyrelsen", "capgemini"]
---

At a recent project, there was a requirement to describe the CSS used on a site, as a documentation, other developers could use. We decided to go a bit further -- not only documenting the CSS classes -- but making a guide that developers could find easy to use. Also we wanted developers with little or no CSS knowledge to be able to use the guide.

The usual design guide that dictates colors for headings, which images to use for bullet lists, margins between elements, line-heights, etc. When it comes to implementing the actual markup, **the usual design guide is no help for developers** when the first page is up on the website.

An HTML Guide has the following advantages over a traditional design guide:

- Developers can focus on business logic.
- No knowledge of CSS required for web developers. Experts took care of CSS, browser bugs, aligning pixels, etc.
- Testing can be less thorough on other browsers once the initial work is done.
- Service providers can save money as one portlet/webpart can integrate into many portals \*)

\*)  over time as a common format emerge on several portals.

It is my hope that we can use examples like this to make development of public applications cheaper and more consistent.

Here is the HTML guide we made in Capgemini recently in collaboration with Erhvervs- & Selskabsstyrelsen ([Danish Commerce and Companies Agency](http://eogs.dk/sw21252.asp))

[htmlguide.virk.dk/](http://htmlguide.virk.dk/) (the guide is in Danish)

## HTML markup description

Each element contains of an HTML example (not an image, but rendered HTML based on current CSS):

![htmlguide-virk-example.png](/wp-content/uploads/2008/02/htmlguide-virk-example.png)

And then there is the corresponding HTML markup for creating that particular example:

![htmlguide-virk-example-html-markup.png](/wp-content/uploads/2008/02/htmlguide-virk-example-html-markup.png)

## Examples of HTML Markup guides

List with examples that are public available on the web

- **Virk.dk (Denmark):** [HTML Guide](http://htmlguide.virk.dk/) (in Danish) Virk.dk is the Danish public portal for everything companies need to interact with public authorities. Technical note: Still has minor browser rendering issues that we are looking into. HTML is as clean as the graphical design allows.
- **TDC (Denmark):** [Metaform guide](http://manual.tdconline.dk/metaform_markup/definition/form/) (in Danish) TDC, the big Danish telco has a similar guide, also public available. Technical note: Suffers from [tag soup](http://en.wikipedia.org/wiki/Tag_soup), but otherwise is very comprehensive.

I will update this list if you know of **any examples that you know of**. If possible, provide all the following  information:

- Name or domain of the guide
- Language
- URL for public version of the guide
- Short description of guide scope or content
- Corresponding graphical design guide (if applicable)
- Technical note
