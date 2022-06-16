<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Click Handler</title>
</head>
<body>
	<h1>Hello World!</h1>
	<!-- Jquery Lib -->
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<!-- end Jquery -->
	<script type="text/javascript">
		
		function handler(event) {
			console.log(`I'm Clicked at${event.pageX}, ${event.pageY}.`);
			$("h1").offset({left : event.pageX, top : event.pageY});
		}

		// $('html').click(function (event) {
		// 	console.log(`I'm Clicked at${event.pageX}, ${event.pageY}.`)
		// })

		$('html').click(handler);		
	</script>
</body>
</html>