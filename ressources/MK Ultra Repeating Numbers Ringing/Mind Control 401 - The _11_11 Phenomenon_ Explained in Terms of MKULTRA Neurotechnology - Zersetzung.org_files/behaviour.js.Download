/**
 * @version    4.8.0
 * @package    AllVideos (plugin)
 * @author     JoomlaWorks - http://www.joomlaworks.net
 * @copyright  Copyright (c) 2006 - 2017 JoomlaWorks Ltd. All rights reserved.
 * @license    GNU/GPL license: http://www.gnu.org/copyleft/gpl.html
 */

var allvideos = {
    ready: function(cb) {
        /in/.test(document.readyState) ? setTimeout('allvideos.ready(' + cb + ')', 9) : cb();
    },

    getRemoteJson: function(url) {
        var remoteJsonScript = document.createElement('script');
        remoteJsonScript.setAttribute('charset', 'utf-8');
        remoteJsonScript.setAttribute('type', 'text/javascript');
        remoteJsonScript.setAttribute('async', 'true');
        remoteJsonScript.setAttribute('src', url);
        return remoteJsonScript;
    },

    embed: function(el) {
        var jsonpCallback = el.callback;
        var tempId = Math.floor(Math.random() * 1000) + 1;
        var responseContainer = [];
        window[jsonpCallback] = function(response) {
            responseContainer.tempId = [response];
        };
        var head = document.getElementsByTagName('head')[0];
        var jsonp = this.getRemoteJson(el.url);
        jsonp.onloadDone = false;
        jsonp.onload = function() {
            if (!jsonp.onloadDone) {
                jsonp.onloadDone = true;
                document.getElementById(el.playerID).innerHTML = responseContainer.tempId[0].html;
            }
        };
        jsonp.onreadystatechange = function() {
            if (("loaded" === jsonp.readyState || "complete" === jsonp.readyState) && !jsonp.onloadDone) {
                jsonp.onloadDone = true;
                document.getElementById(el.playerID).innerHTML = responseContainer.tempId[0].html;
            }
        }
        head.appendChild(jsonp);
    }
}
