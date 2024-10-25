"""

Exercise 5: Days of the Month

This program tells the user how many days are in a specific month using a 
dictionary.

"""

# Create a dictionary to store month numbers and days

months = {
    
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    
}

# Asking the user for the month number 

month = int(input("Enter the month number (1-12)"))

# Checking if the input is valid and printing the number of days

if 1 <= month <= 12:
    print("Number of days: " + str(months[month]))
    
else: 
    print("Invalid month number.")
    
