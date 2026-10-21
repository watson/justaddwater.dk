---
title: "IntelliJ Structural Search to Convert from JUnit3 to Junit4"
date: "2012-01-18T13:37:24"
slug: "intellij-structural-search-to-convert-from-junit3-to-junit4"
url: "/2012/01/18/intellij-structural-search-to-convert-from-junit3-to-junit4/"
wp_id: 1541
categories: ["Code", "Web Development"]
tags: ["Code", "editor", "ide", "intellij", "Java"]
---

Just a quick tip for intellij users. For an old project i wanted to convert JUnit 3 testcases to JUnit4 format. Most stuff was already in place, but after the conversion, i found that some of the old "assertTrue", "assertFalse", and "assertEquals" statements were failing.

So i ended up with some short search/replace, which are really handy in IntelliJ.

## Replace "assertTrue" and "assertFalse" with "assertThat"

Search template

```
assertTrue($msg$, $actual$);
```

Replacement template:

```
org.junit.Assert.assertThat.assertThat($msg$, $actual$, org.hamcrest.core.Is.is(true));
```

## Remove "assertEquals" with delta values

Search template

```
assertEquals($msg$, $expected$, $actual$, $delta$);
```

Replacement template:

```
org.junit.Assert.assertThat($msg$, $actual$, org.hamcrest.core.Is.is($expected$));
```

## Optional Replace "assertEquals" with "assertThat"

Search template

```
assertEquals($msg$, $expected$, $actual$);
```

Replacement template:

```
org.junit.Assert.assertThat.assertThat($msg$, $actual$, org.hamcrest.core.Is.is($expected$));
```

[![](/wp-content/uploads/2012/01/intellij-structural-search-assertequals-replace-by-assertThat-300x247.png "intellij-structural-search-assertequals-replace-by-assertThat")](/wp-content/uploads/2012/01/intellij-structural-search-assertequals-replace-by-assertThat.png)
