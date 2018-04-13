import maps
id_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
class animal:
	def __init__(self, id, name, species, diet, info, interaction):
		self.name = name
		self.id = id
		self.species = species
		if diet == "H":
			self.diet = "Herbivore"
		elif diet == "O":
			self.diet = "Omnivore"
		else:
			self.diet = "Carnivore"
		self.info = info
		self.interaction = interaction
		self.inter_dialogue = """
		[1]     Name and Diet
		[2]     Additional Information
		[3]     Interact
		[Exit]  Leave the exhibit
		"""		
	def interact(self, action):
		if action == "INITIAL":
			return [self.name, self.species, self.diet]
		elif action == "INFO":
			return self.info
		elif action == "INTERACT":
			return self.interaction

class location:
	def __init__(self, animal, exit, description, name, id, neighbors):
		self.animal = animal
		self.exit = exit
		self.description = description
		self.neighbors = neighbors
		temp = []
		for x in self.neighbors:
			temp.append(int(x))
		self.neighbors = temp
		self.id = id
		self.name = name
	def determine_nav(self, zoo):
		total = len(self.neighbors)
		nav = """
			Current Location: """ + self.name + """
			
			Travel Options: """
		for x in self.neighbors:
			string = """
			[""" + str(self.neighbors.index(x)) + """]    """ + zoo.locations[x].name
			nav += string
		if self.exit == "True":
			nav += """
			[Exit] Leave the zoo"""
		if self.animal != "":
			nav += """
			[Look] Observe the exhibit"""
		self.nav = nav

class zoo:
	def __init__(self, locs):
		self.locations = locs
		self.map = maps.mainmap
	def map_update(self, location_id):
		self.map = maps.mainmap
		self.map = self.map.replace(("l" + str(location_id)), "X")
		iter = 0
		self.iter_col = []
		for x in self.locations[location_id].neighbors:
			self.map = self.map.replace("l" + (str(x)), str(iter))
			self.iter_col.append(iter)
			iter += 1
		for x in id_range:
			self.map = self.map.replace(("l" + str(x)), "-")
		self.current_location = location_id
	def close(self):
		exit()
#Reptiles
#human = animal("\"Mark Zuckerberg\"", "Herpus polymorphis", "Omnivore", "\"Mark Zuckerberg\" is a rare example of a previously undiscovered species, a shapeshifting reptile that takes the form of humans", 
#"While this is the only currently discovered specimen, it is theorized that many political or corporate leaders in human society may actually be reptiles", 
#"The reptile looks at you and begins to shout: \"Hello? Hello! Let me out of here! This is highly illegal! My legal team will press charges!\"")

#snake = animal("Copperhead", "Agkistrodon contortrix", "Carnivore", 
#"The Copperhead is a common venomous snake with a bright copper pattern that runs the length of its body",
#"Its venom is one of the weakest of all venomous snakes, yet has strong anti-tumor capabilities", "The Copperhead has better things to do then acknowledge your existence.")

#lizard = animal("Common Basilisk", "Basiliscus basiliscus", "Omnivore", "The Common Basilisk is renowned for its ability to run on the surface of water", 
#"This lizard is named after the mythical Greek monster known as the Basilisk", "The lizards startle and sprint across the small stream to hide in a small plant. After  a few minutes the lizards return to the rocks.")

#Insects
#bombardier = animal("Australian Bombardier Beetle", "Pheropsophus verticalis", "Carnivore", 
#"The Australian Bombardier Beetle is renowned for its ability to blast attackers with a boiling chemical cocktail",
#"The scalding spray is composed mainly of 1,4-Benzoquinone, a chemical that causes skin and eye irritation", 
#"The beetles make a few clicking noises, but largely ignore you")

#ironclad = animal("Ironclad Beetle", "Zopherus xestus", "Herbivore", "Ironclad beetles like to flop over and play dead when threatened.",
#"They are called Ironclad beetles because their tough elytra resemble steel armor plates", 
#"The beetles immediately stop moving and roll over onto their backs.")

#Medusas
#lionsmane = animal("Lion's Mane", "Cyanea capillata", "Carnivore", "The Lion's Mane is the largest species of medusa on Earth",
#"The world record largest Lion's Mane had a top 7 ft 6 in wide and tentacles 121.4 ft long. That specimen was even longer then the now-extinct Blue Whale!",
#"The massive jellyfish cares not about your presence.")

#hydra = animal("Hydra","Hydra magellanica", "Carnivore", "The Hydra is a jellyfish-like creature that attaches itself to plants and waits for prey to drift into its tentacles.",
#"Research has shown that all Hydra species are functionally immortal. Hydra stem cells never lose their ability to regrow tissue, and as such Hydra do not age.",
#"You watch the only known immortal creature in the entire world ignore you.")

#Birds
#archaeopteryx = animal("Archaeopteryx", "Archaeopteryx", "Carnivore", "Archaeopteryx was one of the first feathered creatures to achieve flight.",
#"This particular specimen was revived from a fossil by an unknown means.", "As you go to tap on the glass, you note the Archaeopteryx is eyeing you rather unnervingly. You decide not to test the only barrier between you and a 7-foot prehistoric carnivore.")

#Other
#facebook = animal("Facebook", "Informationus stealius", "Carnivore", "Facebooks are a very successful form of parasite. They attract a host, and then siphon personal information to sell to other companies",
#"Facebooks modify their host's behavior to become socially absorbed, encouraging the victim to use it more frequently, so that the Facebook can feed more.",
#"The Facebooks zip over and start thudding against the glass, trying to get into your phone")



#loc0 = location("", True, "You are standing in the zoo entrance", "Entrance 1", 0, [1, 2, 3])
#loc1 = location(human, False, "A human sits on a bed inside the enclosure, which is built to look like a hotel room", "Hotel", 1, [0, 2, 6, 7, 9])
#loc2 = location(snake, False, "The coppery head of a large snake pokes out from under a hollow rock", "Forest", 2, [0, 1, 3, 4, 5, 6, 7, 9])
#loc3 = location(lizard, False, "A few small, brown lizards rest on rocks in fromt of a narrow stream", "Pond", 3, [0, 2, 5])
#loc4 = location(bombardier, False, "A quantity of beetles are busy scurrying around a cage", "Scrubland", 4, [2, 5, 6])
#loc5 = location(ironclad, False, "A few silvery beetles scurry through dry sand", "Desert", 5, [2, 3, 4])
#loc6 = location(lionsmane, False, "An enormous jellyfish floats impassively in a large, frigid tank", "Arctic Aquarium", 6, [1, 2, 4, 7, 8, 9])
#loc7 = location(archaeopteryx, False, "four large, bird-like creatures stand on two legs in a field of tall grass", "Grasslands", 7, [1, 2, 6, 8, 9])
#loc8 = location(hydra, False, "A bunch of small, jellylike creatures float around a tank", "Aquarium", 8, [6, 7, 9])
#loc9 = location(facebook, False, "A swarm of glowing blue squares with a prominent white 'f' flit around the enclosure", "Cave", 9, [1, 2, 6, 7, 8])