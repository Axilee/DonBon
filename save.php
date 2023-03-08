<?php
  if(isset($_POST['content'])) {
    $content = $_POST['content'];
    if(!file_exists($folder)) {
      mkdir($folder);
    }
    
    $file = fopen("data/data_save.ini", "w");
    fwrite($file, "[KOMENDY]\n");
    foreach ($content as $line) {
        fwrite($file, $line."\n");
    }
    fclose($file);

    echo "Wartość została zapisana w pliku";
  } else {
    echo "Nie udało się zapisać wartości.";
  }
?>