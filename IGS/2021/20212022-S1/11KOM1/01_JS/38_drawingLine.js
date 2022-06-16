<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Intro Canvas 3</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="border: 1px solid black;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		ctx.strokeStyle = "SkyBlue";
		ctx.lineWidth = 4;

		ctx.beginPath();
		ctx.moveTo(10, 10);
		ctx.lineTo(60, 60);
		ctx.moveTo(60, 10);
		ctx.lineTo(10, 60);
		ctx.closePath();
		ctx.stroke();

		ctx.fillStyle = "Pink";
		ctx.beginPath();
		ctx.moveTo(100, 100);
		ctx.lineTo(100, 60);
		ctx.lineTo(130, 30);
		ctx.lineTo(160, 60);
		ctx.lineTo(160, 100);
		ctx.lineTo(100, 100);
		ctx.fill();
		ctx.stroke();
		ctx.closePath()



	</script>
</body>
</html>