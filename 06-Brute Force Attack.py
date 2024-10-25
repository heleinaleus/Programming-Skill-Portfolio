"""

Exercise 6: Brute Force Attack

This program simulates a password entry system that keeps asking until the 
password is correct.

"""

# Setting the correct password

correct_password = "12345"

# Initialize the password variable to enter the loop

password = ""

# Asking for the password until the correct one is entered

while password != correct_password: 
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")

    else:    
        print("Incorrect password.")
    
"""

Optional Requirements

Adding a maximum of 5 password attempts.

"""

# Defining the correct password

correct_password = "12345"
attempts = 0

# Asking for password until the correct or max attempts is reached

while attempts < 5:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        
        
    
    else: 
        attempts += 1 # Increase attempt count
        print(f"Incorrect password. Attempts remaining: {5 - attempts}") # Shows remaining attempts
  
# If the max attempt is reached, deny access

if attempts == 5:
    print("Too many failed attempts! Authorities have been alerted.")
    






