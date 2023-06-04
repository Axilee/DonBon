function loadconfig(){
$(document).ready(function() {
$.get("load.php", function(data) {
  console.log(data);
  $.each(data.KOMENDY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch switch-data zmienne").attr({
        type: "checkbox",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'KOMENDY', 'data-command': key });
      $("#komendy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch switch-data zmienne").attr({
        type: "checkbox",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'KOMENDY', 'data-command': key });
      $("#komendy-checkboxes").append(div);      
    }
  });
  $.each(data.BITSY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch switch-data zmienne").attr({
        type: "checkbox",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'BITSY', 'data-command': 'BITSY'+key });
      $("#bitsy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch switch-data zmienne").attr({
        type: "checkbox",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'BITSY', 'data-command': 'BITSY'+key });
      $("#bitsy-checkboxes").append(div);      
    }

  });
  $.each(data.POINTSY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch switch-data zmienne").attr({
        type: "checkbox",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'POINTSY', 'data-command': 'POINTSY'+key });
      $("#pointsy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch switch-data zmienne").attr({
        type: "checkbox",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'POINTSY', 'data-command': 'POINTSY'+key });
      $("#pointsy-checkboxes").append(div);      
    }
  });
  $.each(data.VALBITSY, function(key, value){
    $('div[data-command="BITSY' + key +'"]').each(function() {
    var valueBox = $("<input>").addClass("input-data zmienne").attr({
      type: "text",
      value: value,
      name: key
    });
      $(this).append(valueBox);
    });
  });
  $.each(data.VALPOINTSY, function(key, value){
    $('div[data-command="POINTSY' + key +'"]').each(function() {
    var valueBox = $("<input>").addClass("input-data zmienne").attr({
      type: "text",
      value: value,
      name: key
    });
      $(this).append(valueBox);
    });
  });

  // $.each(data.VALKOMENDY, function(key, value){
  //   var valueBox = $("<input>").addClass("ugabuga").attr({
  //     type: "number",
  //     value: value
  //   });
  //   $(".komendy").append(valueBox);
  // });
  // $.each(data.VALBITSY, function(key, value){
  //   var valueBox = $("<input>").addClass("ugabuga").attr({
  //     type: "number",
  //     value: value
  //   });
  //   $(".bitsy").append(valueBox);
  // });
  // $.each(data.VALPOINTSY, function(key, value){
  //   var valueBox = $("<input>").addClass("ugabuga").attr({
  //     type: "number",
  //     value: value
  //   });
  //   $(".ch-points").append(valueBox);
  // });

$('.zmienne').on('click keydown',function(event) {
  if(event.type === 'click' || (event.type === 'keydown' && event.keyCode === 13)) {
  const checkboxObj = {
    KOMENDY: [],
    BITSY: [],
    POINTSY: [],
    VALBITSY: [],
    VALPOINTSY: []
  }
  $('.switch-data').each(function () {
    const prefix = $(this).parent().attr('id');
    if($(this).prop('checked')){
      checkboxObj[prefix].push(this.value + " = 1");
    }else{
      checkboxObj[prefix].push(this.value + " = 0");
    }
    });
  $('.input-data').each(function () {
    const prefix = $(this).parent().attr('id');
      checkboxObj['VAL'+prefix].push(this.name + " = " + this.value);
  });
    const checkboxObjJson = JSON.stringify(checkboxObj)
    console.log(checkboxObjJson)
    dataToWrite = {
      content: checkboxObjJson
    }
    $.post("save.php", dataToWrite)
  }
});

});
});
}