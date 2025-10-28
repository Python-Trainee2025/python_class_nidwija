# # ordered and mutable
# '''
#     ordered and mutable
#     for grouping similar items or just items in general
# '''
#
#
# # Accessing Elements
#
# # print(a[3])
# # print(a[1:4])
# # print(a[1])
# # print(len(a))
# # print(a[0:2])
#
# # print(a[::-1])
# # print(a)
#
# a = [1, 2, 3, 4.5, '1', 1, 1, 1]
#
# # a.reverse()
# # print(a)
#
# # Adding Elements
# a.append(10)
# print(a)
#
# a.insert(3,'hello')
# print(a)
#
# a[2]='test'
# print(a)
#
# # a.insert(1, 9)  # Inserts 9 at index 1
# # print(a)
# #
# # a.insert(4, 'ram')  # Inserts 'ram' at index 3
# # print(a)
# #
# #
# # Counting Occurrences
# print(a.count(4))

# Sorting
b = [5, 2, 9, 1, 7]

b.sort()  # Sorts the list in ascending order
print(b)


f=[5,7,2,3,7,99,11,2,0]
d=sorted(f)
print(d)
# print(d)


# List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Concatenation [1, 2, 3, 4, 5, 6]
print(list1 * 2)  # Repetition [1, 2, 3, 1, 2, 3]

a=[1,2,3,41]
# Checking Membership
print(4 in a)  # True
print(10 not in a)  # True

# Removing Elements
a.remove(4)  # Removes first occurrence of 4
print(a)

popped = a.pop(2)  # Removes and returns last element
print(popped)  # 7
print(a)
#
del a[1]  # Deletes element at index 1
print(a)

a.clear()