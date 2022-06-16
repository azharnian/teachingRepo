# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

#map(function, list)
# a, b, c = list(map(int, input().split()))

# numbers = input().split()
# new_numbers = []
# numbers = list(map(int, input().split()))

# for number in numbers:
# 	new_numbers.append(int(number))


# print(a, b, c)
# print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = list(map(lambda x : x+3, numbers))
add_three = lambda x: x+3
new_numbers = numbers[:]
new_numbers = [ add_three(x) for x in numbers ]

new_odd_numbers = [ add_three(number) for number in numbers if number%2!=0 ]

square = lambda x: x**2

#[1, 9, 25, 49, 81]
square_odd_numbers = []

# print(new_numbers)
print(new_odd_numbers)
print(square_odd_numbers)

