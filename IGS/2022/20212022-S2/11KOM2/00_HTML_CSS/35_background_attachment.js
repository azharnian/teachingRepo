<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Learning The Difference Between background-attachment value</title>
	<style type="text/css">
		
		div {
			height: 300px;
			width: 60%;
			max-width: 500px;
			margin: 1rem auto;
			overflow-x: hidden;
			overflow-y: scroll;
		}

		.scroll, .fixed, .local {
			background-image: url(moon.png);
		}

		.scroll {
			background-attachment: scroll;
		}

		.fixed {
			background-attachment: fixed;
		}

		.local {
			background-attachment: local;
		}

		.inner {width: 100%; height: 600px; overflow-y: hidden;}

		.addscroller {margin-bottom: 50rem;}

	</style>
</head>
<body>
	<div class="scroll">
		<div class="inner">
			<h1>Scroll</h1>
		</div>
	</div>
	<div class="fixed">
		<div class="inner">
			<h1>Fixed</h1>
		</div>
	</div>
	<div class="local">
		<div class="inner">
			<h1>Local</h1>
		</div>
	</div>
	<p class="addscroller"></p>
</body>
</html>