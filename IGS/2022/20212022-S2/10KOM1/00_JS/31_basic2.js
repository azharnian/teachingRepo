<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Basic 2</title>
</head>
<body>
	<canvas width="400" height="400" id="canvas" style="background-color: grey;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		ctx.fillStyle = "Black";

		for (let i = 0; i < 20; i++){
			ctx.fillRect(i*20, i*20, 20, 20);
		}
		
	</script>
</body>
</html>