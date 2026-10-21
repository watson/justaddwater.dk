---
title: "Rake Task To Validate All Items on All Models"
date: "2010-02-07T14:13:04"
slug: "rake-task-to-validate-all-items-on-all-models"
url: "/2010/02/07/rake-task-to-validate-all-items-on-all-models/"
wp_id: 1270
categories: ["Ruby on Rails"]
tags: []
author: "jesper"
---

I wanted a way to see if somebody had entered "illegal" data into loaded fixtures. So I wrote this simple rake task. It's also useful to run as you add more validations to your files.

*validate_models.rake — [gist on GitHub](https://gist.github.com/297427)*

``` ruby
#put this file in /lib/tasks and run `rake db:models:validate`
#created 2010-02-07 by Jesper Rønn-Jensen
require 'find'

namespace :db do
  namespace :models do
    desc 'Dumps all models into fixtures.'
    task :validate => :environment do
      models = []
      Find.find(RAILS_ROOT + '/app/models') do |path|
        unless File.directory?(path) then models << path.match(/(\w+).rb/)[1] end
      end
  
      puts "Found models: " + models.join(', ')
      errors = []
      models.each do |m|
        puts "Validating #{m.camelize} items"
#        m.camelize.constantize.transaction do
          m.camelize.constantize.all.each do |item|
            if item.valid?
              print "."
            else
              print "E"
              errors << item
            end
          end
#        end#end transaction
        puts ""
      end
      errors.each do |item|
        puts "ERROR in #{item.inspect}"
      end
    end#end task
  end
end
```
