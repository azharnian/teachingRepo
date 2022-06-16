<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Change Color with Select Option</title>
	<script type="text/javascript">
		document.addEventListener('DOMContentLoaded', () => {

			// document.querySelector("#color-change").onchange = function () {

			// 	// console.log(this.value);
			// 	document.querySelector("#hello").style.color = this.value;
			// }

			document.querySelector("#color-change").onchange = () => {

				document.querySelector("#hello").style.color = document.querySelector("#color-change").value;

			}

		})
	</script>
</head>
<body>
	<h1 id="hello">Hello...!</h1>
	<select id="color-change">
		<option value="black">Black</option>
		<option value="red">Red</option>
		<option value="green">Green</option>
		<option value="blue">Blue</option>
	</select>
</body>
</html>