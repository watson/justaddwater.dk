---
title: "Java Friday Fun: @WTF annotations in code"
date: "2011-09-16T21:52:08"
slug: "java-friday-fun-wtf-annotations-in-code"
url: "/2011/09/16/java-friday-fun-wtf-annotations-in-code/"
wp_id: 1492
categories: ["Code", "Java"]
tags: ["Code", "Java", "quality", "Review", "wtf"]
author: "jesper"
---

Time for a little geeky gimmick. Some developers see and express a lot of "WTF??" while trying to understand code

[![](/wp-content/uploads/2011/09/focus-shift-cartoon-wtf-per-minute-wtfm-300x282.jpg "focus-shift-cartoon-wtf-per-minute-wtfm")](/wp-content/uploads/2011/09/focus-shift-cartoon-wtf-per-minute-wtfm.jpg)

IN this spirit, i created a quick @WTF annotation for Java.

Besides being completely useless (its removed at compile time), its only purpose is to give developers a new way to express themselves in code.

*WTF.java — [gist on GitHub](https://gist.github.com/1222965)*

``` java
@Retention(RetentionPolicy.SOURCE)
@Target({ElementType.TYPE, ElementType.FIELD, ElementType.METHOD, ElementType.CONSTRUCTOR, ElementType.LOCAL_VARIABLE})
public @interface WTF {

    /**
     * Optionally specify <code>explain</code>, and write why you dont understand this annotated element
     */
    String explain() default "";

    /**
     * Optionally add <code>explanation</code>, and to explain why and how the element should be used
     */
    @Deprecated
    String  explanation() default "";
}
```

The cartoon states "The only valid measurement of code quality: WTFs/minute". With the \<code\>@WTF\</code\> annotations, I would like to take it a little further. By annotating the code, you can actually encourage colleagues to help you fix it.

The best fix for WTF-code is of course to refactor, so that it becomes readable.

Interesting article:

<http://www.gridshore.nl/2008/03/29/how-wtfs-improve-code-quality-awareness/>

The original cartoon strip:  <http://www.osnews.com/story/19266/WTFs_m>
