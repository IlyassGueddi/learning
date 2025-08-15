#we use *args when we don’t know how many arguments we’ll get. 

def add_num(*args):
    print(args) # it's not important
    total = 0
    for num in args:
        total += num
    return total

print(add_num(1, 20, 2, 3, 5, 6))
print(add_num(7, 4, 8))