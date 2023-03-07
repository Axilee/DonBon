function loadconfig(){
  var keyVal = [];
  var valueVal = [];
  var partsVal = [];
  $(document).ready(function() {
    $.post("load.php", function(data) {
        pairs = data.split('<br>');
        for (var i = 0; i < pairs.length -1; i++) {
            parts = pairs[i].split(':');
            key = parts[0].trim();
            value = parts[1].trim();
            //console.log(key + ": " + value);// wyjebać
            $("#data-checkboxes").append("<div class='form-check form-switch'><input class='form-check-input' type='checkbox' id='switch"+ key +"><label class='form-check-label' for='flexSwitchCheckDefault'>"+ key +"</label></div>");
            //$("#data-checkboxes").append(key + ": " + value + "<br>");
            partsVal.push(parts);
            keyVal.push(key);
            valueVal.push(value);
        }
    });
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

$("#dataConfig").submit(function(event){
  console.log("[START] dziala sumbit") // wyjebać
  $checkboxValues = $("input[type=checkbox]");
  var i=0;
  $checkboxValues.each(function(){
    if($(this).prop("checked")){
<<<<<<< HEAD
      keyVal.forEach(element => {
      console.log("[Element]" + element);
=======
      valueVal.forEach(element => {
      console.log("[elementy] = " + element[i]);
>>>>>>> b76b2a8 (load.php)
      });
      i++;
      console.log("[checkboxy] wykryto zmiane"); // wyjebać 
    }
  });
  console.log("i warte = "+i);
  //console.log($checkboxValues); // wyjebać
  event.preventDefault();
});
});
}
