//<![CDATA[

function updateCategory(link) {
	category = $(link).attr("id");
	$("#cat_dropdown").text(category);
	$("#category").val(category)
}

function doSearch () {
	var tags = $("#query").select2("val");
	window.location.replace("www.localhost:8080/dashboard/search?query="+tags);
}

$( document ).ready(function() {

	$("#query").select2({
		placeholder: "Choose a tag",
		minimumInputLength: 3,
		multiple: true,
		ajax: { 
	        url: "/dashboard/get_tags",
	        dataType: 'json',
	        data: function (term, page) {
	            return {
	                q: term, // search term
	                page_limit: 10,
	            };
	        },
	        results: function (data, page) { // parse the results into the format expected by Select2.
	            // since we are using custom formatting functions we do not need to alter remote JSON data
	            console.debug("data: "+data)
	            console.debug("page: "+page)
	            return data;
	        }
	    },
	});

});

//]]>