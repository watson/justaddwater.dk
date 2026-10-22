/*************************************

	Remove Children 
	v1.1
	last revision: 11.20.2004
	steve@slayeroffice.com

	Modified by Robin Zalek (v1.1)
	 - Added escape cancelling
	 - http://www.jellyslab.com/~bteo
	
*************************************/

var b=new Array();
var c=1;
document.onkeydown=ck;
el=document.getElementsByTagName('*');
for(i=0;i<el.length;i++){
  if(el[i].tagName.search(/(HTML|BODY)/i)==-1){
    if(el[i].title) el[i].oldTitle=el[i].title;
    el[i].title='click to remove '+el[i].tagName;
    el[i].onclick=function(e){
      t=this;
      if(window.event) e=window.event;
      if((t==e.target)||(window.event)) t.parentNode.removeChild(t);
      if(window.opera) e.stopPropagation();
      return false;
    };
    el[i].onmouseover=function(){
      if(!c)return;
      c=0;
      t=this;
      b[t]=t.style.backgroundColor;
      t.style.background='#DADADA';
    };
    void(
      el[i].onmouseout=function(){
        t=this;
        t.style.backgroundColor=b[t];
        c=1;
      }
    );
  }
}

function ck(e){
	k=window.event?window.event.keyCode:e.keyCode;
	if(k==27) {
    for(i=0;i<el.length;i++){
      if(el[i].tagName.search(/(HTML|BODY)/i)==-1){
        el[i].oldTitle?el[i].title=el[i].oldTitle:el[i].removeAttribute('title');
        el[i].onclick=null;
        el[i].onmouseover=null;
        el[i].onmouseout=null;
        el[i].style.backgroundColor=b[t];
      }
    }
	}
}