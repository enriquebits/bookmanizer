//<![CDATA[
var url_like = "link/like";
var url_dislike = "link/dislike";
var url_favourite = "link/favourite";
var url_flag = "link/flag";
var lid = $("#lid");

function like(anchor) {
	var anchor = $(anchor);
	var dislike = $("#dislike");
	var like = anchor.children('i');
	if (dislike.hasClass('disliked')) {
		dislike.toggleClass('disliked');
	}
	like.toggleClass('liked');
	var isLiked = like.hasClass('liked') == true ? 1 : 0;
	
	$.ajax({
	  type: "POST",
	  url: url_like,
	  data: {'lid': lid.val(), 'isLiked': isLiked}, // serializes the form's elements.
	  success: function(response) {
	            console.log(response); // show response from the script.
	          }
	});
}

function dislike(anchor) {
	var anchor = $(anchor);
	var like = $("#like");
	var dislike = anchor.children('i');
	if (like.hasClass('liked')) {
		like.toggleClass('liked');
	}
	dislike.toggleClass('disliked');
	var isDisliked = dislike.hasClass('disliked') == true ? 1 : 0;

	$.ajax({
	  type: "POST",
	  url: url_dislike,
	  data: {'lid': lid.val(), 'isDisliked': isDisliked}, // serializes the form's elements.
	  success: function(response) {
	            console.log(response); // show response from the script.
	        }
	});
}

function favourite(anchor) {
	var anchor = $(anchor);
	var flag = $("#flag");
	var star = anchor.children('i');
	if (flag.hasClass('flagged')) {
		flag.toggleClass('flagged');
	}
	star.toggleClass('favourite');

	var isFavourite = star.hasClass('favourite') == true ? 1 : 0;

	$.ajax({
	  type: "POST",
	  url: url_favourite,
	  data: {'lid': lid.val(), 'isFavourite': isFavourite}, // serializes the form's elements.
	  success: function(response) {
	            console.log(response); // show response from the script.
	        }
	});
}

function flag(anchor) {
	var anchor = $(anchor);
	var star = $("#favourite");
	var flag = anchor.children('i');
	if (star.hasClass('favourite')) {
		star.toggleClass('favourite');
	}
	flag.toggleClass('flagged');

	var isFlagged = flag.hasClass('flagged') == true ? 1 : 0;

	$.ajax({
	  type: "POST",
	  url: url_flag,
	  data: {'lid': lid.val(), 'isFlagged': isFlagged}, // serializes the form's elements.
	  success: function(response) {
	            console.log(response); // show response from the script.
	        }
	});
}

$( document ).ready(function() {
	$("#show_comments").sidr({
	  name: 'sidr',
	  side: 'right'
	}); 
});

//]]>