<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Loop</title>
</head>
<body>
	<h1>Names</h1>
	<ul>
		{% for name in names %}
			<li>{{ name }}</li>
		{% endfor %}
	</ul>
	<!-- <a href="http://127.0.0.1:5000/more">More ...</a> -->
	<!-- <a href="templates/more.html">More ...</a> -->
	<a href="{{ url_for('more') }}">More ...</a>
</body>
</html>