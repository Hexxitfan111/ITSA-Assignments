import ui
class bowling_score:

	def __init__(self):
		self.rlist = ui.score_input()
		self.score_game()

	def strike_score(self, n):
		strike_score = 0

		if n == 18:
			return self.rlist[19] + self.rlist[20] + 10

		
		roll1 = self.rlist[n+2]
		roll2 = self.rlist[n+3]
		roll3 = self.rlist[n+4]
				
		
		if ((roll1 == 10 and roll3 == -1) or (roll1 < 10 and roll2 == -1)):
			return roll1 + 10
				
		strike_score = strike_score + roll1
	
		if roll1 == 10 and roll2 == -1:
			strike_score = strike_score + roll3
		else: strike_score = strike_score + roll2
				
		return strike_score + 10
	
	def spare_score(self, n):
		roll1  = self.rlist[n+2]
		
		if roll1 == -1:
			return 10

		return roll1 + 10
			
	def score_game(self):
		roll1 = 0
		roll2 = 0
		score = 0
		current_score = 0
		
		for i in range (0, 20, 2):
			roll1 = self.rlist[i]
			roll2 = self.rlist[i+1]
			
			if roll1 == 10:
				current_score = self.strike_score(i)
			elif roll1 + roll2 == 10:
				current_score = self.spare_score(i)
			else:
				if roll1 != -1:
					current_score = current_score + roll1
				if roll2 != -1:
					current_score = current_score + roll2
		
			score = score + current_score        
			current_score = 0

		
		ui.output(('Score for ' + name + ': ' + str(score)))

main_loop = True
while main_loop:
	game = ""
	menu = ui.gather(ui.menu_text)
	if menu.upper() == "NEW":
		name = ui.gather("Enter your name: ")
		game = bowling_score()
	elif menu.upper() == "EXIT":
		ui.output("Exiting program")
		exit()
	else:
		ui.output("Invalid input")
		
	