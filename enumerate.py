# insted of writing all of that

'''
my_list = ["apple", "banana", "cherry"]
index = 1
for fruit in my_list:
    print(index, fruit)
    index += 1
'''

# we just use enumerate and write it like that:

'''
my_list = ["apple", "banana", "cherry"]
for i, fruit in enumerate(my_list, start=1):
    print(i, fruit)
'''

# we can also useit with strings

for i, letter in enumerate("MIAL", start = 1):
    print(i, letter)