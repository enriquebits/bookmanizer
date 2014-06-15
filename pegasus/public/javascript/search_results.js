//<![CDATA[
var finished = false;
var page = 1;

function goToPage (self) {
	$(self).find("#showPage").submit();
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getColor() {
	var c = getRandomInt(0, 6)
	var color = "";
	if( c == 0)
		color = "#ff0800"
	else if(c == 1 )
		color = "#FF8700"
	else if(c == 2 )
		color = "#00e506"
	else if(c == 3 )
		color = "#800080"
	else if(c == 4 )
		color = "#FFFF00"
	else if(c == 5 )
		color = "#664c51"
	else
		color = "#3232ff"
	return color;
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
			var suffix = data.title.length > 51 ? "..." : "";
			var suffix2 = data.description.length > 65 ? "..." : "";
			$(self).find("#title").text(data.title.substring(0, 52)+suffix);
			$(self).find("#description").text(data.description.substring(0, 66)+suffix2);
			var img = typeof data.thumbnail_url === "undefined" ? "/img/link_placeholder.jpg" : data.thumbnail_url;
			$(self).find(".panel-body").attr("style", "background-image: url("+img+");");
			$(self).find(".panel-heading").css("background-color", getColor() );
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