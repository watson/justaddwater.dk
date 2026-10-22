/* Archive adaptation: local dependencies; original author notices follow. */
var so_archive_base = new URL(document.currentScript.src).href.split("/archive-assets/")[0] + "/archive-assets/bookmarklets/slayeroffice";
/***************************************
	HTTP Response Header Viewer Favelet
	version 2.0 
	last revision: 03.01.2005
	steve@slayeroffice.com

	Original version 1.x was done with PHP

	Should you improve upon or modify this code
	please let me know so that I can update the
	version hosted at slayeroffice

	Please leave this notice in tact!

	Thanks to Jim Ley for his article on how
	this could be done with XMLHttpRequest
	http://jibbering.com/2002/4/httprequest.2004.html

***************************************/

var mDown = false;
var mx,my,offsetX,offsetY,mObj;	

function so_getHTTPHeaders() {
	if(!document.getElementById)return;

	if(window.XMLHttpRequest) {
		conn = new XMLHttpRequest();
	} else if(window.ActiveXObject) {
		conn = new ActiveXObject("Msxml2.XMLHTTP");
	} else {
		return alert("Unsupported browser.");	
	}
	
	conn.onreadystatechange=function() {
		if (conn.readyState==4) {
			so_displayHTTPHeaders(conn.getAllResponseHeaders());
		}
	}
	conn.open("HEAD", "/",true);
	conn.send(null)
}


function so_displayHTTPHeaders(responseString) {
	d=document;
	d.onkeypress = so_handleKeyEvent;
	d.onmousemove = so_handleMouseMoveEvent;

	window.scrollTo(0,0);

	cssObj = d.getElementsByTagName("head")[0].appendChild(d.createElement("link"));
	cssObj.setAttribute("type","text/css");
	cssObj.setAttribute("rel","stylesheet");
	cssObj.setAttribute("id","so_css");
	cssObj.setAttribute("href",("http://slayeroffice.com/tools/headerViewer/headerViewer.css".replaceAll("http://slayeroffice.com", so_archive_base)));

	mObj = d.getElementsByTagName("body")[0].appendChild(d.createElement("div"));
	mObj.setAttribute("id","so_mContainer");

	h1 = mObj.appendChild(d.createElement("h1"));
	h1.onmousedown = so_captureOffset;
	h1.onmouseup = function() { 
		mDown = false; 
		so_setOpacity(mObj,100);
	}

	h1.appendChild(d.createTextNode("Response Headers for " + location.hostname));

	responseString = responseString.split("\n");
	ul = mObj.appendChild(d.createElement("ul"));

	for(i=0;i<responseString.length;i++) {
		if(responseString[i]) {
			li = ul.appendChild(d.createElement("li"));
			li.appendChild(d.createTextNode(responseString[i]));		
		}
	}

	so_showCredits();
}

function so_showCredits() {
	d=document;
	mObj = d.getElementById("so_mContainer");
	credits = mObj.appendChild(d.createElement("div"));
	credits.setAttribute("id","so_credits");
	
	credits.appendChild(d.createTextNode("HTTP Response Header Viewer"));
	credits.appendChild(d.createElement("br"));
	credits.appendChild(d.createTextNode("Version 2.0"));
	credits.appendChild(d.createElement("br"));
	credits.appendChild(d.createTextNode("last rev: 03.01.2005"));
	credits.appendChild(d.createElement("br"));

	a = credits.appendChild(d.createElement("a"));
	a.setAttribute("href","http://slayeroffice.com");
	a.setAttribute("target","_blank");
	a.appendChild(d.createTextNode("slayeroffice.com"));

	credits.appendChild(d.createElement("br"));
	credits.appendChild(d.createTextNode("[esc] to "));

	a = credits.appendChild(d.createElement("a"));
	a.setAttribute("href","javascript:void(so_cleanUp())");
	a.appendChild(d.createTextNode("close"));
}

function so_cleanUp() {
	document.getElementsByTagName("body")[0].removeChild(document.getElementById("so_mContainer"));
	document.getElementsByTagName("head")[0].removeChild(document.getElementById("so_css"));
	window.onkeypress = null;
}

function so_handleKeyEvent(so_e) {
	d=document;
	so_keyCode = d.all?window.event.keyCode:so_e.keyCode;
	if(so_keyCode==27)so_cleanUp();
}

function so_handleMouseMoveEvent(e) {
	d = document;
	mx = d.all?window.event.clientX-offsetX:e.pageX-offsetX;
	my = d.all?window.event.clientY-offsetY:e.pageY-offsetY;
	if(mDown) {
		mObj.style.top = my+"px";
		mObj.style.left = mx+"px";
	}
}

function so_setOpacity(obj,op) {
	if(!document.all) {
		op/=100;
		obj.style.opacity = op;
		obj.style.MozOpacity = op;
	} else {
		obj.style.filter = "alpha(opacity=" + op + ")";
	}
}

function so_captureOffset(e) {
	d=document;
	mDown = true;
	so_setOpacity(mObj,70);
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

so_getHTTPHeaders();