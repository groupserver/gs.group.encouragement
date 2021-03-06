'use strict';
// Popup encouragement for a group administrator
//
// Copyright © 2013, 2014, 2016 OnlineGroups.net and Contributors.
// All Rights Reserved.
//
// This software is subject to the provisions of the Zope Public License,
// Version 2.1 (ZPL). http://groupserver.org/downloads/license/
//
// THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
// WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
// FITNESS FOR A PARTICULAR PURPOSE.
jQuery.noConflict();


function GSGroupEncouragement() {
    // To give the chance (3s) for things to load
    var TIMEOUT_TIME = 3000;

    function create_popover(target, title, html, pos) {
        var d = null, onClick = null, t = null, closeButton = null;
        // One day data-dismiss="popover" will work. Not today.
        onClick = 'jQuery(&quot;' + target +
            '&quot;).popover(&quot;hide&quot;);';
        closeButton = '<button type="button" class="close" ' + 'onclick="' +
            onClick + '">&times;</button>';
        d = {animation: true, title: title + closeButton, html: true,
             placement: pos, trigger: 'manual', content: html};
        t = jQuery(target);
        t.popover(d);
        t.popover('show');
        t.next('.popover').find('.popover-title').html(title + closeButton);
    }

    function topics() {
        var e = null, h = null, t = null, b = null, tab = null;
        e = jQuery('#gs-group-encouragement-topics');
        h = e.html();
        t = e.attr('title');
        b = '#gs-group-messages-topics-search-form-new-topic';
        // --=mpj17=-- overflow
        // The New Topic button is in a tab. Tabs have overflow: auto set.
        // This means that the popup is, well, duuurp de duuuurp durp. So
        // here we find the tab, and get rid of the overflow setting.
        tab = jQuery(b).parents('.tab-content');
        tab.css('overflow', 'visible');

        create_popover(b, t, h, 'bottom');
    }

    function invite() {
        var e = null, h = null, t = null, b = null;
        e = jQuery('#gs-group-encouragement-invite');
        h = e.html();
        t = e.attr('title');
        b = '#gs-group-member-invite-base-admin-single';
        create_popover(b, t, h, 'left');
    }

    function about() {
        var e = null, h = null, t = null, b = null;
        e = jQuery('#gs-group-about-tab-admin');
        h = e.html();
        t = e.attr('title');
        b = '#gs-group-about-change-link';
        create_popover(b, t, h, 'bottom');
    }

    function set_private() {
        // If this encouragement annoys too many people it can be changed to
        // an icon next to #gs-group-privacy-admin-link, which will create
        // the popover when clicked.
        var e = null, h = null, t = null, b = null;
        e = jQuery('#gs-group-encouragement-private');
        h = e.html();
        t = e.attr('title');
        b = '#gs-group-privacy-admin-link';
        create_popover(b, t, h, 'left');
    }

    function exists(element) {
        var retval = null;
        retval = jQuery(element).length > 0;
        return retval;
    }

    function setup() {
        if (exists('#gs-group-encouragement-topics')) {
            window.setTimeout(topics, TIMEOUT_TIME);
        } else if (exists('#gs-group-encouragement-invite')) {
            window.setTimeout(invite, TIMEOUT_TIME);
        } else if (exists('#gs-group-about-tab-admin')) {
            window.setTimeout(about, TIMEOUT_TIME);
        } else if (exists('#gs-group-encouragement-private')) {
            window.setTimeout(set_private, TIMEOUT_TIME);
        }
    }
    return {
        init: setup
    };
}


jQuery(window).load(function() {
    var e = null;
    e = GSGroupEncouragement();
    e.init();
});
