<?php
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
		die("<script>window.location.href = '/armbook/index.php';</script>Invalid Session");
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
		die("<script>window.location.href = '/armbook/index.php';</script>Invalid Session");
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
	
	if(isset($_GET['comment'])){
		$maxLength = 300;
		$comment = $_GET['comment'];
		$comment = substr ($comment,0,$maxLength);
		if($stmt = $mysqli->prepare("INSERT INTO posts (user_id_from, user_id_to, text)
VALUES (?, ?, ?)")){
			if($stmt->bind_param("iis", $real_user, $id_to_get, $comment)){
				if(!$stmt->execute()){
					die("Error - Issue executing prepared statement: " . mysqli_error($mysqli));
				}
			}else{
				die("Error - Issue binding prepared statement: " . mysqli_error($mysqli));
			}
			if($stmt->close()){
				echo "Added Comment";
			}else{
				die("Error - Failed to close prepared statement" . mysqli_error($mysqli));
			}
		}else{
			die("Error - Issue preparing statement: " . mysqli_error($mysqli));
		}					

	}else{
		die("There was an issue contact your administrator");
	}

}
?>	
