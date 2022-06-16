
my_foods = ['pizza', 'combro', 'ongol']

my_fav_food = my_foods[1:3] # slicing string dan list
# list[0]
# list[0:2] [start:stop:step]

print(my_foods,"\n", my_fav_food)

#my_friend_foods = my_foods # alias : mereferensikan data
my_friend_foods = my_foods[:]

#print(my_friend_foods)
my_friend_foods.append("burger")
print(my_friend_foods)

print(my_foods)
