<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Adding List</title>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script type="text/javascript">
	
		$(document).ready( () => {

			$("#submit-task").attr('disabled', true);

			$("#entry-task").keyup = () => {

				
				
			}

		});
		

	</script>
</head>
<body>
	<h1>Tugas Hari Ini : </h1>
	<ul id="tasks"></ul>
	<form id="form-task">
		<input type="text" name="" id="entry-task" placeholder="Masukkan Tugas Baru Hari Ini" autocomplete="off">
		<input type="submit" name="" id="submit-task">
	</form>
</body>
</html>