"""

Exercise 8: Simple Search

This program searches for a specific name in a list and finds "Sam."

"""

# List of names

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Search for the name 'Sam' in the list

if "Sam" in names:
    print("Sam found in the list.")

else:
    print("Sam not found.")
    
"""

Optional Requirements 

Let user search for a name

"""

# Allows the user to enter a name to search for

search_name = input("Enter a name to search for: ")

# Checking if the input name is in the list

if search_name in names: 
    print(f"{search_name} is found in the list.")
    
else:
    print(f"{search_name} is not found in the list.")
    

