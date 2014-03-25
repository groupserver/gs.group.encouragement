"use strict";jQuery.noConflict();function GSGroupEncouragement(){var g=3000;function e(l,o,k,p){var n=null,m=null,j=null,i=null;
m="jQuery(&quot;"+l+"&quot;).popover(&quot;hide&quot;);";i='<button type="button" class="close" onclick="'+m+'">&times;</button>';
n={animation:true,title:o+i,html:true,placement:p,trigger:"manual",content:k};j=jQuery(l);
j.popover(n);j.popover("show");j.next(".popover").find(".popover-title").html(o+i)
}function h(){var m=null,l=null,j=null,i=null,k=null;m=jQuery("#gs-group-encouragement-topics");
l=m.html();j=m.attr("title");i="#gs-group-messages-topics-search-form-new-topic";
k=jQuery(i).parents(".tab-content");k.css("overflow","visible");e(i,j,l,"bottom")
}function c(){var l=null,k=null,j=null,i=null;l=jQuery("#gs-group-encouragement-invite");
k=l.html();j=l.attr("title");i="#gs-group-member-invite-base-admin-single";e(i,j,k,"left")
}function d(){var l=null,k=null,j=null,i=null;l=jQuery("#gs-group-about-tab-admin");
k=l.html();j=l.attr("title");i="#gs-group-about-change-link";e(i,j,k,"bottom")}function b(){var l=null,k=null,j=null,i=null;
l=jQuery("#gs-group-encouragement-private");k=l.html();j=l.attr("title");i="#gs-group-privacy-admin-link";
e(i,j,k,"left")}function f(j){var i=null;i=jQuery(j).length>0;return i}function a(){if(f("#gs-group-encouragement-topics")){window.setTimeout(h,g)
}else{if(f("#gs-group-encouragement-invite")){window.setTimeout(c,g)}else{if(f("#gs-group-about-tab-admin")){window.setTimeout(d,g)
}else{if(f("#gs-group-encouragement-private")){window.setTimeout(b,g)}}}}}return{init:a}
}jQuery(window).load(function(){var a=null;a=GSGroupEncouragement();a.init()});