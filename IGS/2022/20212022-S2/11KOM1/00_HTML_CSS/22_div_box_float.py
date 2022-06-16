<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Div Box Float</title>
	<style type="text/css">
		body {
			margin: 0;
		}

		div {
			width: 100px;
			height: 100px;
			border: 5px solid black;
			color: black;
			font-weight: bold;
			margin: 25px;
		}

		div#d1 {
			background-color: red;
			float: left;
		}

		div#d2 {
			background-color: green;
			float: left;
		}

		div#d3 {
			background-color: blue;
			float: left;
		}

		div#d4 {
			background-color: yellow;
			float: right;
		}
	</style>
</head>
<body>
	<div id="d1">DIV #1</div>
	<div id="d2">DIV #2</div>
	<div id="d3">DIV #3</div>
	<div id="d4">DIV #4</div>

</body>
</html>