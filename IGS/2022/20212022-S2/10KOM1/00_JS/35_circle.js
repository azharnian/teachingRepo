<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Drawing Circle</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		ctx.strokeStyle = "Blue";
		ctx.fillStyle = "Blue";
		ctx.lineWidth = 4;

		ctx.beginPath(); // (xp, yp, radius, start, stop, mode)
		ctx.arc(200, 200, 50, 0, 2*Math.PI, false); // clockwise / searah jarum jam (tidak searah kuadran)
		ctx.stroke();
		ctx.fill();

		//buatin function circle

	</script>
</body>
</html>