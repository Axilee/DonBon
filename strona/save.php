<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $content = $_POST['content'];
  $dataArray = array();
  foreach ($content as $element) {
    $data = explode(" = ", $element);
    $dataArray[$data[0]] = $data[1];
  }
  $dataString = "";
  foreach ($dataArray as $key => $value){
    $dataString .= "$key = $value\n";
  }
  file_put_contents("assets\data\data_save.ini", "[KOMENDY]\n" . $dataString);
}
  ?>
