{% extends "layout.html" %}

{% block title %}
	Form
{% endblock title %}

{% block main %}

{% if err_msg %}
	<p style="color: red;">{{ err_msg }}</p>
{% endif %}

<h1>Submit your name!</h1>

<form action="{{ url_for('hello') }}" method="post">
	<input type="text" name="name" placeholder="Enter your name">
	<button>Submit</button>
</form>

{% endblock main %}