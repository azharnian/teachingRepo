<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Change Color</title>
	<script type="text/javascript"> //arrow function
		document.addEventListener('DOMContentLoaded', () => {
			
			document.querySelector('#red').onclick = () => {
				document.querySelector('#hello').style.color = 'red';
			}

			document.querySelector('#green').onclick = () => {
				document.querySelector('#hello').style.color = 'green';
			}

			document.querySelector('#blue').onclick = () => {
				document.querySelector('#hello').style.color = 'blue';
			}
		})
	</script>
</head>
<body>
	<h1 id="hello">Hello...!</h1>
	<button id="red">Red</button>
	<button id="green">Green</button>
	<button id="blue">Blue</button>
</body>
</html>