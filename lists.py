"""
Lists are collection of data
"""

list1 = [
    1,
    2,
    4,
    3,
    7,
    6,
    9,
    4,
    5,
    10,
    11,
    12,
    16,
    80,
    96,
    40,
    35,
    12,
]  # indexes starting from 0
list1.sort()
print(list1)

print(list1[0])  # 80 print the value in 0th index
print(list1[4])  # 12 print the value in 4th index
print(list1[-1])  # 12 print the value from reverse order index
# print(list1[9])  # IndexError

people_list = ["Kathir", "Kannan", "Karthick"]

print(people_list[-1])


# Slicing
print(list1[1:4])  # print 96,40,35 (excludes the ending index)
print(list1[1:])  # prints the values 96,40,35,12 as there is no end index provided
