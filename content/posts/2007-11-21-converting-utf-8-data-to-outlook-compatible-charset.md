---
title: "Converting UTF-8 Data to Outlook Compatible Charset"
date: "2007-11-21T15:30:13"
slug: "converting-utf-8-data-to-outlook-compatible-charset"
url: "/2007/11/21/converting-utf-8-data-to-outlook-compatible-charset/"
wp_id: 784
categories: ["Code", "Ruby on Rails"]
tags: []
author: "jesper"
technorati: ["ruby", "ruby on rails", "charset", "encoding", "utf-8", "latin-1", "iso-8859-1", "iconv"]
---

A problem in a current Rails app just found a decent solution, as Danish letters like æøå did not show up decently. It turned out (surprise) that Outlook had a problem accepting UTF-8 charset.

On the Meeting model in the Rails app I want to save to calendar in an Outlook compatible format. We solved it like this by converting from UTF-8 to ISO-8859-1 when creating the icalendar event.

meeting.rb:

``` ruby
require 'icalendar'
require 'date'

class Meeting < ActiveRecord::Base
  belongs_to :room
  belongs_to :journal

  def to_event
    event = Icalendar::Event.new
    event.summary = "Møde " + (journal.number || "no number..")
    event.description = description.split("\n").join("\n\n")
    event.klass = "PUBLIC"
    event.start = start.to_datetime
    event.end = self.end.to_datetime
    event.location = meeting.room.name + " " meeting.room.address
    event
  end
```

And meetings_controller.rb:

``` ruby
require 'icalendar'
require 'iconv'

class MeetingsController < ApplicationController
  include Icalendar
  def show
    @courtmeeting = Courtmeeting.find(params[:id])
    respond_to do |format|
      format.html # show.html.erb
      format.xml  { render :xml  => @courtmeeting }
      format.ical { render :text => render_to_ical([@courtmeeting])  }
    end
  end


  def render_to_ical(courtmeetings)
    headers['Content-Type'] = "text/calendar; charset=ISO-8859-1"
    cal = Calendar.new
    courtmeetings.each do |meeting|
      cal.add_event(meeting.to_event)
    end
    Iconv.iconv('ISO-8859-1', 'UTF-8', cal.to_ical).to_s
  end
end
```

Very simple, yet very effective way to have your meetings exposed to Outlook in a way that solves the character encoding problems.
