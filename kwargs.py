# **kwargs allows a function to accept any number of named (keyword) arguments
# It stores them in a dictionary inside the function.
'''
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Mial", age=18, city="Casablanca")
'''




def create_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

my_profile = create_profile(name="Mial", age=18, hobby="Football")
print(my_profile)
