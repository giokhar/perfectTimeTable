/*================================================================================
	Item Name: Materialize - Material Design Admin Template
	Version: 4.0
	Author: PIXINVENT
	Author URL: https://themeforest.net/user/pixinvent/portfolio
================================================================================

NOTE:
------
PLACE HERE YOUR OWN JS CODES AND IF NEEDED.
WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR CUSTOM SCRIPT IT'S BETTER LIKE THIS. */

$(function() {
	counter = 1;
	$(".add").click(function () {
	    if (counter < 10){ // Check not to add duplicate items
	  		$("#courses").append($(this).val()+"<br>");
	  	}
	  	counter++;
	});
});