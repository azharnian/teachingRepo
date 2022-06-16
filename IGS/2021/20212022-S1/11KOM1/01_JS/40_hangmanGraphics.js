<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hangman Graphics</title>
</head>
<body>
	<canvas id="canvas" width="600" height="600" style="border: 1px solid black;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		function circle(x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI/3, true);
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
			ctx.stroke();
		}
		
		function drawHangman(x, y, color) {
			//head
			let hisHead = circle(x, y-100, 50, color, true);

			//body
			let body = line(x, y-100, x, y+100, color);

			//hands
			let leftHand = line(x, y-50, x-50, y, color);
			let rightHand = line(x, y-50, x+50, y, color);

			//legs
			let leftLeg = line(x, y+100, x-50, y+150);
			let rigthLeg = line(x, y+100, x+50, y+150);
		}

		// drawHangman(200, 200, "Green");	

	</script>
</body>
</html>