function change() {
    var x = Math.random() * 255;
    var y = Math.random() * 255;
    var z = Math.random() * 255;
    var a = Math.random() * 1;
    document.body.style.background="rgb("+x+","+y+","+z+","+a+")";
}