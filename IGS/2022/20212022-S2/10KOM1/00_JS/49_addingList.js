<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Adding List</title>
	<script type="text/javascript">

		
		document.addEventListener('DOMContentLoaded', function () {

			document.querySelector("#submit-task").disabled = true;

			document.querySelector("#entry-task").onkeyup = function () {

				if (document.querySelector("#entry-task").value.trim().length > 0){
					document.querySelector("#submit-task").disabled = false;
				} else {
					document.querySelector("#submit-task").disabled = true;
				}
				
			}
			
			document.querySelector("#form-task").onsubmit = function () {

				// console.log(document.querySelector("#entry-task").value);

				const li = document.createElement('li');

				li.innerHTML = document.querySelector("#entry-task").value;


				document.querySelector("#tasks").append(li);

				document.querySelector("#entry-task").value = "";

				document.querySelector("#submit-task").disabled = true;

				return false;


			}

		})

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