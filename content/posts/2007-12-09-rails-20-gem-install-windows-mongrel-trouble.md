---
title: "Rails 2.0, gem install, Windows => Mongrel Trouble"
date: "2007-12-09T22:50:58"
slug: "rails-20-gem-install-windows-mongrel-trouble"
url: "/2007/12/09/rails-20-gem-install-windows-mongrel-trouble/"
wp_id: 803
categories: ["Ruby on Rails"]
tags: []
author: "jesper"
technorati: ["ruby", "rails", "mongrel", "rubygems", "copenhagenrb", "rails2.0"]
---

UPDATE December 20th: Problems are history with new Rubygems 1.0 release. See: [Rubygems: Rails 2.0, Mongrel, Windows, solved](/2007/12/20/rubygems-rails-20-mongrel-windows-solved/).

UPDATE December 19th: [Rails changeset 8438](http://dev.rubyonrails.org/changeset/8438) fixes the Rails part of this bug but no release 2.0.3 available yet. Rubygems 1.0 is on the way. Wait for the 1.0 release that contains a bugfix. See my [comment below](/2007/12/09/rails-20-gem-install-windows-mongrel-trouble/#comment-384409) for details. Also added links here in the bottom of the article explaining further.

Read this before running gem update --system and before upgrading to Rails 2.0 on windows. The fast one-sentence version: There is a bug in the current windows ruby "gem" release, but you need to upgrade it for Rails 2.0, read below to stay out of trouble.

This Friday's final release of Rails 2.0 makes everybody eager to upgrade and install. I ran into the same problems as commented in [the release note](http://weblog.rubyonrails.com/2007/12/7/rails-2-0-it-s-done):

> **48. Ray** on 07 Dec 17:58: \[...\]
>
> ERROR: While executing gem … (Zlib::BufError) buffer error

An other error lurks in the background: Rails 2.0 requires rubygems 0.9.4. And standard in the [Ruby one-click installer](http://www.ruby-lang.org/en/downloads/) is rubygems 0.9.2 (my installed version: ruby186-25.exe).

Add to this that some commenters suggest to upgrade rubygems to 0.9.5. WARNING: Don't upgrade Rubygems before you have read which problems it caused me.

``` ruby
gem update --system
```

gave me rubygems 0.9.5 but caused mongrel to stop working. I described the details in the ruby forum thread: "[Mongrel crash on win32](http://www.ruby-forum.com/topic/133033)", which basically says that rubygems 0.9.5 forces a native build on windows that don't work (not on my machine) because i have no compiler installed.

[Luis Lavena](http://www.workingwithrails.com/person/4626-luis-lavena) was great help to me explaining what was going on and how to get pass the problems. Here is what i had to do:

1.  No rubygems 0.9.5 install. Wait for the sequel. If you already did install it, follow Luis' advice in the forum thread.

2.  Check your current rubygems version:

    ``` ruby
    C:\> gem environment
    RubyGems Environment:
    - VERSION: 0.9.2 (0.9.2)
    - INSTALLATION DIRECTORY: c:/ruby/lib/ruby/gems/1.8
    - GEM PATH:
    - c:/ruby/lib/ruby/gems/1.8
    - REMOTE SOURCES:
    - http://gems.rubyforge.org
    ```

3.  Get ready for Rails 2.0 but start with rubygems 0.9.4. Now, here `gem update --system` gets you 0.9.5, so in stead do as Luis Lavena suggested (steps 4-5)

4.  Download the zip file with [rubygems 0.9.4 from rubyforge](http://rubyforge.org/frs/?group_id=126&release_id=11889) ([direct link](http://rubyforge.org/frs/download.php/20990/rubygems-0.9.4.zip))

5. ``` ruby
   C:\&gt; unzip -q rubygems-0.9.4.zip
   C:\> cd rubygems-0.9.4
   C:\> ruby setup.rb config
   C:\> ruby setup.rb install
   ```

6. ``` ruby
   C:\> gem environment
   RubyGems Environment:
   - VERSION: 0.9.4 (0.9.4)
   - INSTALLATION DIRECTORY: c:/ruby/lib/ruby/gems/1.8
   - GEM PATH:
   - c:/ruby/lib/ruby/gems/1.8
   - REMOTE SOURCES:
   - http://gems.rubyforge.org
   ```

7. ``` ruby
   gem update rails -y
   ```

Now everything works as expected. I will eagerly wait for the sequel to rubygems 0.9.5 which would save me for trouble in the future. Don't know why this should be so difficult to me but much easier to others that could just run "gem update --system" and "gem update rails -y". But this description above worked for me.

Related info:

- Rails weblog: [Rails 2.0: It's done!](http://weblog.rubyonrails.com/2007/12/7/rails-2-0-it-s-done) (comments 48, 51, 62, 70, 86, 87, 106, 128)
- Ruby Mongrel forum: "[Mongrel crash on win32](http://www.ruby-forum.com/topic/133033)"
- Riding Rails: [Trouble installing new gems?](http://weblog.rubyonrails.org/2007/12/19/trouble-installing-new-gems) (December 19)
- [Latest RubyGems and Rails is a deadly combo](http://blog.mmediasys.com/2007/12/19/latest-rubygems-and-rails-is-a-deadly-combo/ "Enlace Permanente a Latest RubyGems and Rails is a deadly combo") (December 19)
