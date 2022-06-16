<!-- CounterLocalInterval -->
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Local Storage Test</title>
	<script type="text/javascript">

		if (!localStorage.getItem('counter')) localStorage.setItem('counter', 0);

		document.addEventListener("DOMContentLoaded", () => {

			let counter = localStorage.getItem('counter');

			document.querySelector("#counter").innerHTML =  counter;


			function counting() {
				counter++;
				document.querySelector("#counter").innerHTML =  counter;
				localStorage.setItem('counter', counter);

			}

			setInterval(counting, 1000);



		})
	</script>
</head>
<body>
	<h1 id="counter"></h1>
</body>
</html>