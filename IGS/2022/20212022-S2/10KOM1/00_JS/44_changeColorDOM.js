<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Change Color</title>
</head>
<body>
	<h1 id="header">Helloo ...!</h1>
	<button id="red">Red</button>
	<button id="green">Green</button>
	<button id="blue">Blue</button>

	
	<script type="text/javascript">
		document.querySelector("#red").onclick = () => {
			document.querySelector("#header").style.color = "red";
		}
		document.querySelector("#green").onclick = () => {
			document.querySelector("#header").style.color = "green";
		}
		document.querySelector("#blue").onclick = () => {
			document.querySelector("#header").style.color = "blue";
		}
	</script>
</body>
</html>