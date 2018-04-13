import csv, classes_and_data

animal_data_array = []
animal_array = []


#ADJUST BELOW VARIABLES TO YOUR PYTHON DIRECTORY/FILES
#My Python installation refuses to open files without the full path.
#I have included an alternate zoo as well. Adjust the file paths to the set of files
#i.e. C:/Whatever/PythonDirectory/animals_f.csv
#also change the mainmap variable to false.

animal_file = "C:/Users/Mickey/Documents/GitHub/ITSA-Assignments/Assignments/animal_thing_database_version/animals.csv"
enclosure_file = "C:/Users/Mickey/Documents/GitHub/ITSA-Assignments/Assignments/animal_thing_database_version/enclosures.csv"
neighbors_file = "C:/Users/Mickey/Documents/GitHub/ITSA-Assignments/Assignments/animal_thing_database_version/neighbors.csv"
mainmap = True

enclosure_data_array = []
enclosure_array = []

with open(animal_file, newline='') as csvfile:
	reader_a = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader_a:
		animal_data_array.append(row)
		
with open(enclosure_file, newline='') as csvfile:
	reader_e = csv.reader(csvfile, delimiter=',', quotechar='|')
	temp_dat_arr1 = []
	temp_dat_arr2 = []
	with open(neighbors_file, newline='') as csvfile:
		reader_n = csv.reader(csvfile, delimiter=',', quotechar='|')
		for x in reader_e:
			temp_dat_arr1.append(x)
		for y in reader_n:
			temp_dat_arr2.append(y)
		for x in range(0, len(temp_dat_arr1)):
			temp_dat_arr1[x].append(temp_dat_arr2[x])
			enclosure_data_array.append(temp_dat_arr1[x])

new_array = []
for x in animal_data_array:
	tempinp1 = []
	for y in x:
		tempinp1.append(y.replace(";", ","))
	new_array.append(tempinp1)
animal_data_array = new_array

new_array = []
for x in enclosure_data_array:
	tempinp1 = []
	for y in range(0, len(x)):
		if y == 1:
			tempinp1.append(x[y].replace(";", ","))
		else:
			tempinp1.append(x[y])
	new_array.append(tempinp1)
enclosure_data_array = new_array


for x in range(0, len(animal_data_array)):
	temp1, temp2, temp3, temp4, temp5, temp6 = animal_data_array[x]
	animal_array.append(classes_and_data.animal(temp1, temp2, temp3, temp4, temp5, temp6))

for x in range(0, 10):
	if x == 0:
		temp1 = ""
	else:
		temp1 = animal_array[x-1]
	temp2, temp3, temp4, temp5, temp6 = enclosure_data_array[x]
	enclosure_array.append(classes_and_data.location(temp1, temp2, temp3, temp4, temp5, temp6))
	
Zoo = classes_and_data.zoo(enclosure_array)
#animal_array = List of animals
#enclosure_array = List of full enclosures, including animals and neighbors