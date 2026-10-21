---
title: "Mobile Web Best Practices"
date: "2006-06-28T10:13:32"
slug: "mobile-web-best-practices"
url: "/2006/06/28/mobile-web-best-practices/"
wp_id: 342
categories: ["Accessibility", "Mobile", "Usability", "User experience", "Web Standards"]
tags: []
---

[![W3C Icon](/wp-content/uploads/2006/06/w3c_home.png "W3C Icon")](http://www.w3.org/ "W3C")Yesterday the W3C released a Candidate Recommendation document called "[Mobile Web Best Practices 1.0](http://www.w3.org/TR/2006/CR-mobile-bp-20060627/ "W3C: Mobile Web Best Practices 1.0")". With this document W3C is offering a set of guidelines to help web developers deliver a better user experience to mobile users.

The deadline for providing feedback to W3C is the 27th of August 2006 and all developers are encouraged to try it out.

At the core of the recommendation are 60 statements that every web developer should follow:

> \
>
> 1.  \
> 2.  **Thematic Consistency**\
>     Ensure that content provided by accessing a URI yields a thematically coherent experience when accessed from different devices.
>     \
> 3.  **Capabilities**\
>     Exploit device capabilities to provide an enhanced user experience.
>     \
> 4.  **Deficiencies**\
>     Take reasonable steps to work around deficient implementations.
>     \
> 5.  **Testing**\
>     Carry out testing on actual devices as well as emulators.
>     \
> 6.  **URIs**\
>     Keep the URIs of site entry points short.
>     \
> 7.  **Navbar**\
>     Provide only minimal navigation at the top of the page.
>     \
> 8.  **Balance**\
>     Take into account the trade-off between having too many links on a page and asking the user to follow too many links to reach what they are looking for.
>     \
> 9.  **Navigation**\
>     Provide consistent navigation mechanisms.
>     \
> 10. **Access Keys**\
>     Assign access keys to links in navigational menus and frequently accessed functionality.
>     \
> 11. **Link Target Id**\
>     Clearly identify the target of each link.
>     \
> 12. **Link Target Format**\
>     Note the target file's format unless you know the device supports it.
>     \
> 13. **Image Maps**\
>     Do not use image maps unless you know the device supports them effectively.
>     \
> 14. **Pop Ups**\
>     Do not cause pop-ups or other windows to appear and do not change the current window without informing the user.
>     \
> 15. **Auto Refresh**\
>     Do not create periodically auto-refreshing pages, unless you have informed the user and provided a means of stopping it.
>     \
> 16. **Redirection**\
>     Do not use markup to redirect pages automatically. Instead, configure the server to perform redirects by means of HTTP 3xx codes.
>     \
> 17. **External Resources**\
>     Keep the number of externally linked resources to a minimum.
>     \
> 18. **Suitable**\
>     Ensure that content is suitable for use in a mobile context.
>     \
> 19. **Clarity**\
>     Use clear and simple language.
>     \
> 20. **Limited**\
>     Limit content to what the user has requested.
>     \
> 21. **Page Size Usable**\
>     Divide pages into usable but limited size portions.
>     \
> 22. **Page Size Limit**\
>     Ensure that the overall size of page is appropriate to the memory limitations of the device.
>     \
> 23. **Scrolling**\
>     Limit scrolling to one direction, unless secondary scrolling cannot be avoided.
>     \
> 24. **Central Meaning**\
>     Ensure that material that is central to the meaning of the page precedes material that is not.
>     \
> 25. **Graphics For Spacing**\
>     Do not use graphics for spacing.
>     \
> 26. **Large Graphics**\
>     Do not use images that cannot be rendered by the device. Avoid large or high resolution images except where critical information would otherwise be lost.
>     \
> 27. **Use of Color**\
>     Ensure that information conveyed with color is also available without color.
>     \
> 28. **Color Contrast**\
>     Ensure that foreground and background color combinations provide sufficient contrast.
>     \
> 29. **Background Image Readability**\
>     When using background images make sure that content remains readable on the device.
>     \
> 30. **Page Title**\
>     Provide a short but descriptive page title.
>     \
> 31. **No Frames**\
>     Do not use frames.
>     \
> 32. **Structure**\
>     Use features of the markup language to indicate logical document structure.
>     \
> 33. **Tables Support**\
>     Do not use tables unless the device is known to support them.
>     \
> 34. **Tables Nested**\
>     Do not use nested tables.
>     \
> 35. **Tables Layout**\
>     Do not use tables for layout.
>     \
> 36. **Tables Alternatives**\
>     Where possible, use an alternative to tabular presentation.
>     \
> 37. **Non-Text Alternatives**\
>     Provide a text equivalent for every non-text element.
>     \
> 38. **Objects or Script**\
>     Do not rely on embedded objects or script.
>     \
> 39. **Images Specify Size**\
>     Specify the size of images in markup, if they have an intrinsic size.
>     \
> 40. **Images Resizing**\
>     Resize images at the server, if they have an intrinsic size.
>     \
> 41. **Valid Markup**\
>     Create documents that validate to published formal grammars.
>     \
> 42. **Measures**\
>     Do not use pixel measures and do not use absolute units in markup language attribute values and style sheet property values.
>     \
> 43. **Style Sheets Use**\
>     Use style sheets to control layout and presentation, unless the device is known not to support them.
>     \
> 44. **Style Sheets Support**\
>     Organize documents so that if necessary they may be read without style sheets.
>     \
> 45. **Style Sheets Size**\
>     Keep style sheets small.
>     \
> 46. **Minimize**\
>     Use terse, efficient markup.
>     \
> 47. **Content Format Support**\
>     Send content in a format that is known to be supported by the device.
>     \
> 48. **Content Format Preferred**\
>     Where possible, send content in a preferred format.
>     \
> 49. **Character Encoding Support**\
>     Ensure that content is encoded using a character encoding that is known to be supported by the device.
>     \
> 50. **Character Encoding Use**\
>     Indicate in the response the character encoding being used.
>     \
> 51. **Error Messages**\
>     Provide informative error messages and a means of navigating away from an error message back to useful information.
>     \
> 52. **Cookies**\
>     Do not rely on cookies being available.
>     \
> 53. **Caching**\
>     Provide caching information in HTTP responses.
>     \
> 54. **Fonts**\
>     Do not rely on support of font related styling.
>     \
> 55. **Minimize Keystrokes**\
>     Keep the number of keystrokes to a minimum.
>     \
> 56. **Avoid Free Text**\
>     Avoid free text entry where possible.
>     \
> 57. **Provide Defaults**\
>     Provide pre-selected default values where possible.
>     \
> 58. **Default Input Mode**\
>     Specify a default text entry mode, language and/or input format, if the device is known to support it.
>     \
> 59. **Tab Order**\
>     Create a logical order through links, form controls and objects.
>     \
> 60. **Control Labelling**\
>     Label all form controls appropriately and explicitly associate labels with form controls.
>     \
> 61. **Control Position**\
>     Position labels so they lay out properly in relation to the form controls they refer to.
>     \
>
> \
