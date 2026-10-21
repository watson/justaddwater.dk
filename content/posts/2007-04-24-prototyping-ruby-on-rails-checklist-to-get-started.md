---
title: "Prototyping Ruby on Rails Checklist to Get Started"
date: "2007-04-24T22:06:21"
slug: "prototyping-ruby-on-rails-checklist-to-get-started"
url: "/2007/04/24/prototyping-ruby-on-rails-checklist-to-get-started/"
wp_id: 594
categories: ["Prototyping", "Ruby on Rails"]
tags: []
---

**Update May 10: this article is no longer password protected. [Explanation why](/2007/05/11/ruby-on-rails-checklist-now-public-available/ "Justaddwater.dk: Ruby on Rails Checklist Now Public Available").**

Here is a brief reminder to myself before starting up a prototyping session.

Some of the activities below are done only once on the current machine, some of them you must do with every project. I just wanted to have it all on the same list.

## Laptop preparations

This is for my Windows XP laptop:

- \
- Subversion repository up and running (so you can immediately add the project).
  \
- I do this by installing [TortoiseSVN](http://subversion.tigris.org/servlets/ProjectDocumentList?folderID=91 "TortoiseSVN Download Windows Binaries") and following this explanation in "[how to create a temporary local Subversion repository](/2007/04/26/howto-create-a-temporary-local-subversion-repository/ "Permanent Link to Howto Create a Temporary Local Subversion Repository")".
  \
- Add subversion users and authorization for the current project
  \
- Download latest version of Ruby on Rails (i tend to use latest stable, but latest from trunk would be OK as long as all tests pass). See section on Ruby gems and plugins
  \
- Download and prepare editor (currently I use [e-texteditor](http://www.e-texteditor.com/). As a sidenote, [Aptana released a beta version with rails support](http://radrails.org/download_rails_rdt.php) the other day but it didn't work for me out of the box, so I stick to e-texteditor.)
  \
- Let E-texteditor do the Cygwin install (this way, rails bundles work without extra effort).
  \
- Then run cygwin install manually to add the following packets:\
  subversion, curl, wget, openssh, and I need some text browsers as well for testing pupose (Links and Lynx).\
  The cygwin install file is in "C:\Program Files\e\support\bin"
  \
- Check that your database drivers work and are running the basic operations. I prefer SQLite as it's faster to run from my laptop computer and tests are running faster.
  \
- I prefer a good diff tool like [ExamDiff Pro](http://www.prestosoft.com/ps.asp?page=edp_examdiffpro "Prestosoft ExamDiff Pro") (which tells me the exact parts of lines that are changed), although the built-in diff tool in TortoiseSVN is decent.
  


### Ruby gems and Rails plugins

Assuming you have Ruby and RubyGems installed, install the other gems needed:

    gem install rails --include-dependencies #run only if needed
    gem install rake piston sqlite3-ruby mysql --include-dependencies
    #Command line commands to test your install: gem, rails, svn
    #
    #Remember Mongrel as well
    gem install mongrel --include-dependencies
    #
    #I also use these on a regular basis, but leave them out for now:
    #gem install scrubyt rspec rcov rubyful_soup mechanize hpricot zentest mocha cheat --include-dependencies

Get hold of [ActiveScaffold plugin](http://activescaffold.com/) and my [LocalizationSimplified plugin](/2006/08/24/ruby-on-rails-plugin-localize-your-rails-app/) ([project page](http://rubyforge.org/projects/l10n-simplified/)), and Rails trunk if you like. (maybe I should also add [Smart-Form](http://agilewebdevelopment.com/plugins/smart_form "Smart-Form 1.0 Rails plugin"), and the [Caboose sample app](http://www.caboo.se/articles/2007/4/3/caboose-sample-rails-application), but won't add it here before I try it out)

With the help of [Piston](http://www.rubyinside.com/advent2006/12-piston.html "Managing Rails Plugins With Piston (Ruby Advent Calendar 2006)"), it's easy to administer plugins and version them:

    cd vendor/plugins
    piston import http://dev.rubyonrails.org/svn/rails/trunk vendor/rails
    piston import http://activescaffold.googlecode.com/svn/tags/active_scaffold
    piston import svn://rubyforge.org/var/svn/l10n-simplified

## Client preparation

At the client's place, I look for the following preperational work:

- Find documentation for all accessible apis and services
- Try it
- Locate people that might know about the services and apis available
- investigate authorisation and access issues regarding services and apis
- locate other data, lists, sample data, categories that could potentially be used as fixture data in the prototype app.
- Have a look at existing design. Perhaps design manuals, homepage design, fetch logos or existing graphical material. There might be a page or two that can be used as layout inspiration (Not many pages I see are coded the way I want to build the HTML, so usually I make my own layout.rhtml file).
- Find some standard CSS based layouts that fit your need. More inspiration in the sidebar article "More CSS inspiration".

### More CSS inspiration

Good example from Roger Johanssons 2 column layout. For 3 column layouts, I have not yet found one that fits my needs perfectly. Previosuly I used [redmelon's 3 col layout](http://www.redmelon.net/tstme/3colfixed/) for [Nemkonto](http://nemkonto.dk/) ([redmelons website](http://redmelon.net/) and old link is currently not working). A place to get inspiration is the [3-column layout page at CSS-discuss](http://css-discuss.incutio.com/?page=ThreeColumnLayouts) (be warned that there are too many alternatives there).

### Your tips, tricks and suggestions

Let me know if you have anything that you would like to add to the list, discuss, or think is irrelevant. I'd love to update this post with your suggestions. Main criteria for me: Fast up and running (Getting immediate productivity). Team collaboration in code (so no complex setup features). Please add your good suggestions and comments below.
