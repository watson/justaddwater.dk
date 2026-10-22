/******************************************************
	Page Info
	v1.3
	last revision: 07.30.2004
	steve@slayeroffice.com
	http://slayeroffice.com
	
	Please leave this notice in tact.

	Should you make any modifications
	or improvements to this code, please
	let me know so that I can update the 
	version hosted as slayeroffice.

******************************************************/


var d=document;
d.onkeydown=captureKeyEvent;
d.onmousemove = so_handleMouseMoveEvent;

var bps = new Array(14400,28800,33600,56000,128000,394000,640000,10000000);
var loss = new Array(1,1.15,1.2,1.25);

var mDown = false;
var mx,my,offsetX,offsetY;
var mObj;

function so_init() {
	window.scrollTo(0,0);

	markup = d.getElementsByTagName("html")[0].innerHTML;
	bodymarkup = d.getElementsByTagName("body")[0].innerHTML;

	nContent = bodymarkup.replace(/<(.|\n)+?>/g,"");

	markupSize=bodymarkup.length;

	contentSize = nContent.length;
	titleContent=countTitleAndAlt();
	contentSize -= titleContent;

	contentPercentage = Math.round((contentSize/bodymarkup.length)*100);

	linkLength = d.getElementsByTagName("a").length;
	styleLength = d.getElementsByTagName("style").length;
	attrStyleLength = returnStyleAttributesCount();
	scriptLength = d.getElementsByTagName("script").length;
	imageLength = d.getElementsByTagName("img").length;
	metaLength = d.getElementsByTagName("meta").length;
	comments = returnComments();
	bodySize = bodymarkup.length;
	tableLength = d.getElementsByTagName("table").length;
	commentLength = d.getElementsByTagName("!").length;
	if(d.doctype)commentLength--;

	css = d.getElementsByTagName("head")[0].appendChild(d.createElement("link"));
	css.type="text/css";
	css.rel="stylesheet";
	css.href="http://slayeroffice.com/tools/pagenfo/pagenfo.css";
	css.id="pagenfo_css";

	mObj=d.body.appendChild(d.createElement("div"));
	mObj.id="appContainer";
	
	hObj=mObj.appendChild(d.createElement("h1"));
	hObj.innerHTML="<b>page</b>info";
	hObj.id = "dragHeader";

	h2Obj = mObj.appendChild(d.createElement("h2"));
	h2Obj.innerHTML = "Code Weight Specifics";

	ulObj=mObj.appendChild(d.createElement("ul"));
	ulObj.innerHTML= "<li>Total Code Weight: <b>" + markup.length + "</b> bytes.</li>";
	ulObj.innerHTML+="<li>Body Code Weight: <b>" + bodymarkup.length + "</b> bytes.</li>";
	ulObj.innerHTML+="<li>Content Weight: <b>" + contentSize + "</b> bytes.</li>";
	ulObj.innerHTML+="<li>Percent Markup: <b>" +(100-contentPercentage)+"%</b></li>";
	ulObj.innerHTML+="<li>Percent Content: <b>" + contentPercentage + "%</b></li>";

	h2Obj = mObj.appendChild(d.createElement("h2"));
	h2Obj.innerHTML = "Approximated Download Times";

	mObj.innerHTML+=renderTimeTable(calcTimes(markupSize*8));

	h2Obj = mObj.appendChild(d.createElement("h2"));
	h2Obj.innerHTML = "Markup Specifics";

	ulObj=mObj.appendChild(d.createElement("ul"));
	ulObj.innerHTML+="<li>You have <b>" + linkLength + "</b> &lt;a&gt; elements.</li>";

	ulObj.innerHTML+="<li>You have <b>" + styleLength + "</b> inline &lt;style&gt; elements.</li>";
	if(attrStyleLength!=-1) {
		ulObj.innerHTML+="<li>You have <b>" + attrStyleLength + "</b> style attributes.</li>";
	} else {
		ulObj.innerHTML+="<li><span style=\"color:red;\">Error occured parsing style attributes.</span><li>";
	}
	ulObj.innerHTML+="<li>You have <b>" + scriptLength + "</b> &lt;script&gt; elements.</li>";
	ulObj.innerHTML+="<li>You have <b>" + metaLength + "</b> &lt;meta&gt; elements.</li>";
	ulObj.innerHTML+="<li>You have <b>" + imageLength + "</b> &lt;img&gt; elements.</li>";
	ulObj.innerHTML+="<li>You have <b>" + tableLength + "</b> &lt;table&gt; elements.</li>";
	ulObj.innerHTML+="<li>You have <b>" + comments.length + "</b> comments totalling <b>"+returnCommentByteSize(comments)+" bytes</b>.</li>";
	ulObj.innerHTML+="<li>You have <b>" + titleContent + " bytes</b> of title and alt content.</li>";

	mObj.innerHTML+="<a id=\"pf\" href=\"javascript:printFriendly();\" title=\"Open a new window with a printer friendly view of the data.\">Printable View</a>";
	creditObj = mObj.appendChild(d.createElement("div"));
	creditObj.id="credits";
	creditObj.innerHTML = "[esc] to <a href=\"javascript:cleanUp();\">close</a><br />page info favelet<br />version 1.3<br />last revision: 08.24.2004<br /><a href=\"http://slayeroffice.com\" target=\"_blank\">slayeroffice.com</a>";

	d.getElementById("dragHeader").onmousedown = so_captureOffset;
	d.getElementById("dragHeader").onmouseup = function() { mDown=false; }
}

function countTitleAndAlt() {
	altByteSize = 0;
	allObj = document.getElementsByTagName("*");
	for(i=0;i<allObj.length;i++) {
		nTitle = allObj[i].title;
		nAlt = allObj[i].alt;
		//altByteSize+= nTitle.length+nAlt.length;
		if(nTitle) altByteSize+=nTitle.length;
		if(nAlt) altByteSize+=nAlt.length;
	}
	return altByteSize;
}

function printFriendly() {
	nWin=window.open("","nWin");
	nWin.document.write(d.getElementById("appContainer").innerHTML + "<p>Data for " + location.href);
	nWin.document.body.removeChild(nWin.document.getElementById("credits"));
	nWin.document.body.removeChild(nWin.document.getElementById("pf"));
	nWin.document.getElementsByTagName("table")[0].style.width="30%";
	
}

function renderTimeTable(timesArray) {
	mHTML = "<table cellspacing=\"0\"><tr class=\"headerRow\"><td>bps</td><td>0%</td><td>15%</td><td>20%</td><td>25%</td></tr>";
	for(i=0;i<bps.length;i++) {
		trClass = i%2?"on":"off";
		mHTML+="<tr class="+trClass+"><td>"+bps[i]+"</td>";
		for(j=0;j<timesArray.length;j++) {
			if(timesArray[i][j]!=null)mHTML+="<td>"+timesArray[i][j]+"</td>"
		}
		mHTML+="</tr>";
	}
	mHTML+="</table>"
	return mHTML;
}

function returnStyleAttributesCount() {
	all=d.getElementsByTagName("*");
	styleCount=0;
	for(i=0;i<all.length;i++) {
		obj = all[i];
		if(obj.tagName!="!") {
			// MSIE sometimes flips out on this method. no idea whats causing it other than its an awful, awful browser.
			try {
				for(z=0;z<obj.attributes.length;z++) {
					if(obj.attributes[z].name == "style" && obj.attributes[z].specified)styleCount++;
				}
			}catch(err) { styleCount=-1; }
		}
	}
	return styleCount;
}

function calcTimes(byteSize) {
	times = new Array();
	for(i=0;i<bps.length;i++) {
		times[i] = new Array();
		for(j=0;j<loss.length;j++) times[i][j] = formatTime(Math.round((byteSize/bps[i]) * loss[j]));
	}

	return times;
}

function formatTime(nTime) {
	if(nTime<=59) {
		if(nTime<10) {
			return "00:0"+nTime;
		} else {
			return "00:"+nTime;
		}
	} else {
		nTime/=60;
		nTime=nTime.toFixed(2);
		returnHTML="";
		nTime=nTime.toString();
		nTime=nTime.split(".");
		m=parseInt(nTime[0]);
		s=parseInt(nTime[1]);
		if(m<10) {
			returnHTML+="0"+m+":";
		} else {
			returnHTML+=m+":";
		}

		if(s<10) {
			returnHTML+="0"+s;
		} else {
			returnHTML+=s;
		}

		return returnHTML;
	}
}

function returnComments() {
	commentArray=new Array();
	if(!d.all) {
		all=d.getElementsByTagName("*");
		for(w=0;w<all.length;w++) {
			obj=all[w];
			for(k=0;k<obj.childNodes.length;k++)	if(obj.childNodes[k].nodeType==8)commentArray[commentArray.length]=obj.childNodes[k].nodeValue;
		}
	} else {
		try {
			for(w=0;w<d.getElementsByTagName("!").length;w++) {
				commentArray[commentArray.length]=d.getElementsByTagName("!")[w].innerHTML;
			}
		} catch(err) { }
	}
	return commentArray;
}

function returnCommentByteSize(commentArray) {
	bSize=0;
	for(i=0;i<commentArray.length;i++)bSize+=commentArray[i].length;
	return bSize;
}

function captureKeyEvent(e) {
	keyCode = d.all?window.event.keyCode:e.keyCode;
	if(keyCode == 27) cleanUp();
}

function cleanUp() {
	d.getElementsByTagName("head")[0].removeChild(d.getElementById("pagenfo_css"));
	d.getElementsByTagName("body")[0].removeChild(d.getElementById("appContainer"));
	d.onkeydown = null;
	d.onmousemove = null;
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