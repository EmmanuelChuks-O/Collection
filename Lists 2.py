# lists

# syntax
# listname = [element1, element2, element3...]

my_list = [1, 2, 3, 4, 5, "red", "blue", "green", 3]
print(my_list)

# lists operations

# access elements using index
# index starts at 0

# 1 - index 0
# 2 - index 1
# 3 - index 2
# 4 - index 3
# 5 - index 4
# "red" - index 5
# "blue" - index 6
# "green" - index 7

# index = element - 1

print(my_list[1])
print(my_list[5])

# append

# add elements to list

my_list.append("House")
print(my_list)

# remove

my_list.remove(3)
print(my_list)

# retrieve part of list

print(my_list[1:4])
print(my_list)

# replace
# manually replace list items

# replace red - white
# index of red = 5, position 6

print(my_list[5])
my_list[5] = "White"
print(my_list)