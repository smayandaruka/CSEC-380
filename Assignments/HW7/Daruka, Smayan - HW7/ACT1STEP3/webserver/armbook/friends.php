<?php
ini_set("request_order", "GPC");
include_once("common.php");
$has_session = false;
if(isset($_REQUEST["ARM_SESSION"])){
	$session_id = $_REQUEST["ARM_SESSION"];
	// Get Data
	if($stmt = $mysqli->prepare("SELECT * from sessions where session_id=?")){
		if($stmt->bind_param("s", $session_id)){
			if(!$stmt->execute()){
				die("Error - Issue executing prepared statement: " . mysqli_error($mysqli));
			}
			if($res = $stmt->get_result()){
				$row = $res->fetch_assoc();
				if($res->num_rows != 1){
					die('Error - There is an issue with the database, contact your administrator');
				}else{
					$has_session = true;
					$real_user = $row['user_id'];
					$id_to_get = $row['user_id'];
					$ip = $row['ip'];
					$born = $row['born'];
					$valid = $row['valid'];
				}
			}else{
				die("Error - Getting results: " . mysqli_error($mysqli));
			}
		}else{
			die("Error - Issue binding prepared statement: " . mysqli_error($mysqli));
		}
	}else{
		die("Error - Issue preparing statement: " . mysqli_error($mysqli));
	}	
}else{
	$has_session = false;
}
if($has_session){
	$destroy = false;
	if (!isset($ip) or !isset($id_to_get)){
		die("<script>window.location.href = '/index.php';</script>Invalid Session");
	}
	if($_SERVER['REMOTE_ADDR'] !== $ip){
		$destroy = true;
	}
	if($born < time() - 300){
		$destroy = true;	
	}
	if($valid !== 1){
		$destroy = true;
	}
	if($destroy===true){
		die("<script>window.location.href = '/index.php';</script>Invalid Session");
	}
	// Reset our counter
	$timeNow = time();
	if($stmt = $mysqli->prepare("UPDATE sessions SET born=? where user_id=?")){
		if($stmt->bind_param("ii",$timeNow,$real_user)){
			if(!$stmt->execute()){
				die("Error - Issue executing prepared statement: " . mysqli_error($mysqli));
			}
		}else{
			die("Error - Issue binding prepared statement: " . mysqli_error($mysqli));
		}
		if($stmt->close()){
			// We were succesful.
		}else{
			die("Error - Failed to close prepared statement" . mysqli_error($mysqli));
		}
	}else{
			die("Error - Issue preparing statement: " . mysqli_error($mysqli));
	}
	// If the user is asking for some other persons info
	if(isset($_GET['id'])){
		$id_to_get = $_GET['id'];
	}	
	if($stmt = $mysqli->prepare("SELECT * from profiles where user_id=?")){
		if($stmt->bind_param("i", $id_to_get)){
			if(!$stmt->execute()){
				die("Error - Issue executing prepared statement: " . mysqli_error($mysqli));
			}
			if($res = $stmt->get_result()){
				$row = $res->fetch_assoc();
				if($res->num_rows !== 1){
					die('Error - There is an issue with the database, contact your administrator');
				}else{
					$friends = $row['Friends'];
				}
			}else{
				die("Error - Getting results: " . mysqli_error($mysqli));
			}
		}else{
			die("Error - Issue binding prepared statement: " . mysqli_error($mysqli));
		}
	}else{
		die("Error - Issue preparing statement: " . mysqli_error($mysqli));
	}
	echo $friends . "<BR>";
	$friends = explode(',',$friends);
	if(count($friends) < 1){
		die("Sorry no friends");
	}
	foreach ($friends as &$value) {
		if(!is_numeric($value)){
			die("A problem has occurred contact your administrator");
		}
	}
	
	$ids = implode(', ',$friends);
	$query = "SELECT firstname, lastname FROM users WHERE user_id IN (";
	$query = $query . $ids . ");";
	$result = $mysqli->query($query);
	$query = "SELECT user_id, picture_url FROM profiles WHERE user_id IN (";
	$query = $query . $ids . ");";	
	$result2 = $mysqli->query($query);

	if($result and $result2){
		echo "<table border='1'>";
		while ($row = $result->fetch_assoc()){
			$row2 = $result2->fetch_assoc();
			echo "<td>";
			echo "<img src='".$row2["picture_url"]."' width=100px height=100px>";
			$name = $row["firstname"] . ' ' . $row["lastname"];
			echo "<a href='home.php?id=".$row2["user_id"]."'>". $name . "</a>";
			echo "</td>";
		}
		echo "</table>";
		$result->free();
		$result2->free();
	}else{
		die("Error - Making query: " . mysqli_error($mysqli));
	}

	
	
	
}
?>
