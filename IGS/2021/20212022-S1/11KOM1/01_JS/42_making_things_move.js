<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Making Things Move</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="border:1px solid black"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		let positionX = 0;
		let size = 400;

		function movingSquare() {
			ctx.clearRect(0, 0, 400, 400);
			ctx.fillRect(positionX, 0, 20, 20);

			positionX++;
			if(positionX > 400){
				positionX = 0;
			}
		}

		setInterval(function () {
			ctx.clearRect(0, 0, 400, 400);
			ctx.fillRect(0, 0, size, 400);

			size--;
			if (size < 0){
				size = 400;
			}

		}, 30);
		//4 changing size of a square
	</script>
</body>
</html>