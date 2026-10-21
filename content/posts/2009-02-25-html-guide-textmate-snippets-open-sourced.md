---
title: "HTML Guide Textmate Snippets Open Sourced"
date: "2009-02-25T16:38:02"
slug: "html-guide-textmate-snippets-open-sourced"
url: "/2009/02/25/html-guide-textmate-snippets-open-sourced/"
wp_id: 1036
categories: ["Web Development", "Web Standards"]
tags: ["htmlguide", "portals", "Productivity", "Ruby on Rails", "virk.dk", "Web Development", "Web Standards"]
---

One year ago I published "[Design Guide or HTML Markup Guide](../2008/02/08/design-guide-or-html-markup-guide/ "Permanent Link: Design Guide or HTML Markup Guide")" with link to the HTML guide we did for the biggest Danish business internet portal.

The HTML guide is a really useful tool for every public authority that must deliver applications for the portal.

As a help for my own work back then, I created [virk_dk_htmlsnippets](http://github.com/jesperronn/virk_dk_htmlsnippets/tree/master):

> ## Snippets available
>
> `skel`(tab) -- creates HTML skeleton in blank file. Adds correct doctype, head, body and container divs required for the virk.dk html to show correctly.
>
> `fieldset`(tab) Groups of form elements. Use where you would have used ordinary fieldsets. See HTML guide » [Form grupper (fieldsets)](http://xmltools2.oio.dk/virk/htmlguide/form-fieldset.html)
>
> `button`(tab) -- submit button and other buttons. See HTML guide » [Knapper](http://xmltools2.oio.dk/virk/htmlguide/buttons.html)
>
> `inputcheck`(tab) -- standard checkbox with label and group\
> `inputtext`(tab) -- text field\
> `select`(tab) -- select element
>
> Usage examples see HTML guide [Simple form elementer](http://xmltools2.oio.dk/virk/htmlguide/form-simple.html), [Særlige form elementer](http://xmltools2.oio.dk/virk/htmlguide/form-special.html)
>
> `table`(tab) -- table element. See HTML guide » [Tabeller](http://xmltools2.oio.dk/virk/htmlguide/tables.html)\
> `td`(tab) -- table cell inside table row.\
> `th`(tab) -- table header cell inside table row.

I'm releasing the snippets as open source under the [LGPL license](http://creativecommons.org/licenses/LGPL/2.1/) so you can freely change, and distribute. However, I encourage you to send me the changes and I'll work the relevant changes into the snippets.

Any editor that understands [Textmate](http://macromates.com/) snippets can be used. [E-texteditor](http://e-texteditor.com/) for Windows or [GEdit](http://projects.gnome.org/gedit/) for Unix/Linux will read the snippets as well.

### Download snippets

Go to the project page on GitHub to download [virk_dk_htmlsnippets](http://github.com/jesperronn/virk_dk_htmlsnippets/tree/master)

## Vision: Standard HTML for portals

In general, different portals have different HTML markup. Historically, this is because of many constraints: Limitations in the chosen web framework, limitations in chosen graphical design, random naming of css classes, developer laziness, etc.

What if portals could actually use the same HTML markup for most elements? This way, subcontractors and content providers could deliver content/portlets/webparts for multiple portals.

In Denmark there are only a few major public portals: Virk.dk for businesses, and Borger.dk for citizens. But some content would actually be relevant on both portals. Sadly, the HTML markup is very different.

Imagine how the public authorities would benefit from shared HTML markup:

- Develop only one component with the wanted functionality.
- Easier "mashup" and reuse of data for presentation on multiple portals
- Lower learning curve for developers
- More development accelerators like these snippets would emerge

Next time I get to do work for that project, I would probably also create a Ruby on Rails form builder that automagically would generate the right HTML.
