---
title: "GWT relevant snippets for IntelliJ Idea editor"
date: "2010-10-05T22:47:32"
slug: "gwt-relevant-snippets-for-intellij-idea-editor"
url: "/2010/10/05/gwt-relevant-snippets-for-intellij-idea-editor/"
wp_id: 1361
categories: ["Web Development"]
tags: ["development", "gwt", "Java", "w", "Web Development"]
author: "jesper"
---

I created a list of snippets that I loaded into my IntelliJ editor, which I find useful when working with Google Webtoolkit (GWT). So far, it's a very short list.

Snippet 1: Live template to bootstrap a class to use UI binder logic. Very useful when converting existing (pre gwt 2.0) Java classes to UI binder pattern, which gives better separation of logic and view.

Snippet 2: Create new UiBinder.ui.xml file. Intellij has support for creating entire new java class + uibinder file. That is useful for new classes, but most often I find myself converting an existing class, and needed this shortcut for that.

*com.google.gwt.template.binder.java — [gist on GitHub](https://gist.github.com/612402)*

``` java
/* add this to IntelliJ Idea "File>Settings> Live templates"
 *
 * Abbreviation: binder
 * Group:        user
 * Description:  GWT UiBinder bootstrapping on existing class
 *
 */

    @com.google.gwt.uibinder.client.UiTemplate("$CLASS$.ui.xml")
    interface Binder extends com.google.gwt.uibinder.client.UiBinder<com.google.gwt.user.client.ui.HTMLPanel,$CLASS$> {
    }

    private static Binder ourUiBinder = GWT.create(Binder.class);

    //public $CLASS$() {
    //    com.google.gwt.user.client.ui.HTMLPanel rootElement = ourUiBinder.createAndBindUi(this);
    //}
```

*com.google.gwt.template.file.uibinder.xml — [gist on GitHub](https://gist.github.com/612402)*

``` xml
<!-- 
  add this to IntelliJ Idea "File > Settings > File templates"
  "Templates" tab
  Name:      GWT UI binder
  Extension: xml

-->
<ui:UiBinder xmlns:ui='urn:ui:com.google.gwt.uibinder'
             xmlns:g='urn:import:com.google.gwt.user.client.ui'>
  <${ROOT_TAG_NAME}>
    
  </${ROOT_TAG_NAME}>
</ui:UiBinder>
```
