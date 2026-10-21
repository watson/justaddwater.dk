---
title: "RailsConf Live Notes: Testing Tutorial"
date: "2007-09-17T17:05:18"
slug: "railsconf-live-notes-testing-tutorial"
url: "/2007/09/17/railsconf-live-notes-testing-tutorial/"
wp_id: 714
categories: ["Events/seminars", "Railsconf", "Ruby on Rails"]
tags: []
author: "jesper"
---

I'm at RailsConf Europe here in Berlin, and now attending the full-day session "[Ruby (and Rails) Testing Techniques: Charity Tutorial](http://www.railsconfeurope.com/cs/railseurope2007/view/e_sess/14736) by Marcel Molina and Chad Fowler.

Below are the live notes, I wrote with Mads Buus (we wrote the notes collaboratively with Google Docs, [direct link](http://docs.google.com/Doc?docid=az54pw3d9f_24hsvwnt&hl=en)).

[![IMG_3392_crop](http://farm2.static.flickr.com/1342/1395418767_1d23095952_m.jpg)](http://www.flickr.com/photos/jesper/1395418767/)

[![IMG_3397](http://farm2.static.flickr.com/1411/1396313456_e999c55dfe_m.jpg)](http://www.flickr.com/photos/jesper/1396313456/)

 

- Verifying your expectations.
- Guru reads the output" -testing (just printing stuff out to verify something)
- Testing is better: declare your expectations.
- Real value: Analysis, design process. Bonus: verification.
- If something is too hard to write, you're probably doing it wrong (design is wrong)
- Red, green, refactoring. Write a test that fail, the implement until green.
- Red/green testing: Write code to make testing fail... red. Then write just enough code to make test pass.
- Marcel's loops coding/testing is 1-5 minutes. Possible to work with 20 second loops
- No 'Code smells', no comments. 'method_missing' needs documentation

Your code should be so simple that you shouldnt put comments in your code. If it just says "test_foo" \[new team members\] have to do more brain processing.

Nick: think of my self as a spec writer more than a programmer

Red/green refactor\
\* refactor your tests before

flunk "not implemented" is cool because i can see that it's

RSpec makes "not implemented" yellow so it doesn't mix up with the red

Marcel: Eventually we re all going to be small talk programmers. Ruby is the entry drug

class PokerException \< Exception\
end\
doesnt need right now. always add later. Removed

Chad: i really work in small increments

Marcel: at the beginning i did "existing? tests"\
...and within 15 minutes that test becomes so non valuable.

Chad: I challenge you to write long method names ... at least for a day or two\
When you follow that style, your code will be cleaner and healthier

Write flunking test to identify an assumptions\
def test_all_validation_are_run\
flunk 'we probably want to create a validation test case for this'\
end

Chad: Have you run your other test recently?

Chad: Id like to have only one test failing at a time

[![IMG_3403](http://farm2.static.flickr.com/1192/1395426465_0bd1d6a2d0_m.jpg)](http://www.flickr.com/photos/jesper/1395426465/)

Mads: Instead of fixing the design, we wirte more tests. Are we thinking too much about test than the code?\
Chad: now, were running into friction. and frictions tell us tu stop and think about the design

--- break ---

(my comment: the discussions her usually get into details with "business-logic")

test helper function\
card_with(options) is subverting the benefit of the tests as long as Marcel uses that in the test file only.

replaced with\
validate_card_with(options)\
Card.new(options).validate\
end

Later:\
validate_number_card_with(options)

NumberCard.new(options).validate\
end

Another point:\
card.numbers.sort_by{rand}.first

Private methods in Test::Unit\
doesnt impact Test::Unit\
but the fact is that the reader of the code can ignore them below the private

Chad: TDD enables you to delay difficult decisions.. ... and you keep delaying them, and it ends up that you never have to take the difficult decisions

def self.foo\
end\
or\
class \<\< self\
def foo\
end\
end

M: Visually the latter is better. Easier to grasp overview of the class. Also when you add private methods later, there are more sections of your class

AgileTalk "just print all names of your test methods" (not found by me on google)\
rake task

"Test everything that could possibly break" quote by kent beck.\
That domain spsecific understanding grows over time. So if something weird with card number 11 happens, then you should probably add a test case for number 11.

----lunch break----\
"if it's strip poker I can see why we implement base class"

\$: = LOAD_PATH\
\$: .unshift File.dirname(\_\_FILE\_\_)\
Adding current directory onto our loadpath

DR. Jekyll and Mr hyde\
The good Dr. Jekyll writes a test, then laugh at Mr Hyde (the lazy programmer) and force him to implement the smallest amount of code to make it pass

Incremental refactoring: Even if you are able to see more steps ahead, you should do Incremental refactoring and test on the way.

Moving from low-level to high-level

Metrics for measuring test quality

rake test:ratio (marcels own)\
Code to Test Ratio: 1:1.28

Rcov\
issue: sometimes reports false negatives (example lines not covered "end..end..end")\
c0, c1, c2 coverage\
Line number counting

code to Test ratio and Rcov used together is very good indicators.

Heckle can go into those examaples with more loops on the same line\
if foo && bar && baz

end\
Here Hecle will go in and modify bar until test breaks

Now into the highl-level\
require 'flexmock'\
require 'flexmock/test_unit'\
(Jim Weirich (co?)authored it and we tend to use libraries he wrote)

class GameTest\
attr_reader :game\
def setup\
@game = flexmock('Game')\
@dealer = flexmock('Dealer')\
@player1 = flexmock('Player')\
@player2 = flexmock('Player')\
end

Chad (again): "it would be interesting to run just what you have and see what it does"

player.should_receive(:join).once.ordered.with(game)\
player.should_receive(:bet).once.ordered

partial mock\
from\
@game = flexmock('Game')\
to\
@game = flexmock(Game.new)\
mocks if methods are not implemented.

to\
@game = flexmock(Game).new_instances\
difference??

---..\
fixtures\
pain to deal with, and not so explicit

it makes sense to mock up and never hit the db

class Person \< ActiveRecord::Base\
end

\####test file below:\
flexmock(Person).should_recdeive(:find).with(:first).and_return(admin_for)\
\#... valid_person definde helper method

assert_equal admin_for_company, Person.admin

Marcel\
valid_user_attibutes\
create_valid_user\
create_valid_user_with_company\
\#always methods parametrized to be overridden

Marcel: For 2 years, fixtures made me angry with rails

Chad: We only hate it because its not as good as the rest of Rails, but it's better than what we had before

===RSpec===\
Test::Unit leads to one test per method in your code

Test usually takes longer.\
b vs t Behaviours versus testing: So\
=\> good Test Driven Development with the word "test" removed from it

Is your name Dan, by any chance? Did you coin the term BDD, by any chance?

rspec is a specification framework

tools more implemented and more into textmate\
rake test:spec

it \[string\]\
not passing a block is an unimplemented spec

Its developed way more actively than Test::Unit and it's also the tooling around it

RSpec generators (general opinion) they are probably too long

=== Jesper's notes below:===

Windows shortcuts for E-texteditor

- CTRL+R run test file we're working in.
- CTRL+Shift+R run test in focus
- deft + tab "def test\_ ... end"

Idea for "deft" shortcut: replace all spaces as-you-type with underscores
