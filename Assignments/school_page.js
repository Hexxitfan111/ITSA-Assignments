/*								School Comparison Assignment JavaScript Page
							        Created by: Michael Forgione

+--------------------------------------------------------------------------------------------+
|																							|
+--------------------------------------------------------------------------------------------+

*/




//---------------------------------------------------
function includeJs(jsFilePath) {
    var js = document.createElement("script");

    js.type = "text/javascript";
    js.src = jsFilePath;

    document.head.appendChild(js);
}

includeJs("school_page_data.js");

function init() {
init_1 = document.getElementById("frame_main_1")
init_2 = document.getElementById("frame_main_2")
init_2.innerHTML = data_hog;
init_1.innerHTML = data_win;
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
			frame_main_1.innerHTML = data_dur;
			return;
		case '4':
			alert('4');
			frame_main_1.innerHTML = data_arc;
			return;
		case '5':
		alert('5')
			frame_main_1.innerHTML = data_cas;
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

