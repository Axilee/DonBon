function loadconfig(){
  $(document).ready(function() {
    $.post("load.php", function(data) {

        var pairs = data.split('<br>');
        
        for (var i = 0; i < pairs.length -1; i++) {

            var parts = pairs[i].split(':');
            var key = parts[0].trim();
            var value = parts[1];
            console.log(key + ": " + value);
            $("#data-checkboxes").append("<div class='form-check form-switch'><input class='form-check-input' type='checkbox' id='flexSwitchCheckDefault'><label class='form-check-label' for='flexSwitchCheckDefault'>"+ key +"</label></div>");
            //$("#data-checkboxes").append(key + ": " + value + "<br>");

        }
    });
});
}

$(document).ready(function (){
  $("#points-btn").click(function(){
    $("#current-mode").text("Punkty");
    $.post("save.php", { content: "punkty = 1", folder: "data", filename: "data_save.ini" })
      .done(function() {
        console.log("Zapisano wartość " + "punkty = 1" + " w pliku data_save.ini");
      })
      .fail(function() {
        console.log("Nie udało się zapisać wartości " + result + " w pliku data_save.ini");
      });
  });
  $("#commands-btn").click(function(){
    $("#current-mode").text("Komendy");
    $.post("save.php", { content: "punkty = 0", folder: "data", filename: "data_save.ini" })
      .done(function() {
        console.log("Zapisano wartość " + "punkty = 0" + " w pliku data_save.ini");
      })
      .fail(function() {
        console.log("Nie udało się zapisać wartości " + result + " w pliku data_save.ini");
      });
  });
});

$("#dataConfig").submit(function(event){
  alert("dziala sumbit");
  event.preventDefault();
})
