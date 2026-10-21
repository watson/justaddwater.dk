---
title: "Automatic Excel Time Format Without Colon in Input"
date: "2011-01-05T20:41:43"
slug: "automatic-excel-time-format-without-colon-in-input"
url: "/2011/01/05/automatic-excel-time-format-without-colon-in-input/"
wp_id: 1395
categories: ["office"]
tags: ["excel", "microsoft", "office", "Productivity", "time", "timereporting"]
---

For a simple Excel sheet time reporting, i needed to enter hours every day for arrival and departure time.

Excel is not so smart about the time format. For instance I need to enter "9:00" for nine in the morning. I wanted just to enter "900", and let the excel sheet format the data correctly itself.

I found a working solution on PC Mag: "[Easy Date and Time Entry in Excel Tips](http://www.pcmag.com/article2/0,2817,2316755,00.asp)".

1.  Enter time format as a simple number (like "900" or "1500").
2.  Format the cell to display an extra colon.
3.  In a (hidden?) cell, calculate the time to use for further calculations.

#### Format cells for viewing:

Take the cell and format it so it visually shows the colon for the number that is input. Go to the menu item "Format" \> "Cells..." dialog. Select "Custom" format and input "0\\:00" as shown on the screenshot.

[![](/wp-content/uploads/2011/01/excel-format-normal-number-as-timeformat-300x284.png "excel-format-normal-number-as-timeformat")](/wp-content/uploads/2011/01/excel-format-normal-number-as-timeformat.png)

#### Create (hidden)? cell to calculate time:

Take an adjacent cell and let it interpret the input value as a time value. `=TIME(9, 15, 0)` is equivalent to 09:15:00 and will require 3 parameters for hour, minutes, seconds.

Our inputformat is "915". Extract hours value: `TRUNC(915/100)`\
Extract minutes value with modulus that extracts the rest 15 from 915 divided by 100: `MOD(915, 100)`

So the formula will be `=TIME( TRUNC(915/100), MOD(915,100), 0)`

This calculation is hidden in the final spreadsheet in columns E, G, and J.

Here a screenshot of the result:

[![](/wp-content/uploads/2011/01/excel-format-number-as-time-screenshot-timesheet-300x153.png "excel-format-number-as-time-screenshot-timesheet")](/wp-content/uploads/2011/01/excel-format-number-as-time-screenshot-timesheet.png)

I added the time sheet template here for further convenience.\
[2011-timesheet.xls](http://justaddwater.dk/wp-content/uploads/2011/01/2011-timesheet1.xls) (47KB Excel format)

(timesheet updated January 6th: Sum can now handle more than 24 hours)

IAnd now I can happily save entering colons every day :)
