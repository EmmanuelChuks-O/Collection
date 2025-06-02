# Sets

my_set = {1, 2, 3, 4, 5}

print(my_set)

# add

my_set.add(6)
print(my_set)

# remove elements

my_set.remove(3)
print(my_set)

# union, intersection and difference

# union

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print(union)

# intersection

intersection = set1 & set2
print(intersection)

# difference

difference_set1 = set1 - set2
difference_set2 = set2 - set1

print(difference_set1)
print(difference_set2)