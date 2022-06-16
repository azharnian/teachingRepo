counter = 0

print("Using While loops")
while (counter < 10) do
	print(counter)
	counter = counter + 1
end

print("\nUsing While loops Desc.")
counter = 9
while (counter >= 0) do
	print(counter)
	counter = counter - 1

print("\nUsing For loops")
for x = 0, 9, 1 do -- start, stop, step
	print(x)
end

print("\nUsing For loops Desc.")
for x = 9, 0, -1 do
	print(x)
end