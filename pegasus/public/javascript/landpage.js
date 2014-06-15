//<![CDATA[

$( document ).ready(function() {
	$('.slider').fractionSlider({
		'timeout' : 1000,
		'speedIn' : 1000, // default in - transition speed
		'speedOut' : 500, // default out - transition speed
	});

	// Init Skrollr
	var s = skrollr.init({
		forceHeight: false
	});
	 
	// Refresh Skrollr after resizing our sections
	s.refresh($('.homeSlide'));
});

//]]>