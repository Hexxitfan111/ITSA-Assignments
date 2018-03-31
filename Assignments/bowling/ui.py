def score_input():
		roll_list = []
		frame = 0
		current_index = 0
		
		for i in range (0, 21):
			roll_list.append(-1)
		
		while frame < 10:
			if frame == 9:
				rolls = input('Enter rolls for Frame ' + str(frame + 1) + ' in the following format: [Score 1] [Score 2] [Score 3]. ')
			else:
				rolls = input('Enter rolls for Frame ' + str(frame + 1) + ' in the following format: [Score 1] [Score 2]. ')
			
			framearray = [int(i) for i in rolls.split() if i.isdigit()]
			
			
			if len(framearray) < 2:
				roll_list[current_index] = framearray[0]
			elif len(framearray) == 2:
				roll_list[current_index] = framearray[0]
				roll_list[current_index + 1] = framearray[1]
			else:
				roll_list[current_index] = framearray[0]
				roll_list[current_index + 1] = framearray[1]
				roll_list[current_index + 2] = framearray[2]
					
			current_index = current_index + 2
			frame = frame + 1
		return roll_list
		
def output(msg):
	print(msg)
	
def gather(msg):
	return input(msg)

menu_text = """
Please enter one of the following keywords:
[New]: Score a new game
[Exit]: Exit this program
"""