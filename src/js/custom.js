$(document).ready(function(){
    $(".ck-button").click(function() {
        $(".row").animate(
			{"padding-right": "+=20em", "opacity": "0"}, 
			"slow");
    });
});