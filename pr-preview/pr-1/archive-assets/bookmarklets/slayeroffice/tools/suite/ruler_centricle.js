/* Archive adaptation: local dependencies; original author notices follow. */
var so_archive_base = new URL(document.currentScript.src).href.split("/archive-assets/")[0] + "/archive-assets/bookmarklets/slayeroffice";
/*
	ruler favelet 1.2
	ksmith@centricle
	w/ code from fry@fcc

	hosted version for use with slayeroffice favelet suite
		http://slayeroffice.com/?c=/content/tools/suite.html

*/

drg=false;
d=document;
db=d.body;
d.ondblclick=kR;
d.onkeypress=kR;
rk=false;
mC=prompt('Color:','red');
mq=db.appendChild(d.createElement('div'));
mqs=mq.style;
mqs.position='absolute';
mqs.border='dashed 1px red';
mqs.fontSize='0px';
ctr=db.appendChild(d.createElement('div'));
ctrs=ctr.style;
ctrs.position='absolute';
ctrs.top='-300px';
ctrs.left='-300px';
ctrs.width='85px';
ctrs.background='#eee';
ctrs.padding='5px';
ctrs.border='solid 1px #ccc';
ctrs.font='10px verdana,sans-serif';
ctrs.width='85px';
ctrs.zIndex='99';
ctr.innerHTML='<b>Current:</b><br> x:<span id=\"cX\">0</span> y:<span id=\"cY\">0</span><br><b>Begin:</b><br> x:<span id=\"bX\">0</span> y:<span id=\"bY\">0</span><br><b>End:</b><br> x:<span id=\"eX\">0</span> y:<span id =\"eY\">0</span><br><b>Dimensions:</b><br> w:<span id=\"dX\">0</span> h:<span id=\"dY\">0</span>';
d.onmousemove=fW;
d.onmousedown=bD;
d.onmouseup=eD;
function dgE(i){
	return d.getElementById(i)
}

if(!d.all){
	cX=dgE('cX');
	cY=dgE('cY');
	bX=dgE('bX');
	bY=dgE('bY');
	eX=dgE('eX');
	eY=dgE('eY');
	dX=dgE('dX');
	dY=dgE('dY');
}

dbs=db.style;
dbs.cursor='crosshair';

function fW(e){
	if(rk==true) return;
	x=(e)?e.pageX:event.x;
	y=(e)?e.pageY:event.y;
	ctrs.left=x+15+'px';
	ctrs.top=y+15+'px';
	cX.innerHTML=x;
	cY.innerHTML=y;
	if(drg){
		dX.innerHTML=Math.abs(x-dsX);
		dY.innerHTML=Math.abs(y-dsY);
		if(x-dsX>0){
			mqs.width=x-dsX+'px';
		}else{
			mqs.width=-(x-dsX)+'px';
			mqs.left=x+'px';
			ctrs.left=dsX+15+'px';
		}
		if(y-dsY>0){
			mqs.height=y-dsY+'px';
		}else{
			mqs.height=-(y-dsY)+'px';
			mqs.top=y+'px';
			ctrs.top=dsY+15+'px';
		}
	}
	return false;
}

function bD(e){
	if(rk==true)return;
	mqs.width=0;
	mqs.height=0;
	mqs.borderColor=mC;
	drg=true;
	x=(e)?e.pageX:event.x;
	y=(e)?e.pageY:event.y;
	mqs.visibility='visible';
	mqs.left=x+'px';
	mqs.top=y+'px';
	dsX=x;
	dsY=y;
	bX.innerHTML=x;
	bY.innerHTML=y;
	return true;
}

function eD(e){
	drg=false;
	x=(e)?e.pageX:event.x;
	y=(e)?e.pageY:event.y;
	eX.innerHTML=x;
	eY.innerHTML=y;
	return true;
}

function kR(){
	mqs.visibility='hidden';
	ctrs.top='-300px';
	ctrs.left='-300px';
	dbs.cursor='auto';
	rk=true;
}