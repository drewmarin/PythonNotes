list1 = ['a','b','c']
print(list1)
list2 = [x for x in list1]
print(list2)
list3 = [x for x in list1 if x == 'a']
print(list3)

list11 = [c for c in "string"]
print(list11)

print("".join(list11))
print("-".join(list11))