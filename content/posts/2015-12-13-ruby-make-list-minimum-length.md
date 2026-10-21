---
title: "Ruby make list minimum length"
date: "2015-12-13T21:20:01"
slug: "ruby-make-list-minimum-length"
url: "/2015/12/13/ruby-make-list-minimum-length/"
wp_id: 1781
categories: ["Code", "Ruby on Rails"]
tags: ["Code", "ruby"]
---

In a Ruby on Rails app, I wanted a list to be at least of two items. This could be done in several ways.

Here is a first naïve impementation:

    # Naïve implementation, just return whatever number I need
    def sum_up_a(existing)
      return 2 if existing == 0
      return 1 if existing == 1
      return 0
    end

    sum_up_a(0)   # => 2
    sum_up_a(1)   # => 1
    sum_up_a(2)   # => 0
    sum_up_a(3)   # => 0
    sum_up_a(10)  # => 0

A slightly improved version could investigate number of existing, and return the diff only if needed:

    MIN_COUNT = 2
    # slightly improved with less conditionals
    def sum_up_b(existing)
      return 0 if existing >= MIN_COUNT
      MIN_COUNT - existing
    end

    sum_up_b(0)   # => 2
    sum_up_b(1)   # => 1
    sum_up_b(2)   # => 0
    sum_up_b(3)   # => 0
    sum_up_b(10)  # => 0

 

Now, my favourite. If you look at the result of "MIN_COUNT - existing". This number is negative or zero if we dont want extra rows. This means that we can rewrite the algorithm without any conditional logic like this:

    # my favorite: return the biggest number either 0 or the difference
    # Works well because difference is only positive for numbers where I 
    # need some extra rows
    def sum_up_c(existing)
      [MIN_COUNT - existing, 0].max 
    end

    sum_up_c(0)   # => 2
    sum_up_c(1)   # => 1
    sum_up_c(2)   # => 0
    sum_up_c(3)   # => 0
    sum_up_c(10)  # => 0

I like the latter, since too many conditional statements tend to clutter the logic. Just a short tip and a reminder for myself next time I run into this kind of problem.

 

Complete example gist avalilable on Github:
