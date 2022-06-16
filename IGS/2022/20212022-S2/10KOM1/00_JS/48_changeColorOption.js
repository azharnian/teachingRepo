<!-- 
LIMITATION ARROW FUNCTION
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
 -->
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Change Color</title>
	<script type="text/javascript">
		document.addEventListener('DOMContentLoaded', () =>{

			// document.querySelector("#color-change").onchange = () => {
			// 	document.querySelector("#header").style.color = document.querySelector("#color-change").value;
			// }

			document.querySelector("#color-change").onchange = function () {
				document.querySelector("#header").style.color = this.value;
			}			


		})
	</script>
</head>
<body>
	<h1 id="header">Helloo ...!</h1>
	<select id="color-change">
		<option value="black">Black</option>
		<option value="red">Red</option>
		<option value="green">Green</option>
		<option value="blue">Blue</option>
	</select>

</body>
</html>