/* 	edit cookie value on current site.
	By Jesper Rønn-Jensen
	Load via bookmarklet:
	javascript:(function(){u='http://justaddwater.dk/wp-content/uploads/2007/01/cookieeditor.js';w=window.open();d=w.document;d.write('<html><head></head><body></body></html>');d.close();s=d.body.appendChild(w.document.createElement('script'));s.type='text/javascript';s.src=u;})()
	More info: http://justaddwater.dk/2007/01/29/javascript-cookie-editor-bookmarklet/
*/
var lastMod	='2007-01-29';

var dc,f,loaded=false;
var cN='editable';
re={
  namefield:new RegExp(/^nn/),
	valfield: new RegExp(/^vv/)
};

function init(){
	var _s='<p>Cookie editor. Add and modify cookies on this website. Created by Jesper Rønn-Jensen. This version modified '+lastMod+'</p>';
  _dc=getCookies();
	var i,n,v,t=[];
	_s+='<table><tr><th>Name</th><th>Value</th><th> </th></tr>';
	if(!_dc)
		_s+='<tr><td colspan="3">No Cookies</td></tr>';
	else 
	{
		for(i=0;i<_dc.length;i++){
		  t=_dc[i].indexOf('=');
		  n=_dc[i].substring(0,t);//name
		  v=_dc[i].substring(t+1);//value

		  _s+='<tr><td><span id="nn'+i+'" onclick="startEdit(this)" _name="'+n+'" _val="'+v+'" class="'+cN+'">'+n+'</span></td>';
		  _s+='    <td><span id="vv'+i+'" onclick="startEdit(this)" _name="'+n+'" _val="'+v+'" class="'+cN+'">'+v+'</span></td>';
		  _s+='<td>  <a href="javascript:delCookie(\''+n+'\');init()" title="Remove this cookie">Delete</a></td></tr>';
		}
	}
	_s+='<tr><td><input type="text" name="newname" class="'+cN+'" /></td><td><input type="text" name="newval" class="'+cN+'" /></td>';
	_s+='<td><input type="button" value="add" onclick="saveCookie(this.form.newname.value,this.form.newval.value);init()" /></td>';
	_s+='</table><p><input type="submit" value="refresh" onclick="init()" /></p>';
	_s+='<p>More info: <a href="http://justaddwater.dk/2007/01/29/javascript-cookie-editor-bookmarklet/">Justaddwater.dk cookie editor</a>.</p>';
	_s+='<p>&nbsp;</p>';
	if(!loaded){
		document.title='Cookies at ' + location.hostname;
		document.body.id='cooked';//for CSS declarations in CSS file
		f=document.body.appendChild(document.createElement('H1'));
		f.appendChild(document.createTextNode('Cookies at '+location.hostname));
		f=document.body.appendChild(document.createElement('style'));
		f.type="text/css"; 
		f.innerHTML='h1, h2, h3, h4	{margin-bottom: 0px;}\
    body 			{font-size:10pt; font-family:monospace;margin:8px 0px 8px 0px;}\
    #cooked span{display:block;}\
    #cooked body,span,p{font:84% Verdana}\
    #cooked .editable{width:99%; overflow:hidden;}\
    #cooked table{width:100%; margin:15px;}\
    \
    #cooked span.editable{\
      cursor: pointer; cursor: hand;\
      border: 1px solid white;\
      padding: 2px;\
    }\
    #cooked span.editable:hover{\
      border-color: #ccc;\
      background-color: white;\
    }\
    #cooked input.editable{}\
    ';
		
		f=document.body.appendChild(document.createElement('FORM'));
		f.onsubmit=function(){return false};
		loaded=true;
		document.close();
	}else if(document.forms.length>0){
		f=document.forms[0];
	}
	f.innerHTML=_s;
	
}
function startEdit(o)//o=span element
{
	//hide span
	o.style.display='none';
	//mark parent (td ) as id="editing"
	var p=o.parentNode;
	p.id='editing';
	//create input text field
	q=p.appendChild(document.createElement('INPUT'));
	q.id='editfield';
	q.type='text';
	q.className=cN;
	q.value=o.firstChild.nodeValue;
	q.setAttribute('_name',o.getAttribute('_name'));
	q.setAttribute('_val',o.getAttribute('_val'));
	q.select();

	q.onchange=endEdit;
	q.onblur=restoreAfterEdit;
}
function restoreAfterEdit(evt)//onblur event after onchange
{
	//no changes handled here
	var q=getEventObject(evt);
	//parent td is still="editing"
	var p=q.parentNode;
	p.id=null;
	//remove text field
	p.removeChild(q);
	//show span 
	var o=p.firstChild;
	o.style.display='block';

}
function endEdit(evt)//o=text field
{
	//get text field value 
	var q=getEventObject(evt);
	var val=q.value;
	var n=q.getAttribute('_name');
	var v=q.getAttribute('_val' );
	
	//then, save value
	var o=q.parentNode.firstChild;
	o.firstChild.nodeValue=val;
	dump('o.id.match(namefield): '+(o.id.match(re.namefield)));
	if(o.id.match(re.namefield)){	//the name has changed
		o.setAttribute('_name',val);
		//save old value under new name
		saveCookie(val,v);
		//delete old cookie
		delCookie(n);
		
		//also change corresponding value field
		var id=o.id.replace(re.namefield,'vv');
		o=document.getElementById( id );
		if(o)
		o.setAttribute('_name',val);
		else alert('Should never happen: Not able to rename corresponding value field (id="'+id+'")');
	}
	else{					//the value has changed
		o.setAttribute('_val',val);
		var id=o.id.replace(re.valfield,'nn');
		o=document.getElementById( id );
		if(o)
		o.setAttribute('_val',val);
		else alert('Should never happen: Not able to find corresponding name field (id="'+id+'")');
		saveCookie(n,val);	
	}
}

function getCookies(){
	cookies = (document.cookie)?document.cookie.split('; '):null;
	return cookies;
}

function saveCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function deleteCookie(name) {
	createCookie(name,"",-1);
}




/* Supportive general functions */
function getEventObject(evt)
{
	evt = (evt) ? evt : ( ( window.event ) ? window.event : null);
	if(!evt) return false;
	if(evt.target)	return evt.target;	//Moz equiv.
	else if (evt.srcElement) return evt.srcElement;	//IE only
	else return null;
}
// defensive code: IE is missing DOM0 window.dump()
if ( typeof(dump!='function') ) {function dump(str){}}


init();