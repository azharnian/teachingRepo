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
			margin: 25px;
		}

		div#d1 {
			background-color: red;
			text-align: center;
			padding: 15px;
		}

		div#d2 {
			background-color: green;
			text-align: right;
			padding: 25px 50px 6px 6px;
			
		}

		div#d3 {
			background-color: blue;
			text-align: left;
			padding: 6px 6px 6px 50px;
			
		}

		div#d4 {
			background-color: yellow;
			text-align: center;
			padding: 50px;
		}

		p {
			background-color: white;
		}

	</style>
</head>
<body>

	<div id="d1"><p>DIV #1</p></div>
	<div id="d2"><p>DIV #2</p></div>
	<div id="d3"><p>DIV #3</p></div>
	<div id="d4"><p>DIV #4</p></div>

</body>
</html>