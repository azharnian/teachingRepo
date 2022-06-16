<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Change Color</title>
</head>
<body>
	<h1 id="hello">Hello...!</h1>
	<button id="red">Red</button>
	<button id="green">Green</button>
	<button id="blue">Blue</button>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script type="text/javascript">

	$("#red").click(function () {
		$("#hello").css('color', 'red');
	})

	$("#green").click(function () {
		$("#hello").css('color', 'green');
	})

	$("#blue").click(function () {
		$("#hello").css('color', 'blue');
	})
		
	</script>
</body>
</html>