$(document).ready(function(){
    $("#navPostLink").click(function() {
      $("#postModal").modal();
    });
    $('#postModal').on('shown.bs.modal', function() {
      $('#myInput').focus()
    })
});
