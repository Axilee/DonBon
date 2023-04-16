<?php
$ini_array = parse_ini_file("../python/zmienne.ini", true);
header('Content-Type: application/json');
echo json_encode($ini_array);
?>