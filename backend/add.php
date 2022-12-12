<?php
$username='root';
$password='';
$db_name='testdb';
$server_name='localhost';
$conn = new mysqli($server_name, $username, $password, $db_name);

if($conn->connect_error){
    die("connection failed: REASON".$conn->connect_error);
}
$id=$_GET['id'];
$role=$_GET['role'];

$stmt = $conn->prepare("INSERT INTO members (card_id, dr) VALUES (?,?)");
$stmt->bind_param('si',$id, $role);
$stmt->execute();
echo $stmt->affected_rows;
$stmt->close();
$conn->close();




