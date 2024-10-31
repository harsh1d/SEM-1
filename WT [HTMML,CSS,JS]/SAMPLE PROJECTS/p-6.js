function gen() {
    let num = Math.floor(Math.random() * 100 +1);
    let userGuess = parseInt(document.getElementById('input').value);
    if (userGuess == num) {
        document.getElementById('res').innerHTML="Congratulations! You guessed the number!";
    } else if (userGuess < num) {
        document.getElementById('res').innerHTML="Too low, try again.";
    } else if (userGuess > num) {
        document.getElementById('res').innerHTML="Too high, try again.";
    }
    
}