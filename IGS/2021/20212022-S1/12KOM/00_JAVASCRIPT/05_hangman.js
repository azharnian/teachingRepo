<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hangman Game</title>
</head>
<body>
	<script type="text/javascript">
		//Buat array untuk kumpulan kata-kata (1 perbanyak words minimal 10 dan pakai lowercase)
		var words = [
		"javascript",
		"monkey",
		"amazing",
		"pancake"
		];


		function pickWord(){
			// return a random word
			return words[Math.floor(Math.random() * words.length)];
		};

		function setupAnswerArray(word){
			// return the answer array
			var returnArray = [];
			for (var i =0; i < word.length; i++){
				returnArray[i] = "_";
				//answerArray.push("_");
			};
			return returnArray;
		};

		function showPlayerProgress(answerArray){
			// use alert
			alert(answerArray.join(" "));
		};

		function getGuess(){
			// use promp
			return prompt("Guess a letter, or click cancel to stop playing."); // (2 lower dan upper , tidak casesensitive)
		};

		function updateGameState(){
			// update answer
			if (guess == null){
				isCancel = true;
			} else if (guess.length !== 1) {
				alert("Please enter a single letter.");
			}  else {
				var isCorrect = false;
				for (var j=0; j < word.length ; j++){
					if( (word[j] === guess.toLowerCase())) {
						answerArray[j] = guess;
						remainingLetters--;
						isCorrect = true;
					};
				};
			};
			if (!isCorrect){
				limit--;
			};

		};

		function showAnswerAndCongrats(answerArray){
			// use alert
			if (isCancel){
				alert("Thank you for playing.")
			} else {
				if (limit === 0){
					alert("Sorry, You Lose ...");
				} else {
					alert("Good Job! the answer was "+ word);
				};
				alert(answerArray.join(" "));
			};
		};


		// ambil random satu kata untuk jadi kunci jawaban
		var word = pickWord()

		// menyiapkan jawaban dari user
		var answerArray = setupAnswerArray(word); //["_", "_", "_", "_", "_", "_"]
		

		var remainingLetters = word.length;
		var limit = 5;
		var isCancel = false;
		while ( remainingLetters > 0 && limit > 0){ // (3 beri batas menebak / limiting guesses dan beri pesan yg sesuai)
			 // join convert item in array become text

			showPlayerProgress(answerArray);

			var guess = getGuess();

			updateGameState();
			if (isCancel){
				break;
			};
			
			// The end of loop
		};

		//Congratulate the player (4 perbaiki bug untuk berhasil dan gagal)
		showAnswerAndCongrats(answerArray);

		
		
		

	</script>
</body>
</html>