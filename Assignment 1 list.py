my_list = [10, 20, 30, 40, 50]
print( my_list)
print("Access Element at Index 2:", my_list[2])


my_list.append(60)
print("List After Adding 60:", my_list)

my_list.insert(2, 25)  # Inserting an element at index 2
print("List After Inserting 25 at Index 2:", my_list)

my_list.remove(30)  # Removing an element (value 30)
print("List After Removing 30:", my_list)

my_list.sort()  # Sorting the list in ascending order
print("List After Sorting in Ascending Order:", my_list)

my_list.sort(reverse=True)  # Sorting the list in descending order
print("List After Sorting in Descending Order:", my_list)


my_list.reverse()  # Reversing the list
print("List After Reversing:", my_list)