

cars = ["bmw", "audi", "toyota", "subaru"]

#Sorting
cars.sort() #permanently
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars)) #temporary sorted list


#Searching
item = "toyota"
index_item = cars.index(item)
print(index_item)

isExists = item in cars # True
print(isExists)

item = "datsun"
# print(cars.index(item))

if item in cars:
	index = cars.index(item)
	print(index)
else:
	print("Not Exists")

#Number of items in list
full_name = "Anas Azhar" #str 
print(len(full_name))

print(len(cars))




