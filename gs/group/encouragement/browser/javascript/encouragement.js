jQuery.noConflict();

function GSGroupEncouragement () {

    function create_popover(target, title, html, pos) {
        var d = null;
        var b = null;
        var onClick = null;
        var t = null;
        var closeButton = null;
        // One day data-dismiss="popover" will work. Not today.
        onClick = 'jQuery(&quot;'+target+'&quot;).popover(&quot;hide&quot;);';
        closeButton = '<button type="button" id="close" class="close" '+
            'onclick="'+onClick+'">&times;</button>';
        d = {animation: true, title: title + closeButton, html: true, 
             placement: pos, trigger: 'manual', content: html}
        t = jQuery(target);
        t.popover(d);
        t.popover('show');
    }
    
    function topics() {
        var e = null;
        var h = null;
        var t = null;
        var b = null;
        e = jQuery('#gs-group-encouragement-topics');
        h = e.html();
        t = e.attr('title');
        b = '#gs-group-type-announcement-posts-form-new-topic';
        create_popover(b, t, h, 'right');
    }

    function invite() {
        var e = null;
        var h = null;
        var t = null;
        var b = null;
        e = jQuery('#gs-group-encouragement-invite');
        h = e.html();
        t = e.attr('title');
        b = '#gs-group-member-invite-base-admin-single';
        create_popover(b, t, h, 'left');
    }


    function exists(element) {
        return jQuery(element).length > 0;
    }

    function setup() {
        if (exists('#gs-group-encouragement-topics')) {
            // To give the chance for the No Topics to load
            window.setTimeout(topics, 2000);
        } else if (exists('#gs-group-encouragement-invite')) {
            invite();
        }        
    }
    return {
        init: setup,
    };
}
jQuery(window).load(function() {
    var e = GSGroupEncouragement(); e.init()
});