<?php
  if(isset($_POST['content'])) {
    $content = $_POST['content'];
<<<<<<< HEAD

    // Ustaw ścieżkę do pliku i folderu
    $filename = 'data_save.ini';
    $folder = 'data';
=======
>>>>>>> 2814c02 (Calkowicie zreworkowany main.js)

    if(!file_exists($folder)) {
      mkdir($folder);
    }
    
    $file = fopen("data/data_save.ini", "w");
    fwrite($file, "[KOMENDY]\n");
    foreach ($content as $line) {
        fwrite($file, $line."\n");
    }
    fclose($file);

    echo "Wartość została zapisana w pliku $filename";
  } else {
    echo "Nie udało się zapisać wartości.";
  }
?>