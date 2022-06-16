-- 01-variable-datatype.lua
print("Hello world!")

life = 40 -- number/integer
height = 165.5 -- float
dogSound = "Barking Wuf Wuf" -- string/text
smallTable = {1,2,3} --lists
-- WSpace = game.Workspace -- reference object in roblox
Play = true -- boolean
dictTable = {name = "roger", age = 20, fav_meals = "bakso"} -- dictionary
Enemies = nil --None
mixedTable = {42, "Barking Wuf Wuf", {1,2,3}, false, print} -- game.Workspace,

print(life, height, dogSound, smallTable, Play, dictTable, Enemies, mixedTable) -- , WSpace

X = 10
Y = 5
print(X + Y)
print(X - Y)
print(X * Y)
print(X / Y)
print(X % Y)
print(X ^ Y)
print(-X, -Y)

print(math.pi)
print(math.sqrt(100))
print(math.sin(math.rad(30)))

A = 1
B = 2
print(A == B)
print(A ~= B)
print(A < B)
print(A <= B)
print(A > B)
print(A >= B)

case_one = true
case_two = false
print(case_one and case_two)
print(case_one or case_two)
print(not case_one)
print(not (case_one and case_two))
