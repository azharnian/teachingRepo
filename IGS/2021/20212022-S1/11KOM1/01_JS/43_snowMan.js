<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Snow Man</title>
</head>
<body>
	<canvas id="canvas" width="600" height="600" style="border: 1px solid black;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		function circle(x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			ctx.stroke();
			if (isFilled){
				ctx.fillStyle = color;
				ctx.fill();
			}
			
		}

		function line(initX, initY, finalX, finalY, color) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.moveTo(initX, initY);
			ctx.lineTo(finalX, finalY);
			ctx.stroke()
		}
		
		function drawSnowman(x, y, color, isFilled) {
			//create Head
			let head = circle(x, y-100, 50, "Red", true);
			let leftEye = circle(x-20, y-120, 10, "Black", true);
			let rightEye = circle(x+20, y-120, 10, "Black", true);
			let nose = circle(x, y-100, 5, "Black", true);

			//mouth
			ctx.beginPath()
			ctx.arc(x, y-90, 20, 0, Math.PI, false);
			ctx.stroke();

			//create Body
			let body = circle(x, y+50, 100, "Red", true);
		}

		drawSnowman(300, 300, true);

	</script>
</body>
</html>