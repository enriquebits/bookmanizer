//<![CDATA[
var finished = false;
var page = 1;

function loadMore () {
	if( !finished ) {
		$.get( "/dashboard/search_ajax?tags="+$("#tags").val()+"&page="+page, function( data ) {
			var urls = data.urls
			var arrayLength = urls.length;
			if(arrayLength > 16)
				finished = true;
			for (var i = 0; i < arrayLength; i++) {
			    $.get( "http://api.embed.ly/1/oembed?key=93e6adfaf56b44aba78d8e5384bda3b1&url="+urls[i], function( data ) {
					console.log( data.description )
			    	var res = '<div class="col-md-3"><div class="panel panel-default results-panel"><div class="panel-heading"><h3 class="panel-title">'+data.title+'</h3></div><div class="panel-body" style="background-image: url('+data.thumbnail_url+');" ><div class="panel-body-footer">'+data.description.substring(0, 66)+'...</div></div><div class="panel-footer">Panel footer</div></div></div>'
			    	$("#links").append(res);
			    });
			}
		});		
		page = page + 1;
	}
}

$( document ).ready(function() {
	var cont = 0;
	$(".results-panel").each(function() {
		$.get( "http://api.embed.ly/1/oembed?key=93e6adfaf56b44aba78d8e5384bda3b1&url="+$(this).find("#title").text(), function( data ) {
			$(this).find("#title").text(data.title);	    	
			$(this).find("#description").text(data.description.substring(0, 66));
			$(this).find(".panel-body").css("background-image", "url("+data.thumbnail_url+");");
			cont = cont + 1;
	    });
	});
	page = page + 1;
	if( cont < 16 )
		finished = true;
});

//]]>