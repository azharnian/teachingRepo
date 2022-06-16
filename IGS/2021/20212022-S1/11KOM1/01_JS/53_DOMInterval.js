<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Interval with DOM</title>
	<script type="text/javascript">
		let counter = 0;
		document.addEventListener('DOMContentLoaded', () => {

			setInterval( () => {
				counter++;
				document.querySelector("#counter").innerHTML = counter;
			}, 1000);

		})
	</script>
</head>
<body>
	<h1 id="counter">0</h1>
</body>
</html>