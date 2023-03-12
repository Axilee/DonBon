<?php
$ini_array = parse_ini_file("data/data_save.ini");
$ini = file('assets\data\data_save.ini', FILE_IGNORE_NEW_LINES);
$ini = array_slice($ini, 1);
$ini_array = [];

foreach($ini as $element){
    $element_temp = explode(' = ', $element);
    $ini_array[$element_temp[0]] = $element_temp[1];
}
header('Content-Type: application/json');
echo json_encode($ini_array);
?>