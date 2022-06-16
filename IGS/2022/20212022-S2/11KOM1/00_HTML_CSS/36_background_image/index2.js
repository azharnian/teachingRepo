<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Background Image 2</title>
	<style type="text/css">
		.box {
			margin: 0px auto;
			width: 500px;
			height: 500px;
			/*background-color: gray;*/
			background: url('assets/wolf.png') center bottom / 50% no-repeat, /* top -> front */
						black url('assets/moon.png') center top / cover no-repeat;
		}

		.gap {
			margin-bottom: 500px;
		}
	</style>
</head>
<body>
	<div class="box"></div>
	<p class="gap"></p>
</body>
</html>