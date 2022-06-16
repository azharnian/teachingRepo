<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Offset</title>
</head>
<body>
	<h1 id="heading">Hello World!</h1>
	<!-- Jquery Lib -->
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<!-- end Jquery -->
	<script type="text/javascript">
		// $('#heading').offset({left : 200}); // x axis from left to right
		// $('#heading').offset({top : 500}); // y axis from top to bottom
		// $('#heading').offset({left : 200, top : 500});

		let xPos = 0;

		let move = () => {
			$('#heading').offset({left : xPos});
			xPos++;

			if (xPos > 600){
				xPos = 0;
			}
		}

		let stopAnimating = () => {
			clearInterval(mainloop);
		}

		let mainloop = setInterval(move, 3);
	</script>
	<button onclick="stopAnimating()">STOP !</button>

</body>
</html>