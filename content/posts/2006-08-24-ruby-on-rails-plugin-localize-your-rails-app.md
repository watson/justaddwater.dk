---
title: "Ruby on Rails plugin: Localize your Rails app"
date: "2006-08-24T01:22:19"
slug: "ruby-on-rails-plugin-localize-your-rails-app"
url: "/2006/08/24/ruby-on-rails-plugin-localize-your-rails-app/"
wp_id: 381
categories: ["Best of Justaddwater", "Code", "Ruby on Rails"]
tags: []
author: "jesper"
---

Recently I've been working on a plugin for Ruby on Rails that help me out when creating new Rails applications in Danish. Previously, when we've created Danish prototypes for our customers **all the default Rails error messages were still written in English**.

I generalized it for use with any language, and currently (with the help from contributors) it's now available for download on rubyforge.

![screenshot-localization-simplified-pirate-talk.png](/wp-content/uploads/2006/08/screenshot-localization-simplified-pirate-talk.png)

I gave a short plugin demo at our recent Copenhagen Rails Meetup. [Olle](http://olle.ter.dk/blog/?p=288 "Olle Jonsson: Rails - in your language") and [Jakob](http://mentalized.net/journal/2006/08/21/copenhagenrb_august_meeting/ "Mentalized.net: Copenhagen.rb august meeting") already wrote briefly about it. You can read more (and vote) on agilewebdevelopment page [Localization Simplified](http://www.agilewebdevelopment.com/plugins/localization_simplified "Agile web development: Plugin Localization Simplified").

**Currently supported languages:**

- Danish
- Dutch (thanks Jeroen Houben)
- German
- Spanish (thanks [Luis Villa](http://grancomo.com))
- Swedish (thanks [Olle Jonsson](http://olle.ter.dk/blog/))
- Swedish Chef
- Pirate Talk (thanks Tobias Michaelsen)

![screenshot-localization-simplified-sweedish-chef.png](/wp-content/uploads/2006/08/screenshot-localization-simplified-sweedish-chef.png)\
The main reason why I wanted to support Swedish chef and Pirate talk is that I want to remind myself to have fun while coding. And of course it's a plus that [International Talk like a Pirate day](http://www.google.com/search?q=International%20Talk%20like%20a%20Pirate) is coming up at Sept. 19, arrrh!

**What it does**

This plugin modifies the following most used helpers for Rails

- Localized errors and error headings
- Localized monthnames on date_select etc. (changing the order of Y-M-D, where Rails allows)
- Localized distance_of_time_in_words
- Localized to_currency (but not changing the order of unit/currency)
- Simple pluralization also available in the lang-file (but currently only used for pluralizing "error"=\>"errors" in local language)
- Uses standard Rails methods. In this way, there is no tedious rewrite of localization functions in your view files

There are some FIXME's in the code and any help on the plugin is appreciated.

As I've written in the [Rails Core group](http://groups.google.com/group/rubyonrails-core/browse_thread/thread/346cda3cd39e6fa9), this plugin does some work that I hope will be worked into the Rails framework for easier future internationalization.

> An example: distance_of_time_in_words() are hardcoded and translated into at least 4 different l10n plugins. If it changes in Rails Core, ALL the plugins must be fixed to ensure that the new code is copied to the plugins.
>
> Seen from the perspective of a localized app, there should be as few dependencies as possible, so making hooks available for localization is preferred. In the example above, the texts should be available as a variable (like the error messages in ActiveRecord).
>
> This would be an ideal solution to some of the most important i18n related issues, and I'd like to know the view of the community on this point.
>
> *From my post "[i18n-friendly, plugable Rails core](http://groups.google.com/group/rubyonrails-core/browse_thread/thread/346cda3cd39e6fa9)" in the Ruby on Rails Core list.*

It's my hope that the Rails Core team will acknowledge that it should be easier to localize your application. (Today, many text strings and date/time/currency formats are hard coded and difficult to overwrite).
