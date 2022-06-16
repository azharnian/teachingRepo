<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Background Attachment</title>
	<style type="text/css">

		div {
			height: 600px;
			width: 60%;
			max-width: 500px;
			margin: 1rem auto;

			overflow-x: hidden;
			overflow-y: scroll;
		}

		.scroll, .local, .fixed {
			background-image: url('assets/moon.png');
			background-size: cover;
		}

		.scroll {
			background-attachment: scroll;
		}

		.local {
			background-attachment: local;
		}

		.fixed {
			background-attachment: fixed;
		}
		
	</style>
</head>
<body>
	<div class="scroll">
		<div class="inner"><h1>Scroll</h1></div>
	</div>
	<div class="local">
		<div class="inner"><h1>Local</h1></div>
	</div>
	<div class="fixed">
		<div class="inner"><h1>Fixed</h1></div>
	</div>

	<div class="gap"></div>
</body>
</html>