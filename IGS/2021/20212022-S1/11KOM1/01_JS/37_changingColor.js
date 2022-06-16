<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Intro Canvas 2</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="border: 1px solid black;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		ctx.fillStyle = "Red";
		ctx.fillRect(10, 10, 100, 100);

		ctx.strokeStyle = "Blue";
		ctx.lineWidth = 3;
		ctx.strokeRect(10, 10, 100, 100);

	</script>
</body>
</html>