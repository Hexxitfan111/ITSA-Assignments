// JavaScript

die1=new die("ndie1", 0);
die2=new die("ndie2", 1);
die3=new die("ndie3", 2);
die4=new die("ndie4", 3);
die5=new die("ndie5", 4);

dice_set=[die1, die2, die3, die4, die5];
function new_game() {
	window.location.reload();
}

function init() {
	table_load();
	document.getElementById("dice_cup").src = "https://i.imgur.com/OOhb34l.png";
	document.getElementById("new_game_butt").innerHTML = "New Game";
	document.getElementById("player_name").innerHTML = ("Player Name: " + yahtzee.player.name);
	document.getElementById("player_avatar").src = yahtzee.player.avatar;
	//Dice
	for (i=0; i<5; i++) {
		dice_set[i].render();
	}
	update();
}
function die(id_num, inc) {
	this.held = false;
	this.init = false;
	this.value = "";
	this.sprite = "";
	this.id = id_num;
	this.side = ["",
		"http://www.clker.com/cliparts/m/v/m/J/4/V/dice-1-md.png", 
		"http://laoblogger.com/images/2-dice-clipart-7.jpg",
		"http://www.clker.com/cliparts/M/e/P/O/L/b/dice-3-md.png", 
		"http://www.clker.com/cliparts/r/z/d/a/L/V/dice-4-hi.png", 
		"http://moziru.com/images/five-clipart-dot-8.png", 
		"http://www.clker.com/cliparts/l/6/4/3/K/H/dice-6-hi.png"
	],
	this.render = function render() {
		d_area = document.getElementById("dice_area");
		if (!this.init) {
			d_image = document.createElement("img");
			this.roll();
			d_image.src = this.sprite;
			d_image.id = id_num;
			d_image.className = "die_sprite";
			d_image.addEventListener("click", this.hold.bind(this));
			d_area = d_area.appendChild(d_image);
			yahtzee.throws_left = 2;
			this.init = true;
		} else {
			d_image = document.createElement("img");
			this.roll();
			d_image.src = this.sprite;
			d_image.id = id_num;
			d_image.className = "die_sprite";
			d_image.addEventListener("click", this.hold.bind(this));
			d_area = d_area.appendChild(d_image);
			if (this.held == true) {
				d_image.style.border = "5px solid red";
			} else if (this.held == false) {
				d_image.style = ""
			}
		}
	},
	this.hold = function hold() {
		d_image = document.getElementById(this.id);
		//alert("fire")
		if (this.held == true) {
			//alert("true");
			this.held = false;
			d_image.style = ""
		} else if (this.held == false) {
			//alert("false");
			this.held = true;
			d_image.style.border = "5px solid red";
		}
	},
	this.roll = function roll() {
		if (this.held == false) {
			this.value = (Math.floor(Math.random() * 6)+1);
			this.sprite = this.side[this.value];
		}
		return this.value, this.sprite;
	}
}
function update() {
	if (yahtzee.throws_left == 2 && yahtzee.turns_left == 13) {
		document.getElementById("click_instruct").innerHTML = "&lt;------- Click me to roll the dice!<br><br>Click the red boxes to the right to score a turn!  ---------&gt;";
	} else {
		document.getElementById("click_instruct").innerHTML = "";
	}
	document.getElementById("turns_left").innerHTML = "Turns Remaining: " + yahtzee.turns_left;
	document.getElementById("throws_left").innerHTML = "Throws Remaining: " + yahtzee.throws_left;
}
function newturn() {
	if (yahtzee.turns_left > 0); {
		for (i=0; i<5; i++) {
			dice_set[i].held=false;
		}
		yahtzee.throws_left=3;
		yahtzee.turns_left -= 1;
		if (yahtzee.turns_left == 0) {
			yahtzee.turns_left = 0;
			yahtzee.throws_left = 0;
			update();
			alert("Game Over! Press New Game to play again!");
		} else {
			roll_dice();
		}
	}
	
}
function table_load() {
	yahtzee.scorecard.sub_proc()
	for (i=0; i<yahtzee.scorecard.score_types.length; i++) {
		document.getElementById(yahtzee.scorecard.score_ids[i]).innerHTML = yahtzee.scorecard.score_types[i];
	}
	for (i=0; i<yahtzee.scorecard.score_values.length; i++) {
		document.getElementById(yahtzee.scorecard.score_value_ids[i]).innerHTML = yahtzee.scorecard.score_values[i];
		if ((yahtzee.scorecard.score_values[i] == "") && (i !=6) && (i != 14) && (i != 15)) {
			document.getElementById(yahtzee.scorecard.score_value_ids[i]).className = "pickable";
			document.getElementById(yahtzee.scorecard.score_value_ids[i]).addEventListener("click", score, true);
		}  else {
			document.getElementById(yahtzee.scorecard.score_value_ids[i]).className = "grid_item";
		}
	}
}
function arr_filt(input, target) {
	return input.filter(function(a){return (a == target)})
}
function arr_filt_am(input, num_matches) {
	
	switch (num_matches) {
		case 3:
			a = input.filter(function(x){return (x==input[0])});
			if (a.length >= 3) {
				return true;
			}
			b = input.filter(function(x){return (x==input[1])});
			if (b.length >= 3) {
				return true;
			}
			c = input.filter(function(x){return (x==input[2])});
			if (c.length >= 3) {
				return true;
			}
			return false;
		case 4:
			e = input.filter(function(x){return (x==input[0])});
			if (e.length >= 4) {
				return true;
			}
			f = input.filter(function(x){return (x==input[1])});
			if (f.length >= 4) {
				return true;
			}
			return false;
		case 5:
			g = input.filter(function(x){return (x==input[0])});
			if (g.length == 5) {
				return true;
			}
			return false;
	}
}
function arr_filt_fh(input) {
	input.sort(function(a, b){return a - b});
	if (input.filter(function(x){return (x==input[0])}).length == 3) {
		if (input.filter(function(x){return (x==input[3])}).length == 2) {
			return true;
		}
	} else if (input.filter(function(x){return (x==input[0])}).length == 2) {
		if (input.filter(function(x){return (x==input[3])}).length == 3) {
			return true;
		}
	}
}
function arr_filt_st(input, num) {
	input.sort(function(a, b){return a - b});
	
	switch(num) {
		case 1:
			for (i=0; i<3; i++) {
				if ((input[i] + 1) == input[i+1] && (input[i+1] + 1) == input[i+2] && (input[i+2] + 1) == input[i+3]) {
					return true;
				}
			}
			break;
		case 2:
			for (i=0; i<2; i++) {
				if ((input[i] + 1) == input[i+1] && (input[i+1] + 1) == input[i+2] && (input[i+2] + 1) == input[i+3] && (input[i+3] + 1) == input[i+4]){
					return true;
				}
			}
	}
}

function score() {
	a = document.getElementsByClassName("pickable");
	
	this.removeEventListener("click",score,true);
	this.className = "grid_item";

	
	id_dat = this.id;
	
	sc = [];
	for(i=0; i<5; i++) {
		sc.push(dice_set[i].value)
	}
	sc.sort(function(a, b){return a - b})
	
	switch(id_dat) {
		case "1sc":
			sum = 0;
			op = arr_filt(sc, 1);
			for (i=0; i<op.length; i++) {
				sum += op[i];
			};
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[0] = sum;
			break;
		case "2sc":
			sum = 0;
			op = arr_filt(sc, 2);
			for (i=0; i<op.length; i++) {
				sum += op[i];
			};
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[1] = sum;
			break;
		case "3sc":
			sum = 0;
			op = arr_filt(sc, 3);
			for (i=0; i<op.length; i++) {
				sum += op[i];
			};
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[2] = sum;
			break;
		case "4sc":
			sum = 0;
			op = arr_filt(sc, 4);
			for (i=0; i<op.length; i++) {
				sum += op[i];
			};
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[3] = sum;
			break;
		case "5sc":
			sum = 0;
			op = arr_filt(sc, 5);
			for (i=0; i<op.length; i++) {
				sum += op[i];
			};
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[4] = sum;
			break;
		case "6sc":
			sum = 0;
			op = arr_filt(sc, 6);
			for (i=0; i<op.length; i++) {
				sum += op[i];
			};
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[5] = sum;
			break;
		case "7sc":
			sum = 0;
			op = arr_filt_am(sc, 3);
			if (op) {
				for (i=0; i<5; i++) {
					sum += sc[i];
				} 
			} else {
				sum = 0;
			}
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[7] = sum;
			break;
		case "8sc":
			sum = 0;
			op = arr_filt_am(sc, 4);
			if (op) {
				for (i=0; i<5; i++) {
					sum += sc[i];
				} 
			} else {
				sum = 0;
			}
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[8] = sum;
			break;
		case "9sc":
			op = arr_filt_fh(sc);
			if (op) {
				this.innerHTML = 25;
				yahtzee.scorecard.score_values[9] = 25;
			} else {
				this.innerHTML = 0;
				yahtzee.scorecard.score_values[9] = 0;
			}
			break;
		case "10sc":
			op = arr_filt_st(sc, 1);
			if (op) {
				this.innerHTML = 30;
				yahtzee.scorecard.score_values[10] = 30;
			} else {
				this.innerHTML = 0;
				yahtzee.scorecard.score_values[10] = 0;
			}
			break;
		case "11sc":
			op = arr_filt_st(sc, 2);
			if (op) {
				this.innerHTML = 40;
				yahtzee.scorecard.score_values[11] = 40;
			} else {
				this.innerHTML = 0;
				yahtzee.scorecard.score_values[11] = 0;
			}
			break;
		case "12sc":
			op = arr_filt_am(sc, 5);
			if (op) {
				this.innerHTML = 50;
				yahtzee.scorecard.score_values[12] = 50;
			} else {
				this.innerHTML = 0;
				yahtzee.scorecard.score_values[12] = 0;
			}
			break;
		case "13sc":
			sum = 0;
			for (i=0; i<5; i++) {
				sum += sc[i];
			}
			this.innerHTML = sum;
			yahtzee.scorecard.score_values[13] = sum;
			break;
	}
	//sub_proc();
	val_sum1 = 0;
	val_sum2 = 0;
	val_tot = 0;
	for (i=0; i<6; i++) {
		if (yahtzee.scorecard.score_values[i] != "") {
			val_sum1 += parseInt(yahtzee.scorecard.score_values[i]);
		}
	}
	for (i=7; i<14; i++) {
		if (yahtzee.scorecard.score_values[i] != "") {
			val_sum2 += parseInt(yahtzee.scorecard.score_values[i]);
		}
	}
	val_tot = val_sum1 + val_sum2;
	document.getElementById("sc_sub1").innerHTML = val_sum1;
	document.getElementById("sc_sub2").innerHTML = val_sum2;
	document.getElementById("sc_total").innerHTML = val_tot;
	update();
	newturn();
}
function roll_dice() {
	
	if (yahtzee.throws_left > 0) {
		d_area.innerHTML = "";
		yahtzee.throws_left -= 1;
		document.getElementById("dice_area").innerHTML = "";
		for (i=0; i<5; i++) {
			dice_set[i].roll();
			dice_set[i].render();
		}
	} else {
		alert("You are out of throws this turn!")
	}
	update();
}
