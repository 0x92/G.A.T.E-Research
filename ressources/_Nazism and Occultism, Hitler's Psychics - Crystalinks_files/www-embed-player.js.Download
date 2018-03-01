(function(){var l,aa="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ba;
if("function"==typeof Object.setPrototypeOf)ba=Object.setPrototypeOf;else{var ca;a:{var da={sa:!0},ea={};try{ea.__proto__=da;ca=ea.sa;break a}catch(a){}ca=!1}ba=ca?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var fa=ba;
function n(a,b){a.prototype=aa(b.prototype);a.prototype.constructor=a;if(fa)fa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.o=b.prototype}
for(var ha="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)},ia="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this,ja=function(){function a(){function a(){}
Reflect.construct(a,[],function(){});
return new a instanceof a}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(a,d,e){a=b(a,d);e&&Reflect.setPrototypeOf(a,e.prototype);return a}}return function(a,b,e){void 0===e&&(e=a);
e=aa(e.prototype||Object.prototype);return Function.prototype.apply.call(a,e,b)||e}}(),ka=ia,la=["Reflect",
"construct"],ma=0;ma<la.length-1;ma++){var na=la[ma];na in ka||(ka[na]={});ka=ka[na]}var oa=la[la.length-1];ja!=ka[oa]&&null!=ja&&ha(ka,oa,{configurable:!0,writable:!0,value:ja});var p=this;function q(a){return void 0!==a}
function r(a){return"string"==typeof a}
function t(a,b,c){a=a.split(".");c=c||p;a[0]in c||!c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&q(b)?c[d]=b:c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}}
function v(a,b){for(var c=a.split("."),d=b||p,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function pa(){}
function qa(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function w(a){return"array"==qa(a)}
function ra(a){var b=qa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function sa(a){return"function"==qa(a)}
function ta(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
var ua="closure_uid_"+(1E9*Math.random()>>>0),va=0;function wa(a,b,c){return a.call.apply(a.bind,arguments)}
function xa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function x(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?x=wa:x=xa;return x.apply(null,arguments)}
function y(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
var z=Date.now||function(){return+new Date};
function A(a,b){function c(){}
c.prototype=b.prototype;a.o=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.base=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function B(a){if(Error.captureStackTrace)Error.captureStackTrace(this,B);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
A(B,Error);B.prototype.name="CustomError";var ya=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,"")};
function za(a){if(!Aa.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(Ba,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(Ca,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(Fa,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(Ga,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Ha,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Ia,"&#0;"));return a}
var Ba=/&/g,Ca=/</g,Fa=/>/g,Ga=/"/g,Ha=/'/g,Ia=/\x00/g,Aa=/[\x00&<>"']/;function Ja(a,b){return a<b?-1:a>b?1:0}
function Ka(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var La=Array.prototype.indexOf?function(a,b,c){return Array.prototype.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;
if(r(a))return r(b)&&1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},C=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=r(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Ma=Array.prototype.filter?function(a,b,c){return Array.prototype.filter.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g=r(a)?a.split(""):a,h=0;h<d;h++)if(h in g){var k=g[h];
b.call(c,k,h,a)&&(e[f++]=k)}return e},Na=Array.prototype.map?function(a,b,c){return Array.prototype.map.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=Array(d),f=r(a)?a.split(""):a,g=0;g<d;g++)g in f&&(e[g]=b.call(c,f[g],g,a));
return e};
function Oa(a,b){a:{var c=a.length;for(var d=r(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:r(a)?a.charAt(c):a[c]}
function Pa(a,b){var c=La(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function Qa(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function Ra(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(ra(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;var Sa;a:{var Ta=p.navigator;if(Ta){var Ua=Ta.userAgent;if(Ua){Sa=Ua;break a}}Sa=""}function D(a){return-1!=Sa.indexOf(a)}
;function Va(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Wa(a,b){var c=ra(b),d=c?b:arguments;for(c=c?0:1;c<d.length;c++){if(null==a)return;a=a[d[c]]}return a}
function Xa(a){var b=Ya,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function Za(a){for(var b in a)return!1;return!0}
function $a(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function ab(a){var b={},c;for(c in a)b[c]=a[c];return b}
var bb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function cb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<bb.length;f++)c=bb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;function db(a,b){var c=eb;return Object.prototype.hasOwnProperty.call(c,a)?c[a]:c[a]=b(a)}
;var fb=D("Opera"),E=D("Trident")||D("MSIE"),gb=D("Edge"),hb=D("Gecko")&&!(-1!=Sa.toLowerCase().indexOf("webkit")&&!D("Edge"))&&!(D("Trident")||D("MSIE"))&&!D("Edge"),ib=-1!=Sa.toLowerCase().indexOf("webkit")&&!D("Edge");function jb(){var a=p.document;return a?a.documentMode:void 0}
var lb;a:{var mb="",nb=function(){var a=Sa;if(hb)return/rv:([^\);]+)(\)|;)/.exec(a);if(gb)return/Edge\/([\d\.]+)/.exec(a);if(E)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(ib)return/WebKit\/(\S+)/.exec(a);if(fb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
nb&&(mb=nb?nb[1]:"");if(E){var ob=jb();if(null!=ob&&ob>parseFloat(mb)){lb=String(ob);break a}}lb=mb}var pb=lb,eb={};
function F(a){return db(a,function(){for(var b=0,c=ya(String(pb)).split("."),d=ya(String(a)).split("."),e=Math.max(c.length,d.length),f=0;0==b&&f<e;f++){var g=c[f]||"",h=d[f]||"";do{g=/(\d*)(\D*)(.*)/.exec(g)||["","","",""];h=/(\d*)(\D*)(.*)/.exec(h)||["","","",""];if(0==g[0].length&&0==h[0].length)break;b=Ja(0==g[1].length?0:parseInt(g[1],10),0==h[1].length?0:parseInt(h[1],10))||Ja(0==g[2].length,0==h[2].length)||Ja(g[2],h[2]);g=g[3];h=h[3]}while(0==b)}return 0<=b})}
var qb;var rb=p.document;qb=rb&&E?jb()||("CSS1Compat"==rb.compatMode?parseInt(pb,10):5):void 0;var sb=!E||9<=Number(qb);!hb&&!E||E&&9<=Number(qb)||hb&&F("1.9.1");E&&F("9");function tb(){this.b="";this.g=ub}
tb.prototype.W=!0;tb.prototype.J=function(){return this.b};
function vb(a){return a instanceof tb&&a.constructor===tb&&a.g===ub?a.b:"type_error:TrustedResourceUrl"}
var ub={};function G(){this.b="";this.g=wb}
G.prototype.W=!0;G.prototype.J=function(){return this.b};
function xb(a){return a instanceof G&&a.constructor===G&&a.g===wb?a.b:"type_error:SafeUrl"}
var yb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function zb(a){if(a instanceof G)return a;a=a.W?a.J():String(a);yb.test(a)||(a="about:invalid#zClosurez");return Ab(a)}
var wb={};function Ab(a){var b=new G;b.b=a;return b}
Ab("about:blank");function Bb(){this.b=""}
Bb.prototype.W=!0;Bb.prototype.J=function(){return this.b};
function Cb(a){var b=new Bb;b.b=a;return b}
Cb("<!DOCTYPE html>");Cb("");Cb("<br>");function Db(a,b){var c=b instanceof G?b:zb(b);a.href=xb(c)}
function Eb(a,b,c){a.rel=c;a.href=-1!=c.toLowerCase().indexOf("stylesheet")?vb(b):b instanceof tb?vb(b):b instanceof G?xb(b):zb(b).J()}
function Fb(a,b){a.src=vb(b)}
;function Gb(a,b){this.width=a;this.height=b}
l=Gb.prototype;l.aspectRatio=function(){return this.width/this.height};
l.isEmpty=function(){return!(this.width*this.height)};
l.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
l.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
l.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Hb(a){var b=document;return r(a)?b.getElementById(a):a}
function Ib(a,b){Va(b,function(b,d){b&&b.W&&(b=b.J());"style"==d?a.style.cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:Jb.hasOwnProperty(d)?a.setAttribute(Jb[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})}
var Jb={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Kb(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!sb&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',za(g.name),'"');if(g.type){f.push(' type="',za(g.type),'"');var h={};cb(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=e.createElement(f);g&&(r(g)?f.className=g:w(g)?f.className=g.join(" "):Ib(f,g));2<d.length&&Lb(e,f,d);return f}
function Lb(a,b,c){function d(c){c&&b.appendChild(r(c)?a.createTextNode(c):c)}
for(var e=2;e<c.length;e++){var f=c[e];if(!ra(f)||ta(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(ta(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if(sa(f)){g="function"==typeof f.item;break a}}g=!1}C(g?Qa(f):f,d)}}}
function Mb(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Nb(a){Ob();var b=new tb;b.b=a;return b}
var Ob=pa;var Pb=document,H=window;function Qb(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Rb=(new Date).getTime();function Sb(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a)throw Error("Invalid URI scheme in origin");c="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+
1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function Tb(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;u=m=0}
function b(a){for(var b=g,c=0;64>c;c+=4)b[c/4]=a[c]<<24|a[c+1]<<16|a[c+2]<<8|a[c+3];for(c=16;80>c;c++)a=b[c-3]^b[c-8]^b[c-14]^b[c-16],b[c]=(a<<1|a>>>31)&4294967295;a=e[0];var d=e[1],f=e[2],h=e[3],k=e[4];for(c=0;80>c;c++){if(40>c)if(20>c){var m=h^d&(f^h);var u=1518500249}else m=d^f^h,u=1859775393;else 60>c?(m=d&f|h&(d|f),u=2400959708):(m=d^f^h,u=3395469782);m=((a<<5|a>>>27)&4294967295)+m+k+u+b[c]&4294967295;k=h;h=f;f=(d<<30|d>>>2)&4294967295;d=a;a=m}e[0]=e[0]+a&4294967295;e[1]=e[1]+d&4294967295;e[2]=
e[2]+f&4294967295;e[3]=e[3]+h&4294967295;e[4]=e[4]+k&4294967295}
function c(a,c){if("string"===typeof a){a=unescape(encodeURIComponent(a));for(var d=[],e=0,g=a.length;e<g;++e)d.push(a.charCodeAt(e));a=d}c||(c=a.length);d=0;if(0==m)for(;d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64;for(;d<c;)if(f[m++]=a[d++],u++,64==m)for(m=0,b(f);d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64}
function d(){var a=[],d=8*u;56>m?c(h,56-m):c(h,64-(m-56));for(var g=63;56<=g;g--)f[g]=d&255,d>>>=8;b(f);for(g=d=0;5>g;g++)for(var k=24;0<=k;k-=8)a[d++]=e[g]>>k&255;return a}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var m,u;a();return{reset:a,update:c,digest:d,ua:function(){for(var a=d(),b="",c=0;c<a.length;c++)b+="0123456789ABCDEF".charAt(Math.floor(a[c]/16))+"0123456789ABCDEF".charAt(a[c]%16);return b}}}
;function Ub(a,b,c){var d=[],e=[];if(1==(w(c)?2:1))return e=[b,a],C(d,function(a){e.push(a)}),Vb(e.join(" "));
var f=[],g=[];C(c,function(a){g.push(a.key);f.push(a.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];C(d,function(a){e.push(a)});
a=Vb(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function Vb(a){var b=Tb();b.update(a);return b.ua().toLowerCase()}
;function Wb(a){this.b=a||{cookie:""}}
l=Wb.prototype;l.isEnabled=function(){return navigator.cookieEnabled};
l.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');q(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(z()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
l.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(";"),e=0,f;e<d.length;e++){f=ya(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
l.remove=function(a,b,c){var d=q(this.get(a));this.set(a,"",0,b,c);return d};
l.isEmpty=function(){return!this.b.cookie};
l.clear=function(){for(var a=(this.b.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=ya(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Xb=new Wb("undefined"==typeof document?null:document);Xb.g=3950;function Yb(){var a=[],b=Sb(String(p.location.href)),c=p.__OVERRIDE_SID;null==c&&(c=(new Wb(document)).get("SID"));if(c&&(b=(c=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?p.__SAPISID:p.__APISID,null==b&&(b=(new Wb(document)).get(c?"SAPISID":"APISID")),b)){c=c?"SAPISIDHASH":"APISIDHASH";var d=String(p.location.href);return d&&b&&c?[c,Ub(Sb(d),b,a||null)].join(" "):null}return null}
;function Zb(a,b,c){this.h=c;this.f=a;this.i=b;this.g=0;this.b=null}
Zb.prototype.get=function(){if(0<this.g){this.g--;var a=this.b;this.b=a.next;a.next=null}else a=this.f();return a};
function $b(a,b){a.i(b);a.g<a.h&&(a.g++,b.next=a.b,a.b=b)}
;function ac(a){p.setTimeout(function(){throw a;},0)}
var bc;
function cc(){var a=p.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!D("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=x(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!D("Trident")&&!D("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(q(c.next)){c=c.next;var a=c.ia;c.ia=null;a()}};
return function(a){d.next={ia:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){p.setTimeout(a,0)}}
;function dc(){this.g=this.b=null}
var fc=new Zb(function(){return new ec},function(a){a.reset()},100);
dc.prototype.add=function(a,b){var c=fc.get();c.set(a,b);this.g?this.g.next=c:this.b=c;this.g=c};
dc.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.g=null),a.next=null);return a};
function ec(){this.next=this.scope=this.b=null}
ec.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
ec.prototype.reset=function(){this.next=this.scope=this.b=null};function gc(a,b){hc||ic();jc||(hc(),jc=!0);kc.add(a,b)}
var hc;function ic(){if(-1!=String(p.Promise).indexOf("[native code]")){var a=p.Promise.resolve(void 0);hc=function(){a.then(lc)}}else hc=function(){var a=lc;
!sa(p.setImmediate)||p.Window&&p.Window.prototype&&!D("Edge")&&p.Window.prototype.setImmediate==p.setImmediate?(bc||(bc=cc()),bc(a)):p.setImmediate(a)}}
var jc=!1,kc=new dc;function lc(){for(var a;a=kc.remove();){try{a.b.call(a.scope)}catch(b){ac(b)}$b(fc,a)}jc=!1}
;function I(){this.g=this.g;this.B=this.B}
I.prototype.g=!1;I.prototype.dispose=function(){this.g||(this.g=!0,this.l())};
function mc(a,b){a.g?q(void 0)?b.call(void 0):b():(a.B||(a.B=[]),a.B.push(q(void 0)?x(b,void 0):b))}
I.prototype.l=function(){if(this.B)for(;this.B.length;)this.B.shift()()};
function nc(a){a&&"function"==typeof a.dispose&&a.dispose()}
function oc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];ra(d)?oc.apply(null,d):nc(d)}}
;function pc(a){if(a.classList)return a.classList;a=a.className;return r(a)&&a.match(/\S+/g)||[]}
function qc(a,b){if(a.classList)var c=a.classList.contains(b);else c=pc(a),c=0<=La(c,b);return c}
function rc(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):qc(a,"inverted-hdpi")&&(a.className=Ma(pc(a),function(a){return"inverted-hdpi"!=a}).join(" "))}
;var sc="StopIteration"in p?p.StopIteration:{message:"StopIteration",stack:""};function tc(){}
tc.prototype.next=function(){throw sc;};
tc.prototype.T=function(){return this};
function uc(a){if(a instanceof tc)return a;if("function"==typeof a.T)return a.T(!1);if(ra(a)){var b=0,c=new tc;c.next=function(){for(;;){if(b>=a.length)throw sc;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function vc(a,b){if(ra(a))try{C(a,b,void 0)}catch(c){if(c!==sc)throw c;}else{a=uc(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==sc)throw c;}}}
function wc(a){if(ra(a))return Qa(a);a=uc(a);var b=[];vc(a,function(a){b.push(a)});
return b}
;E&&F("9");!ib||F("528");hb&&F("1.9b")||E&&F("8")||fb&&F("9.5")||ib&&F("528");hb&&!F("8")||E&&F("9");(function(){if(!p.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
p.addEventListener("test",pa,b);p.removeEventListener("test",pa,b);return a})();function xc(a){var b=[];yc(new zc,a,b);return b.join("")}
function zc(){}
function yc(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(w(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),yc(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Ac(d,c),c.push(":"),yc(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Ac(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Bc={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Cc=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Ac(a,b){b.push('"',a.replace(Cc,function(a){var b=Bc[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),Bc[a]=b);return b}),'"')}
;function Dc(a){a.prototype.then=a.prototype.then;a.prototype.$goog_Thenable=!0}
function Ec(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function J(a,b){this.b=0;this.m=void 0;this.h=this.g=this.f=null;this.i=this.j=!1;if(a!=pa)try{var c=this;a.call(b,function(a){Fc(c,2,a)},function(a){Fc(c,3,a)})}catch(d){Fc(this,3,d)}}
function Gc(){this.next=this.context=this.g=this.h=this.b=null;this.f=!1}
Gc.prototype.reset=function(){this.context=this.g=this.h=this.b=null;this.f=!1};
var Hc=new Zb(function(){return new Gc},function(a){a.reset()},100);
function Ic(a,b,c){var d=Hc.get();d.h=a;d.g=b;d.context=c;return d}
function Jc(a){return new J(function(b,c){c(a)})}
function Kc(a,b,c){Lc(a,b,c,null)||gc(y(b,a))}
function Mc(a){return new J(function(b,c){a.length||b(void 0);for(var d=0,e;d<a.length;d++)e=a[d],Kc(e,b,c)})}
function Nc(a){return new J(function(b){var c=a.length,d=[];if(c)for(var e=function(a,e,f){c--;d[a]=e?{aa:!0,value:f}:{aa:!1,reason:f};0==c&&b(d)},f=0,g;f<a.length;f++)g=a[f],Kc(g,y(e,f,!0),y(e,f,!1));
else b(d)})}
J.prototype.then=function(a,b,c){return Oc(this,sa(a)?a:null,sa(b)?b:null,c)};
Dc(J);function Pc(a,b){var c=Ic(b,b,void 0);c.f=!0;Qc(a,c);return a}
function Rc(a,b){return Oc(a,null,b,void 0)}
J.prototype.cancel=function(a){0==this.b&&gc(function(){var b=new Sc(a);Tc(this,b)},this)};
function Tc(a,b){if(0==a.b)if(a.f){var c=a.f;if(c.g){for(var d=0,e=null,f=null,g=c.g;g&&(g.f||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?Tc(c,b):(f?(d=f,d.next==c.h&&(c.h=d),d.next=d.next.next):Uc(c),Vc(c,e,3,b)))}a.f=null}else Fc(a,3,b)}
function Qc(a,b){a.g||2!=a.b&&3!=a.b||Wc(a);a.h?a.h.next=b:a.g=b;a.h=b}
function Oc(a,b,c,d){var e=Ic(null,null,null);e.b=new J(function(a,g){e.h=b?function(c){try{var e=b.call(d,c);a(e)}catch(m){g(m)}}:a;
e.g=c?function(b){try{var e=c.call(d,b);!q(e)&&b instanceof Sc?g(b):a(e)}catch(m){g(m)}}:g});
e.b.f=a;Qc(a,e);return e.b}
J.prototype.u=function(a){this.b=0;Fc(this,2,a)};
J.prototype.A=function(a){this.b=0;Fc(this,3,a)};
function Fc(a,b,c){0==a.b&&(a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself")),a.b=1,Lc(c,a.u,a.A,a)||(a.m=c,a.b=b,a.f=null,Wc(a),3!=b||c instanceof Sc||Xc(a,c)))}
function Lc(a,b,c,d){if(a instanceof J)return Qc(a,Ic(b||pa,c||null,d)),!0;if(Ec(a))return a.then(b,c,d),!0;if(ta(a))try{var e=a.then;if(sa(e))return Yc(a,e,b,c,d),!0}catch(f){return c.call(d,f),!0}return!1}
function Yc(a,b,c,d,e){function f(a){h||(h=!0,d.call(e,a))}
function g(a){h||(h=!0,c.call(e,a))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Wc(a){a.j||(a.j=!0,gc(a.B,a))}
function Uc(a){var b=null;a.g&&(b=a.g,a.g=b.next,b.next=null);a.g||(a.h=null);return b}
J.prototype.B=function(){for(var a;a=Uc(this);)Vc(this,a,this.b,this.m);this.j=!1};
function Vc(a,b,c,d){if(3==c&&b.g&&!b.f)for(;a&&a.i;a=a.f)a.i=!1;if(b.b)b.b.f=null,Zc(b,c,d);else try{b.f?b.h.call(b.context):Zc(b,c,d)}catch(e){$c.call(null,e)}$b(Hc,b)}
function Zc(a,b,c){2==b?a.h.call(a.context,c):a.g&&a.g.call(a.context,c)}
function Xc(a,b){a.i=!0;gc(function(){a.i&&$c.call(null,b)})}
var $c=ac;function Sc(a){B.call(this,a)}
A(Sc,B);Sc.prototype.name="cancel";function K(a){I.call(this);this.j=1;this.h=[];this.i=0;this.b=[];this.f={};this.m=!!a}
A(K,I);l=K.prototype;l.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.j;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.j=e+3;d.push(e);return e};
function ad(a,b,c,d){if(b=a.f[b]){var e=a.b;(b=Oa(b,function(a){return e[a+1]==c&&e[a+2]==d}))&&a.D(b)}}
l.D=function(a){var b=this.b[a];if(b){var c=this.f[b];0!=this.i?(this.h.push(a),this.b[a+1]=pa):(c&&Pa(c,a),delete this.b[a],delete this.b[a+1],delete this.b[a+2])}return!!b};
l.G=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.m)for(e=0;e<c.length;e++){var g=c[e];bd(this.b[g+1],this.b[g+2],d)}else{this.i++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.i--,0<this.h.length&&0==this.i)for(;c=this.h.pop();)this.D(c)}}return 0!=e}return!1};
function bd(a,b,c){gc(function(){a.apply(b,c)})}
l.clear=function(a){if(a){var b=this.f[a];b&&(C(b,this.D,this),delete this.f[a])}else this.b.length=0,this.f={}};
l.l=function(){K.o.l.call(this);this.clear();this.h.length=0};function cd(a){this.b=a}
cd.prototype.set=function(a,b){q(b)?this.b.set(a,xc(b)):this.b.remove(a)};
cd.prototype.get=function(a){try{var b=this.b.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
cd.prototype.remove=function(a){this.b.remove(a)};function dd(a){this.b=a}
A(dd,cd);function ed(a){this.data=a}
function fd(a){return!q(a)||a instanceof ed?a:new ed(a)}
dd.prototype.set=function(a,b){dd.o.set.call(this,a,fd(b))};
dd.prototype.g=function(a){a=dd.o.get.call(this,a);if(!q(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
dd.prototype.get=function(a){if(a=this.g(a)){if(a=a.data,!q(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};function gd(a){this.b=a}
A(gd,dd);gd.prototype.set=function(a,b,c){if(b=fd(b)){if(c){if(c<z()){gd.prototype.remove.call(this,a);return}b.expiration=c}b.creation=z()}gd.o.set.call(this,a,b)};
gd.prototype.g=function(a,b){var c=gd.o.g.call(this,a);if(c){var d;if(d=!b){d=c.creation;var e=c.expiration;d=!!e&&e<z()||!!d&&d>z()}if(d)gd.prototype.remove.call(this,a);else return c}};function hd(a){this.b=a}
A(hd,gd);function id(){}
;function jd(){}
A(jd,id);jd.prototype.clear=function(){var a=wc(this.T(!0)),b=this;C(a,function(a){b.remove(a)})};function kd(a){this.b=a}
A(kd,jd);l=kd.prototype;l.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
l.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
l.get=function(a){a=this.b.getItem(a);if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
l.remove=function(a){this.b.removeItem(a)};
l.T=function(a){var b=0,c=this.b,d=new tc;d.next=function(){if(b>=c.length)throw sc;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
l.clear=function(){this.b.clear()};
l.key=function(a){return this.b.key(a)};function ld(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
A(ld,kd);function md(){var a=null;try{a=window.sessionStorage||null}catch(b){}this.b=a}
A(md,kd);function nd(a){if(!sa(a))if(a&&"function"==typeof a.handleEvent)a=x(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(5E3)?-1:p.setTimeout(a,5E3)}
function od(){var a=null;return Rc(new J(function(b,c){a=nd(function(){b(void 0)});
-1==a&&c(Error("Failed to schedule timer."))}),function(b){p.clearTimeout(a);
throw b;})}
;var pd=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function L(a){return a.match(pd)}
function qd(a){return a?decodeURI(a):a}
function rd(a,b,c){if(w(b))for(var d=0;d<b.length;d++)rd(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function sd(a){var b=[],c;for(c in a)rd(c,a[c],b);return b.join("&")}
function td(a,b){var c=sd(b);if(c){var d=a.indexOf("#");0>d&&(d=a.length);var e=a.indexOf("?");if(0>e||e>d){e=d;var f=""}else f=a.substring(e+1,d);d=[a.substr(0,e),f,a.substr(d)];e=d[1];d[1]=c?e?e+"&"+c:c:e;c=d[0]+(d[1]?"?"+d[1]:"")+d[2]}else c=a;return c}
;var ud=!1,vd="";function wd(a){a=a.match(/[\d]+/g);if(!a)return"";a.length=3;return a.join(".")}
(function(){if(navigator.plugins&&navigator.plugins.length){var a=navigator.plugins["Shockwave Flash"];if(a&&(ud=!0,a.description)){vd=wd(a.description);return}if(navigator.plugins["Shockwave Flash 2.0"]){ud=!0;vd="2.0.0.11";return}}if(navigator.mimeTypes&&navigator.mimeTypes.length&&(a=navigator.mimeTypes["application/x-shockwave-flash"],ud=!(!a||!a.enabledPlugin))){vd=wd(a.enabledPlugin.description);return}try{var b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");ud=!0;vd=wd(b.GetVariable("$version"));
return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");ud=!0;vd="6.0.21";return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"),ud=!0,vd=wd(b.GetVariable("$version"))}catch(c){}})();
var xd=ud,yd=vd;function zd(a,b){var c="script";c=void 0===c?"":c;var d=a.createElement("link");Eb(d,b,"preload");c&&(d.as=c);(c=a.getElementsByTagName("head")[0])&&c.appendChild(d)}
;var Ad=/^\.google\.(com?\.)?[a-z]{2,3}$/,Bd=/\.(cn|com\.bi|do|sl)$/;function Cd(a){return Ad.test(a)&&!Bd.test(a)}
var Dd=p;function Gd(a){a="https://"+("adservice"+a+"/adsid/integrator.js");var b=["domain="+encodeURIComponent(p.location.hostname)];M[3]>=z()&&b.push("adsid="+encodeURIComponent(M[1]));return a+"?"+b.join("&")}
var M,N;function Hd(){Dd=p;M=Dd.googleToken=Dd.googleToken||{};var a=z();M[1]&&M[3]>a&&0<M[2]||(M[1]="",M[2]=-1,M[3]=-1,M[4]="",M[6]="");N=Dd.googleIMState=Dd.googleIMState||{};Cd(N[1])||(N[1]=".google.com");w(N[5])||(N[5]=[]);"boolean"==typeof N[6]||(N[6]=!1);w(N[7])||(N[7]=[]);"number"==typeof N[8]||(N[8]=0)}
function Id(){Hd();return M[1]}
var O={ka:function(){return 0<N[8]},
Ja:function(){N[8]++},
Ka:function(){0<N[8]&&N[8]--},
La:function(){N[8]=0},
shouldRetry:function(){return!1},
ja:function(){return N[5]},
ha:function(a){try{a()}catch(b){p.setTimeout(function(){throw b;},0)}},
fa:function(){if(!O.ka()){var a=p.document,b=function(b){var c=Gd(b);zd(a,c);b=a.createElement("script");b.type="text/javascript";b.onerror=function(){return p.processGoogleToken({},2)};
c=Nb(c);Fb(b,c);try{(a.head||a.body||a.documentElement).appendChild(b),O.Ja()}catch(g){}},c=N[1];
b(c);".google.com"!=c&&b(".google.com");b={};var d=(b.newToken="FBT",b);p.setTimeout(function(){return p.processGoogleToken(d,1)},1E3)}}};
function Jd(a){Hd();var b=Dd.googleToken[5]||0;a&&(0!=b||M[3]>=z()?O.ha(a):(O.ja().push(a),O.fa()));M[3]>=z()&&M[2]>=z()||O.fa()}
function Kd(a){p.processGoogleToken=p.processGoogleToken||function(a,c){var b=a,e=c;b=void 0===b?{}:b;e=void 0===e?0:e;var f=b.newToken||"",g=parseInt(b.freshLifetimeSecs||"",10)||3600,h=parseInt(b.validLifetimeSecs||"",10)||86400,k=b["1p_jar"]||"";b=b.pucrd||"";Hd();1==e?O.La():O.Ka();if(!f&&O.shouldRetry())Cd(".google.com")&&(N[1]=".google.com"),O.fa();else{var m=Dd.googleToken=Dd.googleToken||{},u=0==e&&f&&r(f)&&0<g&&0<h&&r(k),P=!(M[3]>=z())&&0!=e;if(u||P)u=z(),g=u+1E3*g,h=u+1E3*h,1E-5>Math.random()&&
(u="https://pagead2.googlesyndication.com/pagead/gen_204?id=imerr&err="+e,p.google_image_requests||(p.google_image_requests=[]),P=p.document.createElement("img"),P.src=u,p.google_image_requests.push(P)),m[5]=e,m[1]=f,m[2]=g,m[3]=h,m[4]=k,m[6]=b,Hd();if(f||!O.ka()){e=O.ja();for(f=0;f<e.length;f++)O.ha(e[f]);e.length=0}}};
Jd(a)}
;function Ld(a,b){if(1<b.length)a[b[0]]=b[1];else{var c=b[0],d;for(d in c)a[d]=c[d]}}
var Md=window.performance&&window.performance.timing&&window.performance.now?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};var Nd=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};t("yt.config_",Nd,void 0);function Q(a){Ld(Nd,arguments)}
function R(a,b){return a in Nd?Nd[a]:b}
function Od(a){return R(a,void 0)}
function Pd(){return R("PLAYER_CONFIG",{})}
;function Qd(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){S(b)}}:a}
function S(a,b){var c=v("yt.logging.errors.log");c?c(a,b,void 0,void 0,void 0):(c=R("ERRORS",[]),c.push([a,b,void 0,void 0,void 0]),Q("ERRORS",c))}
;function T(a){return R("EXPERIMENT_FLAGS",{})[a]}
;function Rd(a){a&&(a.dataset?a.dataset[Sd("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Td(a,b){return a?a.dataset?a.dataset[Sd(b)]:a.getAttribute("data-"+b):null}
var Ud={};function Sd(a){return Ud[a]||(Ud[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function U(a,b){sa(a)&&(a=Qd(a));return window.setTimeout(a,b)}
function Vd(a){window.clearTimeout(a)}
;var Wd=v("ytPubsubPubsubInstance")||new K;K.prototype.subscribe=K.prototype.subscribe;K.prototype.unsubscribeByKey=K.prototype.D;K.prototype.publish=K.prototype.G;K.prototype.clear=K.prototype.clear;t("ytPubsubPubsubInstance",Wd,void 0);var Xd=v("ytPubsubPubsubSubscribedKeys")||{};t("ytPubsubPubsubSubscribedKeys",Xd,void 0);var Yd=v("ytPubsubPubsubTopicToKeys")||{};t("ytPubsubPubsubTopicToKeys",Yd,void 0);var Zd=v("ytPubsubPubsubIsSynchronous")||{};t("ytPubsubPubsubIsSynchronous",Zd,void 0);
function $d(a,b){var c=ae();if(c){var d=c.subscribe(a,function(){var c=arguments;var f=function(){Xd[d]&&b.apply(window,c)};
try{Zd[a]?f():U(f,0)}catch(g){S(g)}},void 0);
Xd[d]=!0;Yd[a]||(Yd[a]=[]);Yd[a].push(d);return d}return 0}
function be(a){var b=ae();b&&("number"==typeof a?a=[a]:r(a)&&(a=[parseInt(a,10)]),C(a,function(a){b.unsubscribeByKey(a);delete Xd[a]}))}
function ce(a,b){var c=ae();c&&c.publish.apply(c,arguments)}
function de(a){var b=ae();if(b)if(b.clear(a),a)ee(a);else for(var c in Yd)ee(c)}
function ae(){return v("ytPubsubPubsubInstance")}
function ee(a){Yd[a]&&(a=Yd[a],C(a,function(a){Xd[a]&&delete Xd[a]}),a.length=0)}
;var fe=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,ge=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function he(a,b){if(window.spf){var c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(fe,""),c=c.replace(ge,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else ie(a,b)}
function ie(a,b){var c=je(a),d=document.getElementById(c),e=d&&Td(d,"loaded"),f=d&&!e;if(e)b&&b();else{if(b){e=$d(c,b);var g=""+(b[ua]||(b[ua]=++va));ke[g]=e}f||(d=le(a,c,function(){Td(d,"loaded")||(Rd(d),ce(c),U(y(de,c),0))}))}}
function le(a,b,c){var d=document.createElement("SCRIPT");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
d.onreadystatechange=function(){switch(d.readyState){case "loaded":case "complete":d.onload()}};
Fb(d,Nb(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(d,a.firstChild);return d}
function me(a){a=je(a);var b=document.getElementById(a);b&&(de(a),b.parentNode.removeChild(b))}
function ne(a,b){if(a&&b){var c=""+(b[ua]||(b[ua]=++va));(c=ke[c])&&be(c)}}
function je(a){var b=document.createElement("a");Db(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Ka(a)}
var ke={};var oe=null;function pe(){var a=R("BG_I",null),b=R("BG_IU",null),c=R("BG_P",void 0);b?he(b,function(){window.botguard?qe(c):(me(b),S(Error("Unable to load Botguard from "+b),"WARNING"))}):a&&(eval(a),window.botguard?qe(c):S(Error("Unable to load Botguard from JS"),"WARNING"))}
function qe(a){oe=new window.botguard.bg(a);T("botguard_periodic_refresh")&&Md()}
function re(){return null!=oe}
function se(){return oe?oe.invoke():null}
;z();var te=q(XMLHttpRequest)?function(){return new XMLHttpRequest}:q(ActiveXObject)?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function ue(){if(!te)return null;var a=te();return"open"in a?a:null}
function ve(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function we(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," "));e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?w(b[f])?Ra(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
;var xe={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},ye=!1;
function ze(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=L(a)[1]||null,e=qd(L(a)[3]||null);d&&e?(d=c,c=L(a),d=L(d),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?qd(L(c)[3]||null)==e&&(Number(L(c)[4]||null)||null)==(Number(L(a)[4]||null)||null):!0;for(var f in xe){if((e=d=R(xe[f]))&&!(e=c)){e=f;var g=R("CORS_HEADER_WHITELIST")||{},h=qd(L(a)[3]||null);e=h?(g=g[h])?0<=La(g,e):!1:!0}e&&(b[f]=d)}return b}
function Ae(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=Be(a,b);var d=Ce(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(a){if(!e){e=!0;f&&Vd(f);var c=a.ok,d=function(d){d=d||{};var e=b.context||p;c?b.C&&b.C.call(e,d,a):b.onError&&b.onError.call(e,d,a);b.ea&&b.ea.call(e,d,a)};
"JSON"==(b.format||"JSON")&&(c||400<=a.status&&500>a.status)?a.json().then(d,function(){d(null)}):d(null)}});
b.la&&0<b.timeout&&(f=U(function(){e||(e=!0,Vd(f),b.la.call(b.context||p))},b.timeout))}else De(a,b)}
function De(a,b){var c=b.format||"JSON";a=Be(a,b);var d=Ce(a,b),e=!1,f,g=Ee(a,function(a){if(!e){e=!0;f&&Vd(f);var d=ve(a),g=null;if(d||400<=a.status&&500>a.status)g=Fe(c,a,b.Wa);if(d)a:if(a&&204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(g&&g.return_code,10);break a;case "RAW":d=!0;break a}d=!!g}g=g||{};var h=b.context||p;d?b.C&&b.C.call(h,a,g):b.onError&&b.onError.call(h,a,g);b.ea&&b.ea.call(h,a,g)}},b.method,d,b.headers,b.responseType,b.withCredentials);
b.K&&0<b.timeout&&(f=U(function(){e||(e=!0,g.abort(),Vd(f),b.K.call(b.context||p,g))},b.timeout))}
function Be(a,b){b.za&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=R("XSRF_FIELD_NAME",void 0),d=b.Ua;if(d){d[c]&&delete d[c];d=d||{};var e=a.split("#",2);c=e[0];e=1<e.length?"#"+e[1]:"";var f=c.split("?",2);c=f[0];f=we(f[1]||"");for(var g in d)f[g]=d[g];a=td(c,f)+e}return a}
function Ce(a,b){var c=R("XSRF_FIELD_NAME",void 0),d=R("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.w,g=Od("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.Xa||qd(L(a)[3]||null)&&!b.withCredentials&&qd(L(a)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.w&&b.w[g]||(f||(f={}),f[c]=d);f&&r(e)&&(e=we(e),cb(e,f),e=b.ma&&"JSON"==b.ma?JSON.stringify(e):sd(e));f=e||f&&!Za(f);!ye&&f&&"POST"!=b.method&&(ye=!0,S(Error("AJAX request with postData should use POST")));
return e}
function Fe(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Ge(b):null)d={},C(b.getElementsByTagName("*"),function(a){d[a.tagName]=He(a)})}c&&Ie(d);
return d}
function Ie(a){if(ta(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Cb(a[b]);a[c]=d}else Ie(a[b])}}
function Ge(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function He(a){var b="";C(a.childNodes,function(a){b+=a.nodeValue});
return b}
function Je(a,b){b.method="POST";b.w||(b.w={});De(a,b)}
function Ee(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&Qd(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=ue();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c;if(e=ze(a,e))for(var m in e)k.setRequestHeader(m,e[m]),"content-type"==m.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);return k}
;var Ke={},Le=0;function Me(a,b,c,d,e){e=void 0===e?"":e;a&&(c&&(c=Sa,c=!(c&&0<=c.toLowerCase().indexOf("cobalt"))),c?a&&(a=Kb("IFRAME",{src:'javascript:"data:text/html,<body><img src=\\"'+a+'\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a)):e?Ee(a,b,"POST",e,d):R("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d?Ee(a,b,"GET","",d):Ne(a,b))}
function Ne(a,b){var c=new Image,d=""+Le++;Ke[d]=c;c.onload=c.onerror=function(){b&&Ke[d]&&b();delete Ke[d]};
c.src=a}
;var Oe={},Pe=0;
function Qe(a,b,c,d,e,f){f=f||{};f.name=c||R("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||R("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);b=void 0===b?"ERROR":b;e=void 0===e?!1:e;e=window&&window.yterr||(void 0===e?!1:e)||!1;if(a&&e&&!(5<=Pe)){e=a.stacktrace;c=a.columnNumber;d=v("window.location.href");if(r(a))a={message:a,name:"Unknown error",lineNumber:"Not available",fileName:d,stack:"Not available"};else{var g=!1;try{var h=a.lineNumber||a.line||"Not available"}catch(P){h="Not available",g=!0}try{var k=
a.fileName||a.filename||a.sourceURL||p.$googDebugFname||d}catch(P){k="Not available",g=!0}a=!g&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:{message:a.message||"Not available",name:a.name||"UnknownError",lineNumber:h,fileName:k,stack:a.stack||"Not available"}}e=e||a.stack;h=a.lineNumber.toString();isNaN(h)||isNaN(c)||(h=h+":"+c);if(!(Oe[a.message]||0<=e.indexOf("/YouTubeCenter.js")||0<=e.indexOf("/mytube.js"))){k=e;h={Ua:{a:"logerror",t:"jserror",type:a.name,msg:a.message.substr(0,1E3),
line:h,level:void 0===b?"ERROR":b,"client.name":f.name},w:{url:R("PAGE_NAME",window.location.href),file:a.fileName},method:"POST"};f.version&&(h["client.version"]=f.version);k&&(h.w.stack=k);for(var m in f)h.w["client."+m]=f[m];if(m=R("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(var u in m)h.w[u]=m[u];De("/error_204",h);Oe[a.message]=!0;Pe++}}}
;var Re=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};t("yt.msgs_",Re,void 0);function Se(a){Ld(Re,arguments)}
;function Te(a,b){var c=5E3;isNaN(c)&&(c=void 0);var d=v("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):U(a,c||0)}
function Ue(a){if(!isNaN(a)){var b=v("yt.scheduler.instance.cancelJob");b?b(a):Vd(a)}}
;var Ve=[],We=!1;function Xe(){if("1"!=Wa(Pd(),"args","privembed")||!T("do_not_set_cookies_for_ads_on_youtube_nocookie")){var a=function(){We=!0;"google_ad_status"in window?Q("DCLKSTAT",1):Q("DCLKSTAT",2)};
he("//static.doubleclick.net/instream/ad_status.js",a);Ve.push(Te(function(){We||"google_ad_status"in window||(ne("//static.doubleclick.net/instream/ad_status.js",a),Q("DCLKSTAT",3))},1))}}
function Ye(){return parseInt(R("DCLKSTAT",0),10)}
;var Ze=0;t("ytDomDomGetNextId",v("ytDomDomGetNextId")||function(){return++Ze},void 0);var $e={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function af(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.event=a;for(var b in a)b in $e||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?b=a.fromElement:
"mouseout"==this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey}}
af.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
af.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
af.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var Ya=v("ytEventsEventsListeners")||{};t("ytEventsEventsListeners",Ya,void 0);var bf=v("ytEventsEventsCounter")||{count:0};t("ytEventsEventsCounter",bf,void 0);function cf(a,b,c,d){d=void 0===d?!1:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Xa(function(e){return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&e[4]==!!d})}
function df(a,b,c){var d=void 0===d?!1:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=cf(a,b,c,d);if(e)return e;e=++bf.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(d){d=new af(d);if(!Mb(d.relatedTarget,function(b){return b==a}))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new af(b);
b.currentTarget=a;return c.call(a,b)};
g=Qd(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),a.addEventListener(b,g,d)):a.attachEvent("on"+b,g);Ya[e]=[a,b,c,g,d];return e}
function ef(a){a&&("string"==typeof a&&(a=[a]),C(a,function(a){if(a in Ya){var b=Ya[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?d.removeEventListener(e,f,b):d.detachEvent&&d.detachEvent("on"+e,f);delete Ya[a]}}))}
;function ff(){if(null==v("_lact",window)){var a=parseInt(R("LACT"),10);a=isFinite(a)?z()-Math.max(a,0):-1;t("_lact",a,window);t("_fact",a,window);-1==a&&gf();df(document,"keydown",gf);df(document,"keyup",gf);df(document,"mousedown",gf);df(document,"mouseup",gf);$d("page-mouse",gf);$d("page-scroll",gf);$d("page-resize",gf)}}
function gf(){null==v("_lact",window)&&ff();var a=z();t("_lact",a,window);-1==v("_fact",window)&&t("_fact",a,window);(a=v("ytglobal.ytUtilActivityCallback_"))&&a()}
function hf(){var a=v("_lact",window);return null==a?-1:Math.max(z()-a,0)}
;function jf(a,b,c,d,e){this.f=a;this.i=b;this.h=c;this.g=d;this.b=e}
function kf(a){var b={};void 0!==a.f?b.trackingParams=a.f:(b.veType=a.i,null!=a.h&&(b.veCounter=a.h),null!=a.g&&(b.elementIndex=a.g));void 0!==a.b&&(b.dataElement=kf(a.b));return b}
var lf=1;function mf(){if(!nf&&!of||!window.JSON)return null;try{var a=nf.get("yt-player-two-stage-token")}catch(b){}if(!r(a))try{a=of.get("yt-player-two-stage-token")}catch(b){}if(!r(a))return null;try{a=JSON.parse(a,void 0)}catch(b){}return a}
var of,pf=new ld;of=pf.isAvailable()?new hd(pf):null;var nf,qf=new md;nf=qf.isAvailable()?new hd(qf):null;function rf(){var a=R("ROOT_VE_TYPE",void 0);return a?new jf(void 0,a,void 0):null}
function sf(){var a=R("client-screen-nonce")||R("EVENT_ID");return a?a:null}
;function tf(a,b,c){Xb.set(""+a,b,c,"/","youtube.com",!1)}
;function uf(a){if(a){a=a.itct||a.ved;var b=v("yt.logging.screen.storeParentElement");a&&b&&b(new jf(a))}}
;function vf(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=R("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=R("VALID_SESSION_TEMPDATA_DOMAINS",[]),f=qd(L(window.location.href)[3]||null);f&&e.push(f);f=qd(L(d)[3]||null);if(0<=La(e,f)||!f&&0==d.lastIndexOf("/",0))if(T("autoescape_tempdata_url")&&(e=document.createElement("a"),Db(e,d),d=e.href),d){f=L(d);d=f[5];e=f[6];f=f[7];var g="";d&&(g+=d);e&&(g+="?"+e);f&&(g+="#"+f);d=g;e=d.indexOf("#");if(d=0>e?d:d.substr(0,e)){if(b.itct||b.ved)b.csn=b.csn||
sf();if(h){var h=parseInt(h,10);isFinite(h)&&0<h&&(d="ST-"+Ka(d).toString(36),e=b?sd(b):"",tf(d,e,h||5),uf(b))}else h="ST-"+Ka(d).toString(36),d=b?sd(b):"",tf(h,d,5),uf(b)}}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var k=void 0===k?{}:k;var m=void 0===m?"":m;var u=void 0===u?window:u;c=u.location;a=td(a,k)+m;a=a instanceof G?a:zb(a);c.href=xb(a)}return!0}
;t("yt.abuse.botguardInitialized",v("yt.abuse.botguardInitialized")||re,void 0);t("yt.abuse.invokeBotguard",v("yt.abuse.invokeBotguard")||se,void 0);t("yt.abuse.dclkstatus.checkDclkStatus",v("yt.abuse.dclkstatus.checkDclkStatus")||Ye,void 0);t("yt.player.exports.navigate",v("yt.player.exports.navigate")||vf,void 0);t("yt.util.activity.init",v("yt.util.activity.init")||ff,void 0);t("yt.util.activity.getTimeSinceActive",v("yt.util.activity.getTimeSinceActive")||hf,void 0);
t("yt.util.activity.setTimestamp",v("yt.util.activity.setTimestamp")||gf,void 0);var wf={log_event:"events",log_interaction:"interactions"},xf=Object.create(null);xf.log_event="GENERIC_EVENT_LOGGING";xf.log_interaction="INTERACTION_LOGGING";var yf={},zf={},Af=0,V=v("ytLoggingTransportLogPayloadsQueue_")||{};t("ytLoggingTransportLogPayloadsQueue_",V,void 0);var Bf=v("ytLoggingTransportTokensToCttTargetIds_")||{};t("ytLoggingTransportTokensToCttTargetIds_",Bf,void 0);var Cf=v("ytLoggingTransportDispatchedStats_")||{};t("ytLoggingTransportDispatchedStats_",Cf,void 0);
t("ytytLoggingTransportCapturedTime_",v("ytLoggingTransportCapturedTime_")||{},void 0);function Df(a,b){zf[a.endpoint]=b;if(a.V){var c=a.V;var d={};c.videoId?d.videoId=c.videoId:c.playlistId&&(d.playlistId=c.playlistId);Bf[a.V.token]=d;c=Ef(a.endpoint,a.V.token)}else c=Ef(a.endpoint);c.push(a.payload);c.length>=(Number(T("web_logging_max_batch")||0)||20)?Ff():Gf()}
function Ff(){Vd(Af);if(!Za(V)){for(var a in V){var b=yf[a];if(!b){var c=zf[a];if(!c)continue;b=new c;yf[a]=b}c=void 0;var d=a,e=b,f=wf[d],g=Cf[d]||{};Cf[d]=g;b=Math.round(Md());for(c in V[d]){var h=e.b;h={client:{hl:h.Ca,gl:h.Ba,clientName:h.Aa,clientVersion:h.innertubeContextClientVersion}};R("DELEGATED_SESSION_ID")&&(h.user={onBehalfOfUser:R("DELEGATED_SESSION_ID")});h={context:h};h[f]=Ef(d,c);g.dispatchedEventCount=g.dispatchedEventCount||0;g.dispatchedEventCount+=h[f].length;h.requestTimeMs=
b;var k=Bf[c];if(k)a:{var m=h,u=c;if(k.videoId)var P="VIDEO";else if(k.playlistId)P="PLAYLIST";else break a;m.credentialTransferTokenTargetId=k;m.context=m.context||{};m.context.user=m.context.user||{};m.context.user.credentialTransferTokens=[{token:u,scope:P}]}delete Bf[c];Hf(e,d,h)}c=g;d=b;c.previousDispatchMs&&(b=d-c.previousDispatchMs,e=c.diffCount||0,c.averageTimeBetweenDispatchesMs=e?(c.averageTimeBetweenDispatchesMs*e+b)/(e+1):b,c.diffCount=e+1);c.previousDispatchMs=d;delete V[a]}Za(V)||Gf()}}
function Gf(){Vd(Af);Af=U(Ff,R("LOGGING_BATCH_TIMEOUT",1E4))}
function Ef(a,b){b||(b="");V[a]=V[a]||{};V[a][b]=V[a][b]||[];return V[a][b]}
;function If(a,b,c,d,e){var f={};f.eventTimeMs=Math.round(d||Md());f[a]=b;f.context={lastActivityMs:String(d?-1:hf())};Df({endpoint:"log_event",payload:f,V:e},c)}
;function Jf(a,b,c){c.context&&c.context.capabilities&&(c=c.context.capabilities,c.snapshot||c.golden)&&(a="vix");return"/youtubei/"+a+"/"+b}
;function Kf(a){this.b=a||{innertubeApiKey:Od("INNERTUBE_API_KEY"),innertubeApiVersion:Od("INNERTUBE_API_VERSION"),Aa:R("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:Od("INNERTUBE_CONTEXT_CLIENT_VERSION"),Ca:Od("INNERTUBE_CONTEXT_HL"),Ba:Od("INNERTUBE_CONTEXT_GL"),Da:Od("INNERTUBE_HOST_OVERRIDE")||""}}
function Hf(a,b,c){var d={};!R("VISITOR_DATA")&&.01>Math.random()&&S(Error("Missing VISITOR_DATA when sending innertube request."),"WARNING");var e={headers:{"Content-Type":"application/json","X-Goog-Visitor-Id":R("VISITOR_DATA","")},method:"POST",w:c,ma:"JSON",K:function(){d.K()},
la:d.K,C:function(a,b){d.C&&d.C(b)},
Za:function(a){d.C&&d.C(a)},
onError:function(a,b){if(d.onError)d.onError(b)},
Ya:function(a){if(d.onError)d.onError(a)},
timeout:d.timeout,withCredentials:!0},f=Yb();f&&(e.headers.Authorization=f,e.headers["X-Goog-AuthUser"]=R("SESSION_INDEX",0));var g="",h=a.b.Da;h&&(g=h);f&&!g&&(e.headers["x-origin"]=window.location.origin);a=""+g+Jf(a.b.innertubeApiVersion,b,c)+"?alt=json&key="+a.b.innertubeApiKey;T("use_fetch_for_op_xhr")?Ae(a,e):Je(a,e)}
;function Lf(a,b,c){Mf(Kf,{attachChild:{csn:a,parentVisualElement:kf(b),visualElements:[kf(c)]}})}
function Mf(a,b,c){b.eventTimeMs=c?c:Math.round(Md());b.lactMs=hf();Df({endpoint:"log_interaction",payload:b},a)}
;function Nf(a){a=a||{};this.url=a.url||"";this.args=a.args||ab(Of);this.assets=a.assets||{};this.attrs=a.attrs||ab(Pf);this.params=a.params||ab(Qf);this.minVersion=a.min_version||"8.0.0";this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
var Of={enablejsapi:1},Pf={},Qf={allowscriptaccess:"always",allowfullscreen:"true",bgcolor:"#000000"};function Rf(a){a instanceof Nf||(a=new Nf(a));return a}
function Sf(a){var b=new Nf,c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];b[c]="object"==qa(d)?ab(d):d}return b}
;function Tf(){I.call(this);this.b=[]}
n(Tf,I);Tf.prototype.l=function(){for(;this.b.length;){var a=this.b.pop();a.target.removeEventListener(a.name,a.Va)}I.prototype.l.call(this)};var Uf=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function Vf(a){a=a||"";if(window.spf){var b=a.match(Uf);spf.style.load(a,b?b[1]:"",void 0)}else Wf(a)}
function Wf(a){var b=Xf(a),c=document.getElementById(b),d=c&&Td(c,"loaded");d||c&&!d||(c=Yf(a,b,function(){Td(c,"loaded")||(Rd(c),ce(b),U(y(de,b),0))}))}
function Yf(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Nb(a);Eb(d,a,"stylesheet");(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function Xf(a){var b=document.createElement("A");a=Ab(a);Db(b,a);b=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Ka(b)}
;var Zf={cupcake:1.5,donut:1.6,eclair:2,froyo:2.2,gingerbread:2.3,honeycomb:3,"ice cream sandwich":4,jellybean:4.1,kitkat:4.4,lollipop:5.1,marshmallow:6,nougat:7.1},$f;var ag=Sa;ag=ag.toLowerCase();if(-1!=ag.indexOf("android")){var bg=ag.match(/android\D*(\d\.\d)[^;|\)]*[;\)]/);if(bg)$f=parseFloat(bg[1]);else{var cg=[],dg=0,eg;for(eg in Zf)cg[dg++]=eg;var fg=ag.match("("+cg.join("|")+")");$f=fg?Zf[fg[0]]:0}}else $f=void 0;var gg=['video/mp4; codecs="avc1.42001E, mp4a.40.2"','video/webm; codecs="vp8.0, vorbis"'],hg=['audio/mp4; codecs="mp4a.40.2"'];var ig=v("ytLoggingLatencyUsageStats_")||{};t("ytLoggingLatencyUsageStats_",ig,void 0);var jg=0;function kg(a){ig[a]=ig[a]||{count:0};var b=ig[a];b.count++;b.time=Md();jg||(jg=Te(lg,0));return 10<b.count?(11==b.count&&Qe(Error("CSI data exceeded logging limit with key: "+a),0==a.indexOf("info")?"WARNING":"ERROR"),!0):!1}
function lg(){var a=Md(),b;for(b in ig)6E4<a-ig[b].time&&delete ig[b];jg=0}
;function mg(a,b){this.version=a;this.args=b}
;function ng(a){this.topic=a}
ng.prototype.toString=function(){return this.topic};var og=v("ytPubsub2Pubsub2Instance")||new K;K.prototype.subscribe=K.prototype.subscribe;K.prototype.unsubscribeByKey=K.prototype.D;K.prototype.publish=K.prototype.G;K.prototype.clear=K.prototype.clear;t("ytPubsub2Pubsub2Instance",og,void 0);t("ytPubsub2Pubsub2SubscribedKeys",v("ytPubsub2Pubsub2SubscribedKeys")||{},void 0);t("ytPubsub2Pubsub2TopicToKeys",v("ytPubsub2Pubsub2TopicToKeys")||{},void 0);t("ytPubsub2Pubsub2IsAsync",v("ytPubsub2Pubsub2IsAsync")||{},void 0);
t("ytPubsub2Pubsub2SkipSubKey",null,void 0);function pg(a,b){var c=v("ytPubsub2Pubsub2Instance");c&&c.publish.call(c,a.toString(),a,b)}
;var W=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{};function qg(){var a=R("TIMING_TICK_EXPIRATION");a||(a={},Q("TIMING_TICK_EXPIRATION",a));return a}
function rg(){var a=qg(),b;for(b in a)Ue(a[b]);Q("TIMING_TICK_EXPIRATION",{})}
;function sg(a,b){mg.call(this,1,arguments)}
n(sg,mg);function tg(a,b){mg.call(this,1,arguments)}
n(tg,mg);var xg=new ng("aft-recorded"),yg=new ng("timing-sent");var zg=z().toString();var Ag={vc:!0},Bg={ad_allowed:"adTypesAllowed",ad_at:"adType",ad_cpn:"adClientPlaybackNonce",ad_docid:"adVideoId",yt_ad_an:"adNetworks",p:"httpProtocol",t:"transportProtocol",cpn:"clientPlaybackNonce",csn:"clientScreenNonce",docid:"videoId",is_nav:"isNavigation",yt_lt:"loadType",yt_ad:"isMonetized",nr:"webInfo.navigationReason",ncnp:"webInfo.nonPreloadedNodeCount",paused:"playerInfo.isPausedOnLoad",fmt:"playerInfo.itag",yt_pl:"watchInfo.isPlaylist",yt_ad_pr:"prerollAllowed",yt_red:"isRedSubscriber",
st:"serverTimeMs",vph:"viewportHeight",vpw:"viewportWidth",yt_vis:"isVisible"},Cg="ap c cver ei srt yt_fss yt_li ba plid vpil vpni vpst yt_eil vpni2 vpil2 icrc icrt pa GetBrowse_rid GetPlayer_rid GetSearch_rid GetWatchNext_rid cmt pc prerender psc rc start yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis yt_ref yt_sts".split(" "),Dg="isNavigation isMonetized playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber isVisible watchInfo.isPlaylist".split(" "),Eg=!1;
function Fg(a){if("_"!=a[0]){var b=a;W.mark&&(0==b.lastIndexOf("mark_",0)||(b="mark_"+b),W.mark(b))}b=Gg();var c=Md();b[a]&&(b["_"+a]=b["_"+a]||[b[a]],b["_"+a].push(c));b[a]=c;b=qg();if(c=b[a])Ue(c),b[a]=0;Hg()["tick_"+a]=void 0;Md();T("csi_on_gel")?(b=Ig(),"_start"==a?kg("baseline_"+b)||If("latencyActionBaselined",{clientActionNonce:b},Kf,void 0,void 0):kg("tick_"+a+"_"+b)||If("latencyActionTicked",{tickName:a,clientActionNonce:b},Kf,void 0,void 0),a=!0):a=!1;if(a=!a)a=!v("yt.timing.pingSent_");
if(a&&(b=Od("TIMING_ACTION"),a=Gg(),v("ytglobal.timingready_")&&b&&a._start&&(b=Jg()))){T("tighter_critical_section")&&!Eg&&(pg(xg,new sg(Math.round(b-a._start),void 0)),Eg=!0);b=!0;c=R("TIMING_WAIT",[]);if(c.length)for(var d=0,e=c.length;d<e;++d)if(!(c[d]in a)){b=!1;break}b&&Kg()}}
function Lg(){var a=Mg().info.yt_lt="hot_bg";Hg().info_yt_lt=a;if(T("csi_on_gel"))if("yt_lt"in Bg){var b={},c=Bg.yt_lt;0<=La(Dg,c)&&(a=!!a);c=c.split(".");for(var d=b,e=0;e<c.length-1;e++)d[c[e]]=d[c[e]]||{},d=d[c[e]];b[c[c.length-1]]=a;a=Ig();c=Object.keys(b).join("");kg("info_"+c+"_"+a)||(b.clientActionNonce=a,If("latencyActionInfo",b,Kf,void 0,void 0))}else 0<=La(Cg,"yt_lt")||S(Error("Unknown label yt_lt logged with GEL CSI."))}
function Jg(){var a=Gg();if(a.aft)return a.aft;for(var b=R("TIMING_AFT_KEYS",["ol"]),c=b.length,d=0;d<c;d++){var e=a[b[d]];if(e)return e}return NaN}
function Kg(){rg();if(!T("csi_on_gel")){var a=Gg(),b=Mg().info,c=a._start,d;for(d in a)if(0==d.lastIndexOf("_",0)&&w(a[d])){var e=d.slice(1);if(e in Ag){var f=Na(a[d],function(a){return Math.round(a-c)});
b["all_"+e]=f.join()}delete a[d]}e=!!b.ap;if(f=v("ytglobal.timingReportbuilder_")){if(f=f(a,b,void 0))Ng(f,e),Og(),Pg(),Qg(!1,void 0),R("TIMING_ACTION")&&Q("PREVIOUS_ACTION",R("TIMING_ACTION")),Q("TIMING_ACTION","")}else{var g=R("CSI_SERVICE_NAME","youtube");f={v:2,s:g,action:R("TIMING_ACTION",void 0)};var h=b.srt;void 0!==a.srt&&delete b.srt;if(b.h5jse){var k=window.location.protocol+v("ytplayer.config.assets.js");(k=W.getEntriesByName?W.getEntriesByName(k)[0]:null)?b.h5jse=Math.round(b.h5jse-k.responseEnd):
delete b.h5jse}a.aft=Jg();Rg()&&"youtube"==g&&(Lg(),g=a.vc,k=a.pbs,delete a.aft,b.aft=Math.round(k-g));for(var m in b)"_"!=m.charAt(0)&&(f[m]=b[m]);a.ps=Md();b={};m=[];for(d in a)"_"!=d.charAt(0)&&(g=Math.round(a[d]-c),b[d]=g,m.push(d+"."+g));f.rt=m.join(",");(a=v("ytdebug.logTiming"))&&a(f,b);Ng(f,e,void 0);pg(yg,new tg(b.aft+(h||0),void 0))}}}
var Pg=x(W.clearResourceTimings||W.webkitClearResourceTimings||W.mozClearResourceTimings||W.msClearResourceTimings||W.oClearResourceTimings||pa,W);
function Ng(a,b,c){if(T("debug_csi_data")){var d=v("yt.timing.csiData");d||(d=[],t("yt.timing.csiData",d,void 0));d.push({page:location.href,time:new Date,args:a})}d="";for(var e in a)d+="&"+e+"="+a[e];a="/csi_204?"+d.substring(1);if(window.navigator&&window.navigator.sendBeacon&&b){var f=void 0===f?"":f;try{window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,f)||Me(a,void 0,void 0,void 0,f)}catch(g){Me(a,void 0,void 0,void 0,f)}}else Me(a);Qg(!0,c)}
function Ig(){var a=Mg().nonce;if(!a){a:{if(window.crypto&&window.crypto.getRandomValues)try{var b=Array(16),c=new Uint8Array(16);window.crypto.getRandomValues(c);for(a=0;a<b.length;a++)b[a]=c[a];var d=b;break a}catch(e){}d=Array(16);for(b=0;16>b;b++){c=z();for(a=0;a<c%23;a++)d[b]=Math.random();d[b]=Math.floor(256*Math.random())}if(zg)for(b=1,c=0;c<zg.length;c++)d[b%16]=d[b%16]^d[(b-1)%16]/4^zg.charCodeAt(c),b++}b=[];for(c=0;c<d.length;c++)b.push("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_".charAt(d[c]&
63));a=b.join("");Mg().nonce=a}return a}
function Gg(){return Mg().tick}
function Hg(){var a=Mg();"gel"in a||(a.gel={});return a.gel}
function Mg(){return v("ytcsi.data_")||Og()}
function Og(){var a={tick:{},info:{}};t("ytcsi.data_",a,void 0);return a}
function Qg(a,b){t("yt.timing."+(b||"")+"pingSent_",a,void 0)}
function Rg(){var a=Gg(),b=a.pbr,c=a.vc;a=a.pbs;return b&&c&&a&&b<c&&c<a&&1==Mg().info.yt_pvis}
;function Sg(a,b){I.call(this);this.m=this.R=a;this.I=b;this.u=!1;this.f={};this.O=this.H=null;this.A=new K;mc(this,y(nc,this.A));this.i={};this.M=this.P=this.h=this.Z=this.b=null;this.L=!1;this.j=this.F=null;this.S={};this.qa=["onReady"];this.Y=null;this.ga=NaN;this.N={};Tg(this);this.U("WATCH_LATER_VIDEO_ADDED",x(this.Fa,this));this.U("WATCH_LATER_VIDEO_REMOVED",x(this.Ga,this));this.U("onAdAnnounce",x(this.ta,this));this.ra=new Tf;mc(this,y(nc,this.ra))}
n(Sg,I);l=Sg.prototype;
l.da=function(a,b){if(!this.g){this.Z=a;this.b=Sf(a);this.h=this.b.attrs.id||this.h;"video-player"==this.h&&(this.h=this.I,this.b.attrs.id=this.I);this.m.id==this.h&&(this.h+="-player",this.b.attrs.id=this.h);this.b.args.enablejsapi="1";this.b.args.playerapiid=this.I;this.P||(this.P=Ug(this,this.b.args.jsapicallback||"onYouTubePlayerReady"));this.b.args.jsapicallback=null;var c=this.b.attrs.width;c&&(this.m.style.width=Qb(Number(c)||c));if(c=this.b.attrs.height)this.m.style.height=Qb(Number(c)||c);
if(!this.g){if(!b&&!q(this.b.disable.html5)){c=!0;void 0!=this.b.args.deviceHasDisplay&&(c=this.b.args.deviceHasDisplay);if(2.2==$f)var d=!0;else{a:try{var e=v("yt.player.utils.videoElement_");e||(e=document.createElement("VIDEO"),t("yt.player.utils.videoElement_",e,void 0));var f=e;if(f.canPlayType)for(e=c?gg:hg,c=0;c<e.length;c++)if(f.canPlayType(e[c])){d=null;break a}d="fmt.noneavailable"}catch(g){d="html5.missingapi"}d=!d}d=d&&(Vg(this)||this.b.assets.js);this.b.disable.html5=!d;d||(this.b.args.html5_unavailable=
"1")}Wg(this)}this.u&&Xg(this)}};
l.wa=function(){return this.Z};
function Xg(a){a.b.loaded||(a.b.loaded=!0,"0"!=a.b.args.autoplay?a.f.loadVideoByPlayerVars(a.b.args):a.f.cueVideoByPlayerVars(a.b.args))}
function Vg(a){var b=!0,c=Yg(a);c&&a.b&&(a=a.b,b=Td(c,"version")==a.assets.js);return b&&!!v("yt.player.Application.create")}
function Wg(a){if(!a.L){var b=Vg(a);if(b&&"html5"==(Yg(a)?"html5":null))a.M="html5",a.u||a.X();else if(Zg(a),a.M="html5",b&&a.j)a.R.appendChild(a.j),a.X();else{a.b.loaded=!0;var c=!1;a.F=x(function(){c=!0;var a=Sf(this.b);v("yt.player.Application.create")(this.R,a);this.X()},a);
a.L=!0;b?a.F():(he(a.b.assets.js,a.F),Vf(a.b.assets.css),$g(a)&&!c&&t("yt.player.Application.create",null,void 0))}}}
function Yg(a){var b=Hb(a.h);!b&&a.m&&a.m.querySelector&&(b=a.m.querySelector("#"+a.h));return b}
l.X=function(){if(!this.g){var a=Yg(this),b=!1;try{a&&a.getApiInterface&&a.getApiInterface()&&(b=!0)}catch(f){}if(b){if(this.L=!1,!a.isNotServable||!a.isNotServable(this.b.args.video_id)){Tg(this);this.u=!0;a=Yg(this);a.addEventListener&&(this.H=ah(this,a,"addEventListener"));a.removeEventListener&&(this.O=ah(this,a,"removeEventListener"));b=a.getApiInterface();b=b.concat(a.getInternalApiInterface());for(var c=0;c<b.length;c++){var d=b[c];this.f[d]||(this.f[d]=ah(this,a,d))}for(var e in this.i)this.H(e,
this.i[e]);Xg(this);this.P&&this.P(this.f);this.A.G("onReady",this.f)}}else this.ga=U(x(this.X,this),50)}};
function ah(a,b,c){var d=b[c];return function(){try{return a.Y=null,d.apply(b,arguments)}catch(e){"Bad NPObject as private data!"!=e.message&&"sendAbandonmentPing"!=c&&(e.message+=" ("+c+")",a.Y=e,S(e,"WARNING"))}}}
function Tg(a){a.u=!1;if(a.O)for(var b in a.i)a.O(b,a.i[b]);for(var c in a.N)Vd(parseInt(c,10));a.N={};a.H=null;a.O=null;for(var d in a.f)a.f[d]=null;a.f.addEventListener=x(a.U,a);a.f.removeEventListener=x(a.Ma,a);a.f.destroy=x(a.dispose,a);a.f.getLastError=x(a.xa,a);a.f.getPlayerType=x(a.ya,a);a.f.getCurrentVideoConfig=x(a.wa,a);a.f.loadNewVideoConfig=x(a.da,a);a.f.isReady=x(a.Ea,a)}
l.Ea=function(){return this.u};
l.U=function(a,b){if(!this.g){var c=Ug(this,b);if(c){if(!(0<=La(this.qa,a)||this.i[a])){var d=bh(this,a);this.H&&this.H(a,d)}this.A.subscribe(a,c);"onReady"==a&&this.u&&U(y(c,this.f),0)}}};
l.Ma=function(a,b){if(!this.g){var c=Ug(this,b);c&&ad(this.A,a,c)}};
function Ug(a,b){var c=b;if("string"==typeof b){if(a.S[b])return a.S[b];c=function(){var a=v(b);a&&a.apply(p,arguments)};
a.S[b]=c}return c?c:null}
function bh(a,b){var c="ytPlayer"+b+a.I,d=x(function(a){if("html5"==(Yg(this)?"html5":null)){var c=this.b&&this.b.args&&this.b.args.fflags;if(c&&0>c.indexOf("use_html5_player_event_timeout=true")){this.A.G(b,a);return}}var d=U(x(function(){if(!this.g){this.A.G(b,a);var c=this.N,e=String(d);e in c&&delete c[e]}},this),0);
$a(this.N,String(d))},a);
a.i[b]=c;p[c]=d;return c}
l.ta=function(a){ce("a11y-announce",a)};
l.Fa=function(a){ce("WATCH_LATER_VIDEO_ADDED",a)};
l.Ga=function(a){ce("WATCH_LATER_VIDEO_REMOVED",a)};
l.ya=function(){return this.M||(Yg(this)?"html5":null)};
l.xa=function(){return this.Y};
function Zg(a){Fg("dcp");a.cancel();Tg(a);a.M=null;a.b&&(a.b.loaded=!1);var b=Yg(a);"html5"==(Yg(a)?"html5":null)&&(Vg(a)||!$g(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));for(a=a.R;b=a.firstChild;)a.removeChild(b)}
l.cancel=function(){this.F&&ne(this.b.assets.js,this.F);Vd(this.ga);this.L=!1};
l.l=function(){Zg(this);if(this.j&&this.b&&this.j.destroy)try{this.j.destroy()}catch(b){S(b)}this.S=null;for(var a in this.i)p[this.i[a]]=null;this.Z=this.b=this.f=null;delete this.R;delete this.m;I.prototype.l.call(this)};
function $g(a){return a.b&&a.b.args&&a.b.args.fflags?-1!=a.b.args.fflags.indexOf("player_destroy_old_version=true"):!1}
;var ch={},dh="player_uid_"+(1E9*Math.random()>>>0);function eh(a){var b="player";b=r(b)?Hb(b):b;a=Rf(a);var c=dh+"_"+(b[ua]||(b[ua]=++va)),d=ch[c];if(d)return d.da(a),d.f;d=new Sg(b,c);ch[c]=d;ce("player-added",d.f);mc(d,y(fh,d));U(function(){d.da(a)},0);
return d.f}
function fh(a){delete ch[a.I]}
;function gh(a){return(0==a.search("cue")||0==a.search("load"))&&"loadModule"!=a}
function hh(a,b,c){r(a)&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});b=/\/([ve]|embed)\/([^#?]+)/.exec(a.mediaContentUrl);a.videoId=b&&b[2]?b[2]:null;return ih(a)}
function ih(a,b,c){if(ta(a)){b="endSeconds startSeconds mediaContentUrl suggestedQuality videoId two_stage_token".split(" ");c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}return{videoId:a,startSeconds:b,suggestedQuality:c}}
function jh(a,b,c,d){if(ta(a)&&!w(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};r(a)&&16==a.length?b.list="PL"+a:b.playlist=a;return b}
function kh(a){var b=a.video_id||a.videoId;if(r(b)){var c=mf()||{},d=mf()||{};q(void 0)?d[b]=void 0:delete d[b];var e=z()+3E5,f=of;if(f&&window.JSON){r(d)||(d=JSON.stringify(d,void 0));try{f.set("yt-player-two-stage-token",d,e)}catch(g){f.remove("yt-player-two-stage-token")}}(b=c[b])&&(a.two_stage_token=b)}}
;function lh(a){I.call(this);this.b=a;this.b.subscribe("command",this.na,this);this.f={};this.i=!1}
A(lh,I);l=lh.prototype;l.start=function(){this.i||this.g||(this.i=!0,mh(this.b,"RECEIVING"))};
l.na=function(a,b,c){if(this.i&&!this.g){var d=b||{};switch(a){case "addEventListener":r(d.event)&&(a=d.event,a in this.f||(c=x(this.Oa,this,a),this.f[a]=c,this.addEventListener(a,c)));break;case "removeEventListener":r(d.event)&&nh(this,d.event);break;default:this.h.isReady()&&this.h[a]&&(b=oh(a,b||{}),c=this.h.handleExternalCall(a,b,c||null),(c=ph(a,c))&&this.i&&!this.g&&mh(this.b,a,c))}}};
l.Oa=function(a,b){this.i&&!this.g&&mh(this.b,a,this.ba(a,b))};
l.ba=function(a,b){if(null!=b)return{value:b}};
function nh(a,b){b in a.f&&(a.removeEventListener(b,a.f[b]),delete a.f[b])}
l.l=function(){var a=this.b;a.g||ad(a.b,"command",this.na,this);this.b=null;for(var b in this.f)nh(this,b);lh.o.l.call(this)};function qh(a,b){lh.call(this,b);this.h=a;this.start()}
A(qh,lh);qh.prototype.addEventListener=function(a,b){this.h.addEventListener(a,b)};
qh.prototype.removeEventListener=function(a,b){this.h.removeEventListener(a,b)};
function oh(a,b){switch(a){case "loadVideoById":return b=ih(b),kh(b),[b];case "cueVideoById":return b=ih(b),kh(b),[b];case "loadVideoByPlayerVars":return kh(b),[b];case "cueVideoByPlayerVars":return kh(b),[b];case "loadPlaylist":return b=jh(b),kh(b),[b];case "cuePlaylist":return b=jh(b),kh(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];
case "setLoop":return[b.loopPlaylists];case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey]}return[]}
function ph(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
qh.prototype.ba=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return qh.o.ba.call(this,a,b)};
qh.prototype.l=function(){qh.o.l.call(this);delete this.h};function rh(a,b,c,d){I.call(this);this.f=b||null;this.u="*";this.h=c||null;this.sessionId=null;this.channel=d||null;this.F=!!a;this.m=x(this.A,this);window.addEventListener("message",this.m)}
n(rh,I);rh.prototype.A=function(a){if(!("*"!=this.h&&a.origin!=this.h||this.f&&a.source!=this.f)&&r(a.data)){try{var b=JSON.parse(a.data)}catch(c){return}if(!(null==b||this.F&&(this.sessionId&&this.sessionId!=b.id||this.channel&&this.channel!=b.channel))&&b)switch(b.event){case "listening":"null"!=a.origin&&(this.h=this.u=a.origin);this.f=a.source;this.sessionId=b.id;this.b&&(this.b(),this.b=null);break;case "command":this.i&&(!this.j||0<=La(this.j,b.func))&&this.i(b.func,b.args,a.origin)}}};
rh.prototype.sendMessage=function(a,b){var c=b||this.f;if(c){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var d=xc(a);c.postMessage(d,this.u)}catch(e){S(e,"WARNING")}}};
rh.prototype.l=function(){window.removeEventListener("message",this.m);I.prototype.l.call(this)};function sh(a,b,c){rh.call(this,a,b,c||R("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname,"widget");this.j=this.b=this.i=null}
n(sh,rh);function th(){var a=this.g=new sh(!!R("WIDGET_ID_ENFORCE")),b=x(this.Ia,this);a.i=b;a.j=null;this.g.channel="widget";if(a=R("WIDGET_ID"))this.g.sessionId=a;this.h=[];this.j=!1;this.i={}}
l=th.prototype;l.Ia=function(a,b,c){"addEventListener"==a&&b?(a=b[0],this.i[a]||"onReady"==a||(this.addEventListener(a,uh(this,a)),this.i[a]=!0)):this.pa(a,b,c)};
l.pa=function(){};
function uh(a,b){return x(function(a){this.sendMessage(b,a)},a)}
l.addEventListener=function(){};
l.va=function(){this.j=!0;this.sendMessage("initialDelivery",this.ca());this.sendMessage("onReady");C(this.h,this.oa,this);this.h=[]};
l.ca=function(){return null};
function vh(a,b){a.sendMessage("infoDelivery",b)}
l.oa=function(a){this.j?this.g.sendMessage(a):this.h.push(a)};
l.sendMessage=function(a,b){this.oa({event:a,info:void 0==b?null:b})};
l.dispose=function(){this.g=null};function wh(a){th.call(this);this.b=a;this.f=[];this.addEventListener("onReady",x(this.Ha,this));this.addEventListener("onVideoProgress",x(this.Sa,this));this.addEventListener("onVolumeChange",x(this.Ta,this));this.addEventListener("onApiChange",x(this.Na,this));this.addEventListener("onPlaybackQualityChange",x(this.Pa,this));this.addEventListener("onPlaybackRateChange",x(this.Qa,this));this.addEventListener("onStateChange",x(this.Ra,this))}
A(wh,th);l=wh.prototype;l.pa=function(a,b,c){if(this.b[a]){b=b||[];if(0<b.length&&gh(a)){var d=b;if(ta(d[0])&&!w(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=ih.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=hh.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=jh.apply(window,d)}d=e}kh(d);b.length=1;b[0]=d}this.b.handleExternalCall(a,b,c);gh(a)&&vh(this,this.ca())}};
l.Ha=function(){var a=x(this.va,this);this.g.b=a};
l.addEventListener=function(a,b){this.f.push({eventType:a,listener:b});this.b.addEventListener(a,b)};
l.ca=function(){if(!this.b)return null;var a=this.b.getApiInterface();Pa(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c],f=e;if(0==f.search("get")||0==f.search("is")){f=e;var g=0;0==f.search("get")?g=3:0==f.search("is")&&(g=2);f=f.charAt(g).toLowerCase()+f.substr(g+1);try{var h=this.b[e]();b[f]=h}catch(k){}}}b.videoData=this.b.getVideoData();b.currentTimeLastUpdated_=z()/1E3;return b};
l.Ra=function(a){a={playerState:a,currentTime:this.b.getCurrentTime(),duration:this.b.getDuration(),videoData:this.b.getVideoData(),videoStartBytes:0,videoBytesTotal:this.b.getVideoBytesTotal(),videoLoadedFraction:this.b.getVideoLoadedFraction(),playbackQuality:this.b.getPlaybackQuality(),availableQualityLevels:this.b.getAvailableQualityLevels(),videoUrl:this.b.getVideoUrl(),playlist:this.b.getPlaylist(),playlistIndex:this.b.getPlaylistIndex(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),
mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());this.b.getStoryboardFormat&&(a.storyboardFormat=this.b.getStoryboardFormat());vh(this,a)};
l.Pa=function(a){vh(this,{playbackQuality:a})};
l.Qa=function(a){vh(this,{playbackRate:a})};
l.Na=function(){for(var a=this.b.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.b.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],m=this.b.getOption(e,k);b[e][k]=m}}this.sendMessage("apiInfoDelivery",b)};
l.Ta=function(){vh(this,{muted:this.b.isMuted(),volume:this.b.getVolume()})};
l.Sa=function(a){a={currentTime:a,videoBytesLoaded:this.b.getVideoBytesLoaded(),videoLoadedFraction:this.b.getVideoLoadedFraction(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());vh(this,a)};
l.dispose=function(){wh.o.dispose.call(this);for(var a=0;a<this.f.length;a++){var b=this.f[a];this.b.removeEventListener(b.eventType,b.listener)}this.f=[]};function xh(){I.call(this);this.b=new K;mc(this,y(nc,this.b))}
A(xh,I);xh.prototype.subscribe=function(a,b,c){return this.g?0:this.b.subscribe(a,b,c)};
xh.prototype.D=function(a){return this.g?!1:this.b.D(a)};
xh.prototype.j=function(a,b){this.g||this.b.G.apply(this.b,arguments)};function yh(a,b,c){xh.call(this);this.f=a;this.h=b;this.i=c}
A(yh,xh);function mh(a,b,c){if(!a.g){var d=a.f;d.g||a.h!=d.b||(a={id:a.i,command:b},c&&(a.data=c),d.b.postMessage(xc(a),d.h))}}
yh.prototype.l=function(){this.h=this.f=null;yh.o.l.call(this)};function zh(a,b,c){I.call(this);this.b=a;this.h=c;this.i=df(window,"message",x(this.j,this));this.f=new yh(this,a,b);mc(this,y(nc,this.f))}
A(zh,I);zh.prototype.j=function(a){var b;if(b=!this.g)if(b=a.origin==this.h)a:{b=this.b;do{b:{var c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,r(b))){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.f,c.g||c.j("command",b.command,b.data,a.origin))}};
zh.prototype.l=function(){ef(this.i);this.b=null;zh.o.l.call(this)};function Ah(){var a=Bh()?"//googleads.g.doubleclick.net/pagead/id?exp=nomnom":"//googleads.g.doubleclick.net/pagead/id",b=ab(Ch);return new J(function(c,d){b.C=function(a){ve(a)?c(a):d(new Dh("Request failed, status="+a.status,"net.badstatus"))};
b.onError=function(){d(new Dh("Unknown request error","net.unknown"))};
b.K=function(){d(new Dh("Request timed out","net.timeout"))};
De(a,b)})}
function Dh(a,b){B.call(this,a+", errorCode="+b);this.errorCode=b;this.name="PromiseAjaxError"}
n(Dh,B);function Eh(a){this.f=void 0===a?null:a;this.g=0;this.b=null}
Eh.prototype.then=function(a,b,c){return this.f?this.f.then(a,b,c):1===this.g&&a?(a=a.call(c,this.b),Ec(a)?a:Fh(a)):2===this.g&&b?(a=b.call(c,this.b),Ec(a)?a:Gh(a)):this};
Eh.prototype.getValue=function(){return this.b};
Dc(Eh);function Gh(a){var b=new Eh;a=void 0===a?null:a;b.g=2;b.b=void 0===a?null:a;return b}
function Fh(a){var b=new Eh;a=void 0===a?null:a;b.g=1;b.b=void 0===a?null:a;return b}
;function Hh(a){B.call(this,a.message||a.description||a.name);this.isMissing=a instanceof Ih;this.isTimeout=a instanceof Dh&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Sc}
n(Hh,B);Hh.prototype.name="BiscottiError";function Ih(){B.call(this,"Biscotti ID is missing from server")}
n(Ih,B);Ih.prototype.name="BiscottiMissingError";var Ch={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},Jh=null;function Kh(){if("1"===Wa(Pd(),"args","privembed"))return Jc(Error("Biscotti ID is not available in private embed mode"));Jh||(Jh=Rc(Ah().then(Lh),function(a){return Mh(2,a)}));
return Jh}
function Bh(){var a;(a=!!Wa(window,"settings","experiments","flags","html5_serverside_pagead_id_sets_cookie"))||(a=!!R("EXP_HTML5_SERVERSIDE_PAGEAD_ID_SETS_COOKIE",!1));return a||!!T("html5_serverside_pagead_id_sets_cookie")}
function Lh(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new Ih;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new Ih;a=a.id;Nh(a);Jh=Fh(a);Oh(18E5,2);return a}
function Mh(a,b){var c=new Hh(b);Nh("");Jh=Gh(c);0<a&&Oh(12E4,a-1);throw c;}
function Oh(a,b){U(function(){Rc(Ah().then(Lh,function(a){return Mh(b,a)}),pa)},a)}
function Nh(a){t("yt.ads.biscotti.lastId_",a,void 0)}
function Ph(){try{var a=v("yt.ads.biscotti.getId_");return a?a():Kh()}catch(b){return Jc(b)}}
;function Qh(a){B.apply(this,arguments)}
n(Qh,B);Qh.prototype.name="MutsuError";function Rh(){var a=new Qh("ID is missing"),b=new Qh("Timeout"),c=null,d=!1;Kd(function(){c=Id();d=!0});
if(d)return c?Fh(c):Gh(a);var e=new J(function(b,c){Kd(function(){var d=Id();d?b(d):c(a)})}),f=od().then(function(){return Jc(b)});
return Pc(Mc([e,f]),function(){return f.cancel()})}
;function Sh(a){if("1"!==Wa(Pd(),"args","privembed")){a&&!v("yt.ads.biscotti.getId_")&&t("yt.ads.biscotti.getId_",Kh,void 0);try{var b=Ph();if(T("enable_mutsu")){v("yt.ads.mutsu.getId_")||t("yt.ads.mutsu.getId_",Rh,void 0);try{var c=v("yt.ads.mutsu.getId_")()}catch(d){c=Jc(d)}}else c=Jc(new Qh("unimplemented"));Nc([b,c]).then(function(a){var b=a[0];a=a[1];if(b.aa||a.aa){b=b.value;a=a.value;var c={};c.dt=Rb;c.flash=yd||"0";a:{try{var d=window.top.location.href}catch(kb){d=2;break a}d=null!=d?d==window.document.location.href?
0:1:2}d=(c.frm=d,c);d.u_tz=-(new Date).getTimezoneOffset();var h=void 0===h?H:h;try{var k=h.history.length}catch(kb){k=0}d.u_his=k;d.u_java=!!H.navigator&&"unknown"!==typeof H.navigator.javaEnabled&&!!H.navigator.javaEnabled&&H.navigator.javaEnabled();H.screen&&(d.u_h=H.screen.height,d.u_w=H.screen.width,d.u_ah=H.screen.availHeight,d.u_aw=H.screen.availWidth,d.u_cd=H.screen.colorDepth);H.navigator&&H.navigator.plugins&&(d.u_nplug=H.navigator.plugins.length);H.navigator&&H.navigator.mimeTypes&&(d.u_nmime=
H.navigator.mimeTypes.length);d.ca_type=xd?"flash":"image";if(T("enable_server_side_search_pyv")||T("enable_server_side_mweb_search_pyv")){k=window;try{var m=k.screenX;var u=k.screenY}catch(kb){}try{var P=k.outerWidth;var ug=k.outerHeight}catch(kb){}try{var vg=k.innerWidth;var wg=k.innerHeight}catch(kb){}m=[k.screenLeft,k.screenTop,m,u,k.screen?k.screen.availWidth:void 0,k.screen?k.screen.availTop:void 0,P,ug,vg,wg];u=window.top;try{if(u.document&&!u.document.body)var X=new Gb(-1,-1);else{var Da=
(u||window).document,Ed="CSS1Compat"==Da.compatMode?Da.documentElement:Da.body;X=(new Gb(Ed.clientWidth,Ed.clientHeight)).round()}var Ea=X}catch(kb){Ea=new Gb(-12245933,-12245933)}X={};Da=0;p.SVGElement&&p.document.createElementNS&&(Da|=1);X.bc=Da;X.bih=Ea.height;X.biw=Ea.width;X.brdim=m.join();Ea=(X.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[Pb.webkitVisibilityState||Pb.mozVisibilityState||Pb.visibilityState||""]||0,X.wgl=!!H.WebGLRenderingContext,X);for(var Fd in Ea)d[Fd]=Ea[Fd]}void 0!==
b&&(d.bid=b);void 0!==a&&(d.mutsuid=a);d.bsq=Th++;Je("//www.youtube.com/ad_data_204",{za:!1,w:d})}});
U(Sh,18E5)}catch(d){S(d)}}}
var Th=0;var Y=v("ytglobal.prefsUserPrefsPrefs_")||{};t("ytglobal.prefsUserPrefsPrefs_",Y,void 0);function Z(){this.b=R("ALT_PREF_COOKIE_NAME","PREF");var a;if(a=Xb.get(""+this.b,void 0)){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Y[d]=c.toString())}}}
Z.prototype.get=function(a,b){Uh(a);Vh(a);var c=void 0!==Y[a]?Y[a].toString():null;return null!=c?c:b?b:""};
Z.prototype.set=function(a,b){Uh(a);Vh(a);if(null==b)throw Error("ExpectedNotNull");Y[a]=b.toString()};
Z.prototype.remove=function(a){Uh(a);Vh(a);delete Y[a]};
Z.prototype.clear=function(){for(var a in Y)delete Y[a]};
function Vh(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function Uh(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function Wh(a){a=void 0!==Y[a]?Y[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
Z.b=void 0;Z.getInstance=function(){return Z.b?Z.b:Z.b=new Z};var Xh=null,Yh=null,Zh=null,$h={};function ai(a){If(a.payload_name,a.payload,Kf,void 0,void 0)}
function bi(a){var b=a.id;a=a.ve_type;var c=lf++;a=new jf(void 0,a,c,void 0,void 0);$h[b]=a;b=sf();c=rf();b&&c&&Lf(b,c,a)}
function ci(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(Q("client-screen-nonce",b),Q("ROOT_VE_TYPE",a),a=rf()))for(var c in $h){var d=$h[c];d&&Lf(b,a,d)}}
function di(a){$h[a.id]=new jf(a.tracking_params)}
function ei(a){var b=sf();a=$h[a.id];b&&a&&Mf(Kf,{click:{csn:b,visualElement:kf(a)}})}
function fi(a){a=a.ids;var b=sf();if(b)for(var c=0;c<a.length;c++){var d=$h[a[c]];if(d){var e=b,f=Kf;T("interaction_logging_on_gel_web")?If("visualElementShown",{csn:e,ve:kf(d),eventType:1},f):Mf(f,{visibilityUpdate:{csn:e,visualElements:[kf(d)]}},void 0)}}}
function gi(){var a=Xh;a&&a.startInteractionLogging&&a.startInteractionLogging()}
;t("yt.setConfig",Q,void 0);t("yt.config.set",Q,void 0);t("yt.setMsg",Se,void 0);t("yt.msgs.set",Se,void 0);t("yt.logging.errors.log",Qe,void 0);
t("writeEmbed",function(){var a=R("PLAYER_CONFIG",void 0);Sh(!0);"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");var b=document.referrer,c=R("POST_MESSAGE_ORIGIN");window!=window.top&&b&&b!=document.URL&&(a.args.loaderUrl=b);R("LIGHTWEIGHT_AUTOPLAY")&&(a.args.autoplay="1");a.args.autoplay&&kh(a.args);Xh=a=eh(a);a.addEventListener("onScreenChanged",ci);a.addEventListener("onLogClientVeCreated",bi);a.addEventListener("onLogServerVeCreated",di);a.addEventListener("onLogToGel",ai);
a.addEventListener("onLogVeClicked",ei);a.addEventListener("onLogVesShown",fi);a.addEventListener("onReady",gi);b=R("POST_MESSAGE_ID","player");R("ENABLE_JS_API")?Zh=new wh(a):R("ENABLE_POST_API")&&r(b)&&r(c)&&(Yh=new zh(window.parent,b,c),Zh=new qh(a,Yh.f));R("BG_P")&&(R("BG_I")||R("BG_IU"))&&pe();Xe()},void 0);
t("yt.www.watch.ads.restrictioncookie.spr",function(a){Me(a+"mac_204?action_fcts=1");return!0},void 0);
var hi=Qd(function(){Fg("ol");var a=Z.getInstance(),b=!!((Wh("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&qc(document.body,"exp-invert-logo"))if(c&&!qc(document.body,"inverted-hdpi")){var d=document.body;d.classList?d.classList.add("inverted-hdpi"):qc(d,"inverted-hdpi")||(d.className+=0<d.className.length?" inverted-hdpi":"inverted-hdpi")}else!c&&qc(document.body,"inverted-hdpi")&&rc();if(b!=c){b="f"+(Math.floor(119/31)+1);d=Wh(b)||0;d=c?d|67108864:d&-67108865;
0==d?delete Y[b]:Y[b]=d.toString(16).toString();a=a.b;c=[];for(var e in Y)c.push(e+"="+encodeURIComponent(String(Y[e])));tf(a,c.join("&"),63072E3)}}),ii=Qd(function(){var a=Xh;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();R("PL_ATT")&&(oe=null);a=0;for(var b=Ve.length;a<b;a++)Ue(Ve[a]);Ve.length=0;me("//static.doubleclick.net/instream/ad_status.js");We=!1;Q("DCLKSTAT",0);oc(Zh,Yh);if(a=Xh)a.removeEventListener("onScreenChanged",ci),a.removeEventListener("onLogClientVeCreated",bi),a.removeEventListener("onLogServerVeCreated",di),a.removeEventListener("onLogToGel",ai),a.removeEventListener("onLogVeClicked",ei),a.removeEventListener("onLogVesShown",fi),a.removeEventListener("onReady",
gi),a.destroy();$h={}});
window.addEventListener?(window.addEventListener("load",hi),window.addEventListener("unload",ii)):window.attachEvent&&(window.attachEvent("onload",hi),window.attachEvent("onunload",ii));}).call(this);
