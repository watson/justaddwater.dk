// ==UserScript==
// @name           cap nordic internal systems Firefox Login error
// @namespace      http://userscripts.org/users/103819
// @description    Bypass the annoying redirect not happening on Firefox because of HTML in HEAD element.
// @version        1.0
// @include        http://applications.capgemini.se/applications/employee/employee.cfm
// @include        http://applications.capgemini.se/applications/skills/skills.cfm
// @include        http://applications.capgemini.se/applications/Staffing/staffing.cfm
// @include        http://applications.capgemini.se/applications/common/common.cfm
// @include        http://applications.capgemini.se/Applications/ADManager/ADManager.cfm
// @include        http://applications.capgemini.se/Applications/Approve/Approve.cfm
// @include        http://applications.capgemini.se/applications/common/common.cfm
// @include        http://applications.capgemini.se/Applications/CTE/CTE.cfm
// @include        http://applications.capgemini.se/Applications/CTR/CTR.cfm
// @include        http://applications.capgemini.se/Applications/CTRArchive/CTRArchive.cfm
// @include        http://applications.capgemini.se/applications/employee/employee.cfm
// @include        http://applications.capgemini.se/Applications/ESR/ESR.cfm
// @include        http://applications.capgemini.se/Applications/ESRArchive/ESRArchive.cfm
// @include        http://applications.capgemini.se/Applications/Event/Event.cfm
// @include        http://applications.capgemini.se/applications/forms/forms.cfm
// @include        http://applications.capgemini.se/applications/Process/Process.cfm
// @include        http://applications.capgemini.se/Applications/GPS/GPS.cfm
// @include        http://applications.capgemini.se/Applications/object/Object.cfm
// @include        http://applications.capgemini.se/Applications/PDP/PDP.cfm
// @include        http://applications.capgemini.se/Applications/eReview/eReviw.cfm
// @include        http://applications.capgemini.se/Applications/ProjectArchive/ProjectArchive.cfm
// @include        http://applications.capgemini.se/Applications/Project/Project.cfm
// @include        http://applications.capgemini.se/applications/skills/skills.cfm
// @include        http://applications.capgemini.se/applications/Staffing/Staffing.cfm
// ==/UserScript==


// alert(document);
// alert(document.body);
// alert(document.body.innerHTML);

var f = document.forms[0];
alert

var b = document.createElement('input');
b.type = 'submit';
b.value = 'submit this form to login';

document.forms[0].appendChild(b);

document.forms[0].submit();


/*

RESEARCH: found the list of links on this page: http://applications.capgemini.se/index.cfm
var coll = document.getElementsByTagName('a')
for(i=0;i<coll.length;i++) { var t= coll[i].href; if(t.match(/\/applications\//i)) {console.log(coll[i].href); }; }
http://applications.capgemini.se/applications/employee
http://applications.capgemini.se/applications/skills
http://applications.capgemini.se/applications/Staffing
http://applications.capgemini.se/applications/common
http://applications.capgemini.se/Applications/ADManager/
http://applications.capgemini.se/Applications/Approve
http://applications.capgemini.se/applications/CHL
http://applications.capgemini.se/applications/common
http://applications.capgemini.se/Applications/CTE/
http://applications.capgemini.se/Applications/CTR/
http://applications.capgemini.se/Applications/CTRArchive/
http://applications.capgemini.se/applications/employee
http://applications.capgemini.se/Applications/ESR
http://applications.capgemini.se/Applications/ESRArchive
http://applications.capgemini.se/Applications/Event
http://applications.capgemini.se/applications/forms
http://applications.capgemini.se/applications/Process
http://applications.capgemini.se/Applications/GPS/
http://applications.capgemini.se/Applications/object/
http://applications.capgemini.se/Applications/ADManager/?Password=1
http://applications.capgemini.se/Applications/PDP/
http://applications.capgemini.se/Applications/eReview
http://applications.capgemini.se/Applications/ProjectArchive
http://applications.capgemini.se/Applications/Project
http://applications.capgemini.se/applications/recruitment
http://applications.capgemini.se/applications/skills
http://applications.capgemini.se/applications/Staffing
http://intra.nordic.capgemini.com/Applications/WEBTRENDS/WEBTRENDS.htm
*/
