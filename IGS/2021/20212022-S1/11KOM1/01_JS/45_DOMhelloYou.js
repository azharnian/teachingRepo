<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>DOM Click</title>
	<script type="text/javascript">
		document.addEventListener('DOMContentLoaded', function () {

			document.querySelector('#form').onsubmit = function () {
				const name = document.querySelector('#name').value;
				alert(`Hello ... ${name}`);
			}


		});
	</script>
</head>
<body>
	<form id="form">
		<input id="name" type="text" autocomplete="off" placeholder="Your Name">
		<input type="submit">
	</form>
</body>
</html>