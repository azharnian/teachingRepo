<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Intro Canvas</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="border: 1px solid black;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		for (let i=0; i < 20; i++){
			ctx.fillRect(i*20, i*20, 20, 20);
		}
		//ctx.fillRect(0, 0, 20, 20); // pos dan dimensi (x, y, w, h)

	</script>
</body>
</html>