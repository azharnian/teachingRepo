<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{% block title %}{% endblock %}</title>
</head>
<body>
	<header>
		<nav>
			<p>This is Navigation</p>
		</nav>
	</header>
	<section id="main-section">
		{% block main %}

		{% endblock main %}
	</section>
	<footer>
		<p>Here you see footer!</p>
		<a href="{{ url_for('index') }}">Back home!</a>
	</footer>

</body>
</html>