/*								School Comparison Assignment JavaScript Page
							        Created by: Michael Forgione

+--------------------------------------------------------------------------------------------+
|																							|
+--------------------------------------------------------------------------------------------+

*/

start_box_1 = 1; //Starting value for box 1
start_box_2 = 2; //Starting value for box 2


//---------------------------------------------------

data_hog = new XMLHttpRequest();
data_hog.open('GET', 'https://cors-anywhere.herokuapp.com/http://github.com/Hexxitfan111/ITSA-Assignments/blob/master/Assignments/hogwarts_data.html');
data_hog.onload = function() {
    if (data_hog.status === 200) {
        alert(data_hog.responseText);
    }
    else {
        alert('Request failed.  Returned status of ' + data_hog.status);
    }
};
data_hog.send();
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