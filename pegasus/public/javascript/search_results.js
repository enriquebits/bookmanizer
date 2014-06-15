//<![CDATA[
var finished = false;
var page = 1;

function goToPage (self) {
	$(self).find("#showPage").submit();
}

function loadMore () {
	if( !finished ) {
		$.get( "/dashboard/search_ajax?tags="+$("#tags").val()+"&page="+page, function( data ) {
			var urls = data.urls
			var ides = data.ides
			var arrayLength = urls.length;
			if(arrayLength > 16) {
				$("#loadMore").attr("disabled", "disabled");				
				$("#loadMore").text("Finished!!");
				$("#loadMore").addClass("btn-danger");
				$("#loadMore").removeClass("btn-success");
				finished = true;
			}
			for (var i = 0; i < arrayLength; i++) {
			    $.get( "http://api.embed.ly/1/oembed?key=93e6adfaf56b44aba78d8e5384bda3b1&url="+urls[i], function( data ) {
					var img = typeof data.thumbnail_url === "undefined" ? "/img/link_placeholder.jpg" : data.thumbnail_url;
			    	var res = '<div class="col-md-3"><div class="panel panel-default results-panel"><div class="panel-heading"><h3 class="panel-title">'+data.title+'</h3></div><div class="panel-body" style="background-image: url('+img+');" ><div class="panel-body-footer">'+data.description.substring(0, 66)+'...</div></div><div class="panel-footer">Panel footer</div><form id="showPage" method="post" action="/link?lid='+ides[i]+'"></form></div></div>'
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
		var self = this;
		$.get( "http://api.embed.ly/1/oembed?key=93e6adfaf56b44aba78d8e5384bda3b1&url="+$(self).find("#title").text(), function( data ) {
			$(self).find("#title").text(data.title);	    	
			$(self).find("#description").text(data.description.substring(0, 66));
			var img = typeof data.thumbnail_url === "undefined" ? "/img/link_placeholder.jpg" : data.thumbnail_url;
			$(self).find(".panel-body").attr("style", "background-image: url("+img+");");
			cont = cont + 1;
	    });
	});
	page = page + 1;
	if( cont < 16 ) {
		$("#loadMore").attr("disabled", "disabled");
		$("#loadMore").text("Finished!!");
		$("#loadMore").addClass("btn-danger");
		$("#loadMore").removeClass("btn-success");
		finished = true;
	}		
});

//]]>