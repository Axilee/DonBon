<?php
if ($file = fopen("data/data_save.ini","r")){

    fgets($file);

    while(!feof($file)){
        $textperline = fgets($file);
        $data = explode("=", $textperline);
        $key = trim($data[0]);
        $value = trim($data[1]); 
        echo("$key: $value<br>");
    }
    fclose($file);
}

?>