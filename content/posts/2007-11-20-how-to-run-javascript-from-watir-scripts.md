---
title: "How to Run JavaScript From Watir Scripts"
date: "2007-11-20T21:12:20"
slug: "how-to-run-javascript-from-watir-scripts"
url: "/2007/11/20/how-to-run-javascript-from-watir-scripts/"
wp_id: 778
categories: ["Code", "JavaScript"]
tags: []
author: "jesper"
technorati: ["ruby", "enterprise", "business case", "watir", "testing", "javascript"]
---

What's Watir? Read "[Watir: Another sweetspot for Enterprise Ruby](/2006/07/14/watir-sweetspot-enterprise-ruby/)"

Is it possible to run JavaScript functions or execute code from within your Watir test scripts? As a matter of fact it is, but I had a hard time finding the proper documentation for it. Here is what to do and how:

### Call JavaScript Functions from Watir script

``` ruby
win = ie.document.parentWindow
win.ToggleProj('1')
```

### Inject JavaScript to run from Watir script

I used this to alter a JavaScript function on the existing page:

``` ruby
@ie.document.parentWindow.eval('
  window.CheckReport=function(){return true}')
```

As you can see, you can reference the window object and use eval to execute your snippets. The easier way is to add this custom method for easy reference

``` ruby
# Add accessor for DOM window object
class Watir::IE; def window; document.parentWindow; end; end
```

Then you can write the last example as:

``` ruby
@ie.window.eval('
  window.CheckReport=function(){return true}')
```

Much more intuitive and straightforward. Thanks to my colleague [Tobias](http://tobiashm.jaiku.com/) for the trick.

More info

- Justaddwater.dk: [Watir: Another sweetspot for Enterprise Ruby](/2006/07/14/watir-sweetspot-enterprise-ruby/ "Permanent Link: Watir: Another sweetspot for Enterprise Ruby") (July 2006)
- Telerik (by Egil): [Automating Complex JavaScript-rich Controls with Watir](http://blogs.telerik.com/blogs/twisted_asp_net/archive/2006/04/26/201.aspx) (April 2006)
- [DWatir](http://dwatir.rubyforge.org/) for distributed testing is very promising. I saw the demo at RailsConf but had not yet a chance to use. More info in the [code files](http://dwatir.rubyforge.org/svn/trunk/lib/dwatir.rb).
