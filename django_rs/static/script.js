$( document ).ready(function() {

$(".load-scenario").click(function(){

  var app = $(this).data().app;
  var scenario = $(this).data().scenario;
  var icon = $(this).children();
  var flush = "?flush=0";

  if($(this).hasClass("load-scenario-flush")){
    var flush = "";
  }
  var endpoint = app+"/"+scenario+flush;

  var request = $.ajax({
    url: endpoint,
    type: "GET",
  });

  request.done(function() {
    $(icon).toggleClass('glyphicon-play glyphicon-ok');
  });

  request.fail(function(error, textStatus) {
    $(icon).toggleClass('glyphicon-play glyphicon-remove');
  });

 });

});
