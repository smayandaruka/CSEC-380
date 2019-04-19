<?php
// Unset the cookie, this is like good log out -- right?
setcookie("ARM_SESSION", $_COOKIE["ARM_SESSION"], 1);
echo "<script>window.location.href = '/index.php';</script>";
?>