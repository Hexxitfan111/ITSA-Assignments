import classes_and_data, os, repos
if repos.mainmap:
	import maps as maps
else:
	import altmap as maps

def cls():
#clears the console. Supports Windows and Linux, unsure about Mac.
	cls_success = True
	try:
		os.system('cls' if os.name=='nt' else 'clear')
	except Exception:
		cls_success = False

	print("\n" * 100)
	#even if console clear fails, newlines provide an approximation of clearing the console.

	if cls_success:
		os.system('cls' if os.name=='nt' else 'clear')
	else:
		pass

name = input(">Enter username: ")
print("""
>Warning: You have not yet created a password for this account. 
>Adding a password to an account helps protect your information.
>Visit www.microsoft.com for more information.
>Logging in user """ + name + """ (Administrator)...
>...
""")
input(">Login complete. Press [Enter] to continue.")
introloop = True
password = False
password_dat = ""
while introloop:
	cls()
	if password:
		opt = input("""
		>Welcome to the Z.C.O.C.E. Mainframe, """ + name + """ (Administrator)
		>Please select one of the options below:
			[Visit]     Launch the built-in ZooVirtualTour-1.0.4 simulation software
			[Edit]      Launch the Zoo Tycoon Zoo Administrative Program, CLI Edition
			[Exit]      Sign out
		""").upper()
	else:
		opt = input("""
		>Welcome to the Z.C.O.C.E. Mainframe, """ + name + """ (Administrator)
		>Please select one of the options below:
			[Visit]     Launch the built-in ZooVirtualTour-1.0.4 simulation software
			[Edit]      Launch the Zoo Tycoon Zoo Administrative Program, CLI Edition
			[Password]  Create a password for this account
			[Exit]      Sign out
		""").upper()
	if opt == "VISIT":
		cls()
		print(">Loading ZooVirtualTour-1.0.4.exe...  11%")
		print(">Loading ZooVirtualTour-1.0.4.exe...  34%")
		print(">Loading ZooVirtualTour-1.0.4.exe...  57%")
		print(">Loading ZooVirtualTour-1.0.4.exe...  83%")
		print(">Loading ZooVirtualTour-1.0.4.exe...  90%")
		print(">Loading ZooVirtualTour-1.0.4.exe...  100%")
		print(">Initializing...\n\n")
		import visit
		print("\n>Closing program...")
		print(">ZooVirtualTour-1.0.4.exe has successfully shutdown.")
		input(">Press [Enter] to return to menu.")
	elif opt == "EDIT":
		print(">Loading ztedit.exe... 30%(4 dependent files queued.")
		print(">Loading ztedit.exe... 78%(4 dependent files queued.")
		print(">Loading ztedit.exe... 83%(4 dependent files queued.")
		print(">Loading ztedit.exe... 100%(4 dependent files queued.")
		print(">Loading dependency: iptrack.exe...         (3 dependent files queued.")
		print(">Loading dependency: browsermodifier.dll... (2 dependent files queued.")
		print(">Loading dependency: popupads.dll...        (1 dependent file queued.")
		print(">Loading dependency: scanworm.exe...")
		print(">Initializing...")
		import zoo_tycoon_editor
	elif opt == "EXIT":
		cls()
		print("Signing out user " + name + " (Administrator)..." )
		print("Shutting down...")
		input("Press [Enter] to finish shutdown.")
		exit()
	elif opt == "PASSWORD":
		step1 = input(">Enter a password: ")
		step2 = input(">Re-enter the same password: ")
		if step1 == step2:
			input(">Password set! Press [Enter] to return to menu.")
			password_dat = step1
			password = True
		else:
			input(">Error: Passwords do not match. Press [Enter] to return to menu.")
	else:
		print