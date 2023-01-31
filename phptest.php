<?php
//echo 'starting';
$file = $_FILES['myfile'];
$name_ls = explode(".",$file['name']);
$rnd = rand(0, 10000000);
$Fname = 'F' . $rnd . '.' . end($name_ls);
move_uploaded_file($file['tmp_name'], 'uploads/' . $Fname);
shell_exec('python3 Gcloud_code.py "' . $Fname . '"> output.txt 2> output.err');
shell_exec('cp output.txt FRONTEND_/lib/output_txt.txt');
shell_exec('cp uploads/' . $Fname . ' FRONTEND_/lib/output_img.png');
$src = 'uploads/'. $Fname;

//echo $src.'<br/>';
//echo '<img src="'.$src.'">';
//$Vdata = file_get_contents('output.txt');
//$Vdata = file_get_contents('FRONTEND_/src/Res.html');
//echo '<img src="uploads/' . $Fname . '">';
//echo $src.'<br/>';
//echo $Vdata;
echo '<meta http-equiv="refresh" content="0; URL=http://8.213.25.141/FRONTEND_/src/Res.html" />'
?>


