"""
Sets are same as like lists but are unordered and cannot contain duplications
Uses curly brackets
"""

my_set = {1, 2, 4, 35, 4, 32, 2, 3, 4, 50}

print(my_set)

print(len(my_set))

for num in my_set:
    print(num)

# print(my_set[0])  # returns TypeError: 'set' object is not subscriptable

print(sorted(my_set))

my_set.discard(112)
print(sorted(my_set))
my_set.discard(50)
print(sorted(my_set))
my_set.clear()  # clears all the elements

my_set.add(54)
my_set.add(24)
my_set.add(14)
my_set.add(46)
my_set.add(6)
my_set.add(76)


print(sorted(my_set))

my_set.update([76, 72])  # adds 76,72 at the end of the set

print(sorted(my_set))
