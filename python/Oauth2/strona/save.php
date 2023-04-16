<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $content = $_POST['content'];
  print_r($content);
  $contentDecoded = json_decode($content,true);
  $iniContent = '';
  foreach ($contentDecoded as $sectionName => $sectionValues) {
    $iniContent .= "[$sectionName]\n";
  foreach ($sectionValues as $key) {
    $iniContent .= "$key\n";
  }
    $iniContent .= "\n";
}
file_put_contents('../python/zmienne.ini', $iniContent);
}
  ?>
