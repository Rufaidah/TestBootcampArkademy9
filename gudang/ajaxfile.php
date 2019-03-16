<?php  
include "config.php";

$sql = "SELECT categories.id, categories.nama as CategoryName, products.nama as Products  
		FROM categories INNER JOIN products
		ON categories.id = products.categories_id";

$query = mysqli_query($conn, $sql);

if (!$query) {
	die ('SQL Error: ' . mysqli_error($conn));
}

$response = array();

while ($row = mysqli_fetch_assoc($query)) {
	# code...
	$response[] = $row;
}

echo json_encode($response);
exit;
?>