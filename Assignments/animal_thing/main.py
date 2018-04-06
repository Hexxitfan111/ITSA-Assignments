import classes_and_data, os, maps

def cls():
#clears the console. Supports Windows and Linux, unsure about Mac.
	cls_success = True
	try:
		os.system('cls' if os.name=='nt' else 'clear')
	except Exception:
		cls_success = False

	print("/n" * 100)
	#even if console clear fails, newlines provide an approximation of clearing the console.

	if cls_success:
		os.system('cls' if os.name=='nt' else 'clear')
	else:
		pass

def confirm(): input("Press [Enter] to continue...")
#shortcut so I don't have to type 'input("Press [Enter] to continue...")' every time.


mainloop = True
area_loop = False
location = 0
action = ""
print("Welcome to the Zoological Collection of Organisms Common and Esoteric!")
print("We hope you have an excellent visit!")
print("You take a map from the box of maps at the Information Desk.")
print("You open the map and decide where to go first:")
confirm()
cls()
while mainloop:
	cls()
	Zoo = classes_and_data.Zoo
	Zoo.locations[location].determine_nav()
	Zoo.map_update(location)
	ani = Zoo.locations[location].animal
	locs = Zoo.locations
	nav = Zoo.locations[location].nav
	map = Zoo.map
	print(map)
	print(nav)
	action = input("(Enter the value next to the option you would like to pick) ")
	success = True
	try:
		if action.upper() != "LOOK" and action.upper() != "EXIT":
			int(action)
	except Exception:
		success = False
	if success:
		if action.upper() == "LOOK" and (location != 0 or location != 10):
			cls()
			print("You enter the viewing area of the exhibit")
			confirm()
			area_loop = True
		elif action.upper() == "EXIT" and (location == 0 or location == 10):
			cls()
			print("Thank you for visiting the Z.C.O.C.E.! Have an exotic day!")
			print("You turn and leave the zoo.")
			input("(Press [Enter] to exit...)")
			Zoo.close()
		elif (action in (' '.join(str(x) for x in Zoo.iter_col))):
			location = Zoo.locations[location].neighbors[int(action)]
		else:
			input("Invalid input. Press [Enter] to continue...")
	else:
		input("Invalid input. Press [Enter] to continue...")
	while area_loop:
		cls()
		print(locs[location].description)
		print("\n \n")
		print(ani.inter_dialogue)
		inter = input("(Enter the value next to the option you would like to pick) ")
		if inter == "1":
			print("\nYou examine the animal's name and diet:")
			temp1 = ani.interact("INITIAL")
			temp2 = """
			Name:             """ + temp1[0] + """
			Scientific Name:  """ + temp1[1] + """
			Diet:             """ + temp1[2] + """
			"""
			print(temp2)
			confirm()
		elif inter == "3":
			print("\nYou tap on the glass, ignoring the signs that say \"Please do not tap on the glass!\".")
			temp = ani.interact("INTERACT")
			print(temp)
			confirm()
		elif inter == "2":
			print("\nYou examine the fun facts about the animal:")
			temp = ani.interact("INFO")
			temp2 = (temp[0] + ". " + temp[1])
			print(temp2)
			confirm()
		elif inter.upper() == "EXIT":
			print("You turn and leave the exhibit")
			confirm()
			area_loop = False
		else:
			input("Invalid input. Press [Enter] to continue...")