//<![CDATA[

$(document).ready(function() {
	$('#loginbutton').on('click', login );
});

/*function updateStatusCallback(){
   alert('Status updated!!');
   // Your logic here
}

(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/es_LA/sdk.js#xfbml=1&appId=1429178424024008&version=v2.0";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));*/

//]]>


$('#loginbutton').click(function(){
		$.ajaxSetup({ cache: true });
		$.getScript('http:////connect.facebook.net/en_US/all.js#xfbml=1&appId=1429178424024008', function(){
			FB.init({
				appId: '1429178424024008',
			});
			$('#loginbutton,#feedbutton').removeAttr('disabled');
			FB.getLoginStatus(updateStatusCallback);


			var login = FB.getLoginStatus(function(response) {
			  if (response.status === 'connected') {
			    // the user is logged in and has authenticated your
			    // app, and response.authResponse supplies
			    // the user's ID, a valid access token, a signed
			    // request, and the time the access token 
			    // and signed request each expire
			    var uid = response.authResponse.userID;
			    var accessToken = response.authResponse.accessToken;
			  } else if (response.status === 'not_authorized') {
			    // the user is logged in to Facebook, 
			    // but has not authenticated your app
			  } else {
			    // the user isn't logged in to Facebook.
			  }
			 });
			FB.getLoginStatus(function(response) {
			  console.log('######################')
			}, true);


		});
		);     
	});