---
title: "Rubygems: Rails 2.0, Mongrel, Windows, solved"
date: "2007-12-20T21:13:40"
slug: "rubygems-rails-20-mongrel-windows-solved"
url: "/2007/12/20/rubygems-rails-20-mongrel-windows-solved/"
wp_id: 828
categories: ["Ruby on Rails"]
tags: []
author: "jesper"
technorati: ["ruby", "rails", "mongrel", "rubygems", "copenhagenrb", "rails2.0"]
---

Now is the time to revoke the install warning [Rails 2.0, gem install, Windows =\> Mongrel Trouble](/2007/12/09/rails-20-gem-install-windows-mongrel-trouble/ "Permanent Link to Rails 2.0, gem install, Windows => Mongrel Trouble") I wrote about December 9th as Rails 2.0 was released.

Rubygems 1.0 was released 10 hours ago and solves the Win32 problems mentioned in the previous post.

So for now, back to:

``` ruby
> gem update --system
> gem update rails
> gem update mongrel
```

And everything works for me. Note that for now, there still is a problem with mongrel_service (will probably be fixed in next version). Luis Lavena describes a workaround in his updated article.

Related info:

- Justaddwater.dk: [Rails 2.0, gem install, Windows =\> Mongrel Trouble](/2007/12/09/rails-20-gem-install-windows-mongrel-trouble/ "Permanent Link to Rails 2.0, gem install, Windows => Mongrel Trouble")
- Eric Hodel: [RubyGems 1.0.0](http://blog.segment7.net/articles/2007/12/20/rubygems-1-0-0)
- Luis Lavena:[Latest RubyGems and Rails is a deadly combo](http://blog.mmediasys.com/2007/12/19/latest-rubygems-and-rails-is-a-deadly-combo/ "Enlace Permanente a Latest RubyGems and Rails is a deadly combo")
