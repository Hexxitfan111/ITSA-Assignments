/*								School Comparison Assignment JavaScript Page
							        Created by: Michael Forgione

+--------------------------------------------------------------------------------------------+
|																							|
+--------------------------------------------------------------------------------------------+

*/

start_box_1 = 1; //Starting value for box 1
start_box_2 = 2; //Starting value for box 2


//---------------------------------------------------
function load_dat(a) {
	switch (a) {
		case 1:
			data_hog = new XMLHttpRequest();
			data_hog.open("GET", "https://cors-anywhere.herokuapp.com/http://github.com/Hexxitfan111/ITSA-Assignments/blob/master/Assignments/hogwarts_data.html", true);
			data_hog.onreadystatechange = function() {
			if (data_hog.readyState === 4) {  // Makes sure the document is ready to parse.
				if (data_hog.status === 200) {  // Makes sure it's found the file.
					//lines = data_hog.responseText.split("\n"); // Will separate each line into an array
					//var customTextElement = document.getElementById('textHolder');
					return data_hog.responseText;
					}
				}
			}
			data_hog.send(null);
			break;
			
		case 2:
			//------------------------------------------------------
			data_win = new XMLHttpRequest();
			data_win.open("GET", "https://cors-anywhere.herokuapp.com/http://github.com/Hexxitfan111/ITSA-Assignments/blob/master/Assignments/winterhold_data.html", true);
			data_win.onreadystatechange = function() {
				if (data_win.readyState === 4) {  // Makes sure the document is ready to parse.
					if (data_win.status === 200) {  // Makes sure it's found the file.
					//lines = data_win.responseText.split("\n"); // Will separate each line into an array
					//var customTextElement = document.getElementById('textHolder');
					return data_win.responseText;
				}
			}
			}
			data_win.send(null);
			break;
	//--------------------------------------------------------
	}
}
data_dur = "";
data_arc = "";
data_cas = "";


function switch_box(box_number) {
	// 'a' should be equal to 1, 2, 3, 4, or 5.
	sel_box_1 = document.getElementById("frame_1_select"); //Variable for easier later assignmentof data to box 1
	sel_box_2 = document.getElementById("frame_2_select"); //Variable for easier later assignmentof data to box 2
	frame_main_1 = document.getElementById("frame_main_1");
	frame_main_2 = document.getElementById("frame_main_2");
	switch (box_number) {
		case 1:
			switch (sel_box_1.value) {
				case 1:
					frame_main_1.innerHTML = load_dat(1);
					return;
				case 2:
					frame_main_1.innerHTML = load_dat(2);
					return;
				case 3:
					return;
				case 4:
					return;
				case 5:
					return;
			}
		case 2:
		  switch (sel_box_2.value) {
				case 1:
					return;
				case 2:
					return;
				case 3:
					return;
				case 4:
					return;
				case 5:
					return;
	}
}
}