$( document ).ready(function() {

$(".load-scenario").click(function(){

  var app = $(this).data().app;
  var scenario = $(this).data().scenario;
  var iconResult = $(this).siblings(".load-result").children();
  var buttonResult = $(this).siblings(".load-result");
  var flush = "?flush=0";

  if($(this).hasClass("load-scenario-flush")){
    var flush = "";
  }
  var endpoint = app+"/scenarios/"+scenario+flush;

  var request = $.ajax({
    url: endpoint,
    type: "GET",
  });
  

  request.done(function() {
    if(buttonResult.hasClass("btn-primary")){
      buttonResult.toggleClass("btn-primary btn-success");
      iconResult.addClass("glyphicon-ok");
    }else{
      if(buttonResult.hasClass("btn-danger")){
        buttonResult.toggleClass('btn-danger btn-success');
        iconResult.toggleClass('glyphicon-remove glyphicon-ok');
      }
    }
  });

  request.fail(function(error, textStatus) {
    if(buttonResult.hasClass("btn-primary")){
      buttonResult.toggleClass("btn-primary btn-danger");
      iconResult.addClass("glyphicon-remove");
    }else{
      if(buttonResult.hasClass("btn-success")){
        buttonResult.toggleClass('btn-success btn-danger');
        iconResult.toggleClass('glyphicon-ok glyphicon-remove');
      }
    }
  });

 });

});
