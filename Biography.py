"""

Exercise 3: Biography

This program stores and prints my name, hometown, and age using a dictionary.

"""

# Storing user information in a dictionary 

biography = {
    
    'name': "Maria Heleina Leus", 
    'hometown': "Calamba, Laguna, Philippines ",  
    'age': 18
             
}

# Printing the values on separate lines

print("name: " + biography["name"]) 
print("hometown: " + biography["hometown"])
print("age: " + str(biography["age"]))


"""

Advanced Requirement

Ask the user for inputs instead of hardcoding them.

"""

name = input("Enter your name: ")          
hometown = input("Enter your hometown: ")  

# Handling multiple words and converting age to integer

try:
    age = int(input("Enter your age: "))
    
except ValueError:
    print("Invalid input.")   # Error message if the age is not a number
    


    





    



    
    