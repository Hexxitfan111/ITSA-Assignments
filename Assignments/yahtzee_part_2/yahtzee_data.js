yahtzee = {
	//will be named 'Yahtzee' in ac
	"turns_left" : 13,
	"throws_left" : 3,
	"player" : {
		"avatar" : "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Default_profile_picture_%28male%29_on_Facebook.jpg/600px-Default_profile_picture_%28male%29_on_Facebook.jpg",
		"name" : "Player 1"
	},
	"scorecard" : {
		"score_types" : ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Subtotal 1", "Three of a Kind", "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance", "Subtotal 2", "Total"],
		"score_ids" : ["ones","twos","threes","fours","fives","sixes","subtotal1","3ofkind","4ofkind","fullhouse","smstraight","lgstraight","yahtzee","chance","subtotal2","total_score"],
		"score_values" : ["","","","","","","","","","","","","","","",""],
		"score_value_ids" : ["1sc","2sc","3sc","4sc","5sc","6sc","sc_sub1","7sc","8sc","9sc","10sc","11sc","12sc","13sc","sc_sub2","sc_total"],
		"sub_proc" : function sub_proc() {
			sub1 = 0;
			sub2 = 0;
			for (i=0; i<6; i++) {
				if (this.score_values[i] == "") {
					sub1 += 0;
				} else {
					sub1 += parseInt(this.score_values[i]);
				}
				//alert("sub1: " + sub1)
			}
			for (i=7; i<14; i++) {
				if (this.score_values[i] == "") {
					sub2 += 0;
				} else {
					sub2 += parseInt(this.score_values[i]);
				}
				//alert("sub2:" + sub2)
			}
			this.score_values[6] = sub1;
			this.score_values[14] = sub2;
			this.score_values[15] = (sub2 + sub1);
			return this.score_values;
			
		},
		"subtotal" : "",
		"total" : ""
	}
}