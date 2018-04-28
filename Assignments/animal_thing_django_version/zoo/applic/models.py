from django.db import models

# Create your models here.


from django.urls import reverse #Used to generate URLs by reversing the URL patterns



class Animal(models.Model):
	"""
	Model for animal
	"""
	name = models.CharField(max_length=60, help_text="Enter the name of the animal: ", default="")
	nickname = models.CharField(max_length=60, help_text="Enter the nickname of the animal:", default="")
	sci_name = models.CharField(max_length=100, help_text="Enter the scientific name of the animal:", default="")
	
	DIET_CHOICE = (
	("C", "Carnviore"),
	("O", "Omnivore"),
	("H", "Herbivore"),
	)
	
	diet = models.CharField(max_length=1, choices=DIET_CHOICE, blank=True, default='m', help_text="Pick the animal's diet.")
	info = models.CharField(max_length=500, help_text="Enter the animal information: ", default="")
	inter = models.CharField(max_length=500, help_text="Enter the animal interaction information: ", default="")
	
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.name + " | " + self.nickname + " | " + self.diet

class Exhibit(models.Model):
	"""
	Model for exhibits
	"""
	EXIT = (
	("T", "Yes"),
	("F", "No"),
	)
	name = models.CharField(max_length=200, help_text="Enter the exhibit name", default="")
	description = models.CharField(max_length=200, help_text="Enter the exhibit description: ", default="")
	is_exit = models.CharField(max_length=1, choices=EXIT, blank=True, default='m', help_text="Is this exhibit an exit?")
	ex_id = models.CharField(max_length=2,help_text="Enter the exhibit ID number. Must be unique!",default="")
	neighbors = models.CharField(max_length=50,help_text="""Enter ID's of neighbor exhibits, separated by commas. I.E. 1,2,3""",default="")
	animals = models.ManyToManyField(Animal, help_text="Add animals to this exhibit")
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name
	def get_neighbors(self):
		return self.neighbors.split(",")

class Zoo(models.Model):
	"""
	Model for zoo
	"""
	name = models.CharField(max_length=200, help_text="Enter the name of the zoo")
	exhibits = models.ManyToManyField(Exhibit, help_text="Select as many exhibits as you wish. Make sure you have an exit!")
	
	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name