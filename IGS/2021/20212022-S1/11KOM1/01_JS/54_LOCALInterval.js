<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>LocalStorage</title>
	<script type="text/javascript">
		
		if (!localStorage.getItem('counter')) localStorage.setItem('counter', 0);


		document.addEventListener('DOMContentLoaded', () => {

			let counter = localStorage.getItem('counter');

			document.querySelector("#counter").innerHTML = counter;

			setInterval( () => {
				counter++;
				document.querySelector("#counter").innerHTML = counter;
				localStorage.setItem('counter', counter);
			}, 1000);

			// document.querySelector("button").onclick = () => {

			// 	let counter = localStorage.getItem('counter');

			// 	counter++;
			// 	document.querySelector("#counter").innerHTML = counter;
			// 	localStorage.setItem('counter', counter);

			// }

		})
	</script>
</head>
<body>
	<h1 id="counter"></h1>
	<!-- <button>Click Here!</button> -->
</body>
</html>