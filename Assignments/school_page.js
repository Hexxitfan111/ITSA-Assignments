/*								School Comparison Assignment JavaScript Page
							        Created by: Michael Forgione

+--------------------------------------------------------------------------------------------+
|																							|
+--------------------------------------------------------------------------------------------+

*/

start_box_1 = 1; //Starting value for box 1
start_box_2 = 2; //Starting value for box 2


//---------------------------------------------------

import 'school_page_data'

function init() {
init_1 = document.getElementById("frame_main_1")
init_2 = document.getElementById("frame_main_2")
init_2.innerHTML = school_page_data.data_hog;
init_1.innerHTML = school_page_data.data_win;
}


function switch_box_1() {
	// 'a' should be equal to 1, 2, 3, 4, or 5.
	//sel_box_1 = document.getElementById("frame_1_select"); //Variable for easier later assignment of data to box 1
	//sel_box_2 = document.getElementById("frame_2_select"); //Variable for easier later assignment of data to box 2
	frame_main_1 = document.getElementById("frame_main_1");
	frame_main_2 = document.getElementById("frame_main_2");
	//frame_main_1.innerHTML = data_hog;
	alert('box 1')
	switch (document.getElementById("frame_1_select").value) {
		case '1':
			alert('1')
			frame_main_1.innerHTML = data_win;
			return;
		case '2':
			alert('2')
			frame_main_1.innerHTML = data_hog;
			return;
		case '3':
			alert('3');
			return;
		case '4':
			alert('4');
			return;
		case '5':
		alert('5')
			return;
	}
}
function switch_box_2() {
	// 'a' should be equal to 1, 2, 3, 4, or 5.
	//sel_box_1 = document.getElementById("frame_1_select"); //Variable for easier later assignment of data to box 1
	//sel_box_2 = document.getElementById("frame_2_select"); //Variable for easier later assignment of data to box 2
	frame_main_1 = document.getElementById("frame_main_1");
	frame_main_2 = document.getElementById("frame_main_2");
	//frame_main_1.innerHTML = data_hog;
	alert('box 2')
	switch (document.getElementById("frame_2_select").value) {
		case '1':
			alert('1')
			frame_main_2.innerHTML = data_win;
			return;
		case '2':
			alert('2')
			frame_main_2.innerHTML = data_hog;
			return;
		case '3':
			alert('3');
			return;
		case '4':
			alert('4');
			return;
		case '5':
			alert('5')
			return;
	}
}

