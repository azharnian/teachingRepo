<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Hangman ...</title>
</head>
<body>
	<canvas id="canvas" width="800" height="800" style="background-color: grey;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		let circle = function (x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			ctx.closePath();
			ctx.stroke();
			if (isFilled){
				ctx.fillStyle = color;
				ctx.fill();
			}
		}


		let line = function (initX, initY, finalX, finalY, color, width=3){
			ctx.strokeStyle = color;
			ctx.lineWidth = width;

			ctx.beginPath();
			ctx.moveTo(initX, initY);
			ctx.lineTo(finalX, finalY);
			ctx.closePath();
			ctx.stroke();
		}


		let hangman = function (x, y, color){
			let head = circle(x, y, 50, color, true);
			let body = line(x, y+50, x, y+200, "Green", width=20);


			//hands
			let leftHand = line(x, y+50, x-80, y+50+50, "Green", width=10);
			let rightHand = line(x, y+50, x+80, y+50+50, "Green", width=10);

			//legs
			let leftLeg = line(x, y+200, x-80, y+200+50+50, "Green", width=10);
			let rightLeg = line(x, y+200, x+80, y+200+50+50, "Green", width=10);
		}


		hangman(300, 300, "Green");

	</script>
</body>
</html>