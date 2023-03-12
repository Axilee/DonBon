function loadconfig(){
$(document).ready(function() {
$.get("load.php", function(data) {
  console.log(data);
  $.each(data, function(key, value){
    if(value == 1){
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "s1",
        value: key,
        checked : true
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label);
      $("#data-checkboxes").append(div);      
    }else{
      var checkbox = $("<input>").addClass("switch").attr({
        type: "checkbox",
        id: "s1",
        value: key
      });
      var label = $("<label>").attr("for", "s1").text(key);
      var div = $("<div>").append(checkbox, label);
      $("#data-checkboxes").append(div);      
    }
  });

  // TO JEST NOWY SWITCH DO DYNAMICZNEGO DRUKOWANIA
  // <div class="komendy">
  // <input id="s1" type="checkbox" class="switch"><label for="s1">Switch</label>
  // </div>


$('#s1[type="checkbox"]').click(function() {
  console.log("dziala submit");
  var allCheckBoxes = $('#s1[type="checkbox"]');
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
  console.log(serializedCheckBoxes);
  var dataToWrite = {
    content: serializedCheckBoxes,
  };
  $.post("save.php", dataToWrite);   
  console.log(serializedCheckBoxes);
});
});
});
}