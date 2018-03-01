(function(){var l,ba="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ca;
if("function"==typeof Object.setPrototypeOf)ca=Object.setPrototypeOf;else{var da;a:{var ea={xa:!0},fa={};try{fa.__proto__=ea;da=fa.xa;break a}catch(a){}da=!1}ca=da?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var ha=ca;
function n(a,b){a.prototype=ba(b.prototype);a.prototype.constructor=a;if(ha)ha(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.u=b.prototype}
var ia="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)},ja="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;
function ka(a){if(a){for(var b=ja,c=["Object","assign"],d=0;d<c.length-1;d++){var e=c[d];e in b||(b[e]={});b=b[e]}c=c[c.length-1];d=b[c];a=a(d);a!=d&&null!=a&&ia(b,c,{configurable:!0,writable:!0,value:a})}}
var la="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)Object.prototype.hasOwnProperty.call(d,e)&&(a[e]=d[e])}return a};
ka(function(a){return a||la});
(function(){function a(){function a(){}
Reflect.construct(a,[],function(){});
return new a instanceof a}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(a,d,e){a=b(a,d);e&&Reflect.setPrototypeOf(a,e.prototype);return a}}return function(a,b,e){void 0===e&&(e=a);
e=ba(e.prototype||Object.prototype);return Function.prototype.apply.call(a,e,b)||e}})();
var p=this;function q(a){return void 0!==a}
function r(a){return"string"==typeof a}
function ma(a){return"number"==typeof a}
function t(a,b,c){a=a.split(".");c=c||p;a[0]in c||!c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&q(b)?c[d]=b:c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}}
function v(a,b){for(var c=a.split("."),d=b||p,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function na(){}
function oa(a){a.ga=void 0;a.getInstance=function(){return a.ga?a.ga:a.ga=new a}}
function pa(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function w(a){return"array"==pa(a)}
function qa(a){var b=pa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function ra(a){return"function"==pa(a)}
function sa(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
var ta="closure_uid_"+(1E9*Math.random()>>>0),ua=0;function va(a,b,c){return a.call.apply(a.bind,arguments)}
function wa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function x(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?x=va:x=wa;return x.apply(null,arguments)}
function y(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
var z=Date.now||function(){return+new Date};
function xa(a,b){t(a,b,void 0)}
function A(a,b){function c(){}
c.prototype=b.prototype;a.u=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.eb=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function B(a){if(Error.captureStackTrace)Error.captureStackTrace(this,B);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
A(B,Error);B.prototype.name="CustomError";var ya=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(r(a))return r(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},C=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=r(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},za=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f=r(a)?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},Aa=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e=r(a)?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d};
function Ba(a,b){a:{var c=a.length;for(var d=r(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:r(a)?a.charAt(c):a[c]}
function Ca(a,b){var c=ya(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function Da(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function Ea(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(qa(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;var Fa=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function Ha(a){if(!Ia.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(Ja,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(Ka,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(La,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(Ma,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Na,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Oa,"&#0;"));return a}
var Ja=/&/g,Ka=/</g,La=/>/g,Ma=/"/g,Na=/'/g,Oa=/\x00/g,Ia=/[\x00&<>"']/;function Pa(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var Qa;a:{var Ra=p.navigator;if(Ra){var Sa=Ra.userAgent;if(Sa){Qa=Sa;break a}}Qa=""}function D(a){return-1!=Qa.indexOf(a)}
;function Va(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Wa(a,b){var c=qa(b),d=c?b:arguments;for(c=c?0:1;c<d.length;c++){if(null==a)return;a=a[d[c]]}return a}
function Xa(a){var b=Ya,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function Za(a){for(var b in a)return!1;return!0}
function $a(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function ab(a){var b={},c;for(c in a)b[c]=a[c];return b}
var bb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function cb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<bb.length;f++)c=bb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var db=D("Opera"),eb=D("Trident")||D("MSIE"),fb=D("Edge"),gb=D("Gecko")&&!(-1!=Qa.toLowerCase().indexOf("webkit")&&!D("Edge"))&&!(D("Trident")||D("MSIE"))&&!D("Edge"),hb=-1!=Qa.toLowerCase().indexOf("webkit")&&!D("Edge");function ib(){var a=p.document;return a?a.documentMode:void 0}
var jb;a:{var kb="",lb=function(){var a=Qa;if(gb)return/rv:([^\);]+)(\)|;)/.exec(a);if(fb)return/Edge\/([\d\.]+)/.exec(a);if(eb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(hb)return/WebKit\/(\S+)/.exec(a);if(db)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
lb&&(kb=lb?lb[1]:"");if(eb){var mb=ib();if(null!=mb&&mb>parseFloat(kb)){jb=String(mb);break a}}jb=kb}var nb=jb,ob;var pb=p.document;ob=pb&&eb?ib()||("CSS1Compat"==pb.compatMode?parseInt(nb,10):5):void 0;var qb=!eb||9<=Number(ob);function rb(){this.b="";this.f=sb}
rb.prototype.K=!0;rb.prototype.I=function(){return this.b};
rb.prototype.fa=!0;rb.prototype.aa=function(){return 1};
function tb(a){return a instanceof rb&&a.constructor===rb&&a.f===sb?a.b:"type_error:TrustedResourceUrl"}
var sb={};function E(){this.b="";this.f=ub}
E.prototype.K=!0;E.prototype.I=function(){return this.b};
E.prototype.fa=!0;E.prototype.aa=function(){return 1};
function vb(a){return a instanceof E&&a.constructor===E&&a.f===ub?a.b:"type_error:SafeUrl"}
var wb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function xb(a){if(a instanceof E)return a;a=a.K?a.I():String(a);wb.test(a)||(a="about:invalid#zClosurez");return yb(a)}
var ub={};function yb(a){var b=new E;b.b=a;return b}
yb("about:blank");function zb(){this.ea="";this.wa=Ab;this.b=null}
zb.prototype.fa=!0;zb.prototype.aa=function(){return this.b};
zb.prototype.K=!0;zb.prototype.I=function(){return this.ea};
var Ab={};function Bb(a,b){var c=new zb;c.ea=a;c.b=b;return c}
Bb("<!DOCTYPE html>",0);Bb("",0);Bb("<br>",0);function Cb(a,b){var c=b instanceof E?b:xb(b);a.href=vb(c)}
function Db(a,b,c){a.rel=c;a.href=-1!=c.toLowerCase().indexOf("stylesheet")?tb(b):b instanceof rb?tb(b):b instanceof E?vb(b):xb(b).I()}
function Eb(a,b){a.src=tb(b)}
;function Fb(a,b){this.x=q(a)?a:0;this.y=q(b)?b:0}
Fb.prototype.equals=function(a){return a instanceof Fb&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
Fb.prototype.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
Fb.prototype.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
Fb.prototype.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Gb(a,b){this.width=a;this.height=b}
l=Gb.prototype;l.aspectRatio=function(){return this.width/this.height};
l.isEmpty=function(){return!(this.width*this.height)};
l.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
l.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
l.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Hb(a){var b=document;return r(a)?b.getElementById(a):a}
function Ib(a,b){Va(b,function(b,d){b&&b.K&&(b=b.I());"style"==d?a.style.cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:Jb.hasOwnProperty(d)?a.setAttribute(Jb[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})}
var Jb={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Kb(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!qb&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',Ha(g.name),'"');if(g.type){f.push(' type="',Ha(g.type),'"');var h={};cb(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=e.createElement(f);g&&(r(g)?f.className=g:w(g)?f.className=g.join(" "):Ib(f,g));2<d.length&&Lb(e,f,d);return f}
function Lb(a,b,c){function d(c){c&&b.appendChild(r(c)?a.createTextNode(c):c)}
for(var e=2;e<c.length;e++){var f=c[e];if(!qa(f)||sa(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(sa(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if(ra(f)){g="function"==typeof f.item;break a}}g=!1}C(g?Da(f):f,d)}}}
function Mb(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Nb(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;function Ob(a){Pb();var b=new rb;b.b=a;return b}
var Pb=na;var Qb=/^[\w+/_-]+[=]{0,2}$/;function Rb(){var a=p.document.querySelector("script[nonce]");if(a&&(a=a.nonce||a.getAttribute("nonce"))&&Qb.test(a))return a}
;var Sb=document,F=window;function Tb(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Ub=(new Date).getTime();function Vb(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a&&"app"!==a)throw Error("Invalid URI scheme in origin: "+a);c="";var d=b.indexOf(":");if(-1!=d){var e=
b.substring(d+1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function Wb(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;u=m=0}
function b(a){for(var b=g,c=0;64>c;c+=4)b[c/4]=a[c]<<24|a[c+1]<<16|a[c+2]<<8|a[c+3];for(c=16;80>c;c++)a=b[c-3]^b[c-8]^b[c-14]^b[c-16],b[c]=(a<<1|a>>>31)&4294967295;a=e[0];var d=e[1],f=e[2],h=e[3],k=e[4];for(c=0;80>c;c++){if(40>c)if(20>c){var m=h^d&(f^h);var u=1518500249}else m=d^f^h,u=1859775393;else 60>c?(m=d&f|h&(d|f),u=2400959708):(m=d^f^h,u=3395469782);m=((a<<5|a>>>27)&4294967295)+m+k+u+b[c]&4294967295;k=h;h=f;f=(d<<30|d>>>2)&4294967295;d=a;a=m}e[0]=e[0]+a&4294967295;e[1]=e[1]+d&4294967295;e[2]=
e[2]+f&4294967295;e[3]=e[3]+h&4294967295;e[4]=e[4]+k&4294967295}
function c(a,c){if("string"===typeof a){a=unescape(encodeURIComponent(a));for(var d=[],e=0,g=a.length;e<g;++e)d.push(a.charCodeAt(e));a=d}c||(c=a.length);d=0;if(0==m)for(;d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64;for(;d<c;)if(f[m++]=a[d++],u++,64==m)for(m=0,b(f);d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64}
function d(){var a=[],d=8*u;56>m?c(h,56-m):c(h,64-(m-56));for(var g=63;56<=g;g--)f[g]=d&255,d>>>=8;b(f);for(g=d=0;5>g;g++)for(var k=24;0<=k;k-=8)a[d++]=e[g]>>k&255;return a}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var m,u;a();return{reset:a,update:c,digest:d,za:function(){for(var a=d(),b="",c=0;c<a.length;c++)b+="0123456789ABCDEF".charAt(Math.floor(a[c]/16))+"0123456789ABCDEF".charAt(a[c]%16);return b}}}
;function Xb(a,b,c){var d=[],e=[];if(1==(w(c)?2:1))return e=[b,a],C(d,function(a){e.push(a)}),Yb(e.join(" "));
var f=[],g=[];C(c,function(a){g.push(a.key);f.push(a.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];C(d,function(a){e.push(a)});
a=Yb(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function Yb(a){var b=Wb();b.update(a);return b.za().toLowerCase()}
;function Zb(a){this.b=a||{cookie:""}}
l=Zb.prototype;l.isEnabled=function(){return navigator.cookieEnabled};
l.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');q(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(z()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
l.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(";"),e=0,f;e<d.length;e++){f=Fa(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
l.remove=function(a,b,c){var d=q(this.get(a));this.set(a,"",0,b,c);return d};
l.isEmpty=function(){return!this.b.cookie};
l.clear=function(){for(var a=(this.b.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=Fa(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var $b=new Zb("undefined"==typeof document?null:document);$b.f=3950;function ac(a){var b=Vb(String(p.location.href)),c=p.__OVERRIDE_SID;null==c&&(c=(new Zb(document)).get("SID"));if(c&&(b=(c=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?p.__SAPISID:p.__APISID,null==b&&(b=(new Zb(document)).get(c?"SAPISID":"APISID")),b)){c=c?"SAPISIDHASH":"APISIDHASH";var d=String(p.location.href);return d&&b&&c?[c,Xb(Vb(d),b,a||null)].join(" "):null}return null}
;function bc(a,b){this.h=a;this.g=b;this.f=0;this.b=null}
bc.prototype.get=function(){if(0<this.f){this.f--;var a=this.b;this.b=a.next;a.next=null}else a=this.h();return a};
function cc(a,b){a.g(b);100>a.f&&(a.f++,b.next=a.b,a.b=b)}
;function dc(a){p.setTimeout(function(){throw a;},0)}
var ec;
function fc(){var a=p.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!D("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=x(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!D("Trident")&&!D("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(q(c.next)){c=c.next;var a=c.ma;c.ma=null;a()}};
return function(a){d.next={ma:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){p.setTimeout(a,0)}}
;function gc(){this.f=this.b=null}
var ic=new bc(function(){return new hc},function(a){a.reset()});
gc.prototype.add=function(a,b){var c=ic.get();c.set(a,b);this.f?this.f.next=c:this.b=c;this.f=c};
gc.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.f=null),a.next=null);return a};
function hc(){this.next=this.scope=this.b=null}
hc.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
hc.prototype.reset=function(){this.next=this.scope=this.b=null};function jc(a,b){kc||lc();mc||(kc(),mc=!0);nc.add(a,b)}
var kc;function lc(){if(-1!=String(p.Promise).indexOf("[native code]")){var a=p.Promise.resolve(void 0);kc=function(){a.then(oc)}}else kc=function(){var a=oc;
!ra(p.setImmediate)||p.Window&&p.Window.prototype&&!D("Edge")&&p.Window.prototype.setImmediate==p.setImmediate?(ec||(ec=fc()),ec(a)):p.setImmediate(a)}}
var mc=!1,nc=new gc;function oc(){for(var a;a=nc.remove();){try{a.b.call(a.scope)}catch(b){dc(b)}cc(ic,a)}mc=!1}
;var pc=null,qc=null;function rc(){this.f=-1}
;function sc(){this.f=64;this.b=[];this.j=[];this.l=[];this.g=[];this.g[0]=128;for(var a=1;a<this.f;++a)this.g[a]=0;this.i=this.h=0;this.reset()}
A(sc,rc);sc.prototype.reset=function(){this.b[0]=1732584193;this.b[1]=4023233417;this.b[2]=2562383102;this.b[3]=271733878;this.b[4]=3285377520;this.i=this.h=0};
function tc(a,b,c){c||(c=0);var d=a.l;if(r(b))for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.b[0];c=a.b[1];var g=a.b[2],h=a.b[3],k=a.b[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var m=1518500249}else f=c^g^h,m=1859775393;else 60>e?(f=c&g|h&(c|g),m=2400959708):(f=c^g^h,m=
3395469782);f=(b<<5|b>>>27)+f+k+m+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.b[0]=a.b[0]+b&4294967295;a.b[1]=a.b[1]+c&4294967295;a.b[2]=a.b[2]+g&4294967295;a.b[3]=a.b[3]+h&4294967295;a.b[4]=a.b[4]+k&4294967295}
sc.prototype.update=function(a,b){if(null!=a){q(b)||(b=a.length);for(var c=b-this.f,d=0,e=this.j,f=this.h;d<b;){if(0==f)for(;d<=c;)tc(this,a,d),d+=this.f;if(r(a))for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.f){tc(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.f){tc(this,e);f=0;break}}this.h=f;this.i+=b}};
sc.prototype.digest=function(){var a=[],b=8*this.i;56>this.h?this.update(this.g,56-this.h):this.update(this.g,this.f-(this.h-56));for(var c=this.f-1;56<=c;c--)this.j[c]=b&255,b/=256;tc(this,this.j);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.b[c]>>d&255,++b;return a};function G(){this.h=this.h;this.C=this.C}
G.prototype.h=!1;G.prototype.dispose=function(){this.h||(this.h=!0,this.m())};
function uc(a,b){a.h?q(void 0)?b.call(void 0):b():(a.C||(a.C=[]),a.C.push(q(void 0)?x(b,void 0):b))}
G.prototype.m=function(){if(this.C)for(;this.C.length;)this.C.shift()()};
function vc(a){a&&"function"==typeof a.dispose&&a.dispose()}
function wc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];qa(d)?wc.apply(null,d):vc(d)}}
;function xc(a){if(a.classList)return a.classList;a=a.className;return r(a)&&a.match(/\S+/g)||[]}
function yc(a,b){if(a.classList)var c=a.classList.contains(b);else c=xc(a),c=0<=ya(c,b);return c}
function zc(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):yc(a,"inverted-hdpi")&&(a.className=za(xc(a),function(a){return"inverted-hdpi"!=a}).join(" "))}
;var Ac="StopIteration"in p?p.StopIteration:{message:"StopIteration",stack:""};function Bc(){}
Bc.prototype.next=function(){throw Ac;};
Bc.prototype.F=function(){return this};
function Cc(a){if(a instanceof Bc)return a;if("function"==typeof a.F)return a.F(!1);if(qa(a)){var b=0,c=new Bc;c.next=function(){for(;;){if(b>=a.length)throw Ac;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Dc(a,b){if(qa(a))try{C(a,b,void 0)}catch(c){if(c!==Ac)throw c;}else{a=Cc(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==Ac)throw c;}}}
function Ec(a){if(qa(a))return Da(a);a=Cc(a);var b=[];Dc(a,function(a){b.push(a)});
return b}
;function Fc(a,b){this.h={};this.b=[];this.g=this.f=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Fc)for(c=Gc(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function Gc(a){Hc(a);return a.b.concat()}
l=Fc.prototype;l.equals=function(a,b){if(this===a)return!0;if(this.f!=a.f)return!1;var c=b||Ic;Hc(this);for(var d,e=0;d=this.b[e];e++)if(!c(this.get(d),a.get(d)))return!1;return!0};
function Ic(a,b){return a===b}
l.isEmpty=function(){return 0==this.f};
l.clear=function(){this.h={};this.g=this.f=this.b.length=0};
l.remove=function(a){return Object.prototype.hasOwnProperty.call(this.h,a)?(delete this.h[a],this.f--,this.g++,this.b.length>2*this.f&&Hc(this),!0):!1};
function Hc(a){if(a.f!=a.b.length){for(var b=0,c=0;b<a.b.length;){var d=a.b[b];Object.prototype.hasOwnProperty.call(a.h,d)&&(a.b[c++]=d);b++}a.b.length=c}if(a.f!=a.b.length){var e={};for(c=b=0;b<a.b.length;)d=a.b[b],Object.prototype.hasOwnProperty.call(e,d)||(a.b[c++]=d,e[d]=1),b++;a.b.length=c}}
l.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.h,a)?this.h[a]:b};
l.set=function(a,b){Object.prototype.hasOwnProperty.call(this.h,a)||(this.f++,this.b.push(a),this.g++);this.h[a]=b};
l.forEach=function(a,b){for(var c=Gc(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
l.F=function(a){Hc(this);var b=0,c=this.g,d=this,e=new Bc;e.next=function(){if(c!=d.g)throw Error("The map has changed since the iterator was created");if(b>=d.b.length)throw Ac;var e=d.b[b++];return a?e:d.h[e]};
return e};(function(){if(!p.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
p.addEventListener("test",na,b);p.removeEventListener("test",na,b);return a})();function Jc(a){var b=[];Kc(new Lc,a,b);return b.join("")}
function Lc(){}
function Kc(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(w(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),Kc(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Mc(d,c),c.push(":"),Kc(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Mc(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Nc={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Oc=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Mc(a,b){b.push('"',a.replace(Oc,function(a){var b=Nc[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),Nc[a]=b);return b}),'"')}
;function Pc(a){a.prototype.then=a.prototype.then;a.prototype.$goog_Thenable=!0}
function Qc(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function H(a,b){this.b=0;this.l=void 0;this.g=this.f=this.h=null;this.i=this.j=!1;if(a!=na)try{var c=this;a.call(b,function(a){Rc(c,2,a)},function(a){Rc(c,3,a)})}catch(d){Rc(this,3,d)}}
function Sc(){this.next=this.context=this.f=this.g=this.b=null;this.h=!1}
Sc.prototype.reset=function(){this.context=this.f=this.g=this.b=null;this.h=!1};
var Tc=new bc(function(){return new Sc},function(a){a.reset()});
function Uc(a,b,c){var d=Tc.get();d.g=a;d.f=b;d.context=c;return d}
function Vc(a){return new H(function(b,c){c(a)})}
function Wc(a,b,c){Xc(a,b,c,null)||jc(y(b,a))}
function Yc(a){return new H(function(b,c){a.length||b(void 0);for(var d=0,e;d<a.length;d++)e=a[d],Wc(e,b,c)})}
function Zc(a){return new H(function(b){var c=a.length,d=[];if(c)for(var e=function(a,e,f){c--;d[a]=e?{Z:!0,value:f}:{Z:!1,reason:f};0==c&&b(d)},f=0,g;f<a.length;f++)g=a[f],Wc(g,y(e,f,!0),y(e,f,!1));
else b(d)})}
H.prototype.then=function(a,b,c){return $c(this,ra(a)?a:null,ra(b)?b:null,c)};
Pc(H);function ad(a,b){var c=Uc(b,b,void 0);c.h=!0;bd(a,c);return a}
function cd(a,b){return $c(a,null,b,void 0)}
H.prototype.cancel=function(a){0==this.b&&jc(function(){var b=new dd(a);ed(this,b)},this)};
function ed(a,b){if(0==a.b)if(a.h){var c=a.h;if(c.f){for(var d=0,e=null,f=null,g=c.f;g&&(g.h||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?ed(c,b):(f?(d=f,d.next==c.g&&(c.g=d),d.next=d.next.next):fd(c),gd(c,e,3,b)))}a.h=null}else Rc(a,3,b)}
function bd(a,b){a.f||2!=a.b&&3!=a.b||hd(a);a.g?a.g.next=b:a.f=b;a.g=b}
function $c(a,b,c,d){var e=Uc(null,null,null);e.b=new H(function(a,g){e.g=b?function(c){try{var e=b.call(d,c);a(e)}catch(m){g(m)}}:a;
e.f=c?function(b){try{var e=c.call(d,b);!q(e)&&b instanceof dd?g(b):a(e)}catch(m){g(m)}}:g});
e.b.h=a;bd(a,e);return e.b}
H.prototype.o=function(a){this.b=0;Rc(this,2,a)};
H.prototype.w=function(a){this.b=0;Rc(this,3,a)};
function Rc(a,b,c){0==a.b&&(a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself")),a.b=1,Xc(c,a.o,a.w,a)||(a.l=c,a.b=b,a.h=null,hd(a),3!=b||c instanceof dd||id(a,c)))}
function Xc(a,b,c,d){if(a instanceof H)return bd(a,Uc(b||na,c||null,d)),!0;if(Qc(a))return a.then(b,c,d),!0;if(sa(a))try{var e=a.then;if(ra(e))return jd(a,e,b,c,d),!0}catch(f){return c.call(d,f),!0}return!1}
function jd(a,b,c,d,e){function f(a){h||(h=!0,d.call(e,a))}
function g(a){h||(h=!0,c.call(e,a))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function hd(a){a.j||(a.j=!0,jc(a.C,a))}
function fd(a){var b=null;a.f&&(b=a.f,a.f=b.next,b.next=null);a.f||(a.g=null);return b}
H.prototype.C=function(){for(var a;a=fd(this);)gd(this,a,this.b,this.l);this.j=!1};
function gd(a,b,c,d){if(3==c&&b.f&&!b.h)for(;a&&a.i;a=a.h)a.i=!1;if(b.b)b.b.h=null,kd(b,c,d);else try{b.h?b.g.call(b.context):kd(b,c,d)}catch(e){ld.call(null,e)}cc(Tc,b)}
function kd(a,b,c){2==b?a.g.call(a.context,c):a.f&&a.f.call(a.context,c)}
function id(a,b){a.i=!0;jc(function(){a.i&&ld.call(null,b)})}
var ld=dc;function dd(a){B.call(this,a)}
A(dd,B);dd.prototype.name="cancel";function I(a){G.call(this);this.j=1;this.g=[];this.i=0;this.b=[];this.f={};this.l=!!a}
A(I,G);l=I.prototype;l.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.j;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.j=e+3;d.push(e);return e};
function md(a,b,c,d){if(b=a.f[b]){var e=a.b;(b=Ba(b,function(a){return e[a+1]==c&&e[a+2]==d}))&&a.L(b)}}
l.L=function(a){var b=this.b[a];if(b){var c=this.f[b];0!=this.i?(this.g.push(a),this.b[a+1]=na):(c&&Ca(c,a),delete this.b[a],delete this.b[a+1],delete this.b[a+2])}return!!b};
l.J=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.l)for(e=0;e<c.length;e++){var g=c[e];nd(this.b[g+1],this.b[g+2],d)}else{this.i++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.i--,0<this.g.length&&0==this.i)for(;c=this.g.pop();)this.L(c)}}return 0!=e}return!1};
function nd(a,b,c){jc(function(){a.apply(b,c)})}
l.clear=function(a){if(a){var b=this.f[a];b&&(C(b,this.L,this),delete this.f[a])}else this.b.length=0,this.f={}};
l.m=function(){I.u.m.call(this);this.clear();this.g.length=0};function od(a){this.b=a}
od.prototype.set=function(a,b){q(b)?this.b.set(a,Jc(b)):this.b.remove(a)};
od.prototype.get=function(a){try{var b=this.b.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
od.prototype.remove=function(a){this.b.remove(a)};function pd(a){this.b=a}
A(pd,od);function qd(a){this.data=a}
function rd(a){return!q(a)||a instanceof qd?a:new qd(a)}
pd.prototype.set=function(a,b){pd.u.set.call(this,a,rd(b))};
pd.prototype.f=function(a){a=pd.u.get.call(this,a);if(!q(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
pd.prototype.get=function(a){if(a=this.f(a)){if(a=a.data,!q(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};function sd(a){this.b=a}
A(sd,pd);sd.prototype.set=function(a,b,c){if(b=rd(b)){if(c){if(c<z()){sd.prototype.remove.call(this,a);return}b.expiration=c}b.creation=z()}sd.u.set.call(this,a,b)};
sd.prototype.f=function(a){var b=sd.u.f.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<z()||c&&c>z())sd.prototype.remove.call(this,a);else return b}};function td(a){this.b=a}
A(td,sd);function ud(){}
;function vd(){}
A(vd,ud);vd.prototype.clear=function(){var a=Ec(this.F(!0)),b=this;C(a,function(a){b.remove(a)})};function wd(a){this.b=a}
A(wd,vd);l=wd.prototype;l.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
l.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
l.get=function(a){a=this.b.getItem(a);if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
l.remove=function(a){this.b.removeItem(a)};
l.F=function(a){var b=0,c=this.b,d=new Bc;d.next=function(){if(b>=c.length)throw Ac;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
l.clear=function(){this.b.clear()};
l.key=function(a){return this.b.key(a)};function xd(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
A(xd,wd);function yd(){var a=null;try{a=window.sessionStorage||null}catch(b){}this.b=a}
A(yd,wd);function zd(a,b){this.f=a;this.b=null;if(eb&&!(9<=Number(ob))){Ad||(Ad=new Fc);this.b=Ad.get(a);this.b||(b?this.b=document.getElementById(b):(this.b=document.createElement("userdata"),this.b.addBehavior("#default#userData"),document.body.appendChild(this.b)),Ad.set(a,this.b));try{this.b.load(this.f)}catch(c){this.b=null}}}
A(zd,vd);var Bd={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},Ad=null;function Cd(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(a){return Bd[a]})}
l=zd.prototype;l.isAvailable=function(){return!!this.b};
l.set=function(a,b){this.b.setAttribute(Cd(a),b);Dd(this)};
l.get=function(a){a=this.b.getAttribute(Cd(a));if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
l.remove=function(a){this.b.removeAttribute(Cd(a));Dd(this)};
l.F=function(a){var b=0,c=this.b.XMLDocument.documentElement.attributes,d=new Bc;d.next=function(){if(b>=c.length)throw Ac;var d=c[b++];if(a)return decodeURIComponent(d.nodeName.replace(/\./g,"%")).substr(1);d=d.nodeValue;if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
l.clear=function(){for(var a=this.b.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);Dd(this)};
function Dd(a){try{a.b.save(a.f)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function Ed(a,b){this.f=a;this.b=b+"::"}
A(Ed,vd);Ed.prototype.set=function(a,b){this.f.set(this.b+a,b)};
Ed.prototype.get=function(a){return this.f.get(this.b+a)};
Ed.prototype.remove=function(a){this.f.remove(this.b+a)};
Ed.prototype.F=function(a){var b=this.f.F(!0),c=this,d=new Bc;d.next=function(){for(var d=b.next();d.substr(0,c.b.length)!=c.b;)d=b.next();return a?d.substr(c.b.length):c.f.get(d)};
return d};function Fd(a){if(!ra(a))if(a&&"function"==typeof a.handleEvent)a=x(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(5E3)?-1:p.setTimeout(a,5E3)}
function Gd(){var a=null;return cd(new H(function(b,c){a=Fd(function(){b(void 0)});
-1==a&&c(Error("Failed to schedule timer."))}),function(b){p.clearTimeout(a);
throw b;})}
;var Hd=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function J(a){return a.match(Hd)}
function Id(a){return a?decodeURI(a):a}
function Jd(a,b,c){if(w(b))for(var d=0;d<b.length;d++)Jd(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function Kd(a){var b=[],c;for(c in a)Jd(c,a[c],b);return b.join("&")}
function Ld(a,b){var c=Kd(b);if(c){var d=a.indexOf("#");0>d&&(d=a.length);var e=a.indexOf("?");if(0>e||e>d){e=d;var f=""}else f=a.substring(e+1,d);d=[a.substr(0,e),f,a.substr(d)];e=d[1];d[1]=c?e?e+"&"+c:c:e;c=d[0]+(d[1]?"?"+d[1]:"")+d[2]}else c=a;return c}
;function Md(a,b,c){var d="script";d=void 0===d?"":d;var e=a.createElement("link");Db(e,b,"preload");d&&(e.as=d);c&&(e.nonce=c);if(a=a.getElementsByTagName("head")[0])try{a.appendChild(e)}catch(f){}}
;var Nd=/^\.google\.(com?\.)?[a-z]{2,3}$/,Pd=/\.(cn|com\.bi|do|sl|ba|by|ma)$/;function Qd(a){return Nd.test(a)&&!Pd.test(a)}
var Rd=p;function Sd(a){a="https://"+("adservice"+a+"/adsid/integrator.js");var b=["domain="+encodeURIComponent(p.location.hostname)];K[3]>=z()&&b.push("adsid="+encodeURIComponent(K[1]));return a+"?"+b.join("&")}
var K,L;function Td(){Rd=p;K=Rd.googleToken=Rd.googleToken||{};var a=z();K[1]&&K[3]>a&&0<K[2]||(K[1]="",K[2]=-1,K[3]=-1,K[4]="",K[6]="");L=Rd.googleIMState=Rd.googleIMState||{};Qd(L[1])||(L[1]=".google.com");w(L[5])||(L[5]=[]);"boolean"==typeof L[6]||(L[6]=!1);w(L[7])||(L[7]=[]);ma(L[8])||(L[8]=0)}
function Ud(){Td();return K[1]}
var N={da:function(){return 0<L[8]},
Pa:function(){L[8]++},
Qa:function(){0<L[8]&&L[8]--},
Ra:function(){L[8]=0},
shouldRetry:function(){return!1},
na:function(){return L[5]},
la:function(a){try{a()}catch(b){p.setTimeout(function(){throw b;},0)}},
ja:function(){if(!N.da()){var a=p.document,b=function(b){b=Sd(b);a:{try{var c=Rb();break a}catch(h){}c=void 0}var d=c;Md(a,b,d);c=a.createElement("script");c.type="text/javascript";d&&(c.nonce=d);c.onerror=function(){return p.processGoogleToken({},2)};
b=Ob(b);Eb(c,b);try{(a.head||a.body||a.documentElement).appendChild(c),N.Pa()}catch(h){}},c=L[1];
b(c);".google.com"!=c&&b(".google.com");b={};var d=(b.newToken="FBT",b);p.setTimeout(function(){return p.processGoogleToken(d,1)},1E3)}}};
function Vd(a){Td();var b=Rd.googleToken[5]||0;a&&(0!=b||K[3]>=z()?N.la(a):(N.na().push(a),N.ja()));K[3]>=z()&&K[2]>=z()||N.ja()}
function Wd(a){p.processGoogleToken=p.processGoogleToken||function(a,c){var b=a,e=c;b=void 0===b?{}:b;e=void 0===e?0:e;var f=b.newToken||"",g="NT"==f,h=parseInt(b.freshLifetimeSecs||"",10),k=parseInt(b.validLifetimeSecs||"",10);g&&!k&&(k=3600);var m=b["1p_jar"]||"";b=b.pucrd||"";Td();1==e?N.Ra():N.Qa();if(!f&&N.shouldRetry())Qd(".google.com")&&(L[1]=".google.com"),N.ja();else{var u=Rd.googleToken=Rd.googleToken||{},M=0==e&&f&&r(f)&&!g&&ma(h)&&0<h&&ma(k)&&0<k&&r(m);g=g&&!N.da()&&(!(K[3]>=z())||"NT"==
K[1]);var aa=!(K[3]>=z())&&0!=e;if(M||g||aa)g=z(),h=g+1E3*h,k=g+1E3*k,1E-5>Math.random()&&(g="https://pagead2.googlesyndication.com/pagead/gen_204?id=imerr&err="+e,p.google_image_requests||(p.google_image_requests=[]),aa=p.document.createElement("img"),aa.src=g,p.google_image_requests.push(aa)),u[5]=e,u[1]=f,u[2]=h,u[3]=k,u[4]=m,u[6]=b,Td();if(M||!N.da()){e=N.na();for(f=0;f<e.length;f++)N.la(e[f]);e.length=0}}};
Vd(a)}
;function Xd(a,b){if(1<b.length)a[b[0]]=b[1];else{var c=b[0],d;for(d in c)a[d]=c[d]}}
var O=window.performance&&window.performance.timing&&window.performance.now?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};var Yd=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};t("yt.config_",Yd,void 0);function P(a){Xd(Yd,arguments)}
function Q(a,b){return a in Yd?Yd[a]:b}
function Zd(a){return Q(a,void 0)}
function $d(){return Q("PLAYER_CONFIG",{})}
;function ae(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){R(b)}}:a}
function R(a,b,c,d,e){var f=v("yt.logging.errors.log");f?f(a,b,c,d,e):(f=Q("ERRORS",[]),f.push([a,b,c,d,e]),P("ERRORS",f))}
;function S(a){return Q("EXPERIMENT_FLAGS",{})[a]}
;function be(a){a&&(a.dataset?a.dataset[ce("loaded")]="true":a.setAttribute("data-loaded","true"))}
function de(a,b){return a?a.dataset?a.dataset[ce(b)]:a.getAttribute("data-"+b):null}
var ee={};function ce(a){return ee[a]||(ee[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function T(a,b){ra(a)&&(a=ae(a));return window.setTimeout(a,b)}
function fe(a){window.clearTimeout(a)}
;var ge=v("ytPubsubPubsubInstance")||new I;I.prototype.subscribe=I.prototype.subscribe;I.prototype.unsubscribeByKey=I.prototype.L;I.prototype.publish=I.prototype.J;I.prototype.clear=I.prototype.clear;t("ytPubsubPubsubInstance",ge,void 0);var he=v("ytPubsubPubsubSubscribedKeys")||{};t("ytPubsubPubsubSubscribedKeys",he,void 0);var ie=v("ytPubsubPubsubTopicToKeys")||{};t("ytPubsubPubsubTopicToKeys",ie,void 0);var je=v("ytPubsubPubsubIsSynchronous")||{};t("ytPubsubPubsubIsSynchronous",je,void 0);
function ke(a,b){var c=le();if(c){var d=c.subscribe(a,function(){var c=arguments;var f=function(){he[d]&&b.apply(window,c)};
try{je[a]?f():T(f,0)}catch(g){R(g)}},void 0);
he[d]=!0;ie[a]||(ie[a]=[]);ie[a].push(d);return d}return 0}
function me(a){var b=le();b&&(ma(a)?a=[a]:r(a)&&(a=[parseInt(a,10)]),C(a,function(a){b.unsubscribeByKey(a);delete he[a]}))}
function ne(a,b){var c=le();c&&c.publish.apply(c,arguments)}
function oe(a){var b=le();if(b)if(b.clear(a),a)pe(a);else for(var c in ie)pe(c)}
function le(){return v("ytPubsubPubsubInstance")}
function pe(a){ie[a]&&(a=ie[a],C(a,function(a){he[a]&&delete he[a]}),a.length=0)}
;var qe=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,re=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function se(a,b){if(window.spf){var c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(qe,""),c=c.replace(re,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else te(a,b)}
function te(a,b){var c=ue(a),d=document.getElementById(c),e=d&&de(d,"loaded"),f=d&&!e;if(e)b&&b();else{if(b){e=ke(c,b);var g=""+(b[ta]||(b[ta]=++ua));ve[g]=e}f||(d=we(a,c,function(){de(d,"loaded")||(be(d),ne(c),T(y(oe,c),0))}))}}
function we(a,b,c){var d=document.createElement("SCRIPT");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
d.onreadystatechange=function(){switch(d.readyState){case "loaded":case "complete":d.onload()}};
Eb(d,Ob(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(d,a.firstChild);return d}
function xe(a){a=ue(a);var b=document.getElementById(a);b&&(oe(a),b.parentNode.removeChild(b))}
function ye(a,b){if(a&&b){var c=""+(b[ta]||(b[ta]=++ua));(c=ve[c])&&me(c)}}
function ue(a){var b=document.createElement("a");Cb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Pa(a)}
var ve={};var ze=null;function Ae(){var a=Q("BG_I",null),b=Q("BG_IU",null),c=Q("BG_P",void 0);b?se(b,function(){window.botguard?Be(c):(xe(b),R(Error("Unable to load Botguard from "+b),"WARNING"))}):a&&(eval(a),window.botguard?Be(c):R(Error("Unable to load Botguard from JS"),"WARNING"))}
function Be(a){ze=new window.botguard.bg(a);S("botguard_periodic_refresh")&&O()}
function Ce(){return null!=ze}
function De(){return ze?ze.invoke():null}
;z();var Ee=q(XMLHttpRequest)?function(){return new XMLHttpRequest}:q(ActiveXObject)?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function Fe(){if(!Ee)return null;var a=Ee();return"open"in a?a:null}
function Ge(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function He(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," "));e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?w(b[f])?Ea(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
;var Ie={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Je=!1;
function Ke(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=J(a)[1]||null,e=Id(J(a)[3]||null);d&&e?(d=c,c=J(a),d=J(d),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?Id(J(c)[3]||null)==e&&(Number(J(c)[4]||null)||null)==(Number(J(a)[4]||null)||null):!0;for(var f in Ie){if((e=d=Q(Ie[f]))&&!(e=c)){e=f;var g=Q("CORS_HEADER_WHITELIST")||{},h=Id(J(a)[3]||null);e=h?(g=g[h])?0<=ya(g,e):!1:!0}e&&(b[f]=d)}return b}
function Le(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=Me(a,b);var d=Ne(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(a){if(!e){e=!0;f&&fe(f);var c=a.ok,d=function(d){d=d||{};var e=b.context||p;c?b.A&&b.A.call(e,d,a):b.onError&&b.onError.call(e,d,a);b.ia&&b.ia.call(e,d,a)};
"JSON"==(b.format||"JSON")&&(c||400<=a.status&&500>a.status)?a.json().then(d,function(){d(null)}):d(null)}});
b.pa&&0<b.timeout&&(f=T(function(){e||(e=!0,fe(f),b.pa.call(b.context||p))},b.timeout))}else Oe(a,b)}
function Oe(a,b){var c=b.format||"JSON";a=Me(a,b);var d=Ne(a,b),e=!1,f,g=Pe(a,function(a){if(!e){e=!0;f&&fe(f);var d=Ge(a),g=null;if(d||400<=a.status&&500>a.status)g=Qe(c,a,b.gb);if(d)a:if(a&&204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(g&&g.return_code,10);break a;case "RAW":d=!0;break a}d=!!g}g=g||{};var h=b.context||p;d?b.A&&b.A.call(h,a,g):b.onError&&b.onError.call(h,a,g);b.ia&&b.ia.call(h,a,g)}},b.method,d,b.headers,b.responseType,b.withCredentials);
b.M&&0<b.timeout&&(f=T(function(){e||(e=!0,g.abort(),fe(f),b.M.call(b.context||p,g))},b.timeout));
return g}
function Me(a,b){b.Ea&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=Q("XSRF_FIELD_NAME",void 0),d=b.bb;if(d){d[c]&&delete d[c];d=d||{};var e=a.split("#",2);c=e[0];e=1<e.length?"#"+e[1]:"";var f=c.split("?",2);c=f[0];f=He(f[1]||"");for(var g in d)f[g]=d[g];a=Ld(c,f)+e}return a}
function Ne(a,b){var c=Q("XSRF_FIELD_NAME",void 0),d=Q("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.B,g=Zd("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.hb||Id(J(a)[3]||null)&&!b.withCredentials&&Id(J(a)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.B&&b.B[g]||(f||(f={}),f[c]=d);f&&r(e)&&(e=He(e),cb(e,f),e=b.qa&&"JSON"==b.qa?JSON.stringify(e):Kd(e));f=e||f&&!Za(f);!Je&&f&&"POST"!=b.method&&(Je=!0,R(Error("AJAX request with postData should use POST")));
return e}
function Qe(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Re(b):null)d={},C(b.getElementsByTagName("*"),function(a){d[a.tagName]=Se(a)})}c&&Te(d);
return d}
function Te(a){if(sa(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Bb(a[b],null);a[c]=d}else Te(a[b])}}
function Re(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Se(a){var b="";C(a.childNodes,function(a){b+=a.nodeValue});
return b}
function Ue(a,b){b.method="POST";b.B||(b.B={});Oe(a,b)}
function Pe(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&ae(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=Fe();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Ke(a,e))for(var m in e)k.setRequestHeader(m,e[m]),"content-type"==m.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);return k}
;var Ve={},We=0;
function Xe(a,b,c,d,e){e=void 0===e?"":e;a&&(c&&(c=Qa,c=!(c&&0<=c.toLowerCase().indexOf("cobalt"))),c?a&&(a instanceof E||(a=a.K?a.I():String(a),wb.test(a)||(a="about:invalid#zClosurez"),a=yb(a)),b=vb(a),"about:invalid#zClosurez"===b?a="":(b instanceof zb?a=b:(a=null,b.fa&&(a=b.aa()),b=Ha(b.K?b.I():String(b)),a=Bb(b,a)),a=encodeURIComponent(String(Jc(a instanceof zb&&a.constructor===zb&&a.wa===Ab?a.ea:"type_error:SafeHtml")))),/^[\s\xa0]*$/.test(a)||(a=Kb("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+
'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))):e?Pe(a,b,"POST",e,d):Q("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d?Pe(a,b,"GET","",d):Ye(a,b))}
function Ye(a,b){var c=new Image,d=""+We++;Ve[d]=c;c.onload=c.onerror=function(){b&&Ve[d]&&b();delete Ve[d]};
c.src=a}
;var Ze={},$e=0;
function af(a,b,c,d,e,f){f=f||{};f.name=c||Q("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||Q("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);b=void 0===b?"ERROR":b;e=void 0===e?!1:e;e=window&&window.yterr||(void 0===e?!1:e)||!1;if(a&&e&&!(5<=$e)){e=a.stacktrace;c=a.columnNumber;d=v("window.location.href");if(r(a))a={message:a,name:"Unknown error",lineNumber:"Not available",fileName:d,stack:"Not available"};else{var g=!1;try{var h=a.lineNumber||a.line||"Not available"}catch(M){h="Not available",g=!0}try{var k=
a.fileName||a.filename||a.sourceURL||p.$googDebugFname||d}catch(M){k="Not available",g=!0}a=!g&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:{message:a.message||"Not available",name:a.name||"UnknownError",lineNumber:h,fileName:k,stack:a.stack||"Not available"}}e=e||a.stack;h=a.lineNumber.toString();isNaN(h)||isNaN(c)||(h=h+":"+c);if(!(Ze[a.message]||0<=e.indexOf("/YouTubeCenter.js")||0<=e.indexOf("/mytube.js"))){k=e;h={bb:{a:"logerror",t:"jserror",type:a.name,msg:a.message.substr(0,1E3),
line:h,level:void 0===b?"ERROR":b,"client.name":f.name},B:{url:Q("PAGE_NAME",window.location.href),file:a.fileName},method:"POST"};f.version&&(h["client.version"]=f.version);k&&(h.B.stack=k);for(var m in f)h.B["client."+m]=f[m];if(m=Q("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(var u in m)h.B[u]=m[u];Oe(Q("ECATCHER_REPORT_HOST","")+"/error_204",h);Ze[a.message]=!0;$e++}}}
;var bf=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};t("yt.msgs_",bf,void 0);function cf(a){Xd(bf,arguments)}
;function df(){}
function ef(a,b){return ff(a,0,b)}
function gf(a,b){return ff(a,1,b)}
;function hf(){}
n(hf,df);function ff(a,b,c){isNaN(c)&&(c=void 0);var d=v("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):T(a,c||0)}
function jf(a){if(!isNaN(a)){var b=v("yt.scheduler.instance.cancelJob");b?b(a):fe(a)}}
hf.prototype.start=function(){var a=v("yt.scheduler.instance.start");a&&a()};
hf.prototype.pause=function(){var a=v("yt.scheduler.instance.pause");a&&a()};
oa(hf);hf.getInstance();var kf=[],lf=!1;function mf(){if("1"!=Wa($d(),"args","privembed")){var a=function(){lf=!0;"google_ad_status"in window?P("DCLKSTAT",1):P("DCLKSTAT",2)};
se("//static.doubleclick.net/instream/ad_status.js",a);kf.push(gf(function(){lf||"google_ad_status"in window||(ye("//static.doubleclick.net/instream/ad_status.js",a),P("DCLKSTAT",3))},5E3))}}
function nf(){return parseInt(Q("DCLKSTAT",0),10)}
;var of=0;t("ytDomDomGetNextId",v("ytDomDomGetNextId")||function(){return++of},void 0);var pf={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function qf(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.event=a;for(var b in a)b in pf||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?
b=a.fromElement:"mouseout"==this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.b=a.pageX;this.f=a.pageY}}
function rf(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.b=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.f=a.clientY+b}}
qf.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
qf.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
qf.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var Ya=v("ytEventsEventsListeners")||{};t("ytEventsEventsListeners",Ya,void 0);var sf=v("ytEventsEventsCounter")||{count:0};t("ytEventsEventsCounter",sf,void 0);function tf(a,b,c,d){d=void 0===d?!1:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Xa(function(e){return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&e[4]==!!d})}
function U(a,b,c){var d=void 0===d?!1:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=tf(a,b,c,d);if(e)return e;e=++sf.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(d){d=new qf(d);if(!Mb(d.relatedTarget,function(b){return b==a}))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new qf(b);
b.currentTarget=a;return c.call(a,b)};
g=ae(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),a.addEventListener(b,g,d)):a.attachEvent("on"+b,g);Ya[e]=[a,b,c,g,d];return e}
function uf(a){a&&("string"==typeof a&&(a=[a]),C(a,function(a){if(a in Ya){var b=Ya[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?d.removeEventListener(e,f,b):d.detachEvent&&d.detachEvent("on"+e,f);delete Ya[a]}}))}
;function vf(a){this.o=a;this.b=null;this.i=0;this.l=null;this.j=0;this.f=[];for(a=0;4>a;a++)this.f.push(0);this.g=0;this.D=U(window,"mousemove",x(this.G,this));a=x(this.w,this);ra(a)&&(a=ae(a));this.H=window.setInterval(a,25)}
A(vf,G);vf.prototype.G=function(a){q(a.b)||rf(a);var b=a.b;q(a.f)||rf(a);this.b=new Fb(b,a.f)};
vf.prototype.w=function(){if(this.b){var a=O();if(0!=this.i){var b=this.l,c=this.b,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.i);this.f[this.g]=.5<Math.abs((d-this.j)/this.j)?1:0;for(c=b=0;4>c;c++)b+=this.f[c]||0;3<=b&&this.o();this.j=d}this.i=a;this.l=this.b;this.g=(this.g+1)%4}};
vf.prototype.m=function(){window.clearInterval(this.H);uf(this.D)};var wf={};
function xf(a){if(null==v("_lact",window)){var b=parseInt(Q("LACT"),10);b=isFinite(b)?z()-Math.max(b,0):-1;t("_lact",b,window);t("_fact",b,window);-1==b&&W();U(document,"keydown",W);U(document,"keyup",W);U(document,"mousedown",W);U(document,"mouseup",W);S("lact_local_listeners")||a?(U(window,"resize",function(){yf("resize",200)}),U(window,"scroll",function(){yf("scroll",200)}),new vf(function(){yf("mouse",100)}),U(document,"touchstart",W),U(document,"touchend",W)):(ke("page-mouse",W),ke("page-scroll",W),
ke("page-resize",W))}}
function yf(a,b){wf[a]||(wf[a]=!0,gf(function(){W();wf[a]=!1},b))}
function W(){null==v("_lact",window)&&xf();var a=z();t("_lact",a,window);-1==v("_fact",window)&&t("_fact",a,window);(a=v("ytglobal.ytUtilActivityCallback_"))&&a()}
function zf(){var a=v("_lact",window);return null==a?-1:Math.max(z()-a,0)}
;var Af=Math.pow(2,16)-1,Bf={log_event:"events",log_interaction:"interactions"},Cf=Object.create(null);Cf.log_event="GENERIC_EVENT_LOGGING";Cf.log_interaction="INTERACTION_LOGGING";var Df={},Ef={},Ff=0,X=v("ytLoggingTransportLogPayloadsQueue_")||{};t("ytLoggingTransportLogPayloadsQueue_",X,void 0);var Gf=v("ytLoggingTransportTokensToCttTargetIds_")||{};t("ytLoggingTransportTokensToCttTargetIds_",Gf,void 0);var Hf=v("ytLoggingTransportDispatchedStats_")||{};
t("ytLoggingTransportDispatchedStats_",Hf,void 0);t("ytytLoggingTransportCapturedTime_",v("ytLoggingTransportCapturedTime_")||{},void 0);function If(a,b){Ef[a.endpoint]=b;if(S("very_optimistically_create_gel_client"))for(var c in X)if(!Df[c]){var d=Ef[c];d&&(Df[c]=new d)}a.W?(c=a.W,d={},c.videoId?d.videoId=c.videoId:c.playlistId&&(d.playlistId=c.playlistId),Gf[a.W.token]=d,c=Jf(a.endpoint,a.W.token)):c=Jf(a.endpoint);c.push(a.payload);c.length>=(Number(S("web_logging_max_batch")||0)||20)?Kf():Lf()}
function Kf(){fe(Ff);if(!Za(X)){for(var a in X){var b=Df[a];if(!b){var c=Ef[a];if(!c)continue;b=new c;Df[a]=b}c=void 0;var d=a,e=b,f=Bf[d],g=Hf[d]||{};Hf[d]=g;b=Math.round(O());for(c in X[d]){var h=e.b;h={client:{hl:h.Ha,gl:h.Ga,clientName:h.Fa,clientVersion:h.innertubeContextClientVersion}};var k=window.devicePixelRatio;k&&1!=k&&(h.client.screenDensityFloat=String(k));Q("DELEGATED_SESSION_ID")&&(h.user={onBehalfOfUser:Q("DELEGATED_SESSION_ID")});h={context:h};h[f]=Jf(d,c);g.dispatchedEventCount=
g.dispatchedEventCount||0;g.dispatchedEventCount+=h[f].length;if(k=Gf[c])a:{var m=h,u=c;if(k.videoId)var M="VIDEO";else if(k.playlistId)M="PLAYLIST";else break a;m.credentialTransferTokenTargetId=k;m.context=m.context||{};m.context.user=m.context.user||{};m.context.user.credentialTransferTokens=[{token:u,scope:M}]}delete Gf[c];k=h;k.requestTimeMs=b;(M=Q("EVENT_ID",void 0))&&S("enable_gel_web_client_event_id")&&(m=(Q("BATCH_CLIENT_COUNTER",void 0)||0)+1,m>Af&&(m=1),P("BATCH_CLIENT_COUNTER",m),k.serializedClientEventId=
{serializedEventId:M,clientCounter:m});Mf(e,d,h,{retry:!0})}c=g;d=b;c.previousDispatchMs&&(b=d-c.previousDispatchMs,e=c.diffCount||0,c.averageTimeBetweenDispatchesMs=e?(c.averageTimeBetweenDispatchesMs*e+b)/(e+1):b,c.diffCount=e+1);c.previousDispatchMs=d;delete X[a]}Za(X)||Lf()}}
function Lf(){fe(Ff);Ff=T(Kf,Q("LOGGING_BATCH_TIMEOUT",1E4))}
function Jf(a,b){b=void 0===b?"":b;X[a]=X[a]||{};X[a][b]=X[a][b]||[];return X[a][b]}
;function Nf(a,b,c,d){var e=Of,f={};f.eventTimeMs=Math.round(c||O());f[a]=b;f.context={lastActivityMs:String(c?-1:zf())};If({endpoint:"log_event",payload:f,W:d},e)}
;function Pf(a,b,c){c.context&&c.context.capabilities&&(c=c.context.capabilities,c.snapshot||c.golden)&&(a="vix");return"/youtubei/"+a+"/"+b}
function Qf(a){var b={"X-Goog-Visitor-Id":Q("VISITOR_DATA","")},c;a?c="Bearer "+v("gapi.auth.getToken")().cb:c=ac([]);c&&(b.Authorization=c,b["X-Goog-AuthUser"]=Q("SESSION_INDEX",0));return b}
function Rf(a){a=Object.assign({},a);delete a.Authorization;var b=ac();if(b){var c=new sc;c.update(Q("INNERTUBE_API_KEY",void 0));c.update(b);b=c.digest();if(!pc)for(pc={},qc={},c=0;65>c;c++)pc[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".charAt(c),qc[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.".charAt(c);c=qc;for(var d=[],e=0;e<b.length;e+=3){var f=b[e],g=e+1<b.length,h=g?b[e+1]:0,k=e+2<b.length,m=k?b[e+2]:0,u=f>>2;f=(f&3)<<4|h>>4;h=(h&15)<<2|m>>
6;m&=63;k||(m=64,g||(h=64));d.push(c[u],c[f],c[h],c[m])}a.hash=d.join("")}return a}
;function Sf(a,b,c,d){$b.set(""+a,b,c,"/",void 0===d?"youtube.com":d,!1)}
;function Tf(){var a=new xd;(a=a.isAvailable()?new Ed(a,"yt.innertube"):null)||(a=new zd("yt.innertube"),a=a.isAvailable()?a:null);this.b=a?new sd(a):null;this.f=document.domain||window.location.hostname}
Tf.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.b)try{this.b.set(a,b,z()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(Jc(b))}catch(f){return}else e=escape(b);Sf(a,e,c,this.f)};
Tf.prototype.get=function(a,b){var c=void 0,d=!this.b;if(!d)try{c=this.b.get(a)}catch(e){d=!0}if(d&&(c=$b.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Tf.prototype.remove=function(a){this.b&&this.b.remove(a);var b=this.f;$b.remove(""+a,"/",void 0===b?"youtube.com":b)};var Uf=new Tf;function Vf(a,b,c,d){if(d)return null;d=Uf.get("nextId",!0)||1;var e=Uf.get("requests",!0)||{};e[d]={method:a,request:b,authState:Rf(c),requestTime:Math.round(O())};Uf.set("nextId",d+1,86400,!0);Uf.set("requests",e,86400,!0);return d}
function Wf(a){var b=Uf.get("requests",!0)||{};delete b[a];Uf.set("requests",b,86400,!0)}
function Xf(a){var b=Uf.get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(O())-d.requestTime)){var e=d.authState;var f=Rf(Qf(!1));a:{var g=void 0;for(g in e)if(!(g in f)||e[g]!==f[g]){e=!1;break a}for(g in f)if(!(g in e)){e=!1;break a}e=!0}e&&Mf(a,d.method,d.request,{});delete b[c]}}Uf.set("requests",b,86400,!0)}}
;function Of(a){var b=this;this.b=a||{innertubeApiKey:Zd("INNERTUBE_API_KEY"),innertubeApiVersion:Zd("INNERTUBE_API_VERSION"),Fa:Q("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:Zd("INNERTUBE_CONTEXT_CLIENT_VERSION"),Ha:Zd("INNERTUBE_CONTEXT_HL"),Ga:Zd("INNERTUBE_CONTEXT_GL"),Ia:Zd("INNERTUBE_HOST_OVERRIDE")||"",Ja:!!Q("INNERTUBE_USE_THIRD_PARTY_AUTH",!1)};ef(function(){Xf(b)})}
function Mf(a,b,c,d){!Q("VISITOR_DATA")&&.01>Math.random()&&R(Error("Missing VISITOR_DATA when sending innertube request."),"WARNING");var e={headers:{"Content-Type":"application/json"},method:"POST",B:c,qa:"JSON",M:function(){d.M()},
pa:d.M,A:function(a,b){d.A&&d.A(b)},
oa:function(a){d.A&&d.A(a)},
onError:function(a,b){if(d.onError)d.onError(b)},
ib:function(a){if(d.onError)d.onError(a)},
timeout:d.timeout,withCredentials:!0},f=a.b.Ja||!1,g=Qf(f);Object.assign(e.headers,g);var h="",k=a.b.Ia;k&&(h=k);e.headers.Authorization&&!h&&(e.headers["x-origin"]=window.location.origin);h=""+h+Pf(a.b.innertubeApiVersion,b,c)+"?alt=json&key="+a.b.innertubeApiKey;var m;if(d.retry&&S("retry_web_logging_batches")&&(m=Vf(b,c,g,f))){var u=e.A,M=e.oa;e.A=function(a,b){Wf(m);u(a,b)};
c.oa=function(a,b){Wf(m);M(a,b)}}try{S("use_fetch_for_op_xhr")?Le(h,e):Ue(h,e)}catch(aa){if("InvalidAccessError"==aa)m&&(Wf(m),m=0),R(Error("An extension is blocking network request."),"WARNING");
else throw aa;}m&&ef(function(){Xf(a)},5E3)}
;var Yf=z().toString();
function Zf(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=z();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(Yf)for(a=1,b=0;b<Yf.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^Yf.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_".charAt(d[b]&63));
return a.join("")}
;var $f=Zf();function ag(a,b,c,d,e){this.h=a;this.i=b;this.g=c;this.f=d;this.b=e}
function bg(a){var b={};void 0!==a.h?b.trackingParams=a.h:(b.veType=a.i,null!=a.g&&(b.veCounter=a.g),null!=a.f&&(b.elementIndex=a.f));void 0!==a.b&&(b.dataElement=bg(a.b));return b}
var cg=1;function dg(){var a=Q("ROOT_VE_TYPE",void 0);return a?new ag(void 0,a,void 0):null}
function eg(){var a=Q("client-screen-nonce")||Q("EVENT_ID");return a?a:null}
function fg(a,b){P("client-screen-nonce",a);P("ROOT_VE_TYPE",b);window.requestAnimationFrame(function(){setTimeout(function(){a&&Nf("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:$f,clientScreenNonce:a})},0)})}
;function gg(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=Q("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=Q("VALID_SESSION_TEMPDATA_DOMAINS",[]),f=Id(J(window.location.href)[3]||null);f&&e.push(f);f=Id(J(d)[3]||null);if(0<=ya(e,f)||!f&&0==d.lastIndexOf("/",0))if(S("autoescape_tempdata_url")&&(e=document.createElement("a"),Cb(e,d),d=e.href),d){f=J(d);d=f[5];e=f[6];f=f[7];var g="";d&&(g+=d);e&&(g+="?"+e);f&&(g+="#"+f);d=g;e=d.indexOf("#");if(d=0>e?d:d.substr(0,e)){if(b.itct||b.ved)b.csn=b.csn||
eg();if(h){var h=parseInt(h,10);isFinite(h)&&0<h&&(d="ST-"+Pa(d).toString(36),b=b?Kd(b):"",Sf(d,b,h||5))}else h="ST-"+Pa(d).toString(36),b=b?Kd(b):"",Sf(h,b,5)}}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var k=void 0===k?{}:k;var m=void 0===m?"":m;var u=void 0===u?window:u;c=u.location;a=Ld(a,k)+m;a=a instanceof E?a:xb(a);c.href=vb(a)}return!0}
;function hg(a,b,c){ig({attachChild:{csn:a,parentVisualElement:bg(b),visualElements:[bg(c)]}})}
function ig(a){var b=Of;a.eventTimeMs=Math.round(O());a.lactMs=zf();If({endpoint:"log_interaction",payload:a},b)}
;function jg(a){a=a||{};this.url=a.url||"";this.args=a.args||ab(kg);this.assets=a.assets||{};this.attrs=a.attrs||ab(lg);this.params=a.params||ab(mg);this.minVersion=a.min_version||"8.0.0";this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
var kg={enablejsapi:1},lg={},mg={allowscriptaccess:"always",allowfullscreen:"true",bgcolor:"#000000"};function ng(a){var b=new jg,c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];b[c]="object"==pa(d)?ab(d):d}return b}
;function og(){G.call(this);this.b=[]}
n(og,G);og.prototype.m=function(){for(;this.b.length;){var a=this.b.pop();a.target.removeEventListener(a.name,a.fb)}G.prototype.m.call(this)};var pg=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function qg(a){a=a||"";if(window.spf){var b=a.match(pg);spf.style.load(a,b?b[1]:"",void 0)}else rg(a)}
function rg(a){var b=sg(a),c=document.getElementById(b),d=c&&de(c,"loaded");d||c&&!d||(c=tg(a,b,function(){de(c,"loaded")||(be(c),ne(b),T(y(oe,b),0))}))}
function tg(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Ob(a);Db(d,a,"stylesheet");(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function sg(a){var b=document.createElement("A");a=yb(a);Cb(b,a);b=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Pa(b)}
;var ug=v("ytLoggingLatencyUsageStats_")||{};t("ytLoggingLatencyUsageStats_",ug,void 0);var vg=0;function wg(a){ug[a]=ug[a]||{count:0};var b=ug[a];b.count++;b.time=O();vg||(vg=ef(xg,5E3));return 10<b.count?(11==b.count&&af(Error("CSI data exceeded logging limit with key: "+a),0==a.indexOf("info")?"WARNING":"ERROR"),!0):!1}
function xg(){var a=O(),b;for(b in ug)6E4<a-ug[b].time&&delete ug[b];vg=0}
;function yg(a,b){this.version=a;this.args=b}
;function zg(a){this.topic=a}
zg.prototype.toString=function(){return this.topic};var Ag=v("ytPubsub2Pubsub2Instance")||new I;I.prototype.subscribe=I.prototype.subscribe;I.prototype.unsubscribeByKey=I.prototype.L;I.prototype.publish=I.prototype.J;I.prototype.clear=I.prototype.clear;t("ytPubsub2Pubsub2Instance",Ag,void 0);t("ytPubsub2Pubsub2SubscribedKeys",v("ytPubsub2Pubsub2SubscribedKeys")||{},void 0);t("ytPubsub2Pubsub2TopicToKeys",v("ytPubsub2Pubsub2TopicToKeys")||{},void 0);t("ytPubsub2Pubsub2IsAsync",v("ytPubsub2Pubsub2IsAsync")||{},void 0);
t("ytPubsub2Pubsub2SkipSubKey",null,void 0);function Bg(a,b){var c=v("ytPubsub2Pubsub2Instance");c&&c.publish.call(c,a.toString(),a,b)}
;var Y=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{};function Cg(){var a=Q("TIMING_TICK_EXPIRATION");a||(a={},P("TIMING_TICK_EXPIRATION",a));return a}
function Dg(){var a=Cg(),b;for(b in a)jf(a[b]);P("TIMING_TICK_EXPIRATION",{})}
;function Eg(a,b){yg.call(this,1,arguments)}
n(Eg,yg);function Fg(a,b){yg.call(this,1,arguments)}
n(Fg,yg);var Gg=new zg("aft-recorded"),Hg=new zg("timing-sent");var Ig={vc:!0},Jg={ad_allowed:"adTypesAllowed",ad_at:"adType",ad_cpn:"adClientPlaybackNonce",ad_docid:"adVideoId",yt_ad_an:"adNetworks",p:"httpProtocol",t:"transportProtocol",cpn:"clientPlaybackNonce",csn:"clientScreenNonce",docid:"videoId",is_nav:"isNavigation",yt_lt:"loadType",yt_ad:"isMonetized",nr:"webInfo.navigationReason",ncnp:"webInfo.nonPreloadedNodeCount",paused:"playerInfo.isPausedOnLoad",fmt:"playerInfo.itag",yt_pl:"watchInfo.isPlaylist",yt_ad_pr:"prerollAllowed",yt_red:"isRedSubscriber",
st:"serverTimeMs",vph:"viewportHeight",vpw:"viewportWidth",yt_vis:"isVisible"},Kg="ap c cver ei srt yt_fss yt_li plid vpil vpni vpst yt_eil vpni2 vpil2 icrc icrt pa GetBrowse_rid GetPlayer_rid GetSearch_rid GetWatchNext_rid cmt d_vpct d_vpnfi d_vpni pc pfa pfeh pftr prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis yt_ref yt_sts".split(" "),Ng="isNavigation isMonetized playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber isVisible watchInfo.isPlaylist".split(" "),
Og=!1;
function Pg(a){if("_"!=a[0]){var b=a;Y.mark&&(0==b.lastIndexOf("mark_",0)||(b="mark_"+b),Y.mark(b))}b=Qg();var c=O();b[a]&&(b["_"+a]=b["_"+a]||[b[a]],b["_"+a].push(c));b[a]=c;b=Cg();if(c=b[a])jf(c),b[a]=0;Rg()["tick_"+a]=void 0;O();Sg()?(b=Tg(),"_start"==a?wg("baseline_"+b)||Nf("latencyActionBaselined",{clientActionNonce:b},void 0,void 0):wg("tick_"+a+"_"+b)||Nf("latencyActionTicked",{tickName:a,clientActionNonce:b},void 0,void 0),a=!0):a=!1;if(a=!a)a=!v("yt.timing.pingSent_");if(a&&(b=Zd("TIMING_ACTION"),a=
Qg(),v("ytglobal.timingready_")&&b&&a._start&&(b=Ug()))){S("tighter_critical_section")&&!Og&&(Bg(Gg,new Eg(Math.round(b-a._start),void 0)),Og=!0);b=!0;c=Q("TIMING_WAIT",[]);if(c.length)for(var d=0,e=c.length;d<e;++d)if(!(c[d]in a)){b=!1;break}b&&Vg()}}
function Wg(){var a=Xg().info.yt_lt="hot_bg";Rg().info_yt_lt=a;if(Sg())if("yt_lt"in Jg){var b=Jg.yt_lt;0<=ya(Ng,b)&&(a=!!a);if(Sg()){var c={};b=b.split(".");for(var d=c,e=0;e<b.length-1;e++)d[b[e]]=d[b[e]]||{},d=d[b[e]];d[b[b.length-1]]=a;a=Tg();b=Object.keys(c).join("");wg("info_"+b+"_"+a)||(c.clientActionNonce=a,Nf("latencyActionInfo",c,void 0,void 0))}}else 0<=ya(Kg,"yt_lt")||R(Error("Unknown label yt_lt logged with GEL CSI."))}
function Ug(){var a=Qg();if(a.aft)return a.aft;for(var b=Q("TIMING_AFT_KEYS",["ol"]),c=b.length,d=0;d<c;d++){var e=a[b[d]];if(e)return e}return NaN}
function Vg(){Dg();if(!Sg()){var a=Qg(),b=Xg().info,c=a._start,d;for(d in a)if(0==d.lastIndexOf("_",0)&&w(a[d])){var e=d.slice(1);if(e in Ig){var f=Aa(a[d],function(a){return Math.round(a-c)});
b["all_"+e]=f.join()}delete a[d]}e=!!b.ap;if(f=v("ytglobal.timingReportbuilder_")){if(f=f(a,b,void 0))Yg(f,e),Zg(),$g(),ah(!1,void 0),Q("TIMING_ACTION")&&P("PREVIOUS_ACTION",Q("TIMING_ACTION")),P("TIMING_ACTION","")}else{var g=Q("CSI_SERVICE_NAME","youtube");f={v:2,s:g,action:Q("TIMING_ACTION",void 0)};var h=b.srt;void 0!==a.srt&&delete b.srt;if(b.h5jse){var k=window.location.protocol+v("ytplayer.config.assets.js");(k=Y.getEntriesByName?Y.getEntriesByName(k)[0]:null)?b.h5jse=Math.round(b.h5jse-k.responseEnd):
delete b.h5jse}a.aft=Ug();bh()&&"youtube"==g&&(Wg(),g=a.vc,k=a.pbs,delete a.aft,b.aft=Math.round(k-g));for(var m in b)"_"!=m.charAt(0)&&(f[m]=b[m]);a.ps=O();b={};m=[];for(d in a)"_"!=d.charAt(0)&&(g=Math.round(a[d]-c),b[d]=g,m.push(d+"."+g));f.rt=m.join(",");(a=v("ytdebug.logTiming"))&&a(f,b);Yg(f,e,void 0);Bg(Hg,new Fg(b.aft+(h||0),void 0))}}}
var $g=x(Y.clearResourceTimings||Y.webkitClearResourceTimings||Y.mozClearResourceTimings||Y.msClearResourceTimings||Y.oClearResourceTimings||na,Y);
function Yg(a,b,c){if(S("debug_csi_data")){var d=v("yt.timing.csiData");d||(d=[],t("yt.timing.csiData",d,void 0));d.push({page:location.href,time:new Date,args:a})}d="";for(var e in a)d+="&"+e+"="+a[e];a="/csi_204?"+d.substring(1);if(window.navigator&&window.navigator.sendBeacon&&b){var f=void 0===f?"":f;try{window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,f)||Xe(a,void 0,void 0,void 0,f)}catch(g){Xe(a,void 0,void 0,void 0,f)}}else Xe(a);ah(!0,c)}
function Tg(){var a=Xg().nonce;a||(a=Zf(),Xg().nonce=a);return a}
function Qg(){return Xg().tick}
function Rg(){var a=Xg();"gel"in a||(a.gel={});return a.gel}
function Xg(){return v("ytcsi.data_")||Zg()}
function Zg(){var a={tick:{},info:{}};t("ytcsi.data_",a,void 0);return a}
function ah(a,b){t("yt.timing."+(b||"")+"pingSent_",a,void 0)}
function bh(){var a=Qg(),b=a.pbr,c=a.vc;a=a.pbs;return b&&c&&a&&b<c&&c<a&&1==Xg().info.yt_pvis}
function Sg(){return!!S("csi_on_gel")}
;function ch(a,b){G.call(this);this.l=this.T=a;this.H=b;this.o=!1;this.f={};this.R=this.G=null;this.w=new I;uc(this,y(vc,this.w));this.i={};this.O=this.S=this.g=this.Y=this.b=null;this.N=!1;this.j=this.D=null;this.U={};this.ua=["onReady"];this.X=null;this.ka=NaN;this.P={};dh(this);this.V("WATCH_LATER_VIDEO_ADDED",this.La.bind(this));this.V("WATCH_LATER_VIDEO_REMOVED",this.Ma.bind(this));this.V("onAdAnnounce",this.ya.bind(this));this.va=new og(this);uc(this,y(vc,this.va))}
n(ch,G);l=ch.prototype;
l.ha=function(a){if(!this.h){a instanceof jg||(a=new jg(a));this.Y=a;this.b=ng(a);this.g=this.b.attrs.id||this.g;"video-player"==this.g&&(this.g=this.H,this.b.attrs.id=this.H);this.l.id==this.g&&(this.g+="-player",this.b.attrs.id=this.g);this.b.args.enablejsapi="1";this.b.args.playerapiid=this.H;this.S||(this.S=eh(this,this.b.args.jsapicallback||"onYouTubePlayerReady"));this.b.args.jsapicallback=null;if(a=this.b.attrs.width)this.l.style.width=Tb(Number(a)||a);if(a=this.b.attrs.height)this.l.style.height=Tb(Number(a)||
a);fh(this);this.o&&gh(this)}};
l.Ba=function(){return this.Y};
function gh(a){a.b.loaded||(a.b.loaded=!0,"0"!=a.b.args.autoplay?a.f.loadVideoByPlayerVars(a.b.args):a.f.cueVideoByPlayerVars(a.b.args))}
function hh(a){var b=!0,c=ih(a);c&&a.b&&(a=a.b,b=de(c,"version")==a.assets.js);return b&&!!v("yt.player.Application.create")}
function fh(a){if(!a.h&&!a.N){var b=hh(a);if(b&&"html5"==(ih(a)?"html5":null))a.O="html5",a.o||jh(a);else if(kh(a),a.O="html5",b&&a.j)a.T.appendChild(a.j),jh(a);else{a.b.loaded=!0;var c=!1;a.D=function(){c=!0;var b=ng(a.b);v("yt.player.Application.create")(a.T,b);jh(a)};
a.N=!0;b?a.D():(se(a.b.assets.js,a.D),qg(a.b.assets.css),lh(a)&&!c&&t("yt.player.Application.create",null,void 0))}}}
function ih(a){var b=Hb(a.g);!b&&a.l&&a.l.querySelector&&(b=a.l.querySelector("#"+a.g));return b}
function jh(a){if(!a.h){var b=ih(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);c?(a.N=!1,b.isNotServable&&b.isNotServable(a.b.args.video_id)||mh(a)):a.ka=T(function(){jh(a)},50)}}
function mh(a){dh(a);a.o=!0;var b=ih(a);b.addEventListener&&(a.G=nh(a,b,"addEventListener"));b.removeEventListener&&(a.R=nh(a,b,"removeEventListener"));var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=0;d<c.length;d++){var e=c[d];a.f[e]||(a.f[e]=nh(a,b,e))}for(var f in a.i)a.G(f,a.i[f]);gh(a);a.S&&a.S(a.f);a.w.J("onReady",a.f)}
function nh(a,b,c){var d=b[c];return function(){try{return a.X=null,d.apply(b,arguments)}catch(e){"sendAbandonmentPing"!=c&&(e.message+=" ("+c+")",a.X=e,R(e,"WARNING",void 0,void 0,void 0))}}}
function dh(a){a.o=!1;if(a.R)for(var b in a.i)a.R(b,a.i[b]);for(var c in a.P)fe(parseInt(c,10));a.P={};a.G=null;a.R=null;for(var d in a.f)a.f[d]=null;a.f.addEventListener=a.V.bind(a);a.f.removeEventListener=a.Sa.bind(a);a.f.destroy=a.dispose.bind(a);a.f.getLastError=a.Ca.bind(a);a.f.getPlayerType=a.Da.bind(a);a.f.getCurrentVideoConfig=a.Ba.bind(a);a.f.loadNewVideoConfig=a.ha.bind(a);a.f.isReady=a.Ka.bind(a)}
l.Ka=function(){return this.o};
l.V=function(a,b){var c=this,d=eh(this,b);if(d){if(!(0<=ya(this.ua,a)||this.i[a])){var e=oh(this,a);this.G&&this.G(a,e)}this.w.subscribe(a,d);"onReady"==a&&this.o&&T(function(){d(c.f)},0)}};
l.Sa=function(a,b){if(!this.h){var c=eh(this,b);c&&md(this.w,a,c)}};
function eh(a,b){var c=b;if("string"==typeof b){if(a.U[b])return a.U[b];c=function(){var a=v(b);a&&a.apply(p,arguments)};
a.U[b]=c}return c?c:null}
function oh(a,b){var c="ytPlayer"+b+a.H;a.i[b]=c;p[c]=function(c){var d=a.b&&a.b.args&&a.b.args.fflags;if(d&&0>d.indexOf("use_html5_player_event_timeout=true"))a.w.J(b,c);else{var f=T(function(){if(!a.h){a.w.J(b,c);var d=a.P,e=String(f);e in d&&delete d[e]}},0);
$a(a.P,String(f))}};
return c}
l.ya=function(a){ne("a11y-announce",a)};
l.La=function(a){ne("WATCH_LATER_VIDEO_ADDED",a)};
l.Ma=function(a){ne("WATCH_LATER_VIDEO_REMOVED",a)};
l.Da=function(){return this.O||(ih(this)?"html5":null)};
l.Ca=function(){return this.X};
function kh(a){Pg("dcp");a.cancel();dh(a);a.O=null;a.b&&(a.b.loaded=!1);var b=ih(a);b&&(hh(a)||!lh(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));for(a=a.T;b=a.firstChild;)a.removeChild(b)}
l.cancel=function(){this.D&&ye(this.b.assets.js,this.D);fe(this.ka);this.N=!1};
l.m=function(){kh(this);if(this.j&&this.b&&this.j.destroy)try{this.j.destroy()}catch(b){R(Error("Error destroying player: "+b))}this.U=null;for(var a in this.i)p[this.i[a]]=null;this.Y=this.b=this.f=null;delete this.T;delete this.l;G.prototype.m.call(this)};
function lh(a){return a.b&&a.b.args&&a.b.args.fflags?-1!=a.b.args.fflags.indexOf("player_destroy_old_version=true"):!1}
;var ph={},qh="player_uid_"+(1E9*Math.random()>>>0);function rh(a){var b="player";b=r(b)?Hb(b):b;var c=qh+"_"+(b[ta]||(b[ta]=++ua)),d=ph[c];if(d)return d.ha(a),d.f;d=new ch(b,c);ph[c]=d;ne("player-added",d.f);uc(d,y(sh,d));T(function(){d.ha(a)},0);
return d.f}
function sh(a){delete ph[a.H]}
;function th(){var a=uh(),b=vh();if(!a&&!b||!window.JSON)return null;try{var c=a.get("yt-player-two-stage-token")}catch(d){}if(!r(c))try{c=b.get("yt-player-two-stage-token")}catch(d){}if(!r(c))return null;try{c=JSON.parse(c,void 0)}catch(d){}return c}
var vh=Nb(function(){var a=new xd;return a.isAvailable()?new td(a):null}),uh=Nb(function(){var a=new yd;
return a.isAvailable()?new td(a):null});function wh(a){return(0==a.search("cue")||0==a.search("load"))&&"loadModule"!=a}
function xh(a,b,c){r(a)&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});b=/\/([ve]|embed)\/([^#?]+)/.exec(a.mediaContentUrl);a.videoId=b&&b[2]?b[2]:null;return yh(a)}
function yh(a,b,c){if(sa(a)){b="endSeconds startSeconds mediaContentUrl suggestedQuality videoId two_stage_token".split(" ");c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}return{videoId:a,startSeconds:b,suggestedQuality:c}}
function zh(a,b,c,d){if(sa(a)&&!w(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};r(a)&&16==a.length?b.list="PL"+a:b.playlist=a;return b}
function Ah(a){var b=a.video_id||a.videoId;if(r(b)){var c=th()||{},d=th()||{};q(void 0)?d[b]=void 0:delete d[b];var e=z()+3E5,f=vh();if(f&&window.JSON){r(d)||(d=JSON.stringify(d,void 0));try{f.set("yt-player-two-stage-token",d,e)}catch(g){f.remove("yt-player-two-stage-token")}}(b=c[b])&&(a.two_stage_token=b)}}
;function Bh(a){G.call(this);this.b=a;this.b.subscribe("command",this.ra,this);this.f={};this.i=!1}
A(Bh,G);l=Bh.prototype;l.start=function(){this.i||this.h||(this.i=!0,Ch(this.b,"RECEIVING"))};
l.ra=function(a,b,c){if(this.i&&!this.h){var d=b||{};switch(a){case "addEventListener":r(d.event)&&(a=d.event,a in this.f||(c=x(this.Ua,this,a),this.f[a]=c,this.addEventListener(a,c)));break;case "removeEventListener":r(d.event)&&Dh(this,d.event);break;default:this.g.isReady()&&this.g[a]&&(b=Eh(a,b||{}),c=this.g.handleExternalCall(a,b,c||null),(c=Fh(a,c))&&this.i&&!this.h&&Ch(this.b,a,c))}}};
l.Ua=function(a,b){this.i&&!this.h&&Ch(this.b,a,this.ba(a,b))};
l.ba=function(a,b){if(null!=b)return{value:b}};
function Dh(a,b){b in a.f&&(a.removeEventListener(b,a.f[b]),delete a.f[b])}
l.m=function(){var a=this.b;a.h||md(a.b,"command",this.ra,this);this.b=null;for(var b in this.f)Dh(this,b);Bh.u.m.call(this)};function Gh(a,b){Bh.call(this,b);this.g=a;this.start()}
A(Gh,Bh);Gh.prototype.addEventListener=function(a,b){this.g.addEventListener(a,b)};
Gh.prototype.removeEventListener=function(a,b){this.g.removeEventListener(a,b)};
function Eh(a,b){switch(a){case "loadVideoById":return b=yh(b),Ah(b),[b];case "cueVideoById":return b=yh(b),Ah(b),[b];case "loadVideoByPlayerVars":return Ah(b),[b];case "cueVideoByPlayerVars":return Ah(b),[b];case "loadPlaylist":return b=zh(b),Ah(b),[b];case "cuePlaylist":return b=zh(b),Ah(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];
case "setLoop":return[b.loopPlaylists];case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey]}return[]}
function Fh(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
Gh.prototype.ba=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return Gh.u.ba.call(this,a,b)};
Gh.prototype.m=function(){Gh.u.m.call(this);delete this.g};function Hh(a,b,c,d){G.call(this);this.f=b||null;this.o="*";this.g=c||null;this.sessionId=null;this.channel=d||null;this.D=!!a;this.l=x(this.w,this);window.addEventListener("message",this.l)}
n(Hh,G);Hh.prototype.w=function(a){if(!("*"!=this.g&&a.origin!=this.g||this.f&&a.source!=this.f)&&r(a.data)){try{var b=JSON.parse(a.data)}catch(c){return}if(!(null==b||this.D&&(this.sessionId&&this.sessionId!=b.id||this.channel&&this.channel!=b.channel))&&b)switch(b.event){case "listening":"null"!=a.origin&&(this.g=this.o=a.origin);this.f=a.source;this.sessionId=b.id;this.b&&(this.b(),this.b=null);break;case "command":this.i&&(!this.j||0<=ya(this.j,b.func))&&this.i(b.func,b.args,a.origin)}}};
Hh.prototype.sendMessage=function(a,b){var c=b||this.f;if(c){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var d=Jc(a);c.postMessage(d,this.o)}catch(e){R(e,"WARNING")}}};
Hh.prototype.m=function(){window.removeEventListener("message",this.l);G.prototype.m.call(this)};function Ih(a,b,c){Hh.call(this,a,b,c||Q("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname,"widget");this.j=this.b=this.i=null}
n(Ih,Hh);function Jh(){var a=this.f=new Ih(!!Q("WIDGET_ID_ENFORCE")),b=x(this.Oa,this);a.i=b;a.j=null;this.f.channel="widget";if(a=Q("WIDGET_ID"))this.f.sessionId=a;this.g=[];this.j=!1;this.i={}}
l=Jh.prototype;l.Oa=function(a,b,c){"addEventListener"==a&&b?(a=b[0],this.i[a]||"onReady"==a||(this.addEventListener(a,Kh(this,a)),this.i[a]=!0)):this.ta(a,b,c)};
l.ta=function(){};
function Kh(a,b){return x(function(a){this.sendMessage(b,a)},a)}
l.addEventListener=function(){};
l.Aa=function(){this.j=!0;this.sendMessage("initialDelivery",this.ca());this.sendMessage("onReady");C(this.g,this.sa,this);this.g=[]};
l.ca=function(){return null};
function Lh(a,b){a.sendMessage("infoDelivery",b)}
l.sa=function(a){this.j?this.f.sendMessage(a):this.g.push(a)};
l.sendMessage=function(a,b){this.sa({event:a,info:void 0==b?null:b})};
l.dispose=function(){this.f=null};function Mh(a){Jh.call(this);this.b=a;this.h=[];this.addEventListener("onReady",x(this.Na,this));this.addEventListener("onVideoProgress",x(this.Ya,this));this.addEventListener("onVolumeChange",x(this.Za,this));this.addEventListener("onApiChange",x(this.Ta,this));this.addEventListener("onPlaybackQualityChange",x(this.Va,this));this.addEventListener("onPlaybackRateChange",x(this.Wa,this));this.addEventListener("onStateChange",x(this.Xa,this));this.addEventListener("onWebglSettingsChanged",x(this.ab,
this))}
A(Mh,Jh);l=Mh.prototype;l.ta=function(a,b,c){if(this.b[a]){b=b||[];if(0<b.length&&wh(a)){var d=b;if(sa(d[0])&&!w(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=yh.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=xh.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=zh.apply(window,d)}d=e}Ah(d);b.length=1;b[0]=d}this.b.handleExternalCall(a,b,c);wh(a)&&Lh(this,this.ca())}};
l.Na=function(){var a=x(this.Aa,this);this.f.b=a};
l.addEventListener=function(a,b){this.h.push({eventType:a,listener:b});this.b.addEventListener(a,b)};
l.ca=function(){if(!this.b)return null;var a=this.b.getApiInterface();Ca(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c],f=e;if(0==f.search("get")||0==f.search("is")){f=e;var g=0;0==f.search("get")?g=3:0==f.search("is")&&(g=2);f=f.charAt(g).toLowerCase()+f.substr(g+1);try{var h=this.b[e]();b[f]=h}catch(k){}}}b.videoData=this.b.getVideoData();b.currentTimeLastUpdated_=z()/1E3;return b};
l.Xa=function(a){a={playerState:a,currentTime:this.b.getCurrentTime(),duration:this.b.getDuration(),videoData:this.b.getVideoData(),videoStartBytes:0,videoBytesTotal:this.b.getVideoBytesTotal(),videoLoadedFraction:this.b.getVideoLoadedFraction(),playbackQuality:this.b.getPlaybackQuality(),availableQualityLevels:this.b.getAvailableQualityLevels(),videoUrl:this.b.getVideoUrl(),playlist:this.b.getPlaylist(),playlistIndex:this.b.getPlaylistIndex(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),
mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());this.b.getStoryboardFormat&&(a.storyboardFormat=this.b.getStoryboardFormat());Lh(this,a)};
l.Va=function(a){Lh(this,{playbackQuality:a})};
l.Wa=function(a){Lh(this,{playbackRate:a})};
l.Ta=function(){for(var a=this.b.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.b.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],m=this.b.getOption(e,k);b[e][k]=m}}this.sendMessage("apiInfoDelivery",b)};
l.Za=function(){Lh(this,{muted:this.b.isMuted(),volume:this.b.getVolume()})};
l.Ya=function(a){a={currentTime:a,videoBytesLoaded:this.b.getVideoBytesLoaded(),videoLoadedFraction:this.b.getVideoLoadedFraction(),currentTimeLastUpdated_:z()/1E3,playbackRate:this.b.getPlaybackRate(),mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());Lh(this,a)};
l.ab=function(){if(this.b.getSphericalProperties){var a={SphericalProperties:this.b.getSphericalProperties()};Lh(this,a)}};
l.dispose=function(){Mh.u.dispose.call(this);for(var a=0;a<this.h.length;a++){var b=this.h[a];this.b.removeEventListener(b.eventType,b.listener)}this.h=[]};function Nh(){G.call(this);this.b=new I;uc(this,y(vc,this.b))}
A(Nh,G);Nh.prototype.subscribe=function(a,b,c){return this.h?0:this.b.subscribe(a,b,c)};
Nh.prototype.j=function(a,b){this.h||this.b.J.apply(this.b,arguments)};function Oh(a,b,c){Nh.call(this);this.f=a;this.g=b;this.i=c}
A(Oh,Nh);function Ch(a,b,c){if(!a.h){var d=a.f;d.h||a.g!=d.b||(a={id:a.i,command:b},c&&(a.data=c),d.b.postMessage(Jc(a),d.g))}}
Oh.prototype.m=function(){this.g=this.f=null;Oh.u.m.call(this)};function Ph(a,b,c){G.call(this);this.b=a;this.g=c;this.i=U(window,"message",x(this.j,this));this.f=new Oh(this,a,b);uc(this,y(vc,this.f))}
A(Ph,G);Ph.prototype.j=function(a){var b;if(b=!this.h)if(b=a.origin==this.g)a:{b=this.b;do{b:{var c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,r(b))){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.f,c.h||c.j("command",b.command,b.data,a.origin))}};
Ph.prototype.m=function(){uf(this.i);this.b=null;Ph.u.m.call(this)};function Qh(){var a=Wa(window,"settings","experiments","flags","html5_serverside_pagead_id_sets_cookie")||Q("EXP_HTML5_SERVERSIDE_PAGEAD_ID_SETS_COOKIE",!1)||S("html5_serverside_pagead_id_sets_cookie")?"//googleads.g.doubleclick.net/pagead/id?exp=nomnom":"//googleads.g.doubleclick.net/pagead/id",b=ab(Rh),c;return cd(new H(function(d,e){b.A=function(a){Ge(a)?d(a):e(new Sh("Request failed, status="+a.status,"net.badstatus",a))};
b.onError=function(a){e(new Sh("Unknown request error","net.unknown",a))};
b.M=function(a){e(new Sh("Request timed out","net.timeout",a))};
c=Oe(a,b)}),function(a){a instanceof dd&&c.abort();
return Vc(a)})}
function Sh(a,b){B.call(this,a+", errorCode="+b);this.errorCode=b;this.name="PromiseAjaxError"}
n(Sh,B);function Th(a){this.h=void 0===a?null:a;this.f=0;this.b=null}
Th.prototype.then=function(a,b,c){return this.h?this.h.then(a,b,c):1===this.f&&a?(a=a.call(c,this.b),Qc(a)?a:Uh(a)):2===this.f&&b?(a=b.call(c,this.b),Qc(a)?a:Vh(a)):this};
Th.prototype.getValue=function(){return this.b};
Pc(Th);function Vh(a){var b=new Th;a=void 0===a?null:a;b.f=2;b.b=void 0===a?null:a;return b}
function Uh(a){var b=new Th;a=void 0===a?null:a;b.f=1;b.b=void 0===a?null:a;return b}
;function Wh(a){B.call(this,a.message||a.description||a.name);this.isMissing=a instanceof Xh;this.isTimeout=a instanceof Sh&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof dd}
n(Wh,B);Wh.prototype.name="BiscottiError";function Xh(){B.call(this,"Biscotti ID is missing from server")}
n(Xh,B);Xh.prototype.name="BiscottiMissingError";var Rh={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},Yh=null;function Zh(){if("1"===Wa($d(),"args","privembed"))return Vc(Error("Biscotti ID is not available in private embed mode"));Yh||(Yh=cd(Qh().then($h),function(a){return ai(2,a)}));
return Yh}
function $h(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new Xh;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new Xh;a=a.id;bi(a);Yh=Uh(a);ci(18E5,2);return a}
function ai(a,b){var c=new Wh(b);bi("");Yh=Vh(c);0<a&&ci(12E4,a-1);throw c;}
function ci(a,b){T(function(){cd(Qh().then($h,function(a){return ai(b,a)}),na)},a)}
function bi(a){t("yt.ads.biscotti.lastId_",a,void 0)}
function di(){try{var a=v("yt.ads.biscotti.getId_");return a?a():Zh()}catch(b){return Vc(b)}}
;function ei(a){B.apply(this,arguments)}
n(ei,B);ei.prototype.name="YuzuError";function fi(){var a=new ei("ID is missing"),b=new ei("Timeout"),c=null,d=!1;Wd(function(){c=Ud();d=!0});
if(d)return c?Uh(c):Vh(a);var e=new H(function(b,c){Wd(function(){var d=Ud();d?b(d):c(a)})}),f=Gd().then(function(){return Vc(b)});
return ad(Yc([e,f]),function(){return f.cancel()})}
;function gi(a){if("1"!==Wa($d(),"args","privembed")){a&&(v("yt.ads.biscotti.getId_")||xa("yt.ads.biscotti.getId_",Zh));try{var b=di();if(S("enable_yuzu")){v("yt.ads.yuzu.getId_")||t("yt.ads.yuzu.getId_",fi,void 0);try{var c=v("yt.ads.yuzu.getId_")()}catch(d){c=Vc(d)}}else c=Vc(new ei("unimplemented"));Zc([b,c]).then(function(a){var b=a[0];a=a[1];if(b.Z||a.Z){b=b.value;a=a.value;var c={};c.dt=Ub;c.flash="0";a:{try{var d=window.top.location.href}catch(Ua){d=2;break a}d=null!=d?d==window.document.location.href?
0:1:2}d=(c.frm=d,c);d.u_tz=-(new Date).getTimezoneOffset();var h=void 0===h?F:h;try{var k=h.history.length}catch(Ua){k=0}d.u_his=k;d.u_java=!!F.navigator&&"unknown"!==typeof F.navigator.javaEnabled&&!!F.navigator.javaEnabled&&F.navigator.javaEnabled();F.screen&&(d.u_h=F.screen.height,d.u_w=F.screen.width,d.u_ah=F.screen.availHeight,d.u_aw=F.screen.availWidth,d.u_cd=F.screen.colorDepth);F.navigator&&F.navigator.plugins&&(d.u_nplug=F.navigator.plugins.length);F.navigator&&F.navigator.mimeTypes&&(d.u_nmime=
F.navigator.mimeTypes.length);d.ca_type="image";if(S("enable_server_side_search_pyv")||S("enable_server_side_mweb_search_pyv")){k=window;try{var m=k.screenX;var u=k.screenY}catch(Ua){}try{var M=k.outerWidth;var aa=k.outerHeight}catch(Ua){}try{var Lg=k.innerWidth;var Mg=k.innerHeight}catch(Ua){}m=[k.screenLeft,k.screenTop,m,u,k.screen?k.screen.availWidth:void 0,k.screen?k.screen.availTop:void 0,M,aa,Lg,Mg];u=window.top;try{var V=(u||window).document,Ta="CSS1Compat"==V.compatMode?V.documentElement:
V.body;var Ga=(new Gb(Ta.clientWidth,Ta.clientHeight)).round()}catch(Ua){Ga=new Gb(-12245933,-12245933)}V={};Ta=0;p.SVGElement&&p.document.createElementNS&&(Ta|=1);V.bc=Ta;V.bih=Ga.height;V.biw=Ga.width;V.brdim=m.join();Ga=(V.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[Sb.visibilityState||Sb.webkitVisibilityState||Sb.mozVisibilityState||""]||0,V.wgl=!!F.WebGLRenderingContext,V);for(var Od in Ga)d[Od]=Ga[Od]}void 0!==b&&(d.bid=b);void 0!==a&&(d.anid=a);d.bsq=hi++;Ue("//www.youtube.com/ad_data_204",
{Ea:!1,B:d})}});
T(gi,18E5)}catch(d){R(d)}}}
var hi=0;var Z=v("ytglobal.prefsUserPrefsPrefs_")||{};t("ytglobal.prefsUserPrefsPrefs_",Z,void 0);function ii(){this.b=Q("ALT_PREF_COOKIE_NAME","PREF");var a=$b.get(""+this.b,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Z[d]=c.toString())}}}
l=ii.prototype;l.get=function(a,b){ji(a);ki(a);var c=void 0!==Z[a]?Z[a].toString():null;return null!=c?c:b?b:""};
l.set=function(a,b){ji(a);ki(a);if(null==b)throw Error("ExpectedNotNull");Z[a]=b.toString()};
l.remove=function(a){ji(a);ki(a);delete Z[a]};
l.save=function(){var a=this.b,b=[],c;for(c in Z)b.push(c+"="+encodeURIComponent(String(Z[c])));Sf(a,b.join("&"),63072E3)};
l.clear=function(){for(var a in Z)delete Z[a]};
function ki(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function ji(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function li(a){a=void 0!==Z[a]?Z[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
oa(ii);var mi=null,ni=null,oi=null,pi={};function qi(a){Nf(a.payload_name,a.payload,void 0,void 0)}
function ri(a){var b=a.id;a=a.ve_type;var c=cg++;a=new ag(void 0,a,c,void 0,void 0);pi[b]=a;b=eg();c=dg();b&&c&&hg(b,c,a)}
function si(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(fg(b,a),a=dg()))for(var c in pi){var d=pi[c];d&&hg(b,a,d)}}
function ti(a){pi[a.id]=new ag(a.tracking_params)}
function ui(a){var b=eg();a=pi[a.id];b&&a&&(S("interaction_click_on_gel_web")?Nf("visualElementGestured",{csn:b,ve:bg(a),gestureType:"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK"}):ig({click:{csn:b,visualElement:bg(a)}}))}
function vi(a){a=a.ids;var b=eg();if(b)for(var c=0;c<a.length;c++){var d=pi[a[c]];d&&Nf("visualElementShown",{csn:b,ve:bg(d),eventType:1})}}
function wi(){var a=mi;a&&a.startInteractionLogging&&a.startInteractionLogging()}
;t("yt.setConfig",P,void 0);t("yt.config.set",P,void 0);t("yt.setMsg",cf,void 0);t("yt.msgs.set",cf,void 0);t("yt.logging.errors.log",af,void 0);
t("writeEmbed",function(){var a=Q("PLAYER_CONFIG",void 0);gi(!0);"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");var b=document.referrer,c=Q("POST_MESSAGE_ORIGIN");window!=window.top&&b&&b!=document.URL&&(a.args.loaderUrl=b);Q("LIGHTWEIGHT_AUTOPLAY")&&(a.args.autoplay="1");a.args.autoplay&&Ah(a.args);mi=a=rh(a);a.addEventListener("onScreenChanged",si);a.addEventListener("onLogClientVeCreated",ri);a.addEventListener("onLogServerVeCreated",ti);a.addEventListener("onLogToGel",qi);
a.addEventListener("onLogVeClicked",ui);a.addEventListener("onLogVesShown",vi);a.addEventListener("onReady",wi);b=Q("POST_MESSAGE_ID","player");Q("ENABLE_JS_API")?oi=new Mh(a):Q("ENABLE_POST_API")&&r(b)&&r(c)&&(ni=new Ph(window.parent,b,c),oi=new Gh(a,ni.f));Q("BG_P")&&(Q("BG_I")||Q("BG_IU"))&&Ae();mf()},void 0);
t("yt.www.watch.ads.restrictioncookie.spr",function(a){Xe(a+"mac_204?action_fcts=1");return!0},void 0);
var xi=ae(function(){Pg("ol");var a=ii.getInstance(),b=!!((li("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&yc(document.body,"exp-invert-logo"))if(c&&!yc(document.body,"inverted-hdpi")){var d=document.body;d.classList?d.classList.add("inverted-hdpi"):yc(d,"inverted-hdpi")||(d.className+=0<d.className.length?" inverted-hdpi":"inverted-hdpi")}else!c&&yc(document.body,"inverted-hdpi")&&zc();b!=c&&(b="f"+(Math.floor(119/31)+1),d=li(b)||0,d=c?d|67108864:d&-67108865,
0==d?delete Z[b]:Z[b]=d.toString(16).toString(),a.save())}),yi=ae(function(){var a=mi;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();Q("PL_ATT")&&(ze=null);a=0;for(var b=kf.length;a<b;a++)jf(kf[a]);kf.length=0;xe("//static.doubleclick.net/instream/ad_status.js");lf=!1;P("DCLKSTAT",0);wc(oi,ni);if(a=mi)a.removeEventListener("onScreenChanged",si),a.removeEventListener("onLogClientVeCreated",ri),a.removeEventListener("onLogServerVeCreated",ti),a.removeEventListener("onLogToGel",qi),a.removeEventListener("onLogVeClicked",ui),a.removeEventListener("onLogVesShown",vi),a.removeEventListener("onReady",
wi),a.destroy();pi={}});
window.addEventListener?(window.addEventListener("load",xi),window.addEventListener("unload",yi)):window.attachEvent&&(window.attachEvent("onload",xi),window.attachEvent("onunload",yi));xa("yt.abuse.botguardInitialized",v("yt.abuse.botguardInitialized")||Ce);xa("yt.abuse.invokeBotguard",v("yt.abuse.invokeBotguard")||De);xa("yt.abuse.dclkstatus.checkDclkStatus",v("yt.abuse.dclkstatus.checkDclkStatus")||nf);xa("yt.player.exports.navigate",v("yt.player.exports.navigate")||gg);
xa("yt.util.activity.init",v("yt.util.activity.init")||xf);xa("yt.util.activity.getTimeSinceActive",v("yt.util.activity.getTimeSinceActive")||zf);xa("yt.util.activity.setTimestamp",v("yt.util.activity.setTimestamp")||W);}).call(this);
