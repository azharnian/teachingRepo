<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Archs and Circles</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="border:1px solid black"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		function circle(x, y, radius, color) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			ctx.stroke();
		}

		ctx.strokeStyle = "Green";
		ctx.lineWidth = 3;

		ctx.beginPath();
		ctx.arc(50, 50, 20, 0, Math.PI/2, false);
		ctx.stroke();

		// 1/2 lingkaran
		ctx.beginPath();
		ctx.arc(100, 50, 20, 0, Math.PI, false);
		ctx.stroke();

		// 1 lingkaran
		//ctx.beginPath();
		//ctx.arc(150, 50, 20, 0, 2*Math.PI, false);
		//ctx.stroke();
		circle(150, 50, 20, "Cyan");

		// buatin sr function untuk buat lingkaran, circle(x, y, radius, color)
		//1 Buat drawSnowman(x, y); -> x, y -> titik pusat
		//2 Menggambar dengan mouse : menggunakan jQuery, mouseMove (29), clicks(28) (mirip aplikasi paint)
		//3 Buat game hangman, sudah ada animasi hangman yg digantung

	</script>
</body>
</html>