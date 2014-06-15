//<![CDATA[

function loadMore () {
	$.get( "/dashboard/search_ajax", function( data ) {
		var urls = data.urls
		var arrayLength = urls.length;
		for (var i = 0; i < arrayLength; i++) {
		    $.get( "http://api.embed.ly/1/oembed?key=93e6adfaf56b44aba78d8e5384bda3b1&url="+urls[i], function( data ) {
				console.log( data.description )
		    	var res = '<div class="col-md-3"><div class="panel panel-default results-panel"><div class="panel-heading"><h3 class="panel-title">'+data.title+'</h3></div><div class="panel-body" style="background-image: url('+data.thumbnail_url+');" ><div class="panel-body-footer">'+data.description.substring(0, 66)+'...</div></div><div class="panel-footer">Panel footer</div></div></div>'
		    	$("#links").append(res);
		    });
		}
	});
}

$( document ).ready(function() {

});

//]]>