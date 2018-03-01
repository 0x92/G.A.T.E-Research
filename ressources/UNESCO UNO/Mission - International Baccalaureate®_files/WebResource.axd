function epiGat(settings) {
	if (settings.downloads || settings.external || settings.mailto) {
		var isinternal = new RegExp('^' + window.location.protocol + '\/\/' + window.location.host, 'i');

		function addEvent(obj, type, fn) {
			if (obj.addEventListener)
				obj.addEventListener(type, fn, false);
			else if (obj.attachEvent) {
				obj['e' + type + fn] = fn;
				obj[type + fn] = function () { obj['e' + type + fn](window.event); }
				obj.attachEvent('on' + type, obj[type + fn]);
			}
		}

		var isdownload = new RegExp('[.](' + settings.extensions + ')$', 'i');
		var islink = new RegExp('^https?://');
		var ismailto = new RegExp('^mailto:', 'i');

		function instead(e, a) {
		    var isDefaultPrevented = e.defaultPrevented;

			if (e.preventDefault) e.preventDefault();
			else if (event) event.returnValue = false;

			if (isDefaultPrevented == false) {
			    setTimeout(function () { window.location = a.href; }, 200);
			}
		}

	    // https://developers.google.com/analytics/devguides/collection/upgrade/reference/gajs-analyticsjs#events
		addEvent(document, 'click', function (e) {
			e = e || event;
			var a = e.target || e.srcElement;

            // Depend on TrackScriptOption to decided Clasic or Universal or Customer
			var trackingEvent = function (category, action, opt_label, opt_value) {
			    // Universal syntax
			    if (settings.trackingOption == 'Universal') {
			        ga('send', 'event', category, action, opt_label, opt_value);
			    }
			    else { // Classic syntax
			        _gaq.push(['_trackEvent', category, action, opt_label, opt_value]);
			    }
			};

		    // Depend on TrackScriptOption to decided Clasic or Universal or Customer
			var trackingPageView = function (path) {
			    // Universal syntax
			    if (settings.trackingOption == 'Universal') {
			        ga('send', 'pageview', path);
			    }
			    else { // Classic syntax
			        _gaq.push(['_trackPageview', path]);
			    }
			};

			for (; a.parentNode; a = a.parentNode) {
				if (a.tagName !== 'A') {
					continue;
				}

				if (settings.downloads && isdownload.test(a.href)) {
				    var extension = isdownload.exec(a.href);
				    trackingEvent('Download', extension[1].toUpperCase(), a.href.replace(isinternal, ''));

                    if (!a.target || a.target === "_top")
					    instead(e, a);
				}
				else if (settings.external && islink.test(a.href) && !isinternal.test(a.href)) {
				    if (settings.externalsAsViews) {
				        trackingPageView('/external/' + a.href.replace(islink, ''));
				    } else {
				        trackingEvent('External', 'Clicked', a.href);
					}
		            if (!a.target || a.target === "_top")
		                instead(e, a);
				}
				else if (settings.mailto && ismailto.test(a.href)) {
				    trackingEvent('Mailto', 'Clicked', a.href.replace(ismailto, ''));
				}

				return;
			}
		});
	}

    // if track post of the EPiServer.Forms
	if (settings.trackForms == true) {

	    if (typeof $$epiforms == "undefined" || !$$epiforms) {
	        return;
	    }

	    $$epiforms(document).ready(function () {
            
	        $$epiforms(".EPiServerForms").on("formsSubmitted", function (event) {

	            if (event.isFinalizedSubmission != true) {
	                return;
	            }

	            var gaEventCategory = "EPiServer Forms";
	            var gaEventLabel = event.workingFormInfo.Name;
	            var gaEventAction = "EPiServer Forms Submit " + event.workingFormInfo.Id;
	            // Universal syntax
	            if (settings.trackingOption == 'Universal') {
	                ga('send', 'event', gaEventCategory, gaEventAction, gaEventLabel, 1);
	            }
	            else if (settings.trackingOption == 'Classic') { // Classic syntax
	                _gaq.push(['_trackEvent', gaEventCategory, gaEventAction, gaEventLabel, 1]);
	            }
	        });
	    });
	}
};
