/* Archive adaptation: local dependencies; original author notices follow. */
var so_archive_base = new URL(document.currentScript.src).href.split("/archive-assets/")[0] + "/archive-assets/bookmarklets/slayeroffice";
/*************************************
	Document Tree Chart Favelet
	version 1.2
	last revision: 05.14.2004
	steve@slayeroffice.com

	Please notify me of any improvements
	you make to this code so that I 
	can update the version hosted at slayeroffice.

	Please leave this notice in tact!

	(c) 2004 S.G. Chipman

*************************************/
	
var d=document;
d.onkeydown=handleKeyEvent;

var isDisplayed=new Array();
var mObj;
var p=new Array();
var actualNode = new Array();
var nodeIndex=0;
var isShown=0;
var obc=new Array();
var doHighlight=0;

opera = window.opera;

css=d.body.appendChild(d.createElement("link"));
css.type="text/css";
css.rel="Stylesheet";
css.href=opera?("http://slayeroffice.com/tools/dom_chart/dom_chart_tree.css".replaceAll("http://slayeroffice.com", so_archive_base)):("http://slayeroffice.com/tools/dom_chart/dom_chart.css".replaceAll("http://slayeroffice.com", so_archive_base));	
css.xid=1;
isDisplayed[css]=1;
window.scrollTo(0,0);



function so_init() {
	if(d.all && !opera) return alert("Sorry, this doesn't work in your browser yet. A version for yours will be along eventually.");
	all = d.getElementsByTagName("*");
	mObj=d.body.appendChild(d.createElement("div"));
	mObj.id="chartContainer";
	mObj.style.position="absolute";
	mObj.style.top="0px";
	mObj.style.left="0px";
	mObj.xid=1;

	isDisplayed[mObj]=1;
	createElementTree(all);
}

function createElementTree(objs) {
	i=0;
	mHTML="";
	while(objs[i]) {
		if(objs[i].tagName!="!") {
			if(!objs[i].xid) {
				if(!childNodesAreDisplayed(objs[i])) {
					if(!document.all || opera) {
						if(!objs[i].parentNode.tagName) {
							// create the first element that all elements will descend from. presumably the HTML element label
							p[objs[i]]=mObj.appendChild(d.createElement("span"));
							p[objs[i]].className="chartLabel";
							p[objs[i]].innerHTML=objs[i].tagName;
							p[objs[i]].style.backgroundColor = applyBGColor(objs[i].tagName);
							p[objs[i]].xid=1;
							isDisplayed[objs[i]]=1;
						} else {
							p[objs[i]]=p[objs[i].parentNode].appendChild(d.createElement("span"));
							p[objs[i]].className="chartLabel";
							//p[objs[i]].innerHTML=objs[i].tagName;
							p[objs[i]].style.top=p[objs[i]].parentNode.offsetTop+p[objs[i]].parentNode.offsetHeight+"px";
							p[objs[i]].style.backgroundColor = applyBGColor(objs[i].tagName);
							actualNode[nodeIndex]=objs[i];
							p[objs[i]].zid=nodeIndex;
							p[objs[i]].onmouseover=function(){showNode(this.zid);}
							p[objs[i]].onmouseout=function(){isShown=0;hideNode(this.zid);}
							p[objs[i]].xid=1;
							p[objs[i]].title="Parent Node: " + objs[i].parentNode.tagName;
							isDisplayed[objs[i]]=1;
		
								c=p[objs[i]].appendChild(d.createElement("a"));
								c.xid=1;
								c.xref=c.parentNode;
								c.innerHTML = objs[i].tagName;
								c.style.cursor="pointer";
								c.onclick=hideChildren;
						}
					} else {
						// MSIE code goes here...
					}
				}
			nodeIndex++;
			}
		}
		i++;
	}
}

function numChildren(obj) {
	n=0;
	for(c=0;c<obj.childNodes.length;c++) {
		if(obj.childNodes[c].nodeType==1) {
			n++;
		}
	}
	return n;
}

function handleKeyEvent(e) {
	keyCode=d.all?window.event.keyCode:e.keyCode;
	if(keyCode == 27) {
		d.body.removeChild(mObj);
		d.body.removeChild(css);
		d.onkeydown=null;
	} else if (keyCode == 84) {
		if(css.href==("http://slayeroffice.com/tools/dom_chart/dom_chart.css".replaceAll("http://slayeroffice.com", so_archive_base))) {
			css.href = ("http://slayeroffice.com/tools/dom_chart/dom_chart_tree.css".replaceAll("http://slayeroffice.com", so_archive_base));
			return;
		} else {
			css.href = ("http://slayeroffice.com/tools/dom_chart/dom_chart.css".replaceAll("http://slayeroffice.com", so_archive_base));
			return;
		}
	} else if (keyCode == 66) {
		doHighlight=doHighlight?0:1;
	}
}

function applyBGColor(objTagName) {
	r=295-objTagName.charCodeAt(0);
	g=295-objTagName.charCodeAt(1);
	b=295-objTagName.charCodeAt(2);

	if(!g)g=r;
	if(!b)b=r;

	return "rgb("+r+","+g+","+b+")";
}


function hideNode(nodeID) {
	if(!doHighlight)return;
	isShown=0;
	actualNode[nodeID].style.background = obc[nodeID];
}

function showNode(nodeID) {
	if(!doHighlight)return;
	if(isShown)return;
	isShown=1;
	obc[nodeID] =actualNode[nodeID].style.background;
	actualNode[nodeID].style.background="gray";
}

function hideChildren() {
	obj=this.parentNode;
	hideNode(obj.zid);
	obj.parentNode.removeChild(obj);
}

function childNodesAreDisplayed(parentObject){
	for(j=0;j<parentObject.childNodes.length;j++) {
		if(!isDisplayed[parentObject.childNodes[j]])return false;
	}
	//return true;
}

/* MSIE CODE - REMOVED FOR NOW...
		nID=objs[i].uniqueID;
		if(!objs[i].parentNode.tagName) {
			p[nID]=mObj.appendChild(d.createElement("span"));
			p[nID].className="chartLabel";
			p[nID].id=nID;
			p[nID].xid=1;
			p[nID].innerHTML=objs[i].tagName;
			isDisplayed[nID]=1;
		} else {
			p[nID]=p[objs[i].parentNode.uniqueID].appendChild(d.createElement("span"));
			p[nID].className="chartLabel";
			p[nID].innerHTML=objs[i].tagName;
			p[nID].style.top=p[objs[i].uniqueID].offsetTop+p[objs[i].uniqueID].offsetHeight+6+"px";
			p[nID].xid=1;
			p[nID].title="Parent Node: " + objs[i].parentNode.tagName;
		}
*/

so_init();