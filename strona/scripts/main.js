function loadconfig(){
$(document).ready(function() {
$.get("load.php", function(data) {
  console.log(data);
  $.each(data.KOMENDY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "data",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'KOMENDY'});
      $("#komendy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "data",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'KOMENDY'});
      $("#komendy-checkboxes").append(div);      
    }

  });
  $.each(data.BITSY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "data",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'BITSY'});
      $("#bitsy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "data",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'BITSY'});
      $("#bitsy-checkboxes").append(div);      
    }

  });
  $.each(data.POINTSY, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "data",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'POINTSY'});
      $("#pointsy-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "data",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label).attr({id: 'POINTSY'});
      $("#pointsy-checkboxes").append(div);      
    }

  });


$('#data[type="checkbox"]').click(function() {
  wholeValues = [];
  console.log("dziala submit");
  console.log("aaa" + $(this).val())
});
});
});
}
  // var allCheckBoxes = $('#[type="checkbox"]');
  // var serializedCheckBoxes = [];
  // var i = 0;
  // allCheckBoxes.each(function(){
  //   if($(this).prop('checked')){
  //     //console.log($(this).val() + "=1");
  //     serializedCheckBoxes[i] = $(this).val() + " = 1"
  //   }else{
  //     //console.log($(this).val() + "=0");
  //     serializedCheckBoxes[i] = $(this).val() + " = 0"
  //   }
  //   i++;
  // });
  // console.log(serializedCheckBoxes);
  // var dataToWrite = {
  //   content: serializedCheckBoxes,
  // };
  // $.post("save.php", dataToWrite);   
  // console.log(serializedCheckBoxes);