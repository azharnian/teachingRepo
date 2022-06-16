<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Animating with Jquery</title>
	<!-- Jquery Lib -->
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<!-- end Jquery -->
	<script type="text/javascript">

		let changeText = () => {
			$("h1").text("I Love You 3000");
		}

		let action = () => {
			$("h1").fadeOut(3000);
			setTimeout(changeText, 3000);
			$("h1").fadeIn(3000);
		}
		
	</script>
</head>
<body>
	<h1>Javascript is Awesome!</h1>
	<button onclick="action()">Click Me!</button>

	<!-- <script type="text/javascript">
		$("h1").fadeOut(3000); // 3000ms -> 3 s
		$("h1").fadeIn(3000);
		$("h1").slideUp(2000);
		$("h1").slideDown(2000);
	</script> -->

</body>
</html>