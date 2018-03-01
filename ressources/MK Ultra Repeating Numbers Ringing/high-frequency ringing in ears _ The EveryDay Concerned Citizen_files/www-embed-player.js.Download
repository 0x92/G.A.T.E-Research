(function(){var l,aa="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ba;
if("function"==typeof Object.setPrototypeOf)ba=Object.setPrototypeOf;else{var ca;a:{var da={wa:!0},ea={};try{ea.__proto__=da;ca=ea.wa;break a}catch(a){}ca=!1}ba=ca?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var fa=ba;
function n(a,b){a.prototype=aa(b.prototype);a.prototype.constructor=a;if(fa)fa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.u=b.prototype}
(function(){function a(){function a(){}
Reflect.construct(a,[],function(){});
return new a instanceof a}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(a,d,e){a=b(a,d);e&&Reflect.setPrototypeOf(a,e.prototype);return a}}return function(a,b,e){void 0===e&&(e=a);
e=aa(e.prototype||Object.prototype);return Function.prototype.apply.call(a,e,b)||e}})();
var p=this;function q(a){return void 0!==a}
function r(a){return"string"==typeof a}
function ha(a){return"number"==typeof a}
function t(a,b,c){a=a.split(".");c=c||p;a[0]in c||!c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&q(b)?c[d]=b:c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}}
function v(a,b){for(var c=a.split("."),d=b||p,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function ia(){}
function ja(a){a.ga=void 0;a.getInstance=function(){return a.ga?a.ga:a.ga=new a}}
function ka(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function w(a){return"array"==ka(a)}
function la(a){var b=ka(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function ma(a){return"function"==ka(a)}
function na(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
var oa="closure_uid_"+(1E9*Math.random()>>>0),pa=0;function qa(a,b,c){return a.call.apply(a.bind,arguments)}
function ra(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function x(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?x=qa:x=ra;return x.apply(null,arguments)}
function y(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
var z=Date.now||function(){return+new Date};
function A(a,b){function c(){}
c.prototype=b.prototype;a.u=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.ab=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function B(a){if(Error.captureStackTrace)Error.captureStackTrace(this,B);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
A(B,Error);B.prototype.name="CustomError";var sa=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(r(a))return r(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},C=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=r(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},ta=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f=r(a)?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},ua=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e=r(a)?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d};
function va(a,b){a:{var c=a.length;for(var d=r(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:r(a)?a.charAt(c):a[c]}
function wa(a,b){var c=sa(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function xa(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function ya(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(la(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;var za=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function Aa(a){if(!Ba.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(Ea,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(Fa,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(Ga,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(Ha,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Ia,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Ja,"&#0;"));return a}
var Ea=/&/g,Fa=/</g,Ga=/>/g,Ha=/"/g,Ia=/'/g,Ja=/\x00/g,Ba=/[\x00&<>"']/;function Ka(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var La;a:{var Ma=p.navigator;if(Ma){var Na=Ma.userAgent;if(Na){La=Na;break a}}La=""}function D(a){return-1!=La.indexOf(a)}
;function Qa(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Ra(a,b){var c=la(b),d=c?b:arguments;for(c=c?0:1;c<d.length;c++){if(null==a)return;a=a[d[c]]}return a}
function Sa(a){var b=Ta,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function Ua(a){for(var b in a)return!1;return!0}
function Va(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function Wa(a){var b={},c;for(c in a)b[c]=a[c];return b}
var Xa="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function Ya(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<Xa.length;f++)c=Xa[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var Za=D("Opera"),$a=D("Trident")||D("MSIE"),ab=D("Edge"),bb=D("Gecko")&&!(-1!=La.toLowerCase().indexOf("webkit")&&!D("Edge"))&&!(D("Trident")||D("MSIE"))&&!D("Edge"),cb=-1!=La.toLowerCase().indexOf("webkit")&&!D("Edge");function db(){var a=p.document;return a?a.documentMode:void 0}
var eb;a:{var fb="",gb=function(){var a=La;if(bb)return/rv:([^\);]+)(\)|;)/.exec(a);if(ab)return/Edge\/([\d\.]+)/.exec(a);if($a)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(cb)return/WebKit\/(\S+)/.exec(a);if(Za)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
gb&&(fb=gb?gb[1]:"");if($a){var hb=db();if(null!=hb&&hb>parseFloat(fb)){eb=String(hb);break a}}eb=fb}var ib=eb,jb;var kb=p.document;jb=kb&&$a?db()||("CSS1Compat"==kb.compatMode?parseInt(ib,10):5):void 0;var lb=!$a||9<=Number(jb);function mb(){this.b="";this.f=nb}
mb.prototype.J=!0;mb.prototype.H=function(){return this.b};
mb.prototype.fa=!0;mb.prototype.aa=function(){return 1};
function ob(a){return a instanceof mb&&a.constructor===mb&&a.f===nb?a.b:"type_error:TrustedResourceUrl"}
var nb={};function E(){this.b="";this.f=pb}
E.prototype.J=!0;E.prototype.H=function(){return this.b};
E.prototype.fa=!0;E.prototype.aa=function(){return 1};
function qb(a){return a instanceof E&&a.constructor===E&&a.f===pb?a.b:"type_error:SafeUrl"}
var rb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function sb(a){if(a instanceof E)return a;a=a.J?a.H():String(a);rb.test(a)||(a="about:invalid#zClosurez");return tb(a)}
var pb={};function tb(a){var b=new E;b.b=a;return b}
tb("about:blank");function ub(){this.ea="";this.va=vb;this.b=null}
ub.prototype.fa=!0;ub.prototype.aa=function(){return this.b};
ub.prototype.J=!0;ub.prototype.H=function(){return this.ea};
var vb={};function wb(a,b){var c=new ub;c.ea=a;c.b=b;return c}
wb("<!DOCTYPE html>",0);wb("",0);wb("<br>",0);function xb(a,b){var c=b instanceof E?b:sb(b);a.href=qb(c)}
function yb(a,b,c){a.rel=c;a.href=-1!=c.toLowerCase().indexOf("stylesheet")?ob(b):b instanceof mb?ob(b):b instanceof E?qb(b):sb(b).H()}
function zb(a,b){a.src=ob(b)}
;function Ab(a,b){this.x=q(a)?a:0;this.y=q(b)?b:0}
Ab.prototype.equals=function(a){return a instanceof Ab&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
Ab.prototype.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
Ab.prototype.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
Ab.prototype.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Bb(a,b){this.width=a;this.height=b}
l=Bb.prototype;l.aspectRatio=function(){return this.width/this.height};
l.isEmpty=function(){return!(this.width*this.height)};
l.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
l.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
l.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Cb(a){var b=document;return r(a)?b.getElementById(a):a}
function Db(a,b){Qa(b,function(b,d){b&&b.J&&(b=b.H());"style"==d?a.style.cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:Eb.hasOwnProperty(d)?a.setAttribute(Eb[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})}
var Eb={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Fb(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!lb&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',Aa(g.name),'"');if(g.type){f.push(' type="',Aa(g.type),'"');var h={};Ya(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=e.createElement(f);g&&(r(g)?f.className=g:w(g)?f.className=g.join(" "):Db(f,g));2<d.length&&Gb(e,f,d);return f}
function Gb(a,b,c){function d(c){c&&b.appendChild(r(c)?a.createTextNode(c):c)}
for(var e=2;e<c.length;e++){var f=c[e];if(!la(f)||na(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(na(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if(ma(f)){g="function"==typeof f.item;break a}}g=!1}C(g?xa(f):f,d)}}}
function Hb(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Ib(a){Jb();var b=new mb;b.b=a;return b}
var Jb=ia;var Kb=/^[\w+/_-]+[=]{0,2}$/;function Lb(){var a=p.document.querySelector("script[nonce]");if(a&&(a=a.nonce||a.getAttribute("nonce"))&&Kb.test(a))return a}
;var Mb=document,F=window;function Nb(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Ob=(new Date).getTime();function Pb(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a)throw Error("Invalid URI scheme in origin");c="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+
1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function Qb(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;u=m=0}
function b(a){for(var b=g,c=0;64>c;c+=4)b[c/4]=a[c]<<24|a[c+1]<<16|a[c+2]<<8|a[c+3];for(c=16;80>c;c++)a=b[c-3]^b[c-8]^b[c-14]^b[c-16],b[c]=(a<<1|a>>>31)&4294967295;a=e[0];var d=e[1],f=e[2],h=e[3],k=e[4];for(c=0;80>c;c++){if(40>c)if(20>c){var m=h^d&(f^h);var u=1518500249}else m=d^f^h,u=1859775393;else 60>c?(m=d&f|h&(d|f),u=2400959708):(m=d^f^h,u=3395469782);m=((a<<5|a>>>27)&4294967295)+m+k+u+b[c]&4294967295;k=h;h=f;f=(d<<30|d>>>2)&4294967295;d=a;a=m}e[0]=e[0]+a&4294967295;e[1]=e[1]+d&4294967295;e[2]=
e[2]+f&4294967295;e[3]=e[3]+h&4294967295;e[4]=e[4]+k&4294967295}
function c(a,c){if("string"===typeof a){a=unescape(encodeURIComponent(a));for(var d=[],e=0,g=a.length;e<g;++e)d.push(a.charCodeAt(e));a=d}c||(c=a.length);d=0;if(0==m)for(;d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64;for(;d<c;)if(f[m++]=a[d++],u++,64==m)for(m=0,b(f);d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64}
function d(){var a=[],d=8*u;56>m?c(h,56-m):c(h,64-(m-56));for(var g=63;56<=g;g--)f[g]=d&255,d>>>=8;b(f);for(g=d=0;5>g;g++)for(var k=24;0<=k;k-=8)a[d++]=e[g]>>k&255;return a}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var m,u;a();return{reset:a,update:c,digest:d,ya:function(){for(var a=d(),b="",c=0;c<a.length;c++)b+="0123456789ABCDEF".charAt(Math.floor(a[c]/16))+"0123456789ABCDEF".charAt(a[c]%16);return b}}}
;function Rb(a,b,c){var d=[],e=[];if(1==(w(c)?2:1))return e=[b,a],C(d,function(a){e.push(a)}),Sb(e.join(" "));
var f=[],g=[];C(c,function(a){g.push(a.key);f.push(a.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];C(d,function(a){e.push(a)});
a=Sb(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function Sb(a){var b=Qb();b.update(a);return b.ya().toLowerCase()}
;function Tb(a){this.b=a||{cookie:""}}
l=Tb.prototype;l.isEnabled=function(){return navigator.cookieEnabled};
l.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');q(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(z()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
l.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(";"),e=0,f;e<d.length;e++){f=za(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
l.remove=function(a,b,c){var d=q(this.get(a));this.set(a,"",0,b,c);return d};
l.isEmpty=function(){return!this.b.cookie};
l.clear=function(){for(var a=(this.b.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=za(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Ub=new Tb("undefined"==typeof document?null:document);Ub.f=3950;function Vb(){var a=[],b=Pb(String(p.location.href)),c=p.__OVERRIDE_SID;null==c&&(c=(new Tb(document)).get("SID"));if(c&&(b=(c=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?p.__SAPISID:p.__APISID,null==b&&(b=(new Tb(document)).get(c?"SAPISID":"APISID")),b)){c=c?"SAPISIDHASH":"APISIDHASH";var d=String(p.location.href);return d&&b&&c?[c,Rb(Pb(d),b,a||null)].join(" "):null}return null}
;function Wb(a,b){this.h=a;this.g=b;this.f=0;this.b=null}
Wb.prototype.get=function(){if(0<this.f){this.f--;var a=this.b;this.b=a.next;a.next=null}else a=this.h();return a};
function Xb(a,b){a.g(b);100>a.f&&(a.f++,b.next=a.b,a.b=b)}
;function Yb(a){p.setTimeout(function(){throw a;},0)}
var Zb;
function $b(){var a=p.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!D("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=x(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!D("Trident")&&!D("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(q(c.next)){c=c.next;var a=c.ma;c.ma=null;a()}};
return function(a){d.next={ma:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){p.setTimeout(a,0)}}
;function ac(){this.f=this.b=null}
var cc=new Wb(function(){return new bc},function(a){a.reset()});
ac.prototype.add=function(a,b){var c=cc.get();c.set(a,b);this.f?this.f.next=c:this.b=c;this.f=c};
ac.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.f=null),a.next=null);return a};
function bc(){this.next=this.scope=this.b=null}
bc.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
bc.prototype.reset=function(){this.next=this.scope=this.b=null};function dc(a,b){ec||fc();gc||(ec(),gc=!0);hc.add(a,b)}
var ec;function fc(){if(-1!=String(p.Promise).indexOf("[native code]")){var a=p.Promise.resolve(void 0);ec=function(){a.then(ic)}}else ec=function(){var a=ic;
!ma(p.setImmediate)||p.Window&&p.Window.prototype&&!D("Edge")&&p.Window.prototype.setImmediate==p.setImmediate?(Zb||(Zb=$b()),Zb(a)):p.setImmediate(a)}}
var gc=!1,hc=new ac;function ic(){for(var a;a=hc.remove();){try{a.b.call(a.scope)}catch(b){Yb(b)}Xb(cc,a)}gc=!1}
;function G(){this.h=this.h;this.B=this.B}
G.prototype.h=!1;G.prototype.dispose=function(){this.h||(this.h=!0,this.l())};
function jc(a,b){a.h?q(void 0)?b.call(void 0):b():(a.B||(a.B=[]),a.B.push(q(void 0)?x(b,void 0):b))}
G.prototype.l=function(){if(this.B)for(;this.B.length;)this.B.shift()()};
function kc(a){a&&"function"==typeof a.dispose&&a.dispose()}
function lc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];la(d)?lc.apply(null,d):kc(d)}}
;function mc(a){if(a.classList)return a.classList;a=a.className;return r(a)&&a.match(/\S+/g)||[]}
function nc(a,b){if(a.classList)var c=a.classList.contains(b);else c=mc(a),c=0<=sa(c,b);return c}
function oc(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):nc(a,"inverted-hdpi")&&(a.className=ta(mc(a),function(a){return"inverted-hdpi"!=a}).join(" "))}
;var pc="StopIteration"in p?p.StopIteration:{message:"StopIteration",stack:""};function qc(){}
qc.prototype.next=function(){throw pc;};
qc.prototype.U=function(){return this};
function rc(a){if(a instanceof qc)return a;if("function"==typeof a.U)return a.U(!1);if(la(a)){var b=0,c=new qc;c.next=function(){for(;;){if(b>=a.length)throw pc;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function sc(a,b){if(la(a))try{C(a,b,void 0)}catch(c){if(c!==pc)throw c;}else{a=rc(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==pc)throw c;}}}
function tc(a){if(la(a))return xa(a);a=rc(a);var b=[];sc(a,function(a){b.push(a)});
return b}
;(function(){if(!p.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
p.addEventListener("test",ia,b);p.removeEventListener("test",ia,b);return a})();function uc(a){var b=[];vc(new wc,a,b);return b.join("")}
function wc(){}
function vc(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(w(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),vc(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),xc(d,c),c.push(":"),vc(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":xc(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var yc={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},zc=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function xc(a,b){b.push('"',a.replace(zc,function(a){var b=yc[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),yc[a]=b);return b}),'"')}
;function Ac(a){a.prototype.then=a.prototype.then;a.prototype.$goog_Thenable=!0}
function Bc(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function H(a,b){this.b=0;this.m=void 0;this.g=this.f=this.h=null;this.i=this.j=!1;if(a!=ia)try{var c=this;a.call(b,function(a){Cc(c,2,a)},function(a){Cc(c,3,a)})}catch(d){Cc(this,3,d)}}
function Dc(){this.next=this.context=this.f=this.g=this.b=null;this.h=!1}
Dc.prototype.reset=function(){this.context=this.f=this.g=this.b=null;this.h=!1};
var Ec=new Wb(function(){return new Dc},function(a){a.reset()});
function Fc(a,b,c){var d=Ec.get();d.g=a;d.f=b;d.context=c;return d}
function Gc(a){return new H(function(b,c){c(a)})}
function Hc(a,b,c){Ic(a,b,c,null)||dc(y(b,a))}
function Jc(a){return new H(function(b,c){a.length||b(void 0);for(var d=0,e;d<a.length;d++)e=a[d],Hc(e,b,c)})}
function Kc(a){return new H(function(b){var c=a.length,d=[];if(c)for(var e=function(a,e,f){c--;d[a]=e?{Z:!0,value:f}:{Z:!1,reason:f};0==c&&b(d)},f=0,g;f<a.length;f++)g=a[f],Hc(g,y(e,f,!0),y(e,f,!1));
else b(d)})}
H.prototype.then=function(a,b,c){return Lc(this,ma(a)?a:null,ma(b)?b:null,c)};
Ac(H);function Mc(a,b){var c=Fc(b,b,void 0);c.h=!0;Nc(a,c);return a}
function Oc(a,b){return Lc(a,null,b,void 0)}
H.prototype.cancel=function(a){0==this.b&&dc(function(){var b=new Pc(a);Qc(this,b)},this)};
function Qc(a,b){if(0==a.b)if(a.h){var c=a.h;if(c.f){for(var d=0,e=null,f=null,g=c.f;g&&(g.h||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?Qc(c,b):(f?(d=f,d.next==c.g&&(c.g=d),d.next=d.next.next):Rc(c),Sc(c,e,3,b)))}a.h=null}else Cc(a,3,b)}
function Nc(a,b){a.f||2!=a.b&&3!=a.b||Tc(a);a.g?a.g.next=b:a.f=b;a.g=b}
function Lc(a,b,c,d){var e=Fc(null,null,null);e.b=new H(function(a,g){e.g=b?function(c){try{var e=b.call(d,c);a(e)}catch(m){g(m)}}:a;
e.f=c?function(b){try{var e=c.call(d,b);!q(e)&&b instanceof Pc?g(b):a(e)}catch(m){g(m)}}:g});
e.b.h=a;Nc(a,e);return e.b}
H.prototype.o=function(a){this.b=0;Cc(this,2,a)};
H.prototype.w=function(a){this.b=0;Cc(this,3,a)};
function Cc(a,b,c){0==a.b&&(a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself")),a.b=1,Ic(c,a.o,a.w,a)||(a.m=c,a.b=b,a.h=null,Tc(a),3!=b||c instanceof Pc||Uc(a,c)))}
function Ic(a,b,c,d){if(a instanceof H)return Nc(a,Fc(b||ia,c||null,d)),!0;if(Bc(a))return a.then(b,c,d),!0;if(na(a))try{var e=a.then;if(ma(e))return Vc(a,e,b,c,d),!0}catch(f){return c.call(d,f),!0}return!1}
function Vc(a,b,c,d,e){function f(a){h||(h=!0,d.call(e,a))}
function g(a){h||(h=!0,c.call(e,a))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Tc(a){a.j||(a.j=!0,dc(a.B,a))}
function Rc(a){var b=null;a.f&&(b=a.f,a.f=b.next,b.next=null);a.f||(a.g=null);return b}
H.prototype.B=function(){for(var a;a=Rc(this);)Sc(this,a,this.b,this.m);this.j=!1};
function Sc(a,b,c,d){if(3==c&&b.f&&!b.h)for(;a&&a.i;a=a.h)a.i=!1;if(b.b)b.b.h=null,Wc(b,c,d);else try{b.h?b.g.call(b.context):Wc(b,c,d)}catch(e){Xc.call(null,e)}Xb(Ec,b)}
function Wc(a,b,c){2==b?a.g.call(a.context,c):a.f&&a.f.call(a.context,c)}
function Uc(a,b){a.i=!0;dc(function(){a.i&&Xc.call(null,b)})}
var Xc=Yb;function Pc(a){B.call(this,a)}
A(Pc,B);Pc.prototype.name="cancel";function I(a){G.call(this);this.j=1;this.g=[];this.i=0;this.b=[];this.f={};this.m=!!a}
A(I,G);l=I.prototype;l.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.j;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.j=e+3;d.push(e);return e};
function Yc(a,b,c,d){if(b=a.f[b]){var e=a.b;(b=va(b,function(a){return e[a+1]==c&&e[a+2]==d}))&&a.K(b)}}
l.K=function(a){var b=this.b[a];if(b){var c=this.f[b];0!=this.i?(this.g.push(a),this.b[a+1]=ia):(c&&wa(c,a),delete this.b[a],delete this.b[a+1],delete this.b[a+2])}return!!b};
l.I=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.m)for(e=0;e<c.length;e++){var g=c[e];Zc(this.b[g+1],this.b[g+2],d)}else{this.i++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.i--,0<this.g.length&&0==this.i)for(;c=this.g.pop();)this.K(c)}}return 0!=e}return!1};
function Zc(a,b,c){dc(function(){a.apply(b,c)})}
l.clear=function(a){if(a){var b=this.f[a];b&&(C(b,this.K,this),delete this.f[a])}else this.b.length=0,this.f={}};
l.l=function(){I.u.l.call(this);this.clear();this.g.length=0};function $c(a){this.b=a}
$c.prototype.set=function(a,b){q(b)?this.b.set(a,uc(b)):this.b.remove(a)};
$c.prototype.get=function(a){try{var b=this.b.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
$c.prototype.remove=function(a){this.b.remove(a)};function ad(a){this.b=a}
A(ad,$c);function bd(a){this.data=a}
function cd(a){return!q(a)||a instanceof bd?a:new bd(a)}
ad.prototype.set=function(a,b){ad.u.set.call(this,a,cd(b))};
ad.prototype.f=function(a){a=ad.u.get.call(this,a);if(!q(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
ad.prototype.get=function(a){if(a=this.f(a)){if(a=a.data,!q(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};function dd(a){this.b=a}
A(dd,ad);dd.prototype.set=function(a,b,c){if(b=cd(b)){if(c){if(c<z()){dd.prototype.remove.call(this,a);return}b.expiration=c}b.creation=z()}dd.u.set.call(this,a,b)};
dd.prototype.f=function(a){var b=dd.u.f.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<z()||c&&c>z())dd.prototype.remove.call(this,a);else return b}};function ed(a){this.b=a}
A(ed,dd);function fd(){}
;function gd(){}
A(gd,fd);gd.prototype.clear=function(){var a=tc(this.U(!0)),b=this;C(a,function(a){b.remove(a)})};function hd(a){this.b=a}
A(hd,gd);l=hd.prototype;l.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
l.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
l.get=function(a){a=this.b.getItem(a);if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
l.remove=function(a){this.b.removeItem(a)};
l.U=function(a){var b=0,c=this.b,d=new qc;d.next=function(){if(b>=c.length)throw pc;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
l.clear=function(){this.b.clear()};
l.key=function(a){return this.b.key(a)};function id(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
A(id,hd);function jd(){var a=null;try{a=window.sessionStorage||null}catch(b){}this.b=a}
A(jd,hd);function kd(a){if(!ma(a))if(a&&"function"==typeof a.handleEvent)a=x(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(5E3)?-1:p.setTimeout(a,5E3)}
function ld(){var a=null;return Oc(new H(function(b,c){a=kd(function(){b(void 0)});
-1==a&&c(Error("Failed to schedule timer."))}),function(b){p.clearTimeout(a);
throw b;})}
;var md=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function J(a){return a.match(md)}
function nd(a){return a?decodeURI(a):a}
function od(a,b,c){if(w(b))for(var d=0;d<b.length;d++)od(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function pd(a){var b=[],c;for(c in a)od(c,a[c],b);return b.join("&")}
function qd(a,b){var c=pd(b);if(c){var d=a.indexOf("#");0>d&&(d=a.length);var e=a.indexOf("?");if(0>e||e>d){e=d;var f=""}else f=a.substring(e+1,d);d=[a.substr(0,e),f,a.substr(d)];e=d[1];d[1]=c?e?e+"&"+c:c:e;c=d[0]+(d[1]?"?"+d[1]:"")+d[2]}else c=a;return c}
;var rd=!1,sd="";function td(a){a=a.match(/[\d]+/g);if(!a)return"";a.length=3;return a.join(".")}
(function(){if(navigator.plugins&&navigator.plugins.length){var a=navigator.plugins["Shockwave Flash"];if(a&&(rd=!0,a.description)){sd=td(a.description);return}if(navigator.plugins["Shockwave Flash 2.0"]){rd=!0;sd="2.0.0.11";return}}if(navigator.mimeTypes&&navigator.mimeTypes.length&&(a=navigator.mimeTypes["application/x-shockwave-flash"],rd=!(!a||!a.enabledPlugin))){sd=td(a.enabledPlugin.description);return}try{var b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");rd=!0;sd=td(b.GetVariable("$version"));
return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");rd=!0;sd="6.0.21";return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"),rd=!0,sd=td(b.GetVariable("$version"))}catch(c){}})();
var ud=rd,vd=sd;function wd(a,b,c){var d="script";d=void 0===d?"":d;var e=a.createElement("link");yb(e,b,"preload");d&&(e.as=d);c&&(e.nonce=c);if(a=a.getElementsByTagName("head")[0])try{a.appendChild(e)}catch(f){}}
;var xd=/^\.google\.(com?\.)?[a-z]{2,3}$/,yd=/\.(cn|com\.bi|do|sl)$/;function zd(a){return xd.test(a)&&!yd.test(a)}
var Bd=p;function Cd(a){a="https://"+("adservice"+a+"/adsid/integrator.js");var b=["domain="+encodeURIComponent(p.location.hostname)];K[3]>=z()&&b.push("adsid="+encodeURIComponent(K[1]));return a+"?"+b.join("&")}
var K,L;function Dd(){Bd=p;K=Bd.googleToken=Bd.googleToken||{};var a=z();K[1]&&K[3]>a&&0<K[2]||(K[1]="",K[2]=-1,K[3]=-1,K[4]="",K[6]="");L=Bd.googleIMState=Bd.googleIMState||{};zd(L[1])||(L[1]=".google.com");w(L[5])||(L[5]=[]);"boolean"==typeof L[6]||(L[6]=!1);w(L[7])||(L[7]=[]);ha(L[8])||(L[8]=0)}
function Ed(){Dd();return K[1]}
var M={da:function(){return 0<L[8]},
Na:function(){L[8]++},
Oa:function(){0<L[8]&&L[8]--},
Pa:function(){L[8]=0},
shouldRetry:function(){return!1},
na:function(){return L[5]},
la:function(a){try{a()}catch(b){p.setTimeout(function(){throw b;},0)}},
ja:function(){if(!M.da()){var a=p.document,b=function(b){b=Cd(b);a:{try{var c=Lb();break a}catch(h){}c=void 0}var d=c;wd(a,b,d);c=a.createElement("script");c.type="text/javascript";d&&(c.nonce=d);c.onerror=function(){return p.processGoogleToken({},2)};
b=Ib(b);zb(c,b);try{(a.head||a.body||a.documentElement).appendChild(c),M.Na()}catch(h){}},c=L[1];
b(c);".google.com"!=c&&b(".google.com");b={};var d=(b.newToken="FBT",b);p.setTimeout(function(){return p.processGoogleToken(d,1)},1E3)}}};
function Fd(a){Dd();var b=Bd.googleToken[5]||0;a&&(0!=b||K[3]>=z()?M.la(a):(M.na().push(a),M.ja()));K[3]>=z()&&K[2]>=z()||M.ja()}
function Gd(a){p.processGoogleToken=p.processGoogleToken||function(a,c){var b=a,e=c;b=void 0===b?{}:b;e=void 0===e?0:e;var f=b.newToken||"",g="NT"==f,h=parseInt(b.freshLifetimeSecs||"",10),k=parseInt(b.validLifetimeSecs||"",10);g&&!k&&(k=3600);var m=b["1p_jar"]||"";b=b.pucrd||"";Dd();1==e?M.Pa():M.Oa();if(!f&&M.shouldRetry())zd(".google.com")&&(L[1]=".google.com"),M.ja();else{var u=Bd.googleToken=Bd.googleToken||{},Z=0==e&&f&&r(f)&&!g&&ha(h)&&0<h&&ha(k)&&0<k&&r(m);g=g&&!M.da()&&(!(K[3]>=z())||"NT"==
K[1]);var Ca=!(K[3]>=z())&&0!=e;if(Z||g||Ca)g=z(),h=g+1E3*h,k=g+1E3*k,1E-5>Math.random()&&(g="https://pagead2.googlesyndication.com/pagead/gen_204?id=imerr&err="+e,p.google_image_requests||(p.google_image_requests=[]),Ca=p.document.createElement("img"),Ca.src=g,p.google_image_requests.push(Ca)),u[5]=e,u[1]=f,u[2]=h,u[3]=k,u[4]=m,u[6]=b,Dd();if(Z||!M.da()){e=M.na();for(f=0;f<e.length;f++)M.la(e[f]);e.length=0}}};
Fd(a)}
;function Hd(a,b){if(1<b.length)a[b[0]]=b[1];else{var c=b[0],d;for(d in c)a[d]=c[d]}}
var N=window.performance&&window.performance.timing&&window.performance.now?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};var Id=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};t("yt.config_",Id,void 0);function O(a){Hd(Id,arguments)}
function P(a,b){return a in Id?Id[a]:b}
function Jd(a){return P(a,void 0)}
function Kd(){return P("PLAYER_CONFIG",{})}
;function Ld(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Q(b)}}:a}
function Q(a,b,c,d,e){var f=v("yt.logging.errors.log");f?f(a,b,c,d,e):(f=P("ERRORS",[]),f.push([a,b,c,d,e]),O("ERRORS",f))}
;function R(a){return P("EXPERIMENT_FLAGS",{})[a]}
;function Md(a){a&&(a.dataset?a.dataset[Nd("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Od(a,b){return a?a.dataset?a.dataset[Nd(b)]:a.getAttribute("data-"+b):null}
var Pd={};function Nd(a){return Pd[a]||(Pd[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function S(a,b){ma(a)&&(a=Ld(a));return window.setTimeout(a,b)}
function Qd(a){window.clearTimeout(a)}
;var Rd=v("ytPubsubPubsubInstance")||new I;I.prototype.subscribe=I.prototype.subscribe;I.prototype.unsubscribeByKey=I.prototype.K;I.prototype.publish=I.prototype.I;I.prototype.clear=I.prototype.clear;t("ytPubsubPubsubInstance",Rd,void 0);var Sd=v("ytPubsubPubsubSubscribedKeys")||{};t("ytPubsubPubsubSubscribedKeys",Sd,void 0);var Td=v("ytPubsubPubsubTopicToKeys")||{};t("ytPubsubPubsubTopicToKeys",Td,void 0);var Ud=v("ytPubsubPubsubIsSynchronous")||{};t("ytPubsubPubsubIsSynchronous",Ud,void 0);
function Vd(a,b){var c=Wd();if(c){var d=c.subscribe(a,function(){var c=arguments;var f=function(){Sd[d]&&b.apply(window,c)};
try{Ud[a]?f():S(f,0)}catch(g){Q(g)}},void 0);
Sd[d]=!0;Td[a]||(Td[a]=[]);Td[a].push(d);return d}return 0}
function Xd(a){var b=Wd();b&&(ha(a)?a=[a]:r(a)&&(a=[parseInt(a,10)]),C(a,function(a){b.unsubscribeByKey(a);delete Sd[a]}))}
function Yd(a,b){var c=Wd();c&&c.publish.apply(c,arguments)}
function Zd(a){var b=Wd();if(b)if(b.clear(a),a)$d(a);else for(var c in Td)$d(c)}
function Wd(){return v("ytPubsubPubsubInstance")}
function $d(a){Td[a]&&(a=Td[a],C(a,function(a){Sd[a]&&delete Sd[a]}),a.length=0)}
;var ae=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,be=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function ce(a,b){if(window.spf){var c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(ae,""),c=c.replace(be,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else de(a,b)}
function de(a,b){var c=ee(a),d=document.getElementById(c),e=d&&Od(d,"loaded"),f=d&&!e;if(e)b&&b();else{if(b){e=Vd(c,b);var g=""+(b[oa]||(b[oa]=++pa));fe[g]=e}f||(d=ge(a,c,function(){Od(d,"loaded")||(Md(d),Yd(c),S(y(Zd,c),0))}))}}
function ge(a,b,c){var d=document.createElement("SCRIPT");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
d.onreadystatechange=function(){switch(d.readyState){case "loaded":case "complete":d.onload()}};
zb(d,Ib(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(d,a.firstChild);return d}
function he(a){a=ee(a);var b=document.getElementById(a);b&&(Zd(a),b.parentNode.removeChild(b))}
function ie(a,b){if(a&&b){var c=""+(b[oa]||(b[oa]=++pa));(c=fe[c])&&Xd(c)}}
function ee(a){var b=document.createElement("a");xb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Ka(a)}
var fe={};var je=null;function ke(){var a=P("BG_I",null),b=P("BG_IU",null),c=P("BG_P",void 0);b?ce(b,function(){window.botguard?le(c):(he(b),Q(Error("Unable to load Botguard from "+b),"WARNING"))}):a&&(eval(a),window.botguard?le(c):Q(Error("Unable to load Botguard from JS"),"WARNING"))}
function le(a){je=new window.botguard.bg(a);R("botguard_periodic_refresh")&&N()}
function me(){return null!=je}
function ne(){return je?je.invoke():null}
;z();var oe=q(XMLHttpRequest)?function(){return new XMLHttpRequest}:q(ActiveXObject)?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function pe(){if(!oe)return null;var a=oe();return"open"in a?a:null}
function qe(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function re(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," "));e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?w(b[f])?ya(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
;var se={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},te=!1;
function ue(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=J(a)[1]||null,e=nd(J(a)[3]||null);d&&e?(d=c,c=J(a),d=J(d),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?nd(J(c)[3]||null)==e&&(Number(J(c)[4]||null)||null)==(Number(J(a)[4]||null)||null):!0;for(var f in se){if((e=d=P(se[f]))&&!(e=c)){e=f;var g=P("CORS_HEADER_WHITELIST")||{},h=nd(J(a)[3]||null);e=h?(g=g[h])?0<=sa(g,e):!1:!0}e&&(b[f]=d)}return b}
function ve(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=we(a,b);var d=xe(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(a){if(!e){e=!0;f&&Qd(f);var c=a.ok,d=function(d){d=d||{};var e=b.context||p;c?b.C&&b.C.call(e,d,a):b.onError&&b.onError.call(e,d,a);b.ia&&b.ia.call(e,d,a)};
"JSON"==(b.format||"JSON")&&(c||400<=a.status&&500>a.status)?a.json().then(d,function(){d(null)}):d(null)}});
b.oa&&0<b.timeout&&(f=S(function(){e||(e=!0,Qd(f),b.oa.call(b.context||p))},b.timeout))}else ye(a,b)}
function ye(a,b){var c=b.format||"JSON";a=we(a,b);var d=xe(a,b),e=!1,f,g=ze(a,function(a){if(!e){e=!0;f&&Qd(f);var d=qe(a),g=null;if(d||400<=a.status&&500>a.status)g=Ae(c,a,b.cb);if(d)a:if(a&&204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(g&&g.return_code,10);break a;case "RAW":d=!0;break a}d=!!g}g=g||{};var h=b.context||p;d?b.C&&b.C.call(h,a,g):b.onError&&b.onError.call(h,a,g);b.ia&&b.ia.call(h,a,g)}},b.method,d,b.headers,b.responseType,b.withCredentials);
b.L&&0<b.timeout&&(f=S(function(){e||(e=!0,g.abort(),Qd(f),b.L.call(b.context||p,g))},b.timeout))}
function we(a,b){b.Da&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=P("XSRF_FIELD_NAME",void 0),d=b.Za;if(d){d[c]&&delete d[c];d=d||{};var e=a.split("#",2);c=e[0];e=1<e.length?"#"+e[1]:"";var f=c.split("?",2);c=f[0];f=re(f[1]||"");for(var g in d)f[g]=d[g];a=qd(c,f)+e}return a}
function xe(a,b){var c=P("XSRF_FIELD_NAME",void 0),d=P("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.A,g=Jd("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.eb||nd(J(a)[3]||null)&&!b.withCredentials&&nd(J(a)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.A&&b.A[g]||(f||(f={}),f[c]=d);f&&r(e)&&(e=re(e),Ya(e,f),e=b.pa&&"JSON"==b.pa?JSON.stringify(e):pd(e));f=e||f&&!Ua(f);!te&&f&&"POST"!=b.method&&(te=!0,Q(Error("AJAX request with postData should use POST")));
return e}
function Ae(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Be(b):null)d={},C(b.getElementsByTagName("*"),function(a){d[a.tagName]=Ce(a)})}c&&De(d);
return d}
function De(a){if(na(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=wb(a[b],null);a[c]=d}else De(a[b])}}
function Be(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Ce(a){var b="";C(a.childNodes,function(a){b+=a.nodeValue});
return b}
function Ee(a,b){b.method="POST";b.A||(b.A={});ye(a,b)}
function ze(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&Ld(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=pe();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c;if(e=ue(a,e))for(var m in e)k.setRequestHeader(m,e[m]),"content-type"==m.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);return k}
;var Fe={},Ge=0;
function He(a,b,c,d,e){e=void 0===e?"":e;a&&(c&&(c=La,c=!(c&&0<=c.toLowerCase().indexOf("cobalt"))),c?a&&(a instanceof E||(a=a.J?a.H():String(a),rb.test(a)||(a="about:invalid#zClosurez"),a=tb(a)),b=qb(a),"about:invalid#zClosurez"===b?a="":(b instanceof ub?a=b:(a=null,b.fa&&(a=b.aa()),b=Aa(b.J?b.H():String(b)),a=wb(b,a)),a=encodeURIComponent(String(uc(a instanceof ub&&a.constructor===ub&&a.va===vb?a.ea:"type_error:SafeHtml")))),/^[\s\xa0]*$/.test(a)||(a=Fb("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+
'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))):e?ze(a,b,"POST",e,d):P("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d?ze(a,b,"GET","",d):Ie(a,b))}
function Ie(a,b){var c=new Image,d=""+Ge++;Fe[d]=c;c.onload=c.onerror=function(){b&&Fe[d]&&b();delete Fe[d]};
c.src=a}
;var Je={},Ke=0;
function Le(a,b,c,d,e,f){f=f||{};f.name=c||P("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||P("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);b=void 0===b?"ERROR":b;e=void 0===e?!1:e;e=window&&window.yterr||(void 0===e?!1:e)||!1;if(a&&e&&!(5<=Ke)){e=a.stacktrace;c=a.columnNumber;d=v("window.location.href");if(r(a))a={message:a,name:"Unknown error",lineNumber:"Not available",fileName:d,stack:"Not available"};else{var g=!1;try{var h=a.lineNumber||a.line||"Not available"}catch(Z){h="Not available",g=!0}try{var k=
a.fileName||a.filename||a.sourceURL||p.$googDebugFname||d}catch(Z){k="Not available",g=!0}a=!g&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:{message:a.message||"Not available",name:a.name||"UnknownError",lineNumber:h,fileName:k,stack:a.stack||"Not available"}}e=e||a.stack;h=a.lineNumber.toString();isNaN(h)||isNaN(c)||(h=h+":"+c);if(!(Je[a.message]||0<=e.indexOf("/YouTubeCenter.js")||0<=e.indexOf("/mytube.js"))){k=e;h={Za:{a:"logerror",t:"jserror",type:a.name,msg:a.message.substr(0,1E3),
line:h,level:void 0===b?"ERROR":b,"client.name":f.name},A:{url:P("PAGE_NAME",window.location.href),file:a.fileName},method:"POST"};f.version&&(h["client.version"]=f.version);k&&(h.A.stack=k);for(var m in f)h.A["client."+m]=f[m];if(m=P("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(var u in m)h.A[u]=m[u];ye("/error_204",h);Je[a.message]=!0;Ke++}}}
;var Me=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};t("yt.msgs_",Me,void 0);function Ne(a){Hd(Me,arguments)}
;function Oe(){}
function Pe(a,b){return Qe(a,1,b)}
;function Re(){}
n(Re,Oe);function Qe(a,b,c){isNaN(c)&&(c=void 0);var d=v("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):S(a,c||0)}
function Se(a){if(!isNaN(a)){var b=v("yt.scheduler.instance.cancelJob");b?b(a):Qd(a)}}
Re.prototype.start=function(){var a=v("yt.scheduler.instance.start");a&&a()};
Re.prototype.pause=function(){var a=v("yt.scheduler.instance.pause");a&&a()};
ja(Re);Re.getInstance();var Te=[],Ue=!1;function Ve(){if("1"!=Ra(Kd(),"args","privembed")){var a=function(){Ue=!0;"google_ad_status"in window?O("DCLKSTAT",1):O("DCLKSTAT",2)};
ce("//static.doubleclick.net/instream/ad_status.js",a);Te.push(Pe(function(){Ue||"google_ad_status"in window||(ie("//static.doubleclick.net/instream/ad_status.js",a),O("DCLKSTAT",3))},5E3))}}
function We(){return parseInt(P("DCLKSTAT",0),10)}
;var Xe=0;t("ytDomDomGetNextId",v("ytDomDomGetNextId")||function(){return++Xe},void 0);var Ye={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Ze(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.event=a;for(var b in a)b in Ye||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?b=a.fromElement:
"mouseout"==this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.b=a.pageX;this.f=a.pageY}}
function $e(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.b=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.f=a.clientY+b}}
Ze.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Ze.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Ze.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var Ta=v("ytEventsEventsListeners")||{};t("ytEventsEventsListeners",Ta,void 0);var af=v("ytEventsEventsCounter")||{count:0};t("ytEventsEventsCounter",af,void 0);function bf(a,b,c,d){d=void 0===d?!1:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Sa(function(e){return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&e[4]==!!d})}
function U(a,b,c){var d=void 0===d?!1:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=bf(a,b,c,d);if(e)return e;e=++af.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(d){d=new Ze(d);if(!Hb(d.relatedTarget,function(b){return b==a}))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new Ze(b);
b.currentTarget=a;return c.call(a,b)};
g=Ld(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),a.addEventListener(b,g,d)):a.attachEvent("on"+b,g);Ta[e]=[a,b,c,g,d];return e}
function cf(a){a&&("string"==typeof a&&(a=[a]),C(a,function(a){if(a in Ta){var b=Ta[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?d.removeEventListener(e,f,b):d.detachEvent&&d.detachEvent("on"+e,f);delete Ta[a]}}))}
;function df(a){this.o=a;this.b=null;this.i=0;this.m=null;this.j=0;this.f=[];for(a=0;4>a;a++)this.f.push(0);this.g=0;this.D=U(window,"mousemove",x(this.F,this));a=x(this.w,this);ma(a)&&(a=Ld(a));this.G=window.setInterval(a,25)}
A(df,G);df.prototype.F=function(a){q(a.b)||$e(a);var b=a.b;q(a.f)||$e(a);this.b=new Ab(b,a.f)};
df.prototype.w=function(){if(this.b){var a=N();if(0!=this.i){var b=this.m,c=this.b,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.i);this.f[this.g]=.5<Math.abs((d-this.j)/this.j)?1:0;for(c=b=0;4>c;c++)b+=this.f[c]||0;3<=b&&this.o();this.j=d}this.i=a;this.m=this.b;this.g=(this.g+1)%4}};
df.prototype.l=function(){window.clearInterval(this.G);cf(this.D)};var ef={};
function ff(a){if(null==v("_lact",window)){var b=parseInt(P("LACT"),10);b=isFinite(b)?z()-Math.max(b,0):-1;t("_lact",b,window);t("_fact",b,window);-1==b&&V();U(document,"keydown",V);U(document,"keyup",V);U(document,"mousedown",V);U(document,"mouseup",V);R("lact_local_listeners")||a?(U(window,"resize",function(){gf("resize",200)}),U(window,"scroll",function(){gf("scroll",200)}),new df(function(){gf("mouse",100)}),U(document,"touchstart",V),U(document,"touchend",V)):(Vd("page-mouse",V),Vd("page-scroll",V),
Vd("page-resize",V))}}
function gf(a,b){ef[a]||(ef[a]=!0,Pe(function(){V();ef[a]=!1},b))}
function V(){null==v("_lact",window)&&ff();var a=z();t("_lact",a,window);-1==v("_fact",window)&&t("_fact",a,window);(a=v("ytglobal.ytUtilActivityCallback_"))&&a()}
function hf(){var a=v("_lact",window);return null==a?-1:Math.max(z()-a,0)}
;function jf(a,b,c,d,e){this.h=a;this.i=b;this.g=c;this.f=d;this.b=e}
function kf(a){var b={};void 0!==a.h?b.trackingParams=a.h:(b.veType=a.i,null!=a.g&&(b.veCounter=a.g),null!=a.f&&(b.elementIndex=a.f));void 0!==a.b&&(b.dataElement=kf(a.b));return b}
var lf=1;var mf={log_event:"events",log_interaction:"interactions"},nf=Object.create(null);nf.log_event="GENERIC_EVENT_LOGGING";nf.log_interaction="INTERACTION_LOGGING";var of={},pf={},qf=0,W=v("ytLoggingTransportLogPayloadsQueue_")||{};t("ytLoggingTransportLogPayloadsQueue_",W,void 0);var rf=v("ytLoggingTransportTokensToCttTargetIds_")||{};t("ytLoggingTransportTokensToCttTargetIds_",rf,void 0);var sf=v("ytLoggingTransportDispatchedStats_")||{};t("ytLoggingTransportDispatchedStats_",sf,void 0);
t("ytytLoggingTransportCapturedTime_",v("ytLoggingTransportCapturedTime_")||{},void 0);function tf(a,b){pf[a.endpoint]=b;if(R("very_optimistically_create_gel_client"))for(var c in W)if(!of[c]){var d=pf[c];d&&(of[c]=new d)}a.W?(c=a.W,d={},c.videoId?d.videoId=c.videoId:c.playlistId&&(d.playlistId=c.playlistId),rf[a.W.token]=d,c=uf(a.endpoint,a.W.token)):c=uf(a.endpoint);c.push(a.payload);c.length>=(Number(R("web_logging_max_batch")||0)||20)?vf():wf()}
function vf(){Qd(qf);if(!Ua(W)){for(var a in W){var b=of[a];if(!b){var c=pf[a];if(!c)continue;b=new c;of[a]=b}c=void 0;var d=a,e=b,f=mf[d],g=sf[d]||{};sf[d]=g;b=Math.round(N());for(c in W[d]){var h=e.b;h={client:{hl:h.Ga,gl:h.Fa,clientName:h.Ea,clientVersion:h.innertubeContextClientVersion}};var k=window.devicePixelRatio;k&&1!=k&&(h.client.screenDensityFloat=String(k));P("DELEGATED_SESSION_ID")&&(h.user={onBehalfOfUser:P("DELEGATED_SESSION_ID")});h={context:h};h[f]=uf(d,c);g.dispatchedEventCount=
g.dispatchedEventCount||0;g.dispatchedEventCount+=h[f].length;h.requestTimeMs=b;if(k=rf[c])a:{var m=h,u=c;if(k.videoId)var Z="VIDEO";else if(k.playlistId)Z="PLAYLIST";else break a;m.credentialTransferTokenTargetId=k;m.context=m.context||{};m.context.user=m.context.user||{};m.context.user.credentialTransferTokens=[{token:u,scope:Z}]}delete rf[c];xf(e,d,h)}c=g;d=b;c.previousDispatchMs&&(b=d-c.previousDispatchMs,e=c.diffCount||0,c.averageTimeBetweenDispatchesMs=e?(c.averageTimeBetweenDispatchesMs*e+
b)/(e+1):b,c.diffCount=e+1);c.previousDispatchMs=d;delete W[a]}Ua(W)||wf()}}
function wf(){Qd(qf);qf=S(vf,P("LOGGING_BATCH_TIMEOUT",1E4))}
function uf(a,b){b=void 0===b?"":b;W[a]=W[a]||{};W[a][b]=W[a][b]||[];return W[a][b]}
;function yf(a,b,c,d){var e=zf,f={};f.eventTimeMs=Math.round(c||N());f[a]=b;f.context={lastActivityMs:String(c?-1:hf())};tf({endpoint:"log_event",payload:f,W:d},e)}
;function Af(a,b,c){c.context&&c.context.capabilities&&(c=c.context.capabilities,c.snapshot||c.golden)&&(a="vix");return"/youtubei/"+a+"/"+b}
;function zf(a){this.b=a||{innertubeApiKey:Jd("INNERTUBE_API_KEY"),innertubeApiVersion:Jd("INNERTUBE_API_VERSION"),Ea:P("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:Jd("INNERTUBE_CONTEXT_CLIENT_VERSION"),Ga:Jd("INNERTUBE_CONTEXT_HL"),Fa:Jd("INNERTUBE_CONTEXT_GL"),Ha:Jd("INNERTUBE_HOST_OVERRIDE")||""}}
function xf(a,b,c){var d={};!P("VISITOR_DATA")&&.01>Math.random()&&Q(Error("Missing VISITOR_DATA when sending innertube request."),"WARNING");var e={headers:{"Content-Type":"application/json","X-Goog-Visitor-Id":P("VISITOR_DATA","")},method:"POST",A:c,pa:"JSON",L:function(){d.L()},
oa:d.L,C:function(a,b){d.C&&d.C(b)},
gb:function(a){d.C&&d.C(a)},
onError:function(a,b){if(d.onError)d.onError(b)},
fb:function(a){if(d.onError)d.onError(a)},
timeout:d.timeout,withCredentials:!0},f=Vb();f&&(e.headers.Authorization=f,e.headers["X-Goog-AuthUser"]=P("SESSION_INDEX",0));var g="",h=a.b.Ha;h&&(g=h);f&&!g&&(e.headers["x-origin"]=window.location.origin);a=""+g+Af(a.b.innertubeApiVersion,b,c)+"?alt=json&key="+a.b.innertubeApiKey;try{R("use_fetch_for_op_xhr")?ve(a,e):Ee(a,e)}catch(k){if("InvalidAccessError"==k)Q(Error("An extension is blocking network request."),"WARNING");else throw k;}}
;var Bf=z().toString();
function Cf(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=z();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(Bf)for(a=1,b=0;b<Bf.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^Bf.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_".charAt(d[b]&63));
return a.join("")}
;var Df=Cf();function Ef(){if(!Ff&&!Gf||!window.JSON)return null;try{var a=Ff.get("yt-player-two-stage-token")}catch(b){}if(!r(a))try{a=Gf.get("yt-player-two-stage-token")}catch(b){}if(!r(a))return null;try{a=JSON.parse(a,void 0)}catch(b){}return a}
var Gf,Hf=new id;Gf=Hf.isAvailable()?new ed(Hf):null;var Ff,If=new jd;Ff=If.isAvailable()?new ed(If):null;function Jf(){var a=P("ROOT_VE_TYPE",void 0);return a?new jf(void 0,a,void 0):null}
function Kf(){var a=P("client-screen-nonce")||P("EVENT_ID");return a?a:null}
;function Lf(a,b,c){Ub.set(""+a,b,c,"/","youtube.com",!1)}
;function Mf(a){if(a){a=a.itct||a.ved;var b=v("yt.logging.screen.storeParentElement");a&&b&&b(new jf(a))}}
;function Nf(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=P("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=P("VALID_SESSION_TEMPDATA_DOMAINS",[]),f=nd(J(window.location.href)[3]||null);f&&e.push(f);f=nd(J(d)[3]||null);if(0<=sa(e,f)||!f&&0==d.lastIndexOf("/",0))if(R("autoescape_tempdata_url")&&(e=document.createElement("a"),xb(e,d),d=e.href),d){f=J(d);d=f[5];e=f[6];f=f[7];var g="";d&&(g+=d);e&&(g+="?"+e);f&&(g+="#"+f);d=g;e=d.indexOf("#");if(d=0>e?d:d.substr(0,e)){if(b.itct||b.ved)b.csn=b.csn||
Kf();if(h){var h=parseInt(h,10);isFinite(h)&&0<h&&(d="ST-"+Ka(d).toString(36),e=b?pd(b):"",Lf(d,e,h||5),Mf(b))}else h="ST-"+Ka(d).toString(36),d=b?pd(b):"",Lf(h,d,5),Mf(b)}}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var k=void 0===k?{}:k;var m=void 0===m?"":m;var u=void 0===u?window:u;c=u.location;a=qd(a,k)+m;a=a instanceof E?a:sb(a);c.href=qb(a)}return!0}
;t("yt.abuse.botguardInitialized",v("yt.abuse.botguardInitialized")||me,void 0);t("yt.abuse.invokeBotguard",v("yt.abuse.invokeBotguard")||ne,void 0);t("yt.abuse.dclkstatus.checkDclkStatus",v("yt.abuse.dclkstatus.checkDclkStatus")||We,void 0);t("yt.player.exports.navigate",v("yt.player.exports.navigate")||Nf,void 0);t("yt.util.activity.init",v("yt.util.activity.init")||ff,void 0);t("yt.util.activity.getTimeSinceActive",v("yt.util.activity.getTimeSinceActive")||hf,void 0);
t("yt.util.activity.setTimestamp",v("yt.util.activity.setTimestamp")||V,void 0);function Of(a,b,c){Pf({attachChild:{csn:a,parentVisualElement:kf(b),visualElements:[kf(c)]}})}
function Pf(a){var b=zf;a.eventTimeMs=Math.round(N());a.lactMs=hf();tf({endpoint:"log_interaction",payload:a},b)}
;function Qf(a){a=a||{};this.url=a.url||"";this.args=a.args||Wa(Rf);this.assets=a.assets||{};this.attrs=a.attrs||Wa(Sf);this.params=a.params||Wa(Tf);this.minVersion=a.min_version||"8.0.0";this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
var Rf={enablejsapi:1},Sf={},Tf={allowscriptaccess:"always",allowfullscreen:"true",bgcolor:"#000000"};function Uf(a){var b=new Qf,c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];b[c]="object"==ka(d)?Wa(d):d}return b}
;function Vf(){G.call(this);this.b=[]}
n(Vf,G);Vf.prototype.l=function(){for(;this.b.length;){var a=this.b.pop();a.target.removeEventListener(a.name,a.bb)}G.prototype.l.call(this)};var Wf=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function Xf(a){a=a||"";if(window.spf){var b=a.match(Wf);spf.style.load(a,b?b[1]:"",void 0)}else Yf(a)}
function Yf(a){var b=Zf(a),c=document.getElementById(b),d=c&&Od(c,"loaded");d||c&&!d||(c=$f(a,b,function(){Od(c,"loaded")||(Md(c),Yd(b),S(y(Zd,b),0))}))}
function $f(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Ib(a);yb(d,a,"stylesheet");(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function Zf(a){var b=document.createElement("A");a=tb(a);xb(b,a);b=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Ka(b)}
;var ag=v("ytLoggingLatencyUsageStats_")||{};t("ytLoggingLatencyUsageStats_",ag,void 0);var bg=0;function cg(a){ag[a]=ag[a]||{count:0};var b=ag[a];b.count++;b.time=N();bg||(bg=Qe(dg,0,5E3));return 10<b.count?(11==b.count&&Le(Error("CSI data exceeded logging limit with key: "+a),0==a.indexOf("info")?"WARNING":"ERROR"),!0):!1}
function dg(){var a=N(),b;for(b in ag)6E4<a-ag[b].time&&delete ag[b];bg=0}
;function eg(a,b){this.version=a;this.args=b}
;function fg(a){this.topic=a}
fg.prototype.toString=function(){return this.topic};var gg=v("ytPubsub2Pubsub2Instance")||new I;I.prototype.subscribe=I.prototype.subscribe;I.prototype.unsubscribeByKey=I.prototype.K;I.prototype.publish=I.prototype.I;I.prototype.clear=I.prototype.clear;t("ytPubsub2Pubsub2Instance",gg,void 0);t("ytPubsub2Pubsub2SubscribedKeys",v("ytPubsub2Pubsub2SubscribedKeys")||{},void 0);t("ytPubsub2Pubsub2TopicToKeys",v("ytPubsub2Pubsub2TopicToKeys")||{},void 0);t("ytPubsub2Pubsub2IsAsync",v("ytPubsub2Pubsub2IsAsync")||{},void 0);
t("ytPubsub2Pubsub2SkipSubKey",null,void 0);function hg(a,b){var c=v("ytPubsub2Pubsub2Instance");c&&c.publish.call(c,a.toString(),a,b)}
;var X=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{};function ig(){var a=P("TIMING_TICK_EXPIRATION");a||(a={},O("TIMING_TICK_EXPIRATION",a));return a}
function jg(){var a=ig(),b;for(b in a)Se(a[b]);O("TIMING_TICK_EXPIRATION",{})}
;function kg(a,b){eg.call(this,1,arguments)}
n(kg,eg);function lg(a,b){eg.call(this,1,arguments)}
n(lg,eg);var mg=new fg("aft-recorded"),ng=new fg("timing-sent");var og={vc:!0},pg={ad_allowed:"adTypesAllowed",ad_at:"adType",ad_cpn:"adClientPlaybackNonce",ad_docid:"adVideoId",yt_ad_an:"adNetworks",p:"httpProtocol",t:"transportProtocol",cpn:"clientPlaybackNonce",csn:"clientScreenNonce",docid:"videoId",is_nav:"isNavigation",yt_lt:"loadType",yt_ad:"isMonetized",nr:"webInfo.navigationReason",ncnp:"webInfo.nonPreloadedNodeCount",paused:"playerInfo.isPausedOnLoad",fmt:"playerInfo.itag",yt_pl:"watchInfo.isPlaylist",yt_ad_pr:"prerollAllowed",yt_red:"isRedSubscriber",
st:"serverTimeMs",vph:"viewportHeight",vpw:"viewportWidth",yt_vis:"isVisible"},sg="ap c cver ei srt yt_fss yt_li plid vpil vpni vpst yt_eil vpni2 vpil2 icrc icrt pa GetBrowse_rid GetPlayer_rid GetSearch_rid GetWatchNext_rid cmt d_vpct d_vpnfi d_vpni pc pfa pfeh pftr prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis yt_ref yt_sts".split(" "),tg="isNavigation isMonetized playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber isVisible watchInfo.isPlaylist".split(" "),
ug=!1;
function vg(a){if("_"!=a[0]){var b=a;X.mark&&(0==b.lastIndexOf("mark_",0)||(b="mark_"+b),X.mark(b))}b=wg();var c=N();b[a]&&(b["_"+a]=b["_"+a]||[b[a]],b["_"+a].push(c));b[a]=c;b=ig();if(c=b[a])Se(c),b[a]=0;xg()["tick_"+a]=void 0;N();R("csi_on_gel")?(b=yg(),"_start"==a?cg("baseline_"+b)||yf("latencyActionBaselined",{clientActionNonce:b},void 0,void 0):cg("tick_"+a+"_"+b)||yf("latencyActionTicked",{tickName:a,clientActionNonce:b},void 0,void 0),a=!0):a=!1;if(a=!a)a=!v("yt.timing.pingSent_");if(a&&(b=
Jd("TIMING_ACTION"),a=wg(),v("ytglobal.timingready_")&&b&&a._start&&(b=zg()))){R("tighter_critical_section")&&!ug&&(hg(mg,new kg(Math.round(b-a._start),void 0)),ug=!0);b=!0;c=P("TIMING_WAIT",[]);if(c.length)for(var d=0,e=c.length;d<e;++d)if(!(c[d]in a)){b=!1;break}b&&Ag()}}
function Bg(){var a=Cg().info.yt_lt="hot_bg";xg().info_yt_lt=a;if(R("csi_on_gel"))if("yt_lt"in pg){var b={},c=pg.yt_lt;0<=sa(tg,c)&&(a=!!a);c=c.split(".");for(var d=b,e=0;e<c.length-1;e++)d[c[e]]=d[c[e]]||{},d=d[c[e]];b[c[c.length-1]]=a;a=yg();c=Object.keys(b).join("");cg("info_"+c+"_"+a)||(b.clientActionNonce=a,yf("latencyActionInfo",b,void 0,void 0))}else 0<=sa(sg,"yt_lt")||Q(Error("Unknown label yt_lt logged with GEL CSI."))}
function zg(){var a=wg();if(a.aft)return a.aft;for(var b=P("TIMING_AFT_KEYS",["ol"]),c=b.length,d=0;d<c;d++){var e=a[b[d]];if(e)return e}return NaN}
function Ag(){jg();if(!R("csi_on_gel")){var a=wg(),b=Cg().info,c=a._start,d;for(d in a)if(0==d.lastIndexOf("_",0)&&w(a[d])){var e=d.slice(1);if(e in og){var f=ua(a[d],function(a){return Math.round(a-c)});
b["all_"+e]=f.join()}delete a[d]}e=!!b.ap;if(f=v("ytglobal.timingReportbuilder_")){if(f=f(a,b,void 0))Dg(f,e),Eg(),Fg(),Gg(!1,void 0),P("TIMING_ACTION")&&O("PREVIOUS_ACTION",P("TIMING_ACTION")),O("TIMING_ACTION","")}else{var g=P("CSI_SERVICE_NAME","youtube");f={v:2,s:g,action:P("TIMING_ACTION",void 0)};var h=b.srt;void 0!==a.srt&&delete b.srt;if(b.h5jse){var k=window.location.protocol+v("ytplayer.config.assets.js");(k=X.getEntriesByName?X.getEntriesByName(k)[0]:null)?b.h5jse=Math.round(b.h5jse-k.responseEnd):
delete b.h5jse}a.aft=zg();Hg()&&"youtube"==g&&(Bg(),g=a.vc,k=a.pbs,delete a.aft,b.aft=Math.round(k-g));for(var m in b)"_"!=m.charAt(0)&&(f[m]=b[m]);a.ps=N();b={};m=[];for(d in a)"_"!=d.charAt(0)&&(g=Math.round(a[d]-c),b[d]=g,m.push(d+"."+g));f.rt=m.join(",");(a=v("ytdebug.logTiming"))&&a(f,b);Dg(f,e,void 0);hg(ng,new lg(b.aft+(h||0),void 0))}}}
var Fg=x(X.clearResourceTimings||X.webkitClearResourceTimings||X.mozClearResourceTimings||X.msClearResourceTimings||X.oClearResourceTimings||ia,X);
function Dg(a,b,c){if(R("debug_csi_data")){var d=v("yt.timing.csiData");d||(d=[],t("yt.timing.csiData",d,void 0));d.push({page:location.href,time:new Date,args:a})}d="";for(var e in a)d+="&"+e+"="+a[e];a="/csi_204?"+d.substring(1);if(window.navigator&&window.navigator.sendBeacon&&b){var f=void 0===f?"":f;try{window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,f)||He(a,void 0,void 0,void 0,f)}catch(g){He(a,void 0,void 0,void 0,f)}}else He(a);Gg(!0,c)}
function yg(){var a=Cg().nonce;a||(a=Cf(),Cg().nonce=a);return a}
function wg(){return Cg().tick}
function xg(){var a=Cg();"gel"in a||(a.gel={});return a.gel}
function Cg(){return v("ytcsi.data_")||Eg()}
function Eg(){var a={tick:{},info:{}};t("ytcsi.data_",a,void 0);return a}
function Gg(a,b){t("yt.timing."+(b||"")+"pingSent_",a,void 0)}
function Hg(){var a=wg(),b=a.pbr,c=a.vc;a=a.pbs;return b&&c&&a&&b<c&&c<a&&1==Cg().info.yt_pvis}
;function Ig(a,b){G.call(this);this.m=this.S=a;this.G=b;this.o=!1;this.f={};this.P=this.F=null;this.w=new I;jc(this,y(kc,this.w));this.i={};this.N=this.R=this.g=this.Y=this.b=null;this.M=!1;this.j=this.D=null;this.T={};this.ta=["onReady"];this.X=null;this.ka=NaN;this.O={};Jg(this);this.V("WATCH_LATER_VIDEO_ADDED",this.Ja.bind(this));this.V("WATCH_LATER_VIDEO_REMOVED",this.Ka.bind(this));this.V("onAdAnnounce",this.xa.bind(this));this.ua=new Vf(this);jc(this,y(kc,this.ua))}
n(Ig,G);l=Ig.prototype;
l.ha=function(a){if(!this.h){a instanceof Qf||(a=new Qf(a));this.Y=a;this.b=Uf(a);this.g=this.b.attrs.id||this.g;"video-player"==this.g&&(this.g=this.G,this.b.attrs.id=this.G);this.m.id==this.g&&(this.g+="-player",this.b.attrs.id=this.g);this.b.args.enablejsapi="1";this.b.args.playerapiid=this.G;this.R||(this.R=Kg(this,this.b.args.jsapicallback||"onYouTubePlayerReady"));this.b.args.jsapicallback=null;if(a=this.b.attrs.width)this.m.style.width=Nb(Number(a)||a);if(a=this.b.attrs.height)this.m.style.height=Nb(Number(a)||
a);Lg(this);this.o&&Mg(this)}};
l.Aa=function(){return this.Y};
function Mg(a){a.b.loaded||(a.b.loaded=!0,"0"!=a.b.args.autoplay?a.f.loadVideoByPlayerVars(a.b.args):a.f.cueVideoByPlayerVars(a.b.args))}
function Ng(a){var b=!0,c=Og(a);c&&a.b&&(a=a.b,b=Od(c,"version")==a.assets.js);return b&&!!v("yt.player.Application.create")}
function Lg(a){if(!a.h&&!a.M){var b=Ng(a);if(b&&"html5"==(Og(a)?"html5":null))a.N="html5",a.o||Pg(a);else if(Qg(a),a.N="html5",b&&a.j)a.S.appendChild(a.j),Pg(a);else{a.b.loaded=!0;var c=!1;a.D=function(){c=!0;var b=Uf(a.b);v("yt.player.Application.create")(a.S,b);Pg(a)};
a.M=!0;b?a.D():(ce(a.b.assets.js,a.D),Xf(a.b.assets.css),Rg(a)&&!c&&t("yt.player.Application.create",null,void 0))}}}
function Og(a){var b=Cb(a.g);!b&&a.m&&a.m.querySelector&&(b=a.m.querySelector("#"+a.g));return b}
function Pg(a){if(!a.h){var b=Og(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);c?(a.M=!1,b.isNotServable&&b.isNotServable(a.b.args.video_id)||Sg(a)):a.ka=S(function(){Pg(a)},50)}}
function Sg(a){Jg(a);a.o=!0;var b=Og(a);b.addEventListener&&(a.F=Tg(a,b,"addEventListener"));b.removeEventListener&&(a.P=Tg(a,b,"removeEventListener"));var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=0;d<c.length;d++){var e=c[d];a.f[e]||(a.f[e]=Tg(a,b,e))}for(var f in a.i)a.F(f,a.i[f]);Mg(a);a.R&&a.R(a.f);a.w.I("onReady",a.f)}
function Tg(a,b,c){var d=b[c];return function(){try{return a.X=null,d.apply(b,arguments)}catch(e){"sendAbandonmentPing"!=c&&(e.message+=" ("+c+")",a.X=e,Q(e,"WARNING",void 0,void 0,void 0))}}}
function Jg(a){a.o=!1;if(a.P)for(var b in a.i)a.P(b,a.i[b]);for(var c in a.O)Qd(parseInt(c,10));a.O={};a.F=null;a.P=null;for(var d in a.f)a.f[d]=null;a.f.addEventListener=a.V.bind(a);a.f.removeEventListener=a.Qa.bind(a);a.f.destroy=a.dispose.bind(a);a.f.getLastError=a.Ba.bind(a);a.f.getPlayerType=a.Ca.bind(a);a.f.getCurrentVideoConfig=a.Aa.bind(a);a.f.loadNewVideoConfig=a.ha.bind(a);a.f.isReady=a.Ia.bind(a)}
l.Ia=function(){return this.o};
l.V=function(a,b){var c=this,d=Kg(this,b);if(d){if(!(0<=sa(this.ta,a)||this.i[a])){var e=Ug(this,a);this.F&&this.F(a,e)}this.w.subscribe(a,d);"onReady"==a&&this.o&&S(function(){d(c.f)},0)}};
l.Qa=function(a,b){if(!this.h){var c=Kg(this,b);c&&Yc(this.w,a,c)}};
function Kg(a,b){var c=b;if("string"==typeof b){if(a.T[b])return a.T[b];c=function(){var a=v(b);a&&a.apply(p,arguments)};
a.T[b]=c}return c?c:null}
function Ug(a,b){var c="ytPlayer"+b+a.G;a.i[b]=c;p[c]=function(c){var d=a.b&&a.b.args&&a.b.args.fflags;if(d&&0>d.indexOf("use_html5_player_event_timeout=true"))a.w.I(b,c);else{var f=S(function(){if(!a.h){a.w.I(b,c);var d=a.O,e=String(f);e in d&&delete d[e]}},0);
Va(a.O,String(f))}};
return c}
l.xa=function(a){Yd("a11y-announce",a)};
l.Ja=function(a){Yd("WATCH_LATER_VIDEO_ADDED",a)};
l.Ka=function(a){Yd("WATCH_LATER_VIDEO_REMOVED",a)};
l.Ca=function(){return this.N||(Og(this)?"html5":null)};
l.Ba=function(){return this.X};
function Qg(a){vg("dcp");a.cancel();Jg(a);a.N=null;a.b&&(a.b.loaded=!1);var b=Og(a);b&&(Ng(a)||!Rg(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));for(a=a.S;b=a.firstChild;)a.removeChild(b)}
l.cancel=function(){this.D&&ie(this.b.assets.js,this.D);Qd(this.ka);this.M=!1};
l.l=function(){Qg(this);if(this.j&&this.b&&this.j.destroy)try{this.j.destroy()}catch(b){Q(Error("Error destroying player: "+b))}this.T=null;for(var a in this.i)p[this.i[a]]=null;this.Y=this.b=this.f=null;delete this.S;delete this.m;G.prototype.l.call(this)};
function Rg(a){return a.b&&a.b.args&&a.b.args.fflags?-1!=a.b.args.fflags.indexOf("player_destroy_old_version=true"):!1}
;var Vg={},Wg="player_uid_"+(1E9*Math.random()>>>0);function Xg(a){var b="player";b=r(b)?Cb(b):b;var c=Wg+"_"+(b[oa]||(b[oa]=++pa)),d=Vg[c];if(d)return d.ha(a),d.f;d=new Ig(b,c);Vg[c]=d;Yd("player-added",d.f);jc(d,y(Yg,d));S(function(){d.ha(a)},0);
return d.f}
function Yg(a){delete Vg[a.G]}
;function Zg(a){return(0==a.search("cue")||0==a.search("load"))&&"loadModule"!=a}
function $g(a,b,c){r(a)&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});b=/\/([ve]|embed)\/([^#?]+)/.exec(a.mediaContentUrl);a.videoId=b&&b[2]?b[2]:null;return ah(a)}
function ah(a,b,c){if(na(a)){b="endSeconds startSeconds mediaContentUrl suggestedQuality videoId two_stage_token".split(" ");c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}return{videoId:a,startSeconds:b,suggestedQuality:c}}
function bh(a,b,c,d){if(na(a)&&!w(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};r(a)&&16==a.length?b.list="PL"+a:b.playlist=a;return b}
function ch(a){var b=a.video_id||a.videoId;if(r(b)){var c=Ef()||{},d=Ef()||{};q(void 0)?d[b]=void 0:delete d[b];var e=z()+3E5,f=Gf;if(f&&window.JSON){r(d)||(d=JSON.stringify(d,void 0));try{f.set("yt-player-two-stage-token",d,e)}catch(g){f.remove("yt-player-two-stage-token")}}(b=c[b])&&(a.two_stage_token=b)}}
;function dh(a){G.call(this);this.b=a;this.b.subscribe("command",this.qa,this);this.f={};this.i=!1}
A(dh,G);l=dh.prototype;l.start=function(){this.i||this.h||(this.i=!0,eh(this.b,"RECEIVING"))};
l.qa=function(a,b,c){if(this.i&&!this.h){var d=b||{};switch(a){case "addEventListener":r(d.event)&&(a=d.event,a in this.f||(c=x(this.Sa,this,a),this.f[a]=c,this.addEventListener(a,c)));break;case "removeEventListener":r(d.event)&&fh(this,d.event);break;default:this.g.isReady()&&this.g[a]&&(b=gh(a,b||{}),c=this.g.handleExternalCall(a,b,c||null),(c=hh(a,c))&&this.i&&!this.h&&eh(this.b,a,c))}}};
l.Sa=function(a,b){this.i&&!this.h&&eh(this.b,a,this.ba(a,b))};
l.ba=function(a,b){if(null!=b)return{value:b}};
function fh(a,b){b in a.f&&(a.removeEventListener(b,a.f[b]),delete a.f[b])}
l.l=function(){var a=this.b;a.h||Yc(a.b,"command",this.qa,this);this.b=null;for(var b in this.f)fh(this,b);dh.u.l.call(this)};function ih(a,b){dh.call(this,b);this.g=a;this.start()}
A(ih,dh);ih.prototype.addEventListener=function(a,b){this.g.addEventListener(a,b)};
ih.prototype.removeEventListener=function(a,b){this.g.removeEventListener(a,b)};
function gh(a,b){switch(a){case "loadVideoById":return b=ah(b),ch(b),[b];case "cueVideoById":return b=ah(b),ch(b),[b];case "loadVideoByPlayerVars":return ch(b),[b];case "cueVideoByPlayerVars":return ch(b),[b];case "loadPlaylist":return b=bh(b),ch(b),[b];case "cuePlaylist":return b=bh(b),ch(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];
case "setLoop":return[b.loopPlaylists];case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey]}return[]}
function hh(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
ih.prototype.ba=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return ih.u.ba.call(this,a,b)};
ih.prototype.l=function(){ih.u.l.call(this);delete this.g};function jh(a,b,c,d){G.call(this);this.f=b||null;this.o="*";this.g=c||null;this.sessionId=null;this.channel=d||null;this.D=!!a;this.m=x(this.w,this);window.addEventListener("message",this.m)}
n(jh,G);jh.prototype.w=function(a){if(!("*"!=this.g&&a.origin!=this.g||this.f&&a.source!=this.f)&&r(a.data)){try{var b=JSON.parse(a.data)}catch(c){return}if(!(null==b||this.D&&(this.sessionId&&this.sessionId!=b.id||this.channel&&this.channel!=b.channel))&&b)switch(b.event){case "listening":"null"!=a.origin&&(this.g=this.o=a.origin);this.f=a.source;this.sessionId=b.id;this.b&&(this.b(),this.b=null);break;case "command":this.i&&(!this.j||0<=sa(this.j,b.func))&&this.i(b.func,b.args,a.origin)}}};
jh.prototype.sendMessage=function(a,b){var c=b||this.f;if(c){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var d=uc(a);c.postMessage(d,this.o)}catch(e){Q(e,"WARNING")}}};
jh.prototype.l=function(){window.removeEventListener("message",this.m);G.prototype.l.call(this)};function kh(a,b,c){jh.call(this,a,b,c||P("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname,"widget");this.j=this.b=this.i=null}
n(kh,jh);function lh(){var a=this.f=new kh(!!P("WIDGET_ID_ENFORCE")),b=x(this.Ma,this);a.i=b;a.j=null;this.f.channel="widget";if(a=P("WIDGET_ID"))this.f.sessionId=a;this.g=[];this.j=!1;this.i={}}
l=lh.prototype;l.Ma=function(a,b,c){"addEventListener"==a&&b?(a=b[0],this.i[a]||"onReady"==a||(this.addEventListener(a,mh(this,a)),this.i[a]=!0)):this.sa(a,b,c)};
l.sa=function(){};
function mh(a,b){return x(function(a){this.sendMessage(b,a)},a)}
l.addEventListener=function(){};
l.za=function(){this.j=!0;this.sendMessage("initialDelivery",this.ca());this.sendMessage("onReady");C(this.g,this.ra,this);this.g=[]};
l.ca=function(){return null};
function nh(a,b){a.sendMessage("infoDelivery",b)}
l.ra=function(a){this.j?this.f.sendMessage(a):this.g.push(a)};
l.sendMessage=function(a,b){this.ra({event:a,info:void 0==b?null:b})};
l.dispose=function(){this.f=null};function oh(a){lh.call(this);this.b=a;this.h=[];this.addEventListener("onReady",x(this.La,this));this.addEventListener("onVideoProgress",x(this.Wa,this));this.addEventListener("onVolumeChange",x(this.Xa,this));this.addEventListener("onApiChange",x(this.Ra,this));this.addEventListener("onPlaybackQualityChange",x(this.Ta,this));this.addEventListener("onPlaybackRateChange",x(this.Ua,this));this.addEventListener("onStateChange",x(this.Va,this));this.addEventListener("onWebglSettingsChanged",x(this.Ya,
this))}
A(oh,lh);l=oh.prototype;l.sa=function(a,b,c){if(this.b[a]){b=b||[];if(0<b.length&&Zg(a)){var d=b;if(na(d[0])&&!w(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=ah.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=$g.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=bh.apply(window,d)}d=e}ch(d);b.length=1;b[0]=d}this.b.handleExternalCall(a,b,c);Zg(a)&&nh(this,this.ca())}};
l.La=function(){var a=x(this.za,this);this.f.b=a};
l.addEventListener=function(a,b){this.h.push({eventType:a,listener:b});this.b.addEventListener(a,b)};
l.ca=function(){if(!this.b)return null;var a=this.b.getApiInterface();wa(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c],f=e;if(0==f.search("get")||0==f.search("is")){f=e;var g=0;0==f.search("get")?g=3:0==f.search("is")&&(g=2);f=f.charAt(g).toLowerCase()+f.substr(g+1);try{var h=this.b[e]();b[f]=h}catch(k){}}}b.videoData=this.b.getVideoData();b.currentTimeLastUpdated_=z()/1E3;return b};
l.Va=function(a){a={playerState:a,currentTime:this.b.getCurrentTime(),duration:this.b.getDuration(),videoData:this.b.getVideoData(),videoStartBytes:0,videoBytesTotal:this.b.getVideoBytesTotal(),videoLoadedFraction:this.b.getVideoLoadedFraction(),playbackQuality:this.b.getPlaybackQuality(),availableQualityLevels:this.b.getAvailableQualityLevels(),videoUrl:this.b.getVideoUrl(),playlist:this.b.getPlaylist(),playlistIndex:this.b.getPlaylistIndex(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),
mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());this.b.getStoryboardFormat&&(a.storyboardFormat=this.b.getStoryboardFormat());nh(this,a)};
l.Ta=function(a){nh(this,{playbackQuality:a})};
l.Ua=function(a){nh(this,{playbackRate:a})};
l.Ra=function(){for(var a=this.b.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.b.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],m=this.b.getOption(e,k);b[e][k]=m}}this.sendMessage("apiInfoDelivery",b)};
l.Xa=function(){nh(this,{muted:this.b.isMuted(),volume:this.b.getVolume()})};
l.Wa=function(a){a={currentTime:a,videoBytesLoaded:this.b.getVideoBytesLoaded(),videoLoadedFraction:this.b.getVideoLoadedFraction(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());nh(this,a)};
l.Ya=function(){if(this.b.getSphericalConfig){var a={sphericalConfig:this.b.getSphericalConfig()};nh(this,a)}};
l.dispose=function(){oh.u.dispose.call(this);for(var a=0;a<this.h.length;a++){var b=this.h[a];this.b.removeEventListener(b.eventType,b.listener)}this.h=[]};function ph(){G.call(this);this.b=new I;jc(this,y(kc,this.b))}
A(ph,G);ph.prototype.subscribe=function(a,b,c){return this.h?0:this.b.subscribe(a,b,c)};
ph.prototype.j=function(a,b){this.h||this.b.I.apply(this.b,arguments)};function qh(a,b,c){ph.call(this);this.f=a;this.g=b;this.i=c}
A(qh,ph);function eh(a,b,c){if(!a.h){var d=a.f;d.h||a.g!=d.b||(a={id:a.i,command:b},c&&(a.data=c),d.b.postMessage(uc(a),d.g))}}
qh.prototype.l=function(){this.g=this.f=null;qh.u.l.call(this)};function rh(a,b,c){G.call(this);this.b=a;this.g=c;this.i=U(window,"message",x(this.j,this));this.f=new qh(this,a,b);jc(this,y(kc,this.f))}
A(rh,G);rh.prototype.j=function(a){var b;if(b=!this.h)if(b=a.origin==this.g)a:{b=this.b;do{b:{var c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,r(b))){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.f,c.h||c.j("command",b.command,b.data,a.origin))}};
rh.prototype.l=function(){cf(this.i);this.b=null;rh.u.l.call(this)};function sh(){var a=th()?"//googleads.g.doubleclick.net/pagead/id?exp=nomnom":"//googleads.g.doubleclick.net/pagead/id",b=Wa(uh);return new H(function(c,d){b.C=function(a){qe(a)?c(a):d(new vh("Request failed, status="+a.status,"net.badstatus",a))};
b.onError=function(a){d(new vh("Unknown request error","net.unknown",a))};
b.L=function(a){d(new vh("Request timed out","net.timeout",a))};
ye(a,b)})}
function vh(a,b){B.call(this,a+", errorCode="+b);this.errorCode=b;this.name="PromiseAjaxError"}
n(vh,B);function wh(a){this.h=void 0===a?null:a;this.f=0;this.b=null}
wh.prototype.then=function(a,b,c){return this.h?this.h.then(a,b,c):1===this.f&&a?(a=a.call(c,this.b),Bc(a)?a:xh(a)):2===this.f&&b?(a=b.call(c,this.b),Bc(a)?a:yh(a)):this};
wh.prototype.getValue=function(){return this.b};
Ac(wh);function yh(a){var b=new wh;a=void 0===a?null:a;b.f=2;b.b=void 0===a?null:a;return b}
function xh(a){var b=new wh;a=void 0===a?null:a;b.f=1;b.b=void 0===a?null:a;return b}
;function zh(a){B.call(this,a.message||a.description||a.name);this.isMissing=a instanceof Ah;this.isTimeout=a instanceof vh&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Pc}
n(zh,B);zh.prototype.name="BiscottiError";function Ah(){B.call(this,"Biscotti ID is missing from server")}
n(Ah,B);Ah.prototype.name="BiscottiMissingError";var uh={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},Bh=null;function Ch(){if("1"===Ra(Kd(),"args","privembed"))return Gc(Error("Biscotti ID is not available in private embed mode"));Bh||(Bh=Oc(sh().then(Dh),function(a){return Eh(2,a)}));
return Bh}
function th(){var a;(a=!!Ra(window,"settings","experiments","flags","html5_serverside_pagead_id_sets_cookie"))||(a=!!P("EXP_HTML5_SERVERSIDE_PAGEAD_ID_SETS_COOKIE",!1));return a||!!R("html5_serverside_pagead_id_sets_cookie")}
function Dh(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new Ah;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new Ah;a=a.id;Fh(a);Bh=xh(a);Gh(18E5,2);return a}
function Eh(a,b){var c=new zh(b);Fh("");Bh=yh(c);0<a&&Gh(12E4,a-1);throw c;}
function Gh(a,b){S(function(){Oc(sh().then(Dh,function(a){return Eh(b,a)}),ia)},a)}
function Fh(a){t("yt.ads.biscotti.lastId_",a,void 0)}
function Hh(){try{var a=v("yt.ads.biscotti.getId_");return a?a():Ch()}catch(b){return Gc(b)}}
;function Ih(a){B.apply(this,arguments)}
n(Ih,B);Ih.prototype.name="YuzuError";function Jh(){var a=new Ih("ID is missing"),b=new Ih("Timeout"),c=null,d=!1;Gd(function(){c=Ed();d=!0});
if(d)return c?xh(c):yh(a);var e=new H(function(b,c){Gd(function(){var d=Ed();d?b(d):c(a)})}),f=ld().then(function(){return Gc(b)});
return Mc(Jc([e,f]),function(){return f.cancel()})}
;function Kh(a){if("1"!==Ra(Kd(),"args","privembed")){a&&!v("yt.ads.biscotti.getId_")&&t("yt.ads.biscotti.getId_",Ch,void 0);try{var b=Hh();if(R("enable_yuzu")){v("yt.ads.yuzu.getId_")||t("yt.ads.yuzu.getId_",Jh,void 0);try{var c=v("yt.ads.yuzu.getId_")()}catch(d){c=Gc(d)}}else c=Gc(new Ih("unimplemented"));Kc([b,c]).then(function(a){var b=a[0];a=a[1];if(b.Z||a.Z){b=b.value;a=a.value;var c={};c.dt=Ob;c.flash=vd||"0";a:{try{var d=window.top.location.href}catch(Pa){d=2;break a}d=null!=d?d==window.document.location.href?
0:1:2}d=(c.frm=d,c);d.u_tz=-(new Date).getTimezoneOffset();var h=void 0===h?F:h;try{var k=h.history.length}catch(Pa){k=0}d.u_his=k;d.u_java=!!F.navigator&&"unknown"!==typeof F.navigator.javaEnabled&&!!F.navigator.javaEnabled&&F.navigator.javaEnabled();F.screen&&(d.u_h=F.screen.height,d.u_w=F.screen.width,d.u_ah=F.screen.availHeight,d.u_aw=F.screen.availWidth,d.u_cd=F.screen.colorDepth);F.navigator&&F.navigator.plugins&&(d.u_nplug=F.navigator.plugins.length);F.navigator&&F.navigator.mimeTypes&&(d.u_nmime=
F.navigator.mimeTypes.length);d.ca_type=ud?"flash":"image";if(R("enable_server_side_search_pyv")||R("enable_server_side_mweb_search_pyv")){k=window;try{var m=k.screenX;var u=k.screenY}catch(Pa){}try{var Z=k.outerWidth;var Ca=k.outerHeight}catch(Pa){}try{var qg=k.innerWidth;var rg=k.innerHeight}catch(Pa){}m=[k.screenLeft,k.screenTop,m,u,k.screen?k.screen.availWidth:void 0,k.screen?k.screen.availTop:void 0,Z,Ca,qg,rg];u=window.top;try{var T=(u||window).document,Oa="CSS1Compat"==T.compatMode?T.documentElement:
T.body;var Da=(new Bb(Oa.clientWidth,Oa.clientHeight)).round()}catch(Pa){Da=new Bb(-12245933,-12245933)}T={};Oa=0;p.SVGElement&&p.document.createElementNS&&(Oa|=1);T.bc=Oa;T.bih=Da.height;T.biw=Da.width;T.brdim=m.join();Da=(T.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[Mb.visibilityState||Mb.webkitVisibilityState||Mb.mozVisibilityState||""]||0,T.wgl=!!F.WebGLRenderingContext,T);for(var Ad in Da)d[Ad]=Da[Ad]}void 0!==b&&(d.bid=b);void 0!==a&&(d.anid=a);d.bsq=Lh++;Ee("//www.youtube.com/ad_data_204",
{Da:!1,A:d})}});
S(Kh,18E5)}catch(d){Q(d)}}}
var Lh=0;var Y=v("ytglobal.prefsUserPrefsPrefs_")||{};t("ytglobal.prefsUserPrefsPrefs_",Y,void 0);function Mh(){this.b=P("ALT_PREF_COOKIE_NAME","PREF");var a;if(a=Ub.get(""+this.b,void 0)){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Y[d]=c.toString())}}}
l=Mh.prototype;l.get=function(a,b){Nh(a);Oh(a);var c=void 0!==Y[a]?Y[a].toString():null;return null!=c?c:b?b:""};
l.set=function(a,b){Nh(a);Oh(a);if(null==b)throw Error("ExpectedNotNull");Y[a]=b.toString()};
l.remove=function(a){Nh(a);Oh(a);delete Y[a]};
l.save=function(){var a=this.b,b=[],c;for(c in Y)b.push(c+"="+encodeURIComponent(String(Y[c])));Lf(a,b.join("&"),63072E3)};
l.clear=function(){for(var a in Y)delete Y[a]};
function Oh(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function Nh(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function Ph(a){a=void 0!==Y[a]?Y[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
ja(Mh);var Qh=null,Rh=null,Sh=null,Th={};function Uh(a){yf(a.payload_name,a.payload,void 0,void 0)}
function Vh(a){var b=a.id;a=a.ve_type;var c=lf++;a=new jf(void 0,a,c,void 0,void 0);Th[b]=a;b=Kf();c=Jf();b&&c&&Of(b,c,a)}
function Wh(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(O("client-screen-nonce",b),O("ROOT_VE_TYPE",a),b&&yf("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:Df,clientScreenNonce:b}),a=Jf()))for(var c in Th){var d=Th[c];d&&Of(b,a,d)}}
function Xh(a){Th[a.id]=new jf(a.tracking_params)}
function Yh(a){var b=Kf();a=Th[a.id];b&&a&&(R("interaction_click_on_gel_web")?yf("visualElementGestured",{csn:b,ve:kf(a),gestureType:"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK"}):Pf({click:{csn:b,visualElement:kf(a)}}))}
function Zh(a){a=a.ids;var b=Kf();if(b)for(var c=0;c<a.length;c++){var d=Th[a[c]];d&&yf("visualElementShown",{csn:b,ve:kf(d),eventType:1})}}
function $h(){var a=Qh;a&&a.startInteractionLogging&&a.startInteractionLogging()}
;t("yt.setConfig",O,void 0);t("yt.config.set",O,void 0);t("yt.setMsg",Ne,void 0);t("yt.msgs.set",Ne,void 0);t("yt.logging.errors.log",Le,void 0);
t("writeEmbed",function(){var a=P("PLAYER_CONFIG",void 0);Kh(!0);"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");var b=document.referrer,c=P("POST_MESSAGE_ORIGIN");window!=window.top&&b&&b!=document.URL&&(a.args.loaderUrl=b);P("LIGHTWEIGHT_AUTOPLAY")&&(a.args.autoplay="1");a.args.autoplay&&ch(a.args);Qh=a=Xg(a);a.addEventListener("onScreenChanged",Wh);a.addEventListener("onLogClientVeCreated",Vh);a.addEventListener("onLogServerVeCreated",Xh);a.addEventListener("onLogToGel",Uh);
a.addEventListener("onLogVeClicked",Yh);a.addEventListener("onLogVesShown",Zh);a.addEventListener("onReady",$h);b=P("POST_MESSAGE_ID","player");P("ENABLE_JS_API")?Sh=new oh(a):P("ENABLE_POST_API")&&r(b)&&r(c)&&(Rh=new rh(window.parent,b,c),Sh=new ih(a,Rh.f));P("BG_P")&&(P("BG_I")||P("BG_IU"))&&ke();Ve()},void 0);
t("yt.www.watch.ads.restrictioncookie.spr",function(a){He(a+"mac_204?action_fcts=1");return!0},void 0);
var ai=Ld(function(){vg("ol");var a=Mh.getInstance(),b=!!((Ph("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&nc(document.body,"exp-invert-logo"))if(c&&!nc(document.body,"inverted-hdpi")){var d=document.body;d.classList?d.classList.add("inverted-hdpi"):nc(d,"inverted-hdpi")||(d.className+=0<d.className.length?" inverted-hdpi":"inverted-hdpi")}else!c&&nc(document.body,"inverted-hdpi")&&oc();b!=c&&(b="f"+(Math.floor(119/31)+1),d=Ph(b)||0,d=c?d|67108864:d&-67108865,
0==d?delete Y[b]:Y[b]=d.toString(16).toString(),a.save())}),bi=Ld(function(){var a=Qh;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();P("PL_ATT")&&(je=null);a=0;for(var b=Te.length;a<b;a++)Se(Te[a]);Te.length=0;he("//static.doubleclick.net/instream/ad_status.js");Ue=!1;O("DCLKSTAT",0);lc(Sh,Rh);if(a=Qh)a.removeEventListener("onScreenChanged",Wh),a.removeEventListener("onLogClientVeCreated",Vh),a.removeEventListener("onLogServerVeCreated",Xh),a.removeEventListener("onLogToGel",Uh),a.removeEventListener("onLogVeClicked",Yh),a.removeEventListener("onLogVesShown",Zh),a.removeEventListener("onReady",
$h),a.destroy();Th={}});
window.addEventListener?(window.addEventListener("load",ai),window.addEventListener("unload",bi)):window.attachEvent&&(window.attachEvent("onload",ai),window.attachEvent("onunload",bi));}).call(this);
