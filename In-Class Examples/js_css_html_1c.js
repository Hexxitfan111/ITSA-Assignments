//javascript

function create_box() {
	var textBox = document.createElement("input");
	textBox.setAttribute("value", "1");
	textBox.className = "Numeric";
	document.getElementById("textBoxes").appendChild(textBox);
	
}

function add() {
	boxes = Array.from(document.getElementsByClassName('Numeric'));
	a = 0;
	for (i=0; i<boxes.length; i++) {
		a += parseInt(boxes[i].value);
	}
	alert(a);
}