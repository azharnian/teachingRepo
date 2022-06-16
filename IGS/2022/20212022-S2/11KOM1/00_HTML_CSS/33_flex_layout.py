<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Sample Layout</title>
	<style type="text/css">
		
		body {
			margin: 0;
			padding: 0;
		}

		header {
			float: left;
			width: 100%;
			background-color: #7152f4;
		}

		header > img, header > h1 {
			margin-right: 10px;
			display: inline;
		}

		footer {
			position: relative;
			float: left;
			width: 100%;
			background-color: #cccccc;
			text-align: center;
			font-style: italic;
		}

		#main {
			width: 100%;
			display: flex;
		}

		#secondary-content, #tertiary-content {
			flex-shrink: 0;
		}


		#secondary-content {
			order: -1;
			width: 200px;
			background-color: #52f471;
		}

		#tertiary-content {
			width: 125px;
			background-color: #f452d5;
		}

		#secondary-content ul {
			list-style-type: none;
			margin:12px 0px 0px 12px;
			padding: 0px;
		}

		#secondary-content li a:link, #secondary-content li a:visited {
			font-size: 12pt;
			font-weight: bold;
			padding: 3px 0px 3px 3px;
			color: black;
			text-decoration: none;
			display: block;
		}

		#secondary-content li a:hover, #secondary-content li a:active {
			font-size: 12pt;
			font-weight: bold;
			padding: 3px 0px 3px 3px;
			color: white;
			text-decoration: none;
			display: block;

		}

	</style>
</head>
<body>
	<header>
		<img src="igs.png" alt="Ignatius" width="40px">
		<h1>Welcome to IGS</h1>
	</header>
	<section id="main">
		<article id="main-content">
		<!-- CONTENT -->
		<p>
			Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
			cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
			proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
		</p>
		</article>
		<aside id="secondary-content">
		<!-- LEFT SIDE -->
			<ul>
				<li>
					<a href="#">
						Mission
					</a>
				</li>
				<li>
					<a href="#">
						History
					</a>
				</li>
				<li>
					<a href="#">
						Team
					</a>
				</li>
				<li>
					<a href="#">
						Contact Us
					</a>
				</li>
			</ul>

		</aside>
		<aside id="tertiary-content">
		<!-- RIGHT SIDE -->
			<p>
				<strong>
					SPECIAL PROMO
				</strong>
			</p>
			<p>
				Entrance Test Scholarship up to 100% 36 Months.
			</p>

		</aside>
	</section>
	<footer>
		Copyright information usually goes here in the footer.
	</footer>
</body>
</html>