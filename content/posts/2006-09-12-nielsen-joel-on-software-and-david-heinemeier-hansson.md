---
title: "Nielsen, Joel on Software and David Heinemeier Hansson"
date: "2006-09-12T13:39:04"
slug: "nielsen-joel-on-software-and-david-heinemeier-hansson"
url: "/2006/09/12/nielsen-joel-on-software-and-david-heinemeier-hansson/"
wp_id: 390
categories: ["Businesscase"]
tags: []
author: "jesper"
technorati: ["jakob nielsen", "joel spolsky", "david heinemeier hansson", "ruby on rails", "joelonsoftware", "businesscase", "business case", "railsconf"]
---

Jakob Nielsen's newsletters often contains small comments to usability related stuff in the news. His latest newsletter is no exception, but misses a very important point.

From the mail:

> Joel Spolsky wrote about the choice of implementation technology for enterprise projects, making two great points:
>
> (\*) There are three platforms that are all known to work, so pick one of them, avoiding the fancy, but risky ones that don't have a sufficient ecosystem.
>
> (\*) As long as you use one of the safe platforms, success or failure of your project will not be due to which technology you chose, so go with the one your software architect knows the best.
>
> \> <http://www.joelonsoftware.com/items/2006/09/01.html>
>
> Joel's second point matches with our findings from intranet portal projects: what makes a good portal is not the technology (they all suck), but how you fit the tech to your company's needs:
>
> \> <http://www.nngroup.com/reports/intranet/portals>

Unfortunately there is no newsletter archive available for his newsletters. This is not a violation of any of his usability guidelines, but there will probably be no guideline for it before he has an archive up and running — Linkrot for email content is almost as bad as linkrot on the web, I guess.

Please ignore for a moment the way the story ends in a selling proposal for one of the portal studies. The most interesting about this story is actually not here! David Heinemeier Hansson commented on Joels story with some making some brilliant (and fun) points about Joel's article.

> Joel finishes off with a prize so good you can't help but wonder if he's pulling your leg or not. So in summary, Ruby and Rails are both immature, right? A decade for the language, two-something years for the framework. Tens, if not hundreds, of thousands of programmers exposed between the two. Okay, I buy that this could be seen as "immature" if you're into comparing quantity of programmers or deployed applications against, say, Java or PHP.
>
> Now strap yourself in and reach the final paragraph:

> FogBugz is written in Wasabi, a very advanced, functional-programming dialect of Basic with closures and lambdas and Rails-like active records that can be compiled down to VBScript, JavaScript, PHP4 or PHP5. Wasabi is a private, in-house language written by one of our best developers that is optimized specifically for developing FogBugz; the Wasabi compiler itself is written in C#.

> So Joel and friends *invented their own language*, which has to reasonably compile to three and a half different ones. Yes, they're building their Serious Business Stuff application on a 1-off, closed language. So please do as I say, not as I do, dammit. And pick something mainstream and "safe".
>
> I swear I couldn't make this stuff up even if I tried. Joel, you're my new hero of irony. And as soon as you start selling those t-shirts with "Serious Business Stuff", I got green ready to flow. Short of that, I'd take a red teddy bear with the embroidering "Someone is Going to Get Fired".

Jakob Nielsen puts the discussion above in perspective. I really enjoy David's reflections that are going in a completely other direction than Jakob Nielsen's (who seems focused on ending his reflections with a selling proposal of his own material).

### Ruby on Rails for enterprise use

The point David touches here is whether you could consider an "Immature" technology in the enterprise. Joel and David seem to disagree on this point. And Joel seems to disagree with himself. For the case of Ruby on Rails considered immature for the enterprise, i strongly disagree.\
As I wrote [previously](/2006/04/12/rails-prototyping/ "Permanent Link: Ruby on Rails as rapid prototyping tool"), Ruby on Rails has proven to deliver:

- Very high fidelity prototypes that can use real data. The high fidelity give much better findings in usability testing.
- Consistent productivity gains compared to any other prototyping tool.
- Very few lines of code makes it easy to change prototype.
- Doesn’t have to be thrown away after building prototype.

This is not only about prototypes: Massive productivity gains between 2 and 20 times faster development alone should make you consider Rails before other alternatives. The community around Rails is massive compared to other frameworks, and I see there is a strong will to make it even better, increase quality, performance and ease of use (even though I consider Rails to be way in front of competition on this point).

Further reading:

- DHH: [Fear, Uncertain, and Doubt by Joel Spolsky](http://www.loudthinking.com/arc/000596.html "Permanent link")
- Joel Spolsky: [Language Wars](http://www.joelonsoftware.com/items/2006/09/01.html "Joel on Software: Language Wars")
- Justaddwater: [Ruby on Rails for the enterprise: Business perspective](/2006/05/16/rails-enterprise-business-perspective/ "Permanent Link to Ruby on Rails for the enterprise: Business perspective")
- Justaddwater: [Ruby on Rails as rapid prototyping tool](/2006/04/12/rails-prototyping/ "Permanent Link to Ruby on Rails as rapid prototyping tool")
