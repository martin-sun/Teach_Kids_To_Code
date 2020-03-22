# Ask the user for their name
name = input("What is your name? ")

# Keep printing names until we want to quit
while name != "":
    # Print their name 100 times.
    for x in range(100):
        print(name + " ")

    name = input("Type another name, or just hit [ENTER] to quit: ")
    
print("Thanks for playing")


