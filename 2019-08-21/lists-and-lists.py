'''
Task: "Lists and lists"
Difficulty: Beginner
Description: Lists collect a set of items together and are used in all programming languages. There are often methods or functions
that can help you manage lists and their contents (e.g. max(list) will return the largest item in that list)
Using the following list of values: 300, 64, 9011, 2013, 48, 750
Write a program that outputs the following information:
The first item in the list (should be "300")
The fourth item in the list (should be "2013")
The last item in the list (should be "750")
The largest item in the list (should be "9011")
The smallest item in the list (should be "48")
Bonus:
The number of items in the list (should be "6")
The list items in ascending order (should be "48, 64, 300, 750, 2013, 9011")
The list items in descending order (should be "9011, 2013, 750, 300, 64, 48")
'''
items = [300, 64, 9011, 2013, 48, 750]

print("Lists and lists")
print(items)
print("First item:", items[0])
print("Fourth item:", items[3]) # Arrays are zero-based
print("Last item:", items[-1])
print("Largest item:", max(items))
print("Smallest item:", min(items))
print("Bonuses")
print("Number of items in list:", len(items))
items.sort()
print("Items in ascending order:", items)
items.sort(reverse=True)
print("Items in descending order:", items)

'''
Comments: It doesn't matter that we sort the list when we do because we don't need the original order after that point.
If that did matter, we would take a copy of the list first (i.e. "sorteditems = items") and work with the copy.
'''