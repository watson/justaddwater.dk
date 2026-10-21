---
title: "AJAX businesscase: Reduce development costs and increase usability"
date: "2006-02-08T12:00:28"
slug: "ajax-businesscase"
url: "/2006/02/08/ajax-businesscase/"
wp_id: 2
categories: ["AJAX", "Best of Justaddwater", "Businesscase"]
tags: []
author: "jesper"
technorati: ["usabililty", "ajax validation", "javascript", "interaction design", "ASP.Net", "AJAX.Net", "business case"]
---

As a followup to my earlier post "[AJAX performance stats, ROI, and business value](/2006/01/14/ajax-performance-stats-roi-and-business-value/ "Justaddwater.dk: AJAX performance stats, ROI, and business value")", I decided that I'd share with you some considerations on a recent project I was involved in. I can't give you all the juicy details, and I might never be able to show you the final solution or tell, who the customer is.

Anyways, I want to give you some of the details on why we decided to implement AJAX validations in this particular web application. I worked on a project for a Danish company in the financial sector. We had a complex interface where the user had to enter a lot of information about a lot of users. This is illustrated here with user \#1, \#2, and so on.

![AJAX application object model](/wp-content/uploads/2006/01/ajax%20validation%20object%20model.png)

In this particular solution, the typical usage scenario is that an employee has data about multiple users to enter: That could for example be name, age, social security numbers etc.

### Edit one object at a time

We originally looked at two different interaction models. Version 1 where the employee could edit one user at a time, and then go back to the main page, as shown below. I really can't show the webpages used, but here is a sketch that shows the principle.

![ajax validation version 1](/wp-content/uploads/2006/01/ajax%20validation%20version1.png "ajax validation version 1")

So, the employee clicks link to edit user \#1, then back and continue to \#2 etc. This was the standard setup of our development framework: Microsoft ASP.NET 1.1.

To edit one object at a time has some advantages:

- Very low development costs: ASP.NET framework out-of-the-box
- Data is saved while editing one user at a time.
- Focus on one object at a time: You can only edit one and only continue when that single object is edited and has no errors.

On the same time it is also annoying for users in certain situations if they're not allowed to continue until all errors are solved and all required data is filled in.

I see two big disadvantage in this model:

- It requires a lot of clicks. Click to edit user \#1, back to link page, click to edit user#2, etc. This is so-called "[pogosticking](/2006/02/05/pogosticking-and-why-it-should-be-avoided/ "Justaddwater.dk:     Pogosticking and why it should be avoided")". Extra clicks yields extra time and thus ... lower performance (XX todo: usability)
- Only to be able to edit one user at a time could be annoying under some conditions. It's like an Excel spreadsheet where you can only edit one row at a time — It will work, but could be cumbersome when editing in a particular column.

So besides the expected extra time consumption, the real problem here is when data is entered in a non-linear way. To stay in the Excel example, if we decide to organize by rows, then what will happen if the user wants to edit columns: It will be absolutely cumbersome.

A few interviews and meetings later, we decided that this was not a solution that the end users could benefit from: Too cumbersome.

### Edit multiple objects at the same time

In this scenario, we decided to support easier editing of all objects at a time. Like in the Excel metaphor it will be possible to edit by row or by column.\
![ajax validation version 2](/wp-content/uploads/2006/01/ajax%20validation%20version2.png "ajax validation version 2")

Some advantages of this screen layout:

- Significantly faster task completion (faster to fill out the form)
- Less [pogosticking](/2006/02/05/pogosticking-and-why-it-should-be-avoided/ "Justaddwater.dk:     Pogosticking and why it should be avoided") and therefore less back-and-forth navigation
- Easier to edit non-linear: In a prefilled form, it will be easy to edit just a few fields.

**All in all: Easier to use, less navigation and faster completion of the form**.\
In the usability tests I've participated in, users always make errors, typos, misconceptions, etc. The real timesaver in this example are the AJAX field validations.

### AJAX validations the big time-saver

For validations on the page, we wanted the application to validate each input field immediately. When the user moves on to the next field, the field value is sent back to the web server and validated. If field contents are not recognized, print an error message below field and set red background color on field.

![ajax validation version 2 with text describing behaviour](/wp-content/uploads/2006/01/ajax%20validation%20version2text.png "ajax validation version 2 with text describing behaviour")

This way, we give the user **feedback as soon as possible without interrupting users work**.

- Unobtrusive error messages (users decide when to correct the error)
- Error messages occur where errors occur
- Preserves the benefits from multiple edit

Also, in this way, we do all validations server-side. Here, fields appear to be validated client-side, but behind the scenes, field data is sent to the webserver. This means that no JavaScript validations have to be coded (which I usually see as a time-consuming task).

For security reasons, we always have to code server-side validations. In this way, we only code validations on the webserver, but use them on the client-side, which in this particular project is a big time-saver. For instance, there is a date field that only accepts days on which banks are open. This calculation is fairly complex for Danish companies because bank holidays tend to move every year. For this particular project, it might end with a database table lookup, so the validation would be impossible (or very expensive) using JavaScript.

### Conclusion

The reasons we choose AJAX validations for this particular project are:

- **Lower development costs**: Only server-side validations had to be coded. These validations can then be executed client-side via the AJAX framework. Depending on browser compatibility, we have probably saved 20-40% of the time it took writing the server-side validations.
- **Faster user interface**: No unnessecary navigation back-and-forth to fill out data on multiple objects.
- **Unobtrusive error handling**: Errors can be corrected immediately and in an un-obtrusive way: The user can continue typing in other fields or correct errors as they happen. Compare this to the old variant, where an alertbox is triggered. Alertboxes say "correct me NOW before you do anything else".

These are the details I can share with you, and it certainly does not fulfill the wishes of Andre Charland, Ebusiness-Apps who's [Looking for More AJAX Case Studies](http://blogs.ebusiness-apps.com/andre/?p=81 "Permanent Link: Looking for More AJAX Case Studies").
