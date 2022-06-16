<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Follow The Mouse</title>
</head>
<body>
	<canvas id="canvas" width="500" height="500" style="background-color: grey;"></canvas>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script type="text/javascript">
		let canvas = $('#canvas');
		let ctx = canvas[0].getContext('2d');

		let mouseX = 0;
		let mouseY = 0;
		let easing = 0.1;
		let x = 0;
		let y = 0;

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

		canvas.mousemove( function (event) {
			// console.log(event.pageX, event.pageY);
			mouseX = event.pageX;
			mouseY = event.pageY;
		})

		setInterval(function (){
			let targetX = mouseX;
			let targetY = mouseY;

			x += (targetX - x) * easing;
			y += (targetY - y) * easing;

			ctx.clearRect(0, 0, canvas[0].width, canvas[0].height);
			circle(x, y, 10, "Purple", true);
		}, 30);
	</script>
</body>
</html>