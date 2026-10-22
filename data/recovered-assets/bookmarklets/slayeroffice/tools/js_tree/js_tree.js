/*************************************

	Javascript Object Tree
	version 1.0
	last revision:04.11.2004
	steve@slayeroffice.com
	http://slayeroffice.com
	
	(c)2004 S.G. Chipman

	Please notify me of any modifications
	you make to this code so that I can 
	update the version hosted on slayeroffice.com


************************************/

var so_d=document;

var so_types=new Array();
var so_objs=new Array();
var so_hidden = new Array();
document.onkeydown=so_handleKeyEvent;
so_opera = window.opera;

function so_init() {
	if(document.all && !so_opera)return alert("Sorry, this only works in Mozilla and Firefox currently.");
	mObj=so_d.body.appendChild(so_d.createElement("div"));
	mObj.id="so_mContainer";
	sObj=so_d.body.appendChild(so_d.createElement("link"));
	sObj.id="so_mStyle";
	sObj.type="text/css";
	sObj.rel="StyleSheet";
	sObj.href="http://slayeroffice.com/tools/js_tree/js_tree.css";

	so_parseJS();
	so_buildTree();

	cObj=mObj.appendChild(so_d.createElement("div"));
	cObj.className="credits";
	cObj.innerHTML = "<b>[esc] to <a href=\"javascript:so_cleanUp();\">close</a></b><br />Javascript Object Tree<br />version 1.0<br />last revision:04.11.2004<br /><a target=\"_blank\" href=\"http://slayeroffice.com\">slayeroffice.com</a>";

	window.scrollTo(0,0);
}

function so_format(str) {
	str=str.replace(/</g,"&lt;");
	str=str.replace(/>/g,"&gt;");
	return str;
}

function so_parseJS() {
	win=window;
	for(js in win) {
		try {
			if(win[js] && js.toString().indexOf("so_")==-1 && win[js].toString().indexOf("[native code]")==-1) {
				t=typeof(win[js]);
				if(!so_objs[t.toString()]) {
					so_types[so_types.length]=t;;
					so_objs[t]=new Array();
				}
				if(win[js].toString().indexOf("[object")==-1) {
					index=so_objs[t].length
					so_objs[t][index]=new Array();
					so_objs[t][index][0]=js;
					so_objs[t][index][1]=so_format(win[js].toString());
				}
			}
		} catch(err) { }
	}
}

function so_show(objID) {
	so_d.getElementById(objID).style.display=so_hidden[objID]?"none":"block";
	so_hidden[objID]=so_hidden[objID]?0:1;
}

function so_changeSpan(spanID) {
	if(so_d.getElementById(spanID).innerHTML.indexOf("+")>-1){
		so_d.getElementById(spanID).innerHTML="[-]";
	} else {
		so_d.getElementById(spanID).innerHTML="[+]";
	}
}

function so_buildTree() {
	mHTML="<ul class=\"topLevel\">";
	so_types.sort();
	so_objIndex=0;
	for(i=0;i<so_types.length;i++) {
		mHTML+="<li style=\"cursor:pointer;\" onclick=\"so_show('ul"+i+"');so_changeSpan('sp" + i + "')\"><span id=\"sp" + i + "\">[+]</span><b>" + so_types[i] + "</b> (" + so_objs[so_types[i]].length + ")</li><ul style=\"display:none;\" id=\"ul"+i+"\">";
		so_hidden["ul"+i]=0;
		for(e=0;e<so_objs[so_types[i]].length;e++) {
			mHTML+="<li style=\"cursor:pointer;\" onclick=\"so_show('mul" + so_objIndex + "');so_changeSpan('sk" + so_objIndex + "')\"><span id=\"sk" + so_objIndex + "\">[+]</span>" + so_objs[so_types[i]][e][0] + "</li><ul id=\"mul" + so_objIndex + "\" style=\"display:none;\"><li style=\"list-style-type:none;\"><pre>" + so_objs[so_types[i]][e][1] + "</pre></li></ul>";
			so_hidden["mul"+so_objIndex]=0;
			so_objIndex++;
		}
		mHTML+="</ul>";
	}
	mHTML+="</ul>";
	so_d.getElementById("so_mContainer").innerHTML =mHTML;
}

function so_handleKeyEvent(e) {
	keyCode=document.all?window.event.keyCode:e.keyCode;
	if(keyCode==27) {
		so_cleanUp();
	}
}

function so_cleanUp() {
	so_d.body.removeChild(so_d.getElementById("so_mContainer"));
	so_d.body.removeChild(so_d.getElementById("so_mStyle"));
	so_d.body.removeChild(so_d.getElementById("sst"));
	document.onkeydown=null;
}
so_init();