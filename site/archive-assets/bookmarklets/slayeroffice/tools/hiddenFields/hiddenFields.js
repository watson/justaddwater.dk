/* Archive adaptation: local dependencies; original author notices follow. */
var so_archive_base = new URL(document.currentScript.src).href.split("/archive-assets/")[0] + "/archive-assets/bookmarklets/slayeroffice";
function getFieldValues() {	
	d=document;
	f=d.forms;
	if(!f.length)return alert("No Forms!");
	r=d.body.appendChild(d.createElement("div"));
	r.id="frmInfo";
	z=d.body.appendChild(d.createElement("link"));
	z.id="frmStyles";
	z.rel="Stylesheet";
	z.href=("http://slayeroffice.com/tools/hiddenFields/styles.css".replaceAll("http://slayeroffice.com", so_archive_base));
	m=0;
	for(i=0;i<f.length;i++) {
		n="";
		e=f[i].elements;
		p=0;
		label=0;
		while(e[p]) {
			if(!e[p])break;
			if(e[p].type=="hidden") {
				if(!label) {
					h1=r.appendChild(d.createElement("h1"));
					try{ h1.innerHTML="Form["+i+"]" } catch(err) { }
					label=1;
				}
				v=r.appendChild(d.createElement("span"));
				v.innerHTML=e[p].name+": ";
				t=r.appendChild(d.createElement("input"));
				t.type="text";
				t.id="c" + m;
				t.value = e[p].value;t.rel=p;
				n="javascript:void(document.forms["+i+"].elements["+p+"].value=document.getElementById('c"+m+"').value)";
				m++;
				s=r.appendChild(d.createElement("a"));
				s.href=n;
				s.innerHTML="[change]";
				r.appendChild(d.createElement("br"));
			}
		p++;
		}
	}
	if(m==0) {
		alert("No Hidden Fields!");
		d.body.removeChild(document.getElementById("frmInfo"));
		return;
	}
	q=r.appendChild(d.createElement("a"));
	q.className="close";
	q.href="javascript:void(cleanUp());";
	q.innerHTML = "[close]";

	h4=r.appendChild(d.createElement("h4"));
	h4.innerHTML="Hidden Field Value Modifier v1.0<br />Last Revision: 02.18.2004<br /><a href=\"http://slayeroffice.com\">http://slayeroffice.com</a>";
	window.scrollTo(0,0);
}

function cleanUp() {
	document.body.removeChild(document.getElementById("frmStyles"));
	document.body.removeChild(document.getElementById("frmInfo"));
}

getFieldValues();

