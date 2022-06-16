# #a, b, c, d = input().split(" ")
# numbers = input().split(" ")
# # a, b, c, d = int(a), int(b), int(c), int(d)
# #print(a, b, c, d)
# # print(numbers)
# new_numbers = []

# for number in numbers:
# 	new_numbers.append(int(number))

# print(new_numbers)

# numbers = list(map(int, input().split(" ")))
# numbers = input().split()
# numbers = [ int(number) for number in input().split() ]
# print(numbers)

add_3 = lambda x : x+3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_numbers = list(map(add_3, numbers))
# new_numbers = list(map(lambda x: x+3, numbers))

#buat list baru 'new_numbers' yg tiap item dikuadratkan dan diperoleh dari list numbers yg hanya bilangan genap.
# [4, 16, 36, 64, 100]

square = lambda x: x*x

new_numbers = [ square(number) for number in numbers if number%2 == 0]

print(new_numbers)







