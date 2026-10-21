---
title: "Rails tip: Scaffold lists more usable"
date: "2006-05-19T11:56:51"
slug: "rails-tip-scaffolding-lists"
url: "/2006/05/19/rails-tip-scaffolding-lists/"
wp_id: 261
categories: ["Code", "Ruby on Rails", "Usability"]
tags: []
author: "jesper"
---

You might wonder what a code example is doing here in a blog about usability and web standards. As you might know, Thomas and I are both web developers, and we're really obsessed about **making usable web applications**.

What better way than to share code for things that make web apps more usable. Thomas has already [shared code that we use for this blog](/2006/05/02/justaddwaterdk-wordpress-plugins/ "Justaddwater.dk WordPress Plugins") to make it more usable (and I know there is more to come!).

This tip is regarding scaffolding code in Ruby on Rails (which we use in Capgemini). The problem is that usually your data model contains **so many attributes, that it wrecks the list view totally**. There are so many horisontal columns in the table that it's impossible to see all columns on the screen, you get horizontal scroll. And even worse: The actions (view, edit, destroy) are completely hidden.

From usability, we know that we should assist the user's focus on what's important on this page. In a list view, the primary task is to choose the right row to work on. To support this, we should **hide all columns irrelevant to the task**.

## Ruby on Rails

In Ruby on Rails, I did that by customizing the columns I wanted to view.

In the model I add a new method `self.`**`simple_content_columns`**:

``` ruby
def self.simple_content_columns
  column_names = %w{company_number name address}
  columns = []
  for c in self.content_columns do
    columns < < c if column_names.include?(c.name)
  end
  columns
end
```

Then in the list view I change from "model.content_columns" to "model.simple_content_columns" in the file: file "\_list.rhtml":

``` ruby
<table>
  <tr>
  < % for column in Company.simple_content_columns %>
    <th>< %= column.human_name %></th>
  < % end %>
  </tr>
  
< % for company in @companies %>
  <tr>
  < % for column in Company.simple_content_columns %>
    <td>< %=h company.send(column.name) %></td>
  < % end %>
[...]
```

The only thing I modified in the view file was to replace `Company.content_columns` with `Company.`**`simple_`**`content_columns`.

It's not particularly pretty, but it works. If you want something more fancy, you could take a look at the "[scaffolding extension](http://wiki.rubyonrails.org/rails/pages/Scaffolding+Extensions+Plugin)" plugin for Rails. I look forward to your improvements/suggestions/comments.\
