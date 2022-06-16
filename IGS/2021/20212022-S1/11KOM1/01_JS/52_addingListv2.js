<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>ADDING LIST</title>
	<script type="text/javascript">
		document.addEventListener('DOMContentLoaded', () => {

			document.querySelector("#submit-task").disabled = true;

			document.querySelector("#entry-task").onkeyup = () =>{

				if (document.querySelector("#entry-task").value.length > 0){

					document.querySelector("#submit-task").disabled = false;
				} else {

					document.querySelector("#submit-task").disabled = true;
				}
				
			}

			document.querySelector("#form-task").onsubmit = () =>{

				// const task = document.querySelector("#task").value;

				const li = document.createElement('li');
				li.innerHTML = document.querySelector("#entry-task").value;

				document.querySelector("#tasks").append(li);

				document.querySelector("#entry-task").value = "";
				document.querySelector("#submit-task").disabled =true;

				return false;
			}

		})
	</script>
</head>
<body>
	<h1>Tasks :</h1>
	<form id="form-task">
		<input type="text" id="entry-task" autocomplete="off" placeholder="New Task">
		<input type="submit" id="submit-task">
	</form>
	<ul id="tasks"> <!-- unordered list  , ol ordered list-->
		
	</ul>
</body>
</html>