/**
* @author    JoomlaShine.com http://www.joomlashine.com
* @copyright Copyright (C) 2008 - 2011 JoomlaShine.com. All rights reserved.
* @license   GNU/GPL v2 http://www.gnu.org/licenses/gpl-2.0.html
*/

	var JSNTemplate = {
		_templateParams:		{},

		initOnDomReady: function()
		{
			// Setup HTML code for typography
			JSNUtils.createGridLayout("DIV", "grid-layout", "grid-col", "grid-lastcol");
			JSNUtils.createExtList("list-number-", "span", "jsn-listbullet", true);
			JSNUtils.createExtList("list-icon", "span", "jsn-listbullet", false);

			// Setup Go to top link settings
			if (_templateParams.enableGotopLink) {
				JSNUtils.setToTopLinkCenter(_templateParams.enableRTL, false);
				JSNUtils.setSmoothScroll(false);
				JSNUtils.setFadeScroll(false);
			}

			// General layout setup
			JSNUtils.setupLayout();

			// Setup mobile menu
			JSNUtils.setMobileMenu("menu-mainmenu", _templateParams.mobileMenuEffect);

			if (JSNUtils.isDesktopViewOnMobile(_templateParams)) {
				// Setup mobile sticky
				if (_templateParams.enableMobileMenuSticky && JSNUtils.checkMobile()) {
					JSNUtils.setMobileSticky();
				}
			}
			else {
				JSNUtils.initMenuForDesktopView();
			}

			// Setup module dropdown on mobile
			JSNUtils.setDropdownModuleEvents();

			// Setup mobile sitetool
			JSNUtils.setMobileSitetool();

			// Stick main menu to top
			if (_templateParams.enableDesktopMenuSticky) {
				JSNUtils.setDesktopSticky();
			}
			// Setup event to update megamenu submenu position
		    try {
			JSNMegamenu.setMegamenuSubmenuPosition(_templateParams.enableRTL);
			JSNMegamenu.setMegamenuSubmenuStyle();
		    }
		    catch(err) {
		    }
		},

		initOnLoad: function()
		{
			// Setup event to update submenu position
			JSNUtils.setSubmenuPosition(_templateParams.enableRTL);

			// Stick positions layout setup
			JSNUtils.setVerticalPosition("jsn-pos-stick-leftmiddle", 'middle');
			JSNUtils.setVerticalPosition("jsn-pos-stick-rightmiddle", 'middle');
		},

		initTemplate: function(templateParams)
		{
			// Store template parameters
			_templateParams = templateParams;

			// Init template on "domready" event
			window.addEvent('domready', JSNTemplate.initOnDomReady);
			window.addEvent('load', JSNTemplate.initOnLoad);
		}
	}; // must have ; to prevent syntax error when compress
