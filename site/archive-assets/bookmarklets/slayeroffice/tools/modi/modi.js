/* Archive adaptation: local dependencies; original author notices follow. */
var so_archive_base = new URL(document.currentScript.src).href.split("/archive-assets/")[0] + "/archive-assets/bookmarklets/slayeroffice";
/*************************************

	Mouseover DOM Inspector 
	v1.2
	last revision: 05.17.2004
	steve@slayeroffice.com

*************************************/

d=document;
da=d.getElementsByTagName("*");
dg=d.getElementById;
d.onmousemove=cm;
dci=1;
d.onkeydown=ck;
var ob;
var useBorder=1;

for(i=0;i<da.length;i++){
	if(da[i].tagName!="HTML"&&da[i].tagName!="BODY"&&da[i].tagName!="!"){
		da[i].onmouseover=si;
		da[i].onmouseout=hi;
	}
}
css = d.body.appendChild(d.createElement("link"));
css.id = "modiStyleSheet";
css.rel="stylesheet";
css.href=("http://slayeroffice.com/tools/modi/modi.css".replaceAll("http://slayeroffice.com", so_archive_base));
css.type="text/css";

m=d.body.appendChild(d.createElement("div"));
m.id="mData";
dm=d.getElementById("mData");
dms=dm.style;
dms.border="2px solid #006699"
dms.font="10px verdana,sans seriff"
dms.position="absolute";
dms.color="#000000";
dms.padding="4px";
dms.backgroundColor="#E8F7FD";
dms.textAlign="left";
dms.zIndex = "100";

var activeObj=null; var editObj=null; var txtFocus=0;

var htmlView = d.body.appendChild(d.createElement("div"));
htmlView.style.display="none";
htmlView.id="hView";


function cm(e){
	x=d.all?window.event.clientX+returnScrollDimensions(0):e.clientX;
	y=d.all?window.event.clientY+returnScrollDimensions(1):e.pageY;
	dm.style.top=(y+15)+"px";
	dm.style.left=(x+15)+"px";
}

function ck(e){
	k=document.all?window.event.keyCode:e.keyCode;
	if(k==27) {
		if(htmlView.style.display == "none") {
			activeObj.style.backgroundColor=ob;
			d.body.removeChild(document.getElementById("mData"));
			d.body.removeChild(document.getElementById("modiStyleSheet"));
			d.body.removeChild(htmlView);
			document.onmousemove="";
			document.onkeypress="";
			for(z=0;z<da.length;z++){ 
				da[z].onmouseover=null;
				da[z].onmouseout=null;
			}
		} else {
			txtFocus=0;
			htmlView.style.display="none";
		}
	}  else if(k==66) {
		if(txtFocus)return;
		if(useBorder)if(activeObj)activeObj.style.backgroundColor = ob;
		useBorder=useBorder?0:1;
	} else if (k == 86 || k == 83) {
		if(txtFocus)return;
		editObj=activeObj;
		showInnerHTML();
	}
}

function showInnerHTML() {
	innerHTML = editObj.innerHTML;

	htmlView.style.top = y+"px";
	htmlView.style.left = x+"px";
	htmlView.innerHTML = "<textarea onfocus=\"txtFocus=1;\" onblur=\"txtFocus=0;\" id=\"zHTML\" style=\"font:9px verdana;\" rows=\"20\" cols=\"40\">" + innerHTML + "</textarea>";
	htmlView.innerHTML += "<br /><span>innerHTML for " + activeObj.tagName + "| <a href=\"javascript:applyChange();\">Apply Changes</a></span>";
	htmlView.style.display="block";
}

function applyChange() {
	editObj.innerHTML = d.getElementById("zHTML").value;
}

function returnScrollDimensions(which) {
	if(which) {
		if(document.body.scrollTop != 0)return document.body.scrollTop;
		if(document.documentElement.scrollTop != 0)return document.documentElement.scrollTop;
	} else {
		if(document.body.scrollLeft != 0)return document.body.scrollTop;
		if(document.documentElement.scrollLeft != 0)return document.documentElement.scrollLeft;
	}
	return 0;
}

function hi(){
	try {
		if(useBorder)this.style.backgroundColor=ob;
	} catch(err) { }
	dci=1;
}

function si(){
	if(!dci)return;
	ta=this.attributes;
	activeObj=this;
	ob=this.style.backgroundColor;
	dci=0;
	dd="Element Type: <b>&lt;" + this.tagName + "&gt;</b><br />";
	for(i=0;i<ta.length;i++)if(ta[i].specified && (ta[i].value!="" && ta[i].value!="null"))dd+="<b>"+ta[i].name+"</b>=\"" + ta[i].value + "\"<br />";
	dm.innerHTML=dd;
	if(useBorder)this.style.backgroundColor="#C0C0C0";
}
