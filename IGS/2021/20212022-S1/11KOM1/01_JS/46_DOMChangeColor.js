<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Change Color</title>
	<script type="text/javascript">
		document.addEventListener('DOMContentLoaded', function () {
			
			document.querySelector('#red').onclick = function () {
				document.querySelector('#hello').style.color = 'red';
			}

			document.querySelector('#green').onclick = function () {
				document.querySelector('#hello').style.color = 'green';
			}

			document.querySelector('#blue').onclick = function () {
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