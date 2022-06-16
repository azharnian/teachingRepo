<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Div Box</title>
	<style type="text/css">

		body {
			margin: 0;
		}
		
		div {
			width: 30%;
			height: 100px;
			border: 5px solid black;
			font-weight: bold;
			text-align: center;
			/*margin: 15px;*/
		}

		div#d1 {
			background-color: red;
			margin: 0;
		}

		div#d2 {
			background-color: green;
			margin: 5px 0px 0px 15px;
		}

		div#d3 {
			background-color: blue;
			margin: 0px 0px 0px 75px;
		}

		div#d4 {
			background-color: yellow;
			margin: 25px 0px 0px 250px;
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