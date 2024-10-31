function add() {
    var n1 = parseInt(document.getElementById('n1').value);
    var n2 = parseInt(document.getElementById('n2').value);
    var sum = n1 + n2;
    document.getElementById('hide').innerHTML = "Result's are: "+sum;
}