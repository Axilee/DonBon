<?php
$ini_array = parse_ini_file("../python/zmienne.ini");
$ini = file('..\python\zmienne.ini', FILE_IGNORE_NEW_LINES);
$ini = array_slice($ini, 1);
$ini_array = [];

foreach($ini as $element){
    $element_temp = explode(' = ', $element);
    if (count($element_temp) == 2) {
        $ini_array[$element_temp[0]] = $element_temp[1];
    }
}

header('Content-Type: application/json');
echo json_encode($ini_array);
?>