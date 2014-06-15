//<![CDATA[
function like(anchor) {
	var anchor = $(anchor);
	var dislike = $("#dislike");
	var like = anchor.children('i');
	if (dislike.hasClass('disliked')) {
		dislike.toggleClass('disliked');
	}
	like.toggleClass('liked');
}

function dislike(anchor) {
	var anchor = $(anchor);
	var like = $("#like");
	var dislike = anchor.children('i');
	if (like.hasClass('liked')) {
		like.toggleClass('liked');
	}
	dislike.toggleClass('disliked');
}

function favourite(anchor) {
	var anchor = $(anchor);
	var flag = $("#flag");
	var star = anchor.children('i');
	if (flag.hasClass('flagged')) {
		flag.toggleClass('flagged');
	}
	star.toggleClass('favourite');
}

function flag(anchor) {
	var anchor = $(anchor);
	var star = $("#favourite");
	var flag = anchor.children('i');
	if (star.hasClass('favourite')) {
		star.toggleClass('favourite');
	}
	flag.toggleClass('flagged');
}

$( document ).ready(function() {
	$("#show_comments").sidr({
	  name: 'sidr',
	  side: 'right'
	}); 
});

//]]>