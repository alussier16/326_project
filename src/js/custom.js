$(document).ready(function(){
    // $(".ck-button").click(function() {
    //     $("#first-card").show("slide", { direction: "left" }, 1000);
    //   //   $("#first-card").animate(
		// 	// {"padding-right": "+=80%"},
		// 	// "slow");
    //
    // });
    $(".ck-button").click(function() {
      $("#first-card").toggle("slide");
      $("#first-card-2").removeAttr("hidden");
      $("#first-card-2").toggle("slide");
    });
});
