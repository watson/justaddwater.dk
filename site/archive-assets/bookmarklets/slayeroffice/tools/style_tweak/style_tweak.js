/* Archive adaptation: local dependencies; original author notices follow. */
var so_archive_base = new URL(document.currentScript.src).href.split("/archive-assets/")[0] + "/archive-assets/bookmarklets/slayeroffice";
var originalRules = "";
var oWidth,oHeight;
var isImport = new Array();

var d = document;

window.scrollTo(0,0);

var mDown = false;
var mx,my,offsetX,offsetY;

function so_init() {
	if(document.all) {
		alert("Sorry! This only works in Mozilla and Firefox at the moment. A version for your browser will come around eventually.");
		return;
	}

	d.onmousemove = so_handleMouseMoveEvent;
	d.onkeyup = so_handleKeyUpEvent;

	mObj = d.body.appendChild(d.createElement("div"));
	mObj.id="nContainer";

	hObj = mObj.appendChild(d.createElement("h1"));
	hObj.id = "dragHeader";
	hObj.innerHTML = "slayeroffice | style tweak";
	hObj.title = "Click and drag here.";

	mObj.innerHTML += createSelectorDropDown(getSelectors());

	// for some reason applying the events to the object reference var 
	// is nullified after appending the innerHTML returned by createSelectorDropDown
	// so we do it here with direct object references.
	d.getElementById("dragHeader").onmousedown = so_captureOffset;
	d.getElementById("dragHeader").onmouseup = function() { mDown = false; }

	styleObject = mObj.appendChild(d.createElement("link"));
	styleObject.rel="Stylesheet";
	styleObject.type="text/css";
	styleObject.href=("http://slayeroffice.com/tools/style_tweak/style_tweak.css".replaceAll("http://slayeroffice.com", so_archive_base));
	styleObject.id="sst_css";

	tObj = mObj.appendChild(d.createElement("textarea"));
	tObj.id="mRules";

	bObj = mObj.appendChild(d.createElement("input"));
	bObj.className="btn";
	bObj.type = "button";
	bObj.id="nBtn";
	bObj.title="Apply these rules to the selector.";
	bObj.value="Apply";
	bObj.onclick= function() { addNewSelector()}

	bObj = mObj.appendChild(d.createElement("input"));
	bObj.type = "button";
	bObj.className="btn";
	bObj.id="rBtn";
	bObj.title="Reset the css rules to the original ones.";
	bObj.value="Reset";

	bObj = mObj.appendChild(d.createElement("input"));
	bObj.type = "button";
	bObj.className="btn";
	bObj.id="sBtn";
	bObj.value="Show";
	bObj.title="Show all of the CSS.";
	bObj.onclick=function(){ doOutput(); }


	bObj = mObj.appendChild(d.createElement("input"));
	bObj.type = "button";
	bObj.className="btn";
	bObj.id="dBtn";
	bObj.value="Delete";
	bObj.title="Delete Selector.";

	bObj = mObj.appendChild(d.createElement("input"));
	bObj.type = "button";
	bObj.className="btn";
	bObj.id="cBtn";
	bObj.value="Close";
	bObj.title="Close the application.";
	bObj.onclick=function(){ cleanUp(); }

	sObj = mObj.appendChild(d.createElement("div"));
	sObj.className="credits";
	sObj.innerHTML="<strong>style sheet tweaker</strong><br />version 1.2<br />last revision:08.23.2004<br />steve@slayeroffice.com<br />http://slayeroffice.com<br />";
	
}

function cleanUp() {
	try {
		d.body.removeChild(d.getElementById("nContainer"));
		d.body.removeChild(d.getElementById("sst_css"));
		d.body.removeChild(d.getElementById("sst"));
		d.onmousemove = null;
		d.onkeyup = null;
	} catch(err) { }
}

function getSelectors() {
	try {
		s=d.styleSheets;
		if(!s.length)return -1;
		mSelectors=new Array();;
		for(i=0;i<s.length;i++) {
			if(s[i].media.mediaText!="print") {
				for(e=0;e<s[i].cssRules.length;e++) {
					if(s[i].cssRules[e].cssText.indexOf("@import")>-1){
						ss=s[i].cssRules[e].styleSheet
						isImport[i]=1;
						for(r=0;r<ss.cssRules.length;r++)mSelectors[mSelectors.length]= _parseSelector(ss,r,i)
					} else {
						isImport[i]=0;
						mSelectors[mSelectors.length] = _parseSelector(s[i],e,i);
					}
				}
			}
		}
		return mSelectors;
	} catch(err) {
		alert("An error has occured while parsing the style sheet:\n\n" + err.message);
		cleanUp();
		return -1;
	}
}

function getCSSRules(selectorIndexArray) {
	if(selectorIndexArray=="null") {
		//d.getElementById("mRules").value="";
		d.getElementById("nBtn").onclick = function() { addNewSelector()}
		return;
	}

	if(selectorIndexArray=="addNew") {
		d.getElementById("nBtn").onclick = function() { addNewSelector()}
		d.getElementById("mRules").value="";
	} else {
		selectorIndexArray = selectorIndexArray.split(",");
		d.getElementById("nBtn").onclick = function() { changeRules(d.getElementById('mRules').value,selectorIndexArray[0],selectorIndexArray[1])}
		d.getElementById("rBtn").onclick = function() { restoreOriginalRule(selectorIndexArray[0],selectorIndexArray[1])}
		d.getElementById("dBtn").onclick=function() { removeRule(selectorIndexArray[0],selectorIndexArray[1]) }
		if(!isImport[selectorIndexArray[0]]) {
			originalRules = d.styleSheets[selectorIndexArray[0]].cssRules[selectorIndexArray[1]].style.cssText;
		} else {
			originalRules = d.styleSheets[selectorIndexArray[0]].cssRules[0].styleSheet.cssRules[selectorIndexArray[1]].style.cssText;
		}
		writeCSSRules(originalRules.split(";"));
	}
}


function writeCSSRules(rulesArray) {
	d.getElementById("mRules").value="";
	for(p=0;p<rulesArray.length-1;p++)d.getElementById("mRules").value+=rulesArray[p]+";\n";
}

function createSelectorDropDown(selectorArray) {
	if(selectorArray==-1) {
		alert("No Style Sheets!");
		cleanUp();
		return;
	}
	mHTML="<select id=\"selectors\" name=\"selectors\" onchange=\"getCSSRules(this.value);\"><option value=\"null\">-- Choose a Selector --</option>";
	mHTML+="<option value=\"addNew\">-- Add New Selector(s) --</option>";
	for(m=0;m<selectorArray.length;m++) {
		mHTML+="<option value=\"" + selectorArray[m][2] + "," + selectorArray[m][1] + "\">" + selectorArray[m][0] + "</option>";
	}
	mHTML+="</select>";
	return mHTML;
}

function returnLastStyleSheetIndex() {
	for(i=d.styleSheets.length-2;i>-1;i--) {
		nMedia=d.styleSheets[i].media.mediaText.toLowerCase();
		if(nMedia=="screen" || nMedia=="all")return i;
	}
}

function addNewSelector() {
	newRules = d.getElementById('mRules').value.split("}");
	//index=returnLastStyleSheetIndex();
	for(i=0;i<newRules.length;i++) {
		try {
			//d.styleSheets[index].insertRule(newRules[i]+"}",d.styleSheets[index].cssRules.length);
			d.styleSheets[0].insertRule(newRules[i]+"}",0);
		} catch(err) { }
	}
	d.body.removeChild(d.getElementById("nContainer"));
	so_init();
}

function doOutput() {
	mHTML = "";
	for(i=2;i<d.getElementById("selectors").options.length;i++) {
		mHTML+= d.getElementById("selectors").options[i].innerHTML + " {\n";
		selectorIndexArray = d.getElementById("selectors").options[i].value.split(",");
		if(!isImport[selectorIndexArray[0]]) {
			originalRules = d.styleSheets[selectorIndexArray[0]].cssRules[selectorIndexArray[1]].style.cssText;
		} else {
			originalRules = d.styleSheets[selectorIndexArray[0]].cssRules[0].styleSheet.cssRules[selectorIndexArray[1]].style.cssText;
		}
		originalRules=originalRules.split(";");
		for(p=0;p<originalRules.length-1;p++)mHTML+="&#9;"+originalRules[p]+";\n";
		mHTML+="}\n\n";
	}

	zWin =window.open("","zWin","");
	zWin.document.write("<pre style=\"font:9px verdana;\">" + mHTML + "</pre>");
}

function removeRule(styleSheetIndex,ruleIndex) {
	if(!isImport[styleSheetIndex]) {
		d.styleSheets[styleSheetIndex].deleteRule(ruleIndex);
	} else {
		d.styleSheets[styleSheetIndex].cssRules[0].styleSheet.deleteRule(ruleIndex);
	}
	d.body.removeChild(d.getElementById("nContainer"));
	so_init();
}

function restoreOriginalRule(styleSheetIndex,ruleIndex) {
	if(!isImport[styleSheetIndex]) {
		d.styleSheets[styleSheetIndex].cssRules[ruleIndex].style.cssText = originalRules;
	} else {
		d.styleSheets[styleSheetIndex].cssRules[0].styleSheet.cssRules[ruleIndex].style.cssText = originalRules;
	}
	writeCSSRules(originalRules.split(";"));
}

function changeRules(ruleText,styleSheetIndex,ruleIndex) {
	if(!isImport[styleSheetIndex]) {
		d.styleSheets[styleSheetIndex].cssRules[ruleIndex].style.cssText = ruleText;
	} else {
		d.styleSheets[styleSheetIndex].cssRules[0].styleSheet.cssRules[ruleIndex].style.cssText = ruleText;
	}
}

function _parseSelector(styleSheetObject,styleSheetRuleIndex,styleSheetIndex) {
	return new Array(styleSheetObject.cssRules[styleSheetRuleIndex].selectorText,styleSheetRuleIndex,styleSheetIndex);
}

function so_captureOffset(e) {
	mDown = true;
	x = parseInt(this.parentNode.offsetLeft);
	y = parseInt(this.parentNode.offsetTop);

	if(document.all) {
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

function so_handleKeyUpEvent(e) {
	keyCode = d.all?window.event.keyCode:e.keyCode;
	if(keyCode == 27) cleanUp();
}

so_init();