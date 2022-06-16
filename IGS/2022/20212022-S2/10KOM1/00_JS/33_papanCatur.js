<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Basic Changing Color</title>
</head>
<body>
	<canvas width="800" height="800" id="canvas" style="background-color: white;"></canvas>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		const width = canvas.width/8;

		// baris genap col ganjil -> mulai dari hitam-putih-hitam
		// baris genap col genap -> mulai dari putih-hitam-putih

		// baris ganjil col ganjil -> mulai dari putih-hitam-putih
		// baris ganjil col genap - > mulai dari hitam-putih-hitam
		let fill;
		// row = 0;
		for (let row = 0; row < 8; row++){
			for (let col = 0; col < 8; col++){
				/*
				if (row % 2  === 0){
					if (col % 2 === 0){
						fill = "White";
					} else {
						fill = "Black";
					}
				} else {
					if (col % 2 === 0){
						fill = "Black";
					} else {
						fill = "White";
					}
				}
				ctx.fillStyle = fill;
				ctx.fillRect(col*width, row*width, width, width);
				*/
				if ((row + col)%2 !==0 ){
					ctx.fillRect(col*width, row*width, width, width);
				}
			}	
		}
		
		
	</script>
</body>
</html>