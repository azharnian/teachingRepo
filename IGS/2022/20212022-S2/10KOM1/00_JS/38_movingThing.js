<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Making Thing Move</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="background-color: grey;"></canvas>
	<script type="text/javascript">
			
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		let width = canvas.width;
		let height = canvas.height;

		let positionX = 0;
		let direction = 1;
		let color = "Black";

		// ctx.fillRect(positionX, 0, 20, 20);

		setInterval( () => {
			ctx.clearRect(0, 0, width, height);
			ctx.fillStyle = color;
			ctx.fillRect(positionX, 0, 20, 20);

			positionX += direction*1;
			if (positionX > width){
				direction = -1;
				color = "White";
			}

			if (positionX < 0){
				direction = 1;
				color = "Black";
			}

			
			// positionX ++;
			// if (positionX > width){
			// 	positionX = 0;
			// }
			
		}, 5);

	</script>
</body>
</html>