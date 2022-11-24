<?php
$username='root';
$password='';
$db_name='arduino_db';
$server_name='localhost';
$conn = new mysqli($server_name, $username, $password, $db_name);

if($conn->connect_error){
    die("connection failed: REASON".conn->connect_error);
}
$id=$_GET['id'];

$stmt = $conn->prepare("SELECT full_name, dr FROM members WHERE card_id= ?");
$stmt->bind_param('s',$id);
$stmt->execute();
$stmt->bind_result($name, $role);
if($stmt->fetch()){
    $stmt->close();
    if($role==1){
        $dr_stmt = $conn->prepare("SELECT members.full_name, lectures.LECTURE_NAME, lectures.start_at, lectures.end_at FROM members, lectures WHERE members.card_id=? AND members.card_id=lectures.card_id");
        $dr_stmt->bind_param("s",$id);
        $dr_stmt->execute();
        $dr_stmt->bind_result($dr_name, $lectures, $start_at, $end_at);
        while($dr_stmt->fetch()){
        echo "DR|".$dr_name."|".$lectures."|".$start_at."|".$end_at."<br>";
        }
        $dr_stmt->close();
    }
    elseif($role==0){
        echo "SD|".$name;
    }
}else{
    die("ID isn't in the records");
}
$conn->close();
?>
