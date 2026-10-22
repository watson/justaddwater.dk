/*********************************************

	Color List Favelet for Mozilla Based Browsers
	version 1.3
	last revision:
		v1.3: 02.10.2006
		v1.2: 11.05.2004
	steve@slayeroffice.com
	http://slayeroffice.com

	Please leave this notice intact!

	Should you make any modifications/improvements
	to this code please let me know so that I can
	update the version hosted at slayeroffice

*********************************************/

var d=document;
var colors=new Array();
var mObj;
var foundWhere = new Array();

d.onkeydown=so_captureKeyEvent;
d.onmousemove = so_handleMouseMoveEvent;
var mDown = false;
var mx,my,offsetX,offsetY;

function so_init() {
	if(document.all)return alert("This version of the Color List is for Mozilla based browsers.\n\nPlease see slayeroffice.com for a version for your browser.");

	window.scrollTo(0,0);

	sObj=d.getElementsByTagName("head")[0].appendChild(d.createElement("link"));
	sObj.type = "text/css";
	sObj.rel="stylesheet";
	sObj.href="http://slayeroffice.com/tools/color_list/color_list.css";
	sObj.id = "so_color_list_css";

	so_createContainer();
	so_getStyleSheetColors();
	so_getInlineColors();
	so_getAttributeColors();
	
	h1 = mObj.appendChild(d.createElement("h1"));
	h1.id = "dragHeader";
	b = h1.appendChild(d.createElement("b"));
	b.appendChild(d.createTextNode("slayer"));
	h1.appendChild(d.createTextNode("office | tools | color list"));


	so_createColorTable();

	credits = mObj.appendChild(d.createElement("div"));
	credits.id = "so_credits";
	credits.appendChild(d.createTextNode("[esc] to "));
	a = credits.appendChild(d.createElement("a"));
	a.href = "javascript:so_cleanUp();";
	a.appendChild(d.createTextNode("close"));
	credits.appendChild(d.createElement("br"));
	credits.appendChild(d.createTextNode("Color List v1.3"));
	credits.appendChild(d.createElement("br"));
	credits.appendChild(d.createTextNode("Last Revision: 02.10.2006"));
	credits.appendChild(d.createElement("br"));
	a = credits.appendChild(d.createElement("a"));
	a.href = "http://slayeroffice.com";
	a.appendChild(d.createTextNode("slayeroffice.com"));

	d.getElementById("dragHeader").onmousedown = so_captureOffset;
	d.getElementById("dragHeader").onmouseup = function() { mDown=false; }
}

function so_captureKeyEvent(e) {
	keyCode = d.all?window.event.keyCode:e.keyCode;
	if(keyCode == 27) so_cleanUp();
}

function so_cleanUp() {
	d.getElementsByTagName("head")[0].removeChild(d.getElementById("so_color_list_css"));
	d.getElementsByTagName("body")[0].removeChild(d.getElementById("so_mContainer"));
	d.onkeydown = null;
	d.onmousemove = null;
}

function so_createColorTable() {
	colors = colors.sort();
	so_tableContainer = mObj.appendChild(d.createElement("div"));
	so_tableContainer.id = "so_tableContainer";
	tbl = so_tableContainer.appendChild(d.createElement("table"));

	for(i=0;i<colors.length;i++) {
		if(colors[i]!="NAN") {
			tr = tbl.appendChild(d.createElement("tr"));
			tr.height = "20";
			tr.valign = "middle"

			td1 = tr.appendChild(d.createElement("td"));
			td1.width = "20";
			div = td1.appendChild(d.createElement("div"));
			div.style.backgroundColor = "#" + colors[i];
			div.title="Click this color to view it as the base color in the Color Palette Creator.";
			div.style.cursor = "pointer";
			div.className = "swatch";
			div.style.marginTop = "-13px";
			div.xColor = colors[i];
			div.onclick = function() {
				window.open("http://slayeroffice.com/tools/color_palette/?hex=" + this.xColor);
			}
			td2 = tr.appendChild(d.createElement("td"));
			td2.valign = "middle"
			td2.width = "65";
			td2.appendChild(d.createTextNode("#"+colors[i]));

			td3 = tr.appendChild(d.createElement("td"));
			td3.valign="middle";
			td3.appendChild(d.createTextNode(so_longHexToDec(colors[i])));
		}
	}
}

function so_createContainer() {
	mObj=d.body.appendChild(d.createElement("div"));
	mObj.id = "so_mContainer";	
}

function so_checkColors(ruleObj) {
	colorChecks = new Array("backgroundColor","color","border","borderColor","borderTop","borderRight","borderBottom","borderLeft","borderTopColor","borderRightColor","borderBottomColor","borderLeftColor");
	for(j=0;j<colorChecks.length;j++) {
		clr = eval('ruleObj.' + colorChecks[j]);
		clr=clr.match(/rgb(\([^\)]*\))/gi);
		if(clr)so_addToColorArray(clr[0],"Stylesheet as " + colorChecks[j]);
	}
}

function so_getStyleSheetColors() {
	s=d.styleSheets;
	if(!s.length)return;
	for(i=0;i<s.length;i++) {
		try {
			for(e=0;e<s[i].cssRules.length;e++) {
				rules = s[i].cssRules[e].cssText;
				if(rules.indexOf("@import")>-1) {
					ss=s[i].cssRules[e].styleSheet;
					for(u=0;u<ss.cssRules.length;u++) {
						ruleObj = ss.cssRules[u].style;
						so_checkColors(ruleObj);
					}
				} else {
					ruleObj = s[i].cssRules[e].style;
					so_checkColors(ruleObj);
				}
			}
		} catch(err) { 
			if(err.message.indexOf("Access")>-1) {
				alert("An ACCESS DENIED error has occured while parsing style sheet #" + i + ".\n\nCheck to make sure the domain you are on is the same as the style sheet.\n\neg: slayeroffice.com is NOT the same as www.slayeroffice.com");
			}
		}
	}
	return colors;
}

function so_addToColorArray(val,fnd) {
	if(!val)return;
	val=val.toString();
	val=val.replace(/rgb\(/,"");
	val=val.replace(/\)/,"");
	val = so_rgbToHex(val.split(","));
	if(!so_existsInArray(val,colors)) {
		colors[colors.length]=val; 
		foundWhere[foundWhere.length]=fnd;
	}
}

function so_longHexToDec(longHex) {
	r=toDec(longHex.substring(0,2));
	g=toDec(longHex.substring(2,4));
	b=toDec(longHex.substring(4,6));
	return new Array(r,g,b);
}

function toDec(hex) {
	return parseInt(hex,16);
}

function so_getInlineColors() {
	allObj = document.getElementsByTagName("*");
	for(i=0;i<allObj.length;i++) {
		obj=allObj[i];
		if(obj.tagName!="!") {
		for(b=0;b<obj.attributes.length;b++) {
			if(obj.attributes[b].specified && obj.attributes[b].name == "style") {
				rules = obj.attributes[b].value;
				rules = rules.split(";")
				for(z=0;z<rules.length;z++) {
					if(rules[z].indexOf("rgb")>-1) {
						clr = rules[z].match(/rgb(\([^\)]*\))/gi);
						if(clr) {
							r=rules[z].split(":");
							so_addToColorArray(clr[0],"Inline Style as " + r[0]);
						}
					}
				}
			}
		}
		}
	}
}


function so_getAttributeColors() {
	allObj = d.getElementsByTagName("*");
	for(i=0;i<allObj.length;i++) {
		obj=allObj[i];
		if(obj.tagName!="!"){
		for(b=0;b<obj.attributes.length;b++) {
			if(obj.attributes[b].specified && obj.attributes[b].name=="color" || obj.attributes[b].name=="bgcolor") {
				aColor = obj.attributes[b].value;
				if(aColor.indexOf("#")>-1) {
					aColor = aColor.toUpperCase();
					aColor = aColor.replace(/#/g,"");
					if(!so_existsInArray(aColor,colors)) {
						colors[colors.length] = aColor;
						foundWhere[foundWhere.length] = "Attribute: " + obj.attributes[b].name;
					}
				}
			}
		}
		}
	}
}

function so_rgbToHex(rgbArray) {
	hexReturn="";
	for(w=0;w<rgbArray.length;w++) {
		rgbArray[w]=parseInt(rgbArray[w]);
		hex=rgbArray[w].toString(16);
		if(hex.length==1)hex="0"+hex;
		if(hex==100)hex="FF";
		hexReturn+=hex.toUpperCase();
	}
	return hexReturn;
}


function so_existsInArray(nValue,nArray) {
	for(p=0;p<nArray.length;p++) {
		if(nArray[p] == nValue)return true;
	}
	return false;
}

function so_captureOffset(e) {
	mDown = true;
	x = parseInt(mObj.offsetLeft);
	y = parseInt(mObj.offsetTop);

	if(d.all) {
		offsetX=window.event.clientX - x;
		offsetY=window.event.clientY - y;
	} else {
		offsetX = e.pageX - x;
		offsetY = e.pageY - y;
	}
}

function so_handleMouseMoveEvent(e) {
	mx = d.all?window.event.clientX-offsetX:e.pageX-offsetX;
	my = d.all?window.event.clientY-offsetY:e.pageY-offsetY;
	if(mDown) {
		mObj.style.top = my+"px";
		mObj.style.left = mx+"px";
	}
}

so_init();