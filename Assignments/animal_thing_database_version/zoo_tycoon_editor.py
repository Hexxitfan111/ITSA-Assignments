####################################################################
"""WARNING: MY PYTHON INSTALLATION REQUIRES ABSOLUTE FILE PATHS. IN ORDER TO FUNCTION YOU WILL NEED TO 
CHANGE THE PATHS TO FIT YOUR COMPUTER"""
####################################################################
from tempfile import NamedTemporaryFile
import classes_and_data, os, repos, csv, shutil

a_file = "C:/Users/Mickey/Documents/GitHub/ITSA-Assignments/Assignments/animal_thing_database_version/animals.csv"
e_file = "C:/Users/Mickey/Documents/GitHub/ITSA-Assignments/Assignments/animal_thing_database_version/enclosures.csv"
n_file = "C:/Users/Mickey/Documents/GitHub/ITSA-Assignments/Assignments/animal_thing_database_version/neighbors.csv"


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

def cts(inp):
	inp.replace(",", ";")
	return inp
		
def write_file():
	edit_run = True
	while edit_run:
		ed_opt = input("Do you wish to edit the [A]nimals, [E]nclosures, or [N]eigbors file, or [Exit] the program?").upper()
		if ed_opt == "A":
			fields = ["ID", "Name", "SciName", "Diet", "Info", "Inter"]
			print("Animal class input structure: [ID],[Name],[Scientific Name],[Diet],[Info],[Interaction] ")
			id = input("Enter ID: (Integer from 1-9) ")
			name = input("Enter Name: (String) ")
			s_name = input("Enter Scientific Name: (String) ")
			diet = input("Enter Diet: (C, O, H, for carnivore, omnivore, and herbivore respectively) ")
			info = cts(input("Enter Info: (String)"))
			inter = cts(input("Enter Interaction: (String) "))
			tempfile = NamedTemporaryFile(mode='w', delete=False)
			with open(a_file, "w", newline="" ) as csvfile, tempfile:
				reader = csv.DictReader(csvfile, delimiter=",", fieldnames=fields)
				writer = csv.DictWriter(tempfile, delimiter=",", fieldnames=fields)
				for row in reader:
					if str(int(row["ID"])-1) == id:
						row["Name"],row["SciName"],row["Diet"],row["Info"],row["Inter"] = name,s_name,diet,info,inter
					row = {"Name":row["Name"],"SciName":row["SciName"],"Diet":row["Diet"],"Info":row["Info"],"Inter":row["Inter"]}
					writer.writerow(row)
			shutil.move(tempfile.name, a_file)
		elif ed_opt == "E":
			fields = ["Exit", "Description", "Name", "ID"]
			print("Enclosure class input structure: [Exit],[Description],[Name],[ID] ")
			exit = input("Enter Exit: ('True' or 'False') ")
			desc = cts(input("Enter Description: (String) "))
			name = input("Enter Name: (String) ")
			id = input("""Enter ID: (Integer from 0-9, with 0 being the default exit. 
			Animals are added to enclosures by id number. ID 0 is the exit, and animal ID's 1-9 are
			matched with enclosure ID's 1-9) 
			""")
			tempfile = NamedTemporaryFile(mode='w', delete=False)
			with open(e_file, "rw", newline="" ) as csvfile, tempfile:
				reader = csv.DictReader(csvfile, delimiter=",", fieldnames=fields)
				writer = csv.DictWriter(tempfile, delimiter=",", fieldnames=fields)
				for row in reader:
					if row["ID"] == id:
						row["Name"],row["Description"],row["Exit"] = name,desc,exit
					row = {"Name":row["Name"],"Description":row["Description"],"Exit":row["Exit"]}
					writer.writerow(row)
			shutil.move(tempfile.name, e_file)
		elif ed_opt == "EXIT":
			edit_run = False
			
print("\n\nWelcome to the Zoo Tycoon: Zoo Administrative Program (ZTZAP), CLI Edition!")
print("(Version 2.4.7)")
input("Press [Enter] to continue.")
cls()
print("""\n
Latest Update Notes (v2.4.7):
	>In light of recent events concerning Facebook, Zoo Tycoon: Zoo Administrative Program
	 no longer collects and sells user information without permission.
	
	>In light of the recent ZTZAP management corruption scandal, our programming team has 
	 fixed a major glitch allowing ZTZAP to access certain Dark Web sites and online chat rooms.
	
	>Fixed major unintentional programming oversight allowing ZTZAP to automatically create and 
	 maintain network backdoors, rootkits, ransomware, and other malware.
	
	>Fixed a few other security vulnerabilities.
Visit the ZTZAP website for full details.

Planned Features:
	>Implementation of a system where users pay money to unlock different areas of the editor. 
	 This is intended to encourage fairness and give users a sense of progression and accomplishment.
	 
	>Implementation of a remote access module to allow our Russia-based Support Team easier troubleshooting.
	
	>Implementation of a microphone and camera monitor to ensure that ZTZAP is not being used for illicit activites.
	 This data will be transmitted ONLY to the ZT Quality Assurance office over our most secure Telnet line.
To see the full list of planned features, visit the ZTZAP website.
""")
input("\n\nPress [Enter] to begin editing.")
editloop = True
while editloop:
	cls()
	opt = input("""
	ZTZAP version 2.4.7
	Please select an option:
	+-------------------------------------------------------------+
	|WARNING: EDITOR IS CURRENTLY UNSTABLE AND MAY BREAK THE FILES|
	|         A BACKUP ANIMALS FILE HAS BEEN INCLUDED.            |
	|  USE EDITOR AT OWN RISK. ZTZAP NOT RESPONSIBLE FOR DAMAGES. |
	+-------------------------------------------------------------+
		[Create]        Make new animals and locations in a new file
		[Edit]          Edit the animals and location in an existing file
		[Policy]        View the ZTZAP Privacy Policy
		[Silk Road]     Connect to the built in illegal merchandise store interface
		[Exit]          Exit ZTZAP
	""").upper()
	if opt == "CREATE":
		pass
	elif opt == "EDIT":
			write_file()
	elif opt == "POLICY":
		print("""
		                PRIVACY POLICY:
						By using this program you agree that Zoo Tycoon: Zoo Administrative Program and its parent,
						Totally Legitimate Enterprises, LLC, (Hereafter referred to collectively as ZTZAP), are not
						to be held accountable for any and all instances of personal injury, disfigurement, death,
						identity theft, fraud, and all other infringements as either a direct or indirect result of 
						using this program. ZTZAP maintains that any data collected by this program will be sold to
						the highest bidder in the interest of maintaining a fair trade envrionment. 
		""")
		input("Press [Enter] to return to menu.")
	elif opt == "SILK ROAD":
		print("Oops! This feature is now deprecated. View the update notes or website for more information.")
		input("Press [Enter] to return to the menu.")
	elif opt == "EXIT":
		editloop = False
	else:
		print("Invalid input. Please try again.")
