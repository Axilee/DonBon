<?php
  if(isset($_POST['content'])) {
    $content = $_POST['content'];
221
    // Ustaw ścieżkę do pliku i folderu
    $filename = 'data_save.ini';
    $folder = 'data';

    // Sprawdź, czy folder istnieje, jeśli nie, utwórz go
    if(!file_exists($folder)) {
      mkdir($folder);
    }
    
    // Otwórz plik w trybie do zapisu i zapisz wartość
    $file = fopen("$folder/$filename", "a");
    fwrite($file, "$content\n");
    fclose($file);

    echo "Wartość została zapisana w pliku $filename";
  } else {
    echo "Nie udało się zapisać wartości.";
  }
?>