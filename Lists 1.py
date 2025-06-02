# Introduction to Lists

# what is a list?
# 1. set of ordered items
# 2. have an index
# 3. know the order
# shopping list in python: apples, oranges, bananas, cheese

shopping_list = ["apples", "oranges", "bananas", "cheese"]
print(shopping_list)
print(shopping_list[0])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[0:3]) # slicing does not count the end range
# how to add items? lists are mutable. we can append
shopping_list.append("blueberries") # append to add items in the list
shopping_list[0] = "cherries" # update items in the list
del shopping_list[0] # delete items in list
print(len(shopping_list)) # gets the length of list
print(shopping_list)

shopping_list2 = ["bread", "eggs", "yam"]
print(shopping_list + shopping_list2) # adding two lists together
print(shopping_list * 2 ) #repeating the list twice

list_num = [1, 5, 7, 9, 15]
print(max(list_num)) # finding the maximum number
print(min(list_num)) # finding the minimum number




