$(document).ready(function(){
    // $(".ck-button").click(function() {
    //     $("#first-card").show("slide", { direction: "left" }, 1000);
    //   //   $("#first-card").animate(
		// 	// {"padding-right": "+=80%"},
		// 	// "slow");
    //
    // });
    var hideoptions = {  "direction" : "left",  "mode" : "hide"};
    var showoptions = {"direction" : "right","mode" : "show"};
    $(".ck-button").click(function() {
      // $("#first-card").toggle("slide");
      // $("#first-card-2").removeAttr("hidden");
      // $("#first-card-2").toggle("slide");
      // $( "#firstCard" ).effect( "slide", hideoptions, 1000); //notice, no callback
      // $( "#firstCard2" ).effect( "slide", showoptions, 1000);
    });
    $("#navPostLink").click(function() {
      $("#postModal").modal();
    });
    $('#postModal').on('shown.bs.modal', function() {
      $('#myInput').focus()
    })
});

function move() {
    var divs = document.getElementsByClassName("reaction-bar"), i=divs.length, r=0, id = 0;
    while(i--){
      r = divs[i].getAttribute("reactVal");
      for(var j=0; j < r; j++){
        divs[i].style.width = j + '%';
      }
    }
}
