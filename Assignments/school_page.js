/*								School Comparison Assignment JavaScript Page
							        Created by: Michael Forgione

+--------------------------------------------------------------------------------------------+
|																							|
+--------------------------------------------------------------------------------------------+

*/
sel_box_1 = document.getElementById("frame_1_select"); //Variable for easier later assignmentof data to box 1
sel_box_2 = document.getElementById("frame_2_select"); //Variable for easier later assignmentof data to box 2
start_box_1 = 1; //Starting value for box 1
start_box_2 = 2; //Starting value for box 2


//---------------------------------------------------
data_hog = new XMLHttpRequest();
data_hog.open("GET", "hogwarts_data.html", true);
data_hog.onreadystatechange = function() {
  if (data_hog.readyState === 4) {  // Makes sure the document is ready to parse.
    if (data_hog.status === 200) {  // Makes sure it's found the file.
      allText = data_hog.responseText; 
      //lines = data_hog.responseText.split("\n"); // Will separate each line into an array
      var customTextElement = document.getElementById('textHolder');
customTextElement.innerHTML = data_hog.responseText;
    }
  }
}
data_hog.send(null);
//------------------------------------------------------
data_win = new XMLHttpRequest();
data_win.open("GET", "winterhold_data.html", true);
data_win.onreadystatechange = function() {
  if (data_win.readyState === 4) {  // Makes sure the document is ready to parse.
    if (data_win.status === 200) {  // Makes sure it's found the file.
      allText = data_win.responseText; 
      //lines = data_win.responseText.split("\n"); // Will separate each line into an array
      var customTextElement = document.getElementById('textHolder');
customTextElement.innerHTML = data_win.responseText;
    }
  }
}
data_win.send(null);
//--------------------------------------------------------
data_dur =
data_arc =
data_cas =


function switch_box(box_number) {
	// 'a' should be equal to 1, 2, 3, 4, or 5.
	switch (box_number) {
		case 1:
			switch (sel_box_1.value) {
				case 1:
					frame_main_1.innerHTML = hogwarts_data;
					return;
				case 2:
					frame_main_1.innerHTML = winterhold_data;
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