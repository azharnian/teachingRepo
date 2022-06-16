<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>ChessBoard</title>
</head>
<body>
	<canvas id="canvas" width="600" height="600" style="border: 1px solid black;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");
		const width = 600/8;


		for (let row = 0; row < 8; row++){
			for (let col = 0; col < 8; col++){
				
				ctx.beginPath();
				if (row % 2 === 0){
					if (col % 2 === 0){
						ctx.fillStyle = "White";
					} else {
						ctx.fillStyle = "Black";
					}
					ctx.fillRect(col*width, row*width, width, width);
				} else {
					if (col % 2 === 0){
						ctx.fillStyle = "Black";
					} else {
						ctx.fillStyle = "White";
					}
					ctx.fillRect(col*width, row*width, width, width);
				}
				
				// if ( (row+col) % 2 !== 0){
				// 	ctx.beginPath();
				// 	ctx.fillRect(col*width, row*width, width, width);
				// }
			}
		}
		

	</script>
</body>
</html>