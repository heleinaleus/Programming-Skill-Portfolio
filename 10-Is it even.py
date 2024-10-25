"""

Exercise 10: Is it even? 

This program tests if a value is even or odd.

"""

# Function to check if a number is even or odd

def check_even_odd(number):
    
    if (number % 2) == 0:
        return("The number is even.")
        
    else:
        return("The number is odd.")

# Main function to get user input and call the check function

def main():
    
    number = int(input("Enter a number: "))
    print(check_even_odd(number))
    
# Running the main function

if __name__ == "__main__":
    main()
    


