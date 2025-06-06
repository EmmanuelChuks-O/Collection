# list comprehension = a concise way to create lists in Python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
# or
# for x in range(1,11):
#     doubles.append(x*2)

print(doubles)
print(triples)
print(squares)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0 ]
odd_nums = [num for num in numbers if num % 2 == 1 ]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)