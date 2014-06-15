//<![CDATA[

$( document ).ready(function() {
	$('.slider').fractionSlider({
		'timeout' : 1500,
		'speedIn' : 1500, // default in - transition speed
		'speedOut' : 1000, // default out - transition speed
	});

	// Init Skrollr
	var s = skrollr.init({
		forceHeight: false
	});
	 
	// Refresh Skrollr after resizing our sections
	s.refresh($('.homeSlide'));
});

//]]>