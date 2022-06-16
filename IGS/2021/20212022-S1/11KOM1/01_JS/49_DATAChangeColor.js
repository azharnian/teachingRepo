<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Change Color with data-*</title>
	<script type="text/javascript">
		document.addEventListener('DOMContentLoaded', () => {

			document.querySelectorAll(".color-change").forEach( button => {
					console.log(button);
					button.onclick = () => {
						document.querySelector('#hello').style.color = button.dataset.color;
					}

				}
			)

		})
	</script>
</head>
<body>
	<h1 id="hello">Hello...!</h1>
	<button class="color-change" data-color="red">Red</button>
	<button class="color-change" data-color="green">Green</button>
	<button class="color-change" data-color="blue">Blue</button>
</body>
</html>