function loadconfig(){
$(document).ready(function() {
$.get("load.php", function(data) {
  console.log(data);
  $.each(data.KOMENDY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch switch-data").attr({
        type: "checkbox",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'KOMENDY'});
      $("#komendy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch switch-data").attr({
        type: "checkbox",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'KOMENDY'});
      $("#komendy-checkboxes").append(div);      
    }

  });
  $.each(data.BITSY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch switch-data").attr({
        type: "checkbox",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'BITSY'});
      $("#bitsy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch switch-data").attr({
        type: "checkbox",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'BITSY'});
      $("#bitsy-checkboxes").append(div);      
    }

  });
  $.each(data.POINTSY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch switch-data").attr({
        type: "checkbox",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'POINTSY'});
      $("#pointsy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch switch-data").attr({
        type: "checkbox",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'POINTSY'});
      $("#pointsy-checkboxes").append(div);      
    }

  });


$('.switch-data').click(function() {
  const checkboxObj = {
    KOMENDY: [],
    BITSY: [],
    POINTSY: []
  }
  $('.switch-data').each(function () {
    const prefix = $(this).parent().attr('id');
    if($(this).prop('checked')){
      checkboxObj[prefix].push(this.value + " = 1");
    }else{
      checkboxObj[prefix].push(this.value + " = 0");
    }
    });
    const checkboxObjJson = JSON.stringify(checkboxObj)
    console.log(checkboxObjJson)
    dataToWrite = {
      content: checkboxObjJson
    }
    $.post("save.php", dataToWrite)

});
});
});
}