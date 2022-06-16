<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Interactive and Stop: Alarm</title>
	<script type="text/javascript">

		let statusText;
		let textButton;
		
		let doHomework = () => {

			alert("You need to do your homework!");
		}
		
		let alarm = setTimeout(doHomework, 5000);

		
		let startStopAlarm = () => {

			if (document.querySelector("#status").innerHTML === "On"){
				clearTimeout(alarm);
				statusText = "Off";
				textButton = "Start Alarm";
			} else {
				statusText = "On";
				textButton = "Stop Alarm";
				alarm = setTimeout(doHomework, 5000);
			}
			document.querySelector("#status").innerHTML = statusText;
			document.querySelector("button").innerHTML = textButton;
		}

		
	</script>
</head>
<body>
	<h1>Alarm <span id="status">On</span> </h1>
	<button onclick="startStopAlarm()">Stop Alarm</button>
</body>
</html>