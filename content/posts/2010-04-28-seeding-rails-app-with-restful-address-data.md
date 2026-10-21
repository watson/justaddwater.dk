---
title: "Seeding Rails App With RESTful Address Data"
date: "2010-04-28T11:55:26"
slug: "seeding-rails-app-with-restful-address-data"
url: "/2010/04/28/seeding-rails-app-with-restful-address-data/"
wp_id: 1341
categories: ["Code", "Ruby on Rails"]
tags: ["bootstrap", "Code", "rails", "ruby"]
---

Grabbing data from Restful webservices has never been easier. I use this code in the Rails /db/seeds.rb file to grab data from the Danish webservice with addresses, municipalities, regions, etc.

I decided to import the data into a local database to ensure it could work offline.

Code from `/db/seeds.rb` file:

[View gist 382105 on GitHub](https://gist.github.com/382105)

Now I can access municipalities in a grouped selectbox like so in the view code:

    <%
     options = option_groups_from_collection_for_select(Region.all, :kommuner, :name, :id, :name) 
    %>

    <%=
     f.select("kommune_id", options, {}, {:class => "short"}) 
    %>

The final result rendered in the user interface:\
![](/wp-content/uploads/2010/04/Screen-shot-2010-04-28-at-3.18.06-PM.png "Rails rendered optgroup selectbox")

This code is based on Rails 2.3.5.
