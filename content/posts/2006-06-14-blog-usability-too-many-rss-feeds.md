---
title: "Blog Usability: Too many RSS feeds"
date: "2006-06-14T14:51:52"
slug: "blog-usability-too-many-rss-feeds"
url: "/2006/06/14/blog-usability-too-many-rss-feeds/"
wp_id: 311
categories: ["Atom", "Best of Justaddwater", "Blogging", "justaddwater.dk", "RSS", "Syndication", "Usability", "WordPress"]
tags: []
---

![Large Feedicon](/wp-content/uploads/2006/06/feed-icon-128x128.png "Large Feedicon")After reading "[Pick a Format (Any Format)](http://nick.typepad.com/blog/2006/05/pick_a_format_a.html "Nick Bradbury: Pick a Format (Any Format)")" by Nick Bradbury (tip by: [Jeremy Voorhis](http://www.jvoorhis.com/ "jvoorhis") on [Octoblog](http://outside-thoughts.octopod.info/articles/2006/06/12/switching-to-mephisto "Octoblog: Switching to Mephisto")) we must say that we totally agree. The point in the post is simple:

> I keep running across sites that offer **the same exact content** as an RSS feed *and* an Atom feed.
>
> What's the point of this? Making readers choose a feed format is like asking them to choose between an HTML and XHTML version of your site - technically there are differences, but end users shouldn't have to care about this. They just want to subscribe to your words of wisdom without having to deal with the plumbing.

Here at justaddwater.dk we have on our front-page and in all our posts always only linked to our RSS 2.0 feed - So far so good. But in our HTML source there have always been a list of alternate tags linking to both Atom and RSS 0.92.

To not alienate our readers that have been using Atom or RSS 0.92 we have decided not to actually shutdown these feeds, only remove them from our HTML. This way no new user will start to use them.

To take it even further we need to implement proper [feedicons](http://feedicons.com/) instead of just writing RSS 2.0 (a technical description many users don't understand) - But that must be on our [to-do list](http://wa7son.tadalist.com/lists/public/194116 "justaddwater.dk usability improvements").

### Conclusion

WordPress (and others) should **let the administrator choose which syndication feed to offer** the readers. It should also **incorporate the feedicon** into the default design.
