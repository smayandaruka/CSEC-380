<!DOCTYPE html>
<html>
<body>
</body>
    <div id = pluginslist></div>
<?php
    $referer = $_SERVER['HTTP_REFERER'];
    $ip = $_SERVER['REMOTE_ADDR'];
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    echo("Referer: ".$referer);
    echo("IP: ".$ip);
    echo("User-Agent: ".$user_agent);
?>
<script>
var length = navigator.plugins.length;
var plugins = "Plugins installed: ";
for(var i = 0; i < length; i++){
    if(length == 1)
        plugins = plugins + navigator.plugins[i].name;
    else
        plugins = plugins + navigator.plugins[i].name + ", "; 
}
document.getElementById("pluginslist").innerHTML = plugins;
</script>
</html>
