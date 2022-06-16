<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Drawing Lines</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		function line(x1, y1, x2, y2, color="Black", width=1){
			ctx.strokeStyle = color;
			ctx.lineWidth = width;

			ctx.beginPath();
			ctx.moveTo(x1, y1);
			ctx.lineTo(x2, y2);
			ctx.closePath();
			ctx.stroke();
		}

		// garis biasa
		// default strokeStyle "Black", lineWidth 1
		// ctx.strokeStyle = "Pink";
		// ctx.lineWidth = 10;

		// ctx.beginPath();
		// ctx.moveTo(10, 10);
		// ctx.lineTo(60, 60);
		// ctx.closePath();
		// ctx.stroke();

		line(10, 10, 60, 60, "Pink", 10);

		// rumah
		ctx.strokeStyle = "Orange";
		ctx.lineWidth = 1;
		ctx.fillStyle = "Green";

		ctx.beginPath();
		ctx.moveTo(100, 100);
		ctx.lineTo(100, 60);
		ctx.lineTo(130, 30);
		ctx.lineTo(160, 60);
		ctx.lineTo(160, 100);
		ctx.lineTo(100, 100);
		ctx.closePath();
		ctx.stroke();
		ctx.fill();



	</script>
</body>
</html>