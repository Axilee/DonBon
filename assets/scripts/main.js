function loadconfig(){
$(document).ready(function() {
$.getJSON("load.php", function(data) {
  console.log(data);
  $.each(data, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("form-check-input").attr({
        type: "checkbox",
        id: "switchForBot",
        value: key,
        checked : true
      });
      var label = $("<label>").addClass("form-check-label").attr("for", "switchForBot").text(key);
      var div = $("<div>").addClass("form-check form-switch").append(checkbox, label);
      $("#data-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("form-check-input").attr({
        type: "checkbox",
        id: "switchForBot",
        value: key
      });
      var label = $("<label>").addClass("form-check-label").attr("for", "switchForBot").text(key);
      var div = $("<div>").addClass("form-check form-switch").append(checkbox, label);
      $("#data-checkboxes").append(div);      
    }
  });

  // TO JEST NOWY SWITCH DO DYNAMICZNEGO DRUKOWANIA
  // <div class="komendy">
  // <input id="s1" type="checkbox" class="switch"><label for="s1">Switch</label>
  // </div>


$('#switchForBot[type="checkbox"]').click(function() {
  console.log("dziala submit");
  var allCheckBoxes = $('#switchForBot[type="checkbox"]');
  var serializedCheckBoxes = [];
  var i = 0;
  allCheckBoxes.each(function(){
    if($(this).prop('checked')){
      //console.log($(this).val() + "=1");
      serializedCheckBoxes[i] = $(this).val() + " = 1"
    }else{
      //console.log($(this).val() + "=0");
      serializedCheckBoxes[i] = $(this).val() + " = 0"
    }
    i++;
  });
  var dataToWrite = {
    content: serializedCheckBoxes,
    folder: "data",
    filename: "data_save.ini"
  };
  $.post("save.php", dataToWrite);   
  console.log(serializedCheckBoxes);
});
});
});
}