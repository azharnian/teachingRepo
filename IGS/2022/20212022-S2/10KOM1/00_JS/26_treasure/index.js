<!-- 
1. Ubah gambar peta dengan ukuran yg lebih besar.
2. Ubah pesan yang akan disampaikan saat klik bagian gambar peta
3. Tambahkan limit klik dan diakhir dengan pesan game over melalui alert box jika limit telah habis.
4. Tampilkan sisa limit (boleh digabung dengan id message, boleh juga di element object lain).
5. Deploy ke google script / github pages.
 -->

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Find the buried treasure</title>
</head>
<body>
	<h1>Find the buried treasure</h1>
	<img src="https://cdn.discordapp.com/attachments/896354219261583372/941608946463014933/treasuremap.jpg" style="width: 400px;">
	<p id="message">
		
	</p>
	<!-- Jquery Lib -->
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<!-- end Jquery -->
	<script type="text/javascript">
		console.log(`x : ${$('img').position().left} , y : ${$('img').position().top}`);

		function getRandomNumber(init_position ,size) {
			return Math.floor(Math.random() * size) + Math.ceil(init_position);
		}

		function getDistance(event, target) {
			let dx = event.offsetX - target.x;
			let dy = event.offsetY - target.y;

			return Math.sqrt( (dx*dx) + (dy*dy));
		}

		function getMessage(distance) {
			
			if (distance < 10) {
				return "Terbakar"
			} else if (distance < 20) {
				return "Sangat Panas"
			} else if (distance < 40) {
				return "Panas"
			} else if (distance < 80) {
				return "Hangat"
			} else if (distance < 160) {
				return "Dingin"
			} else if (distance < 320) {
				return "Sangat Dingin"
			} else {
				return "Membeku"
			}

		}

		let width = $('img').width();
		let height = $('img').height();

		console.log(width, height);


		let target = {
			x : getRandomNumber($('img').position().left , width),
			y : getRandomNumber($('img').position().top, height )
		}

		// $("body").append('<h1 id="target" style="color:red;">X</h1>');

		// $("#target").offset({left: target.x, top: target.y});
		console.log(target);
		$('img').click( function (event) {
			let distance = getDistance(event, target);
			let message = getMessage(distance);
			console.log(event.pageX, event.pageY);
			console.log(message);
			console.log(target);
			$('#message').text(message);

			if (distance < 8){
				alert(`Found the treasure!`)
			}
		})







	</script>
</body>
</html>