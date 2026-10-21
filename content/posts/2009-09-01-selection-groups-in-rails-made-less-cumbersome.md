---
title: "Selection Groups in Rails made less cumbersome"
date: "2009-09-01T14:50:32"
slug: "selection-groups-in-rails-made-less-cumbersome"
url: "/2009/09/01/selection-groups-in-rails-made-less-cumbersome/"
wp_id: 1128
categories: ["Code", "Ruby on Rails"]
tags: ["Code", "rails", "Ruby on Rails", "Web Development"]
author: "jesper"
---

I made this addition today after (once again) struggling with option groups for a nested Rails model.

My solution: create a new tag for FormOptionsHelper: grouped_select

<http://gist.github.com/179075>

*form_options_helper_to_add_grouped_select.rb — [gist on GitHub](https://gist.github.com/179083)*

``` ruby
### lib/form_options_helper.rb 
require 'action_view/helpers/form_helper'
module ActionView
  module Helpers
    module FormOptionsHelper
 
      ##
      def grouped_select(object, method, choices, options = {}, html_options = {})
        InstanceTag.new(object, method, self, options.delete(:object)).to_grouped_select_tag(choices, options, html_options)
      end
      
    end
    
    class InstanceTag
      include FormOptionsHelper
      def to_grouped_select_tag(choices, options, html_options)
        html_options = html_options.stringify_keys
        add_default_name_and_id(html_options)
        value = value(object)
        selected_value = options.has_key?(:selected) ? options[:selected] : value
        disabled_value = options.has_key?(:disabled) ? options[:disabled] : nil
        content_tag("select", add_options(grouped_options_for_select(choices, :selected => selected_value, :disabled => disabled_value), options, selected_value), html_options)
      end
 
    end
    
    class FormBuilder
      def grouped_select(method, choices, options = {}, html_options = {})
        @template.grouped_select(@object_name, method, choices, objectify_options(options), @default_options.merge(html_options))
      end
    end
  end
end

### config/environment.rb
require 'form_options_helper'

### app/models/expense_type.rb 
class ExpenseType < ActiveRecord::Base
  validates_uniqueness_of :name
  
  #returns grouped options split in 'popular' and 'all'
  def self.groups
    all_types = self.all.map{|t| [t.name, t.id]}
    [
      ['popular', all_types[0..2]],
      ['all', all_types]
    ]
  end
  
end


### app/views/expense_report/_expense_item.rb
<li class="expense_item">
  <%= expense.grouped_select :expense_type_id, ExpenseType.groups, {:include_blank => true}, {:class => 'expense_type'} %>
  ...
</li>
```
