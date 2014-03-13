"use strict";jQuery.noConflict();function GSGroupEncouragement(){function e(k,n,j,o){var m=null,l=null,i=null,h=null;
l="jQuery(&quot;"+k+"&quot;).popover(&quot;hide&quot;);";h='<button type="button" class="close" onclick="'+l+'">&times;</button>';
m={animation:true,title:n+h,html:true,placement:o,trigger:"manual",content:j};i=jQuery(k);
i.popover(m);i.popover("show");i.next(".popover").find(".popover-title").html(n+h)
}function g(){var m=null,l=null,j=null,i=null,k=null;m=jQuery("#gs-group-encouragement-topics");
l=m.html();j=m.attr("title");i="#gs-group-messages-topics-search-form-new-topic";
k=jQuery(i).parents(".tab-content");k.css("overflow","visible");e(i,j,l,"bottom")
}function c(){var l=null,k=null,j=null,i=null;l=jQuery("#gs-group-encouragement-invite");
k=l.html();j=l.attr("title");i="#gs-group-member-invite-base-admin-single";e(i,j,k,"left")
}function d(){var l=null,k=null,j=null,i=null;l=jQuery("#gs-group-about-tab-admin");
k=l.html();j=l.attr("title");i="#gs-group-about-change-link";e(i,j,k,"bottom")}function b(){var l=null,k=null,j=null,i=null;
l=jQuery("#gs-group-encouragement-private");k=l.html();j=l.attr("title");i="#gs-group-privacy-admin-link";
e(i,j,k,"left")}function f(i){var h=null;h=jQuery(i).length>0;return h}function a(){if(f("#gs-group-encouragement-topics")){window.setTimeout(g,2000)
}else{if(f("#gs-group-encouragement-invite")){c()}else{if(f("#gs-group-about-tab-admin")){d()
}else{if(f("#gs-group-encouragement-private")){b()}}}}}return{init:a}}jQuery(window).load(function(){var a=null;
a=GSGroupEncouragement();a.init()});