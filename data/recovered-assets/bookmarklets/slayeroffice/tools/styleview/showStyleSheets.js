
/*********************************************

	Style Sheet Viewer Favelet
	version 1.0
	last revision: 03.12.2004
	steve@slayeroffice.com
	http://slayeroffice.com/?c=/tools/styleview/styleview.html

	please notify me of any modifications you make
	so that I can update the version hosted
	at slayeroffice.com

	(c) 2004 S.G. Chipman
*********************************************/

function showStyleSheets() {
	if(document.all) return alert("This tool is designed for Gecko based browsers like Mozilla and Firefox.");
	try {
	m="";
	d=document;
	s=d.styleSheets;
	if(!s.length)return alert("No style sheets!");
	for(i=0;i<s.length;i++){
		m+="<u>Style Sheet #"+(i+1)+"</u><br />"; //<ul>";
		if(s[i].type) m+= "type: " + s[i].type + "<br />";
		if(s[i].rel) m+="rel: " + s[i].rel + "<br /";
		if(s[i].href) m+="href: " + s[i].href + "<br />";
		m+="<ul>";
		for(e=0;e<s[i].cssRules.length;e++){
			if(s[i].cssRules[e].cssText.indexOf("@import")>-1) {
				ss = s[i].cssRules[e].styleSheet;
				for(r=0;r<ss.cssRules.length;r++) m+=parseStyleSheetRule(ss,r);
			} else {
				m+=parseStyleSheetRule(s[i],e);
			}
		}
		m+="</ul>";
	}
	z=d.body.appendChild(document.createElement("div"));
	z.id="f";
	z.style.position="absolute";
	z.style.top="0";
	z.style.border="2px solid #000";
	z.style.font="9pt verdana";
	z.style.backgroundColor="#E3EBED";
	z.style.lineHeight="1.5em";
	z.style.color="#000";
	z.style.backgroundImage="url(http://slayeroffice.com/gr/office_logo_green.gif)";
	z.style.backgroundPosition="bottom right";
	z.style.backgroundRepeat="no-repeat";
	z.style.textAlign="left";
	z.style.padding="5px";
	z.style.zIndex="100";
	z.innerHTML=m + "<div style=\"font:9px verdana;\">Style Sheet Viewer<br />Version 1.0<br />Last Revision: 03.12.2004<br /><a href=\"javascript:removeFaveletObjects();\">close</a></div>"
	} catch(err) {
		alert("An error occured parsing the stylesheet.\n\n" + err.message);
	}
}

function parseStyleSheetRule(styleSheetObject,styleSheetRuleIndex) {
	w="<b>"+styleSheetObject.cssRules[styleSheetRuleIndex].selectorText+"</b><ul>";
	t=styleSheetObject.cssRules[styleSheetRuleIndex].style.cssText.split(";");
	k=0;
	while(t[k]){
		w+="<li>"+t[k]+"</li>";
		k++;
	}
	w+="</ul>";
	return w;
}

function removeFaveletObjects() {
	document.body.removeChild(document.getElementById("f"));
	document.body.removeChild(document.getElementById("sss"));
}

showStyleSheets();