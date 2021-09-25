list1 = [2, 2, 2]
list2 = [1, 1, 1]
difference = []
zip_object = zip(list1, list2)
for list1_i, list2_i in zip_object:
    difference. append(list1_i-list2_i)
print(difference)