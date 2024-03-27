



# - Create a function that takes in 3 parameters(firstname, lastname, age) and

# returns a dictionary based on those values



def newish_function(firstname, lastname, age):
    new_dict = {
        "First name": firstname,
        "Last name": lastname,
        "Age": age,
    }
    return new_dict

printable_dict = newish_function("Gytenis", "Borusas", 33)

print(printable_dict)


