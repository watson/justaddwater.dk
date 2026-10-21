---
title: "Rails Localization Plugin Release Version 0.9"
date: "2008-01-13T22:26:44"
slug: "rails-localization-plugin-release-version-09"
url: "/2008/01/13/rails-localization-plugin-release-version-09/"
wp_id: 858
categories: ["Ruby on Rails"]
tags: []
---

Just a quick note to tell that I released version 0.9 of the L10n-simplified plugin. It has been a year since last release, but I had nohurry since the last version already fit for Rails 2.0.

One of the nice changes for this release is that you can now set your localized language in the environment.rb file like this:

> L10N_LANG = :da \#or whatever language/locale you wish

[Download the relase 0.9 from Rubyforge](http://rubyforge.org/frs/?group_id=2074&release_id=18106)

### Supported languages

\* Czech\
\* Danish\
\* Dutch\
\* English (for running test cases and comparing to normal texts)\
\* Finnish\
\* French\
\* French (Canadian)\
\* German\
\* Italian\
\* Korean\
\* Norwegian\
\* Portugese\
\* Russian\
\* Serbian\
\* Spanish\
\* Spanish (argentinian)\
\* Swedish\
\* Swedish Chef, and\
\* Pirate talk (just for the fun of it)\
\* any other language you want. Just dump your translation in the /lib folder

### Full changelog:

> \* --- release 0.9 (2008-01-13) ---\
> \* Possible to set language in environment.rb: L10N_LANG = :de\
> \* UTF-8 database charset configuration is default in Rails 1.2+ and 2.0, so not needed in plugin more.\
> \* L10n-Simplified plugin also available as gem from this release\
> \* Moved changelog from README to separate file changelog.txt\
> \* Removed duplicate line from lang_de.rb\
> \* Russian translation (thanks Denis Pankratov)\
> \* Corrected German date/time format (thanks Christian W Zuckschwerdt)\
> \* Added Portugese translation (thanks Carlos Afonso)\
> \* Italian translation adjustments (thanks Michele Franzin)\
> \* Fixed translation error in Swedish translation (thanks Ingemar Edsborn)\
> \* Czech translation by Karel Minařík\
> \* French lang file updated (thanks Bruno Michel)\
> \* Added Serbian (thanks Slobodan Kovacevic)\
> \* Lang_it file must be UTF-8 encoded (thanks Fabio Bonelli)\
> \* Added rake task for creating a release "rake package"\
> \* Fixed rake task for generating rdoc in UTF-8 format\
> \* Added Norwegian (thanks Fredrik Bach)

### More info:

- Justaddwater: [Ruby on Rails plugin: Localize your Rails app](/2006/08/24/ruby-on-rails-plugin-localize-your-rails-app/ "Permanent Link to Ruby on Rails plugin: Localize your Rails app") (Aug 2006)
- Rubyforge [Localization Simplified homepage](http://rubyforge.org/projects/l10n-simplified/) ([download release 0.9](http://rubyforge.org/frs/?group_id=2074&release_id=18106))
- Rails Wiki: [InternationalizationComparison](http://wiki.rubyonrails.com/rails/pages/InternationalizationComparison)
- Agilewebdevelopment plugin page: [L10N-Simplified](http://agilewebdevelopment.com/plugins/localization_simplified) (remember to vote)
