//<![CDATA[

$( document ).ready(function() {
	$('.slider').fractionSlider();

	// Init Skrollr
	var s = skrollr.init({
		forceHeight: false
	});
	 
	// Refresh Skrollr after resizing our sections
	s.refresh($('.homeSlide'));
});

//]]>