<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Sample Link Style</title>
	<style type="text/css">
		a, li{
			font-family: Verdana, sans-serif;
			font-weight: bold;
			text-decoration: none;
		}
		/*a hyperlink that has not been visited previously*/
		a:link {
			color: lightblue;
		}
		/*a hyperlink that has been visited previously and is present in browser memory*/
		a:visited {
			color: #cccccc;
		}
		/*a hyperlink as a user's mouse hovers over it(and before it has been clicked)*/
		a:hover {
			color: #d42424;
		}

		/*a hyperlink as the user active the link. This is often used on device where there is no mouse (clicking is not possible) */
		a:focus {
			color: black;
		}

		/*a hyperlink that is in the act of being clicked but has not yet been release*/
		a:active {
			color: green;
		}

		/*selector.class: pseudo-class*/
		a.footerlink:hover {
			color: lightsalmon;
		}
	</style>
</head>
<body>
	<h1>
		Sample link style
	</h1>
	<ol>
		<li>
			<a href="https://www.google.com" target="_blank">The fisrt time you see me, I should be a light blue, bold, non-underlined link in the Verdana font.</a>
		</li>
		<li>
			<a href="#">The fisrt time you see me, I should be a light blue, bold, non-underlined link in the Verdana font.</a>
		</li>
	</ol>
	<footer>
		<p>
			Contact Us : <a href="#" class="footerlink">anas.sty@gmail.com</a>
		</p>
	</footer>
</body>
</html>