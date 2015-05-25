//<![CDATA[

function updateCategory(link) {
	category = $(link).attr("id");
	$("#cat_dropdown").text(category);
	$("#category").val(category)
}

function doAdd () {
	var tags = $("#tags_form").select2("val");
	$("#tags_input").val(tags);
	$("#link_form").submit();
}

$( document ).ready(function() {

	$("#tags_form").select2({
		placeholder: "Add a tag",
		minimumInputLength: 3,
		multiple: true,
		tags: true,
		tokenSeparators: [",", " "],
		createSearchChoice: function(term, data) {
		  if ($(data).filter(function() {
		    return this.text.localeCompare(term) === 0;
		  }).length === 0) {
		    return {
		      id: term,
		      text: term
		    };
		  }
		},
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