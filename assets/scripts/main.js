function loadconfig(){
  $(document).ready(function() {
    var keyVal = [];
    var valueVal = [];
    var partsVal = [];
    $.post("load.php", function(data) {
      pairs = data.split('<br>');
        for (var i = 0; i < pairs.length -1; i++) {
            parts = pairs[i].split(':');
            key = parts[0].trim();
            value = parts[1].trim();
            //console.log(key + ": " + value);// wyjebać
            if(value == 1){
              $("#data-checkboxes").append("<div class='form-check form-switch'><input class='form-check-input' type='checkbox' id='switch-"+ key +"' value='"+ key +"' checked><label class='form-check-label' for='flexSwitchCheckDefault'>"+ key +"</label></div>");
            }else{
              $("#data-checkboxes").append("<div class='form-check form-switch'><input class='form-check-input' type='checkbox' id='switch-"+ key +"' value='"+ key +"'><label class='form-check-label' for='flexSwitchCheckDefault'>"+ key +"</label></div>");
            }
            //$("#data-checkboxes").append(key + ": " + value + "<br>");
            partsVal.push(parts);
            keyVal.push(key);
            valueVal.push(value);
        }

$("#points-btn").click(function(){
  $("#current-mode").text("Punkty");
  $.post("save.php", { content: "punkty = 1", folder: "data", filename: "data_save.ini" })
    .done(function() {
      console.log("Zapisano wartość " + "punkty = 1" + " w pliku data_save.ini");// wyjebać
    })
    .fail(function() {
      console.log("Nie udało się zapisać wartości " + result + " w pliku data_save.ini");// wyjebać
        });
    });
$("#commands-btn").click(function(){
  $("#current-mode").text("Komendy");
  $.post("save.php", { content: "punkty = 0", folder: "data", filename: "data_save.ini" })
    .done(function() {
      console.log("Zapisano wartość " + "punkty = 0" + " w pliku data_save.ini");// wyjebać
    })
    .fail(function() {
      console.log("Nie udało się zapisać wartości " + result + " w pliku data_save.ini");// wyjebać
        });
    });
var i = 0;
$("input[type=checkbox]").change(function(){
  console.log("[START] dziala sumbit") // wyjebać
  $checkboxValues = $("input[type=checkbox]");
  if ($(this).is(":checked")){
    console.log("[checkboxy] wykryto zmiane w " + $(this).prop("value")); // wyjebać 
  }
});
});
});
}
