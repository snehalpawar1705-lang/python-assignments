set_a = {10, 20, 30, 40, 50}
print("Created Set A:", set_a)


# Accessing elements 
print("Accessing Set Elements:")
for element in set_a:
    print(element, end=" ")
print()


set_b = {40, 50, 60, 70, 80}
print("Set B:", set_b)
union_set = set_a.union(set_b)
print("Union of Set A and Set B:", union_set)


intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B:", intersection_set)


difference_set_a_b = set_a.difference(set_b)  # Elements in A but not in B
print("Difference of Set A - Set B:", difference_set_a_b)


