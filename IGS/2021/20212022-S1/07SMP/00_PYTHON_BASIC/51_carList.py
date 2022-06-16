#changing, adding, removing item in lists

motors = ["honda legenda", "yamaha fizr", "suzuki shogun"]

print(motors)

motors[0] = "ducati"

print(motors) # ["ducati", "yamaha fizr", "suzuki shogun"]

#adding element

motors.append("kawasaki")

print(motors)

#inserting element

motors.insert(1, "viar")

print(motors) # ['Ducati', 'Viar', 'Yamaha Fizr', 'Suzuki Shogun', 'Kawasaki']

#removing element

motors.pop(3) # menggunakan index

print(motors)

motors.remove("kawasaki") # menggunakan value

print(motors)

del motors[0]

print(motors) # ["viar", "fizr"]