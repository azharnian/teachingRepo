<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Simplest Paint</title>
</head>
<body>
	<canvas id="canvas" width="800" height="600" style="border: 1px solid black;"></canvas>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
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

		// function clickHandler(event) {
		// 	circle(event.pageX, event.pageY, 5, "Black", true);
		// }		

		$("html").mousemove(function (event){
			circle(event.pageX, event.pageY, 10, "Black", true);
		});

		//$("html").click(clickHandler);
	</script>
</body>
</html>