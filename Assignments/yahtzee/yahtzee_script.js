// JavaScript

abstraction_mode = yahtzee_start;
abs_val = 1
function init() {
	table_load();
	document.getElementById("dice_cup").src = "https://i.imgur.com/OOhb34l.png";
	document.getElementById("roll_butt").innerHTML = "Roll the Dice!";
	document.getElementById("new_game_butt").innerHTML = "New Game";
	document.getElementById("turns_left").innerHTML = "Turns Remaining: " + abstraction_mode.turns_left;
	document.getElementById("throws_left").innerHTML = "Throws Remaining: " + abstraction_mode.throws_left;
	document.getElementById("abs_switch").innerHTML = "Next Abstraction";
	document.getElementById("dice_area").innerHTML = "";
	document.getElementById("player_name").innerHTML = ("Player Name: " + abstraction_mode.player.name);
	document.getElementById("player_avatar").src = abstraction_mode.player.avatar;
	//Dice
	die1=abstraction_mode.die; 
	die2=abstraction_mode.die;
	die3=abstraction_mode.die;
	die4=abstraction_mode.die;
	die5=abstraction_mode.die;
	dice=[die1, die2, die3, die4, die5];
	roll_dice();
	return dice;
}

function table_load() {
	abstraction_mode.scorecard.sub_proc()
	for (i=0; i<abstraction_mode.scorecard.score_types.length; i++) {
		document.getElementById(abstraction_mode.scorecard.score_ids[i]).innerHTML = abstraction_mode.scorecard.score_types[i];
	}
	for (i=0; i<abstraction_mode.scorecard.score_values.length; i++) {
		document.getElementById(abstraction_mode.scorecard.score_value_ids[i]).innerHTML = abstraction_mode.scorecard.score_values[i];
	}
}

function roll_dice() {
	for (i=0; i<5; i++) {
		a = dice[i].roll();
		b = document.createElement("img");
		b.src = dice[i].sprite;
		b.className = "die_sprite";
		b = document.getElementById("dice_area").appendChild(b);
		
	}
}

function switch_abs(){
	if (abs_val == 1) {
		abs_val = 2;
		abstraction_mode = yahtzee_mid;
		init();
	} else if (abs_val == 2) {
		abs_val = 3;
		abstraction_mode = yahtzee_end;
		init();
	} else if (abs_val == 3) {
		abs_val = 1;
		abstraction_mode = yahtzee_start;
		init();
	}
}