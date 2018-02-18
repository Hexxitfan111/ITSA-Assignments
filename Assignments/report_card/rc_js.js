//Javascript



function data_evaluate() {
	document.getElementById("title").innerHTML = '';
	document.getElementById("img").innerHTML = '';
	document.getElementById("grade_table").innerHTML = '';
	document.getElementById("id_number").innerHTML = '';
	choice = document.getElementById("student_select");
	main = document.getElementById("wrapper_main");
	switch (choice.value) {
		case 0:
			main.innerHTML = '';
			break;
		default:
			data_parse((choice.value-1));
			break;
	}
}

function data_parse(num) {
	title = document.getElementById("title");
	avatar = document.getElementById("img");
	grade_table = document.getElementById("grade_table");
	id_number = document.getElementById("id_number");
	
	//title text elements
	title.innerHTML = students[num]["lastName"]+", "+students[num]["firstName"] +". " + "<br>" + students[num]["streetAddress"] + ". " + "<br>" + students[num]["city"] + ", " + students[num]["state"] + ", " + students[num]["zipCode"];
	
	
	/*title_text_l1 = document.createTextNode(students[num]["lastName"]+", "+students[num]["firstName"] +". ");
	title_text_l2 = document.createTextNode(students[num]["streetAddress"] + ". ");
	title_text_l3 = document.createTextNode(students[num]["city"] + ", " + students[num]["state"] + ", " + students[num]["zipCode"]);
	title_text_l1.id = "tl1";
	title_text_l2.id = "tl2";
	title_text_l3.id = "tl3";
	title.appendChild(title_text_l1);
	title.appendChild(title_text_l2);
	title.appendChild(title_text_l3);*/
	
	//avatar images
	avatar_link = document.createElement("img");
	avatar_link.src = students[num]["avatar"];
	avatar_link.id = "avatar_pic";
	avatar.appendChild(avatar_link);
	
	//jump over to the table spawning function
	grade_table.appendChild(create_table(num));
	
	//add the id number field
	id_number_text = document.createTextNode(students[num]["idNumber"]);
	id_number.appendChild(id_number_text);
}

function create_table(num) {
	table = document.createElement("table");
	thead = document.createElement("thead");
	tbody = document.createElement("tbody");
	head_row = document.createElement("tr");
	["Course","Instructor","Term 1", "Term 2", "Term 3", "Term 4", "Average"].forEach(function(el) {
		var th=document.createElement("th");
		th.appendChild(document.createTextNode(el));
		head_row.appendChild(th);
		});
	thead.appendChild(head_row);
    table.appendChild(thead);
	tick = 0
	students[num]["courses"][0]["termGrades"].push(Math.floor((students[num]["courses"][0]["termGrades"][0]+students[num]["courses"][0]["termGrades"][1]+students[num]["courses"][0]["termGrades"][2]+students[num]["courses"][0]["termGrades"][3])/4));
	students[num]["courses"][1]["termGrades"].push(Math.floor((students[num]["courses"][1]["termGrades"][0]+students[num]["courses"][1]["termGrades"][1]+students[num]["courses"][1]["termGrades"][2]+students[num]["courses"][1]["termGrades"][3])/4));
	students[num]["courses"][2]["termGrades"].push(Math.floor((students[num]["courses"][2]["termGrades"][0]+students[num]["courses"][2]["termGrades"][1]+students[num]["courses"][2]["termGrades"][2]+students[num]["courses"][2]["termGrades"][3])/4));
	while (tick < 3) {
		var tr = document.createElement("tr");
			var td = document.createElement("td");
			td.appendChild(document.createTextNode(students[num]["courses"][tick]["courseName"]));
			tr.appendChild(td);
			var td = document.createElement("td");
			td.appendChild(document.createTextNode(students[num]["courses"][tick]["instructor"]));
			tr.appendChild(td);
		for (var a in students[num]["courses"][tick]["termGrades"]) {  
			var td = document.createElement("td");
			td.appendChild(document.createTextNode(students[num]["courses"][tick]["termGrades"][a]));
			tr.appendChild(td);
			}
			
		tbody.appendChild(tr);
		tick ++;
		}
	    table.appendChild(tbody);             
    return table;
}
