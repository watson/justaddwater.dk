---
title: "Ruby on Rails for the enterprise: Business perspective"
date: "2006-05-16T00:06:38"
slug: "rails-enterprise-business-perspective"
url: "/2006/05/16/rails-enterprise-business-perspective/"
wp_id: 226
categories: ["Businesscase", "Ruby on Rails"]
tags: []
---

Thought this would be a good opportunity to have a look at the business perspective of using Ruby on Rails for the enterprise. [The Business Case for Ruby on Rails](http://www.quotedprintable.com/articles/2005/12/21/the-business-case-for-ruby-on-rails "Quoted Printable: The Business Case for Ruby on Rails") inspired me to see what has been written on the business perspective since this was written December last year.

As I wrote [previously](/2006/04/12/rails-prototyping/ "Permanent Link: Ruby on Rails as rapid prototyping tool"), Ruby on Rails has proven to deliver:

- \
- Very high fidelity prototypes that can use real data. The high fidelity give much better findings in usability testing.
  \
- Consistent productivity gains compared to any other prototyping tool.
  \
- Very few lines of code makes it easy to change prototype.
  \
- Doesn’t have to be thrown away after building prototype.
  

But this was focused mostly on rapid prototyping as an obvious sweetspot for Rails. **Here are the other articles I found for this roundup**:

Mentalized.net: [One day with Scott Raymond](http://mentalized.net/journal/2006/05/14/one_day_with_scott_raymond/ "Mentalized.net: One day with Scott Raymond") by Jacob Skjerning

> Thursday marked a major step on the path to exploring Rails as an alternative for [BiQ](http://www.biq.dk/). [As I’ve mentioned earlier](http://mentalized.net/journal/2006/03/16/looking_for_a_rails_champion/) I’ve been looking for someone to come and present Rails for us.
>
> \[...\]
>
> The advice that in particular struck a chord with me was a pragmatic “fail fast” advice. Dig into the meaty parts, get your fears out of the way, or fail now, before you’ve spent months with nothing to show for it.
>
> Monday will hear the decision of wether we’ll move ahead. Currently, I have no reason to believe otherwise.

Their task is to consider [rewriting an ASP/VBScript system](http://mentalized.net/journal/2006/03/16/looking_for_a_rails_champion/):

> At the day job I’m the sole developer and maintainer of a legacy ASP/VBScript system. Yes, ASP/VBScript. No, not .NET. And yes, it’s driving me insane. The code contains around 42000 lines of VBSCript drivel and 30000 lines of supporting Python code.
>
> The other day I told my boss that I thought we should really, really consider rewriting the application. The existing one is getting cumbersome, hard to maintain, and let’s face it; it’s sucking my soul dry. My suggestion for a new platform is, for a lot of reasons, Ruby on Rails.

[Ruby on Rails is web2.0 on rocket fuel](http://web2.wsj2.com/ruby_on_rails_11_web_20_on_rocket_fuel.htm) by Dion Hinchcliffe:

> I could spend a lot more time talking about the details of Ruby and Ruby on Rails but the important point to take away is that it puts extreme power in the hands of the average Web developer by collapsing the common tasks from literally days to just hours or even minutes in some cases. I've seen some of the demonstrations in person (most recently [Hansson's talk](http://web2.wsj2.com/a_compelling_ajax_discussion_in_new_york_city.htm) at Real-World Ajax) and am continually impressed by how fast and easily that working software can be created with Rails. Creating blog or wiki software from scratch can literally take just a few minutes.
>
> Web 2.0 software development has its own set of expectations and [best practices](http://web2.wsj2.com/news_from_the_field_web_20_best_practices.htm): rapid feature evolution, real-time feature monitoring, all functionality available in both the GUI and as Web services so others can use them in their own apps, and more. Rails makes all of these easy to do using one of the highest productivity languages out there. That's not to say Rails [is perfect,](http://discuss.joelonsoftware.com/default.asp?joel.3.309321.3) it's so new it couldn't possibly be fault-free, but there is clear evidence today of its reliability, scalability and ease-of-use (once you get past a brief learning curve.)

[Ruby on Rails enterprise ready?](http://dev2dev.bea.com/blog/jonmountjoy/archive/2005/11/ruby_on_rails_e.html) by Jon Mountjoy:

> Something else that's interesting is that issues like this \[distributed transactions\] are not stopping adoption of Rails. Companies like [37signals](http://www.37signals.com/) are forging ahead creating great solutions, deployed and live. Obviously Rails is "good enough" - its lack of many enterprise features, distributed transactions being another important one, doesn't prevent adoption. Perhaps 37signals do something funky with their database connection handling, or perhaps it just doesn't matter for the vast majority of applications out there. I suspect that the latter is closer to the truth.
>
> In J2EE land we tend to focus on solving the difficult problems, instead of making the easy problems easier to code. This is one of the biggest lessons that J2EE can learn from Rails - [productivity](http://dev2dev.bea.com/blog/editors/archive/2005/07/productivity.html).

[Ruby on Rails from a Business Perspective](http://www.screamingatthekeyboard.com/articles/2006/03/02/ruby-on-rails-vs-php-from-a-business-perspective) via [The Case for Rails: Talking to Management](http://blog.inquirylabs.com/2006/03/29/the-case-for-rails-talking-to-management/ "Inquiry labs blog: The Case for Rails: Talking to Management")

> It also helps that Ruby on Rails can crank out a system in about 1/3rd of the time as PHP, but that’s probably my own coding preferences talking.

Business case for [Ruby on Rails vs. Java](http://www.jroller.com/page/obie?entry=productivity_arbitrage "Obie Fernandez: Productivity Arbitrage") by Obie Fernandez (via [Curt Hibbs](http://blog.curthibbs.us/articles/2005/12/21/productivity-arbitrage-and-ajax/ "Curt Hibbs: Productivity arbitage and AJAX"))

> *Want a realistic example of what I’m describing? Two well-respected consultancies find themselves competing head-to-head for a project: a fairly typical internal web application, of the type that large corporate clients often request. Both consultancies follow Agile practices. Timely delivery for this project is critical (as usual), but delivering on-time is particularly important in this case. The client will get hit with severe regulatory penalties if the new system is not implemented within a year’s time.*


> *The decision makers at **Consultancy A** propose a Java-based solution at a price of a million dollars, and they estimate final delivery within 10 months. Their bid is competitively-priced and they feel confident about it. They plan to allocate an experienced team using a mature platform (Java). They calculate, using rough figures, that 6 resources x \$97 blended hourly rate x 10 months equals about \$1MM, a gross margin of about 25%. A higher margin would be better, but all-in-all this deal is not too shabby.*


> *The folks at **Consultancy B** also have extensive experience building the kind of webapp needed and they see a potential productivity arbitrage play. Instead of Java, they differentiate themselves by pitching a Ruby on Rails solution. Quite innocently, they undercut their competition by pricing their bid at \$800K and promising delivery within 6 months. According to their calculations, (and once again, these are rough figures), 4 resources x \$192 rate x 8 months equals about \$800k. That rate (\$192) represents a much higher gross margin, even taking into account that Consultancy B pays its consultants higher salaries.*


> ***Can you guess who won?** Consultancy B won! At the contract signing, the client CIO says that it was a “no brainer” and lists the following reasons in order of increasing importance…*

Thoughtworks (US technology consultants Martin Fowler, Obie Fernandez, etc.) mentions quite a few advantages on their [technology page](http://www.thoughtworks.com/ruby.html "Thoughtworks: Ruby"):

> Our ongoing project work with Ruby and Rails proves that Ruby excels in the following applications:\
>
> - \
> - Web 2.0 applications that make use of REST and/or AJAX designs
>   \
> - Small to medium Web-based applications with aggressive time-to-market goals
>   \
> - Low-cost internal prototypes and pilot applications
>   \
> - Highly-targeted internal applications and utility programs
>   \
> - So-called 'soft layer' APIs on hardened transactional systems
>   \
> - Build systems for complex enterprise systems
>   \
>
> 

Justaddwater.dk [Ruby on Rails as rapid prototyping tool](/2006/04/12/rails-prototyping/ "Permanent Link: Ruby on Rails as rapid prototyping tool") by me:

> At my work in Capgemini Denmark, we have used Rails for some months at work projects and it has proven to deliver:\
>
> - \
> - Very high fidelity prototypes that can use real data. The high fidelity give much better findings in usability testing.
>   \
> - Consistent productivity gains compared to any other prototyping tool.
>   \
> - Very few lines of code makes it easy to change prototype.
>   \
> - Doesn’t have to be thrown away after building prototype.
>   \
>
> \
> Consider the fact that Rails can actually live on in the application development. I believe that Rails is a perfect match for making rapid prototype development. Also this approach is what Garret Dimon invented “**just build it**“, and it fits like a glove with the agile approach of the guys at 37signals.

Real world sucess stories: List of [web applications running Ruby on Rails](http://www.rubyonrails.org/applications "Rubyonrails.org: Applications running Ruby on Rails"), and another [list of Ruby apps](http://www.rubygarden.org/ruby?RealWorldRuby "Rubygarden.org: Real-world ruby success stories") (web applications at the bottom).

Do you know of any relevant articles out there? Please add to my list. I'm mostly looking for the not-so-technical and management targeted.

Vaguely related, the final word is from my blogging partner Thomas Watson, [currently at JavaOne](/2006/05/09/javaone-2006-blogger-meetup/ "justaddwater.dk: JavaOne 2006 Blogger Meetup") in San Fransisco, took this photo near the Golden Gate Bridge:

[](/2006/05/16/rails-enterprise-business-perspective/keep-off-rails-thumbjpg/ "keep-off-rails-thumb.jpg")

[](/2006/05/16/rails-enterprise-business-perspective/keep-off-rails-thumbjpg/ "keep-off-rails-thumb.jpg")

[![keep-off-rails-thumb.jpg](/wp-content/uploads/2006/05/keep-off-rails-thumb.jpg)](/2006/05/16/rails-enterprise-business-perspective/keep-off-rails-thumbjpg/ "keep-off-rails-thumb.jpg")

Sure hope that not everybody will follow the advice of San Fransisco Authorities to keep off Ruby on Rails.
