my_foods = ['pizza', 'clementine', 'burger']

my_favorite_foods = my_foods[0:2]

# friend_favorite_foods = my_foods # alias list reference to my_foods
friend_favorite_foods = my_foods[:]

print(my_foods)
print(my_favorite_foods)

print()
print(friend_favorite_foods)
friend_favorite_foods.append('martabak')

print()
print(friend_favorite_foods)

print()
print(my_foods)