<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>SessionStorage</title>
	<script type="text/javascript">
		
		if (!sessionStorage.getItem('counter')) sessionStorage.setItem('counter', 0);


		document.addEventListener('DOMContentLoaded', () => {

			// setInterval( () => {
			// 	counter++;
			// 	document.querySelector("#counter").innerHTML = counter;
			// 	localStorage.setItem('counter', counter);
			// }, 1000);

			document.querySelector("#counter").innerHTML = sessionStorage.getItem('counter');

			document.querySelector("button").onclick = () => {

				let counter = sessionStorage.getItem('counter');

				counter++;
				document.querySelector("#counter").innerHTML = counter;
				sessionStorage.setItem('counter', counter);

			}

		})
	</script>
</head>
<body>
	<h1 id="counter"></h1>
	<button>Click Here!</button>
</body>
</html>