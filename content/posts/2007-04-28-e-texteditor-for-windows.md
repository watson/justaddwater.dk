---
title: "E-Texteditor For Windows"
date: "2007-04-28T00:55:38"
slug: "e-texteditor-for-windows"
url: "/2007/04/28/e-texteditor-for-windows/"
wp_id: 605
categories: ["Code", "CSS", "HTML", "JavaScript", "Productivity", "Ruby on Rails", "Software"]
tags: []
author: "jesper"
technorati: ["editor", "e-texteditor", "etexteditor", "windows", "textmate", "html", "css", "javascript", "rails", "ruby on rails", "ruby", "rubyonrails", "cygwin"]
---

I have been looking a fast, intuitive editor for my Windows laptop.

Now I stopped looking. E-texteditor for windows is very intuitive and easy to use. I highly recommend watching the screencast (a short tour of some of the best features). Although it's still in beta, it seems so much better than the alternatives.

I'm using it for HTML, CSS, JavaScript, Ruby on Rails editing. And it just works.

[![e-texteditor-homepage.png](/wp-content/uploads/2007/04/e-texteditor-homepage.png)](http://www.e-texteditor.com/index.html "E-texteditor homepage with screenshot")

One note for avoiding future head-scratching: In order to get the keyboard shortcuts (so-called bundles) to work, I had to delete Cygwin and let E install it automatically. Afterwards I had to add packages manually: Subversion (svn)

Other improvements that would be handy:\
In HTML mode there is a shortcut "doctype \[tab\]", but there is no shortcut for creating the rest of the HTML document. It's probably easy to add (but i'm not into doing it yet). Besides, I think an addition like this would be a benefit to everybody, so it should be included in the general bundle.

In Ruby files, when looking on Ruby on Rails, it defaults the files to Ruby (because they are and they end in .rb). However, there is a lot of functionality with regards to Rails, so it would actually work better, if .rb defaulted to Ruby. Here is a [workaround to add .rb files to Rails syntax](http://www.e-texteditor.com/forum/viewtopic.php?p=3361#3361 "E-texteditor forum: Set Rails file from Ruby to Rails").

I also added a bug report "[Block selection should work without the mouse](http://www.e-texteditor.com/forum/viewtopic.php?t=1120 "E-Texteditor forum")" (guess I'm a usability geek).

The simple [cheatsheet for E-texteditor](http://cheat.errtheblog.com/s/e/ "ErrTheBlog E-texteditor cheatsheet.") at errtheblog is worth checking out, although it contains only the general shortcuts and not the Rails specific ones. Via: [RubyInside](http://www.rubyinside.com/e-texteditor-a-windows-textmate-or-why-apple-should-buy-textmate-413.html "RubyInside: E-TextEditor: A Windows TextMate? (Or ").
