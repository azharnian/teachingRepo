<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Basic Layout</title>
	<style type="text/css">
		
		body {
			margin: 0;
			padding: 0;
			min-width: 525px;
		}

		header {
			float: left;
			background-color: #7152f4;
			color: white;
			width: 100%;
		}

		footer {
			
			background-color: #cccccc;
			text-align: center;
			font-style: italic;
			width: 100%;
		}

		header > img, header > h1 {
			margin-right: 20px;
			display: inline;
		}

		#main {
			display: table;
		}

		#main-content, #secondary-content, #tertiary-content{
			display: table-cell;
		}


		#main-content {
				

		}

		#secondary-content {
			background-color: #52f471;
			width: 200px;
			

		}

		#tertiary-content {
			background-color: #f452d5;
			width: 125px;
			

		}

	</style>
</head>
<body>
	<header>
		<img src="10_pic.png" width="50px">
		<h1>International Rambang School</h1>
	</header>
	<section id="main">
		<aside id="secondary-content">
			<!-- NAVIGATION -->
			<nav>
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
			</nav>
		</aside>
		
		<article id="main-content">
			<h1>Welcome to International Rambang School</h1>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
				tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
				consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
				cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
				proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
				tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
				consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
				cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
				proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>
		</article>

		

		<aside id="tertiary-content">
			<!-- ADS -->
			<p>
				<strong>SPECIAL PROMO!</strong>
			</p>
			<p>
				Member Get Member ... 
			</p>
		</aside>

	</section>
	<footer>
		Copyright information usually goes here in the footer.
	</footer>
</body>
</html>