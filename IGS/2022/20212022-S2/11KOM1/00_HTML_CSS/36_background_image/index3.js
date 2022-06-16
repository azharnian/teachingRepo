<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Background Attachment</title>
	<style type="text/css">
		div {
			margin: 10px auto;

			height: 600px;
			width: 60%;

			max-width: 500px;

			/*background-color: gray;*/

			overflow-x: hidden;
			overflow-y: scroll;
		}

		.inner {
			width: 100%;
			height: 600px;
			overflow-y: hidden;
		}

		.gap {
			margin-bottom: 50rem;
		}

		.scroll, .fixed, .local {
			background-image: url('assets/moon.png');
		}

		.scroll{ background-attachment: scroll; }

		.fixed{ background-attachment: fixed; }

		.local{ background-attachment: local; }


		
	</style>
</head>
<body>
	<div class="scroll">
		<div class="inner"><h1>Scroll</h1></div>
	</div>
	<div class="fixed">
		<div class="inner"><h1>Fixed</h1></div>
	</div>
	<div class="local">
		<div class="inner"><h1>Local</h1></div>
	</div>

	<p class="gap"></p>
</body>
</html>