<?php
$ini_array = parse_ini_file("data/data_save.ini");
header('Content-Type: application/json');
echo json_encode($ini_array);
?>