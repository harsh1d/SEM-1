function make() {
    const para = document.createElement("span"); //creating a temp element
    var x = document.getElementById("input").value; //taking the value of the user for to-do list

    const node = document.createTextNode(x);   //5-9 are basically to put the value in the html and to show it
    para.appendChild(node);
    const element = document.getElementById("num");
    const buttom_list = document.getElementById("res");
    element.insertBefore(para, buttom_list);
 
    const button = document.createElement("button");
    element.insertBefore(button, buttom_list);
    const button2 = document.createElement("button"); //11-16 are justing creating  buttons and give em style
    element.insertBefore(button2, buttom_list);
    button.className = "input";
    button2.className = "input";

    const num = document.createTextNode("completed");
    button.appendChild(num);
    document.createElement("span");  //18-22 are basicaly adding name inside the button
    const num2 = document.createTextNode("delete");
    button2.appendChild(num2);

    const hr = document.createElement("hr");
    element.insertBefore(hr, buttom_list); // made a hr for just a lil speration
    hr.className = "hr";


    button.onclick = function complitated() {
        para.style.textDecorationLine = "line-through";  //showing itz done 
    }
    button2.onclick = function remove() {
        para.remove();
        button.remove(); //removing the elements or the list
        button2.remove();
        hr.remove();
    }
}