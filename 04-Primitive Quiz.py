"""

Exercise 4: Primitive Quiz

This program asks the user a question, checks their answer, and gives feedback.

"""

# Ask the user for the capital of France

answer = input("What is the capital of France?")

# Checking the answer and providing feedback

if answer.lower() == "paris" :
    print("Correct!")   
    
else: 
    print("Wrong!")   
    
"""

Advanced Requirement

Make the program a quiz on 10 European capitals.

"""

# Dictionary of countries and their capitals

capitals = {
    
    'France': 'Paris', 'Italy': 'Rome', 'Germany': 'Berlin', 
    'Russia': 'Moscow', 'Austria': 'Vienna', 'Belgium': 'Brussels',
    'Greece': 'Athens', 'Latvia': 'Riga', 'Norway': 'Oslo', 
    'Netherlands': 'Amsterdam'
    
}

# Looping through each question in the quiz and providing feedback

for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}? ").lower()  # Ask user the capital for each country
    if answer == capital.lower():                                 
        print("Correct!")
        
    else:
        print("Wrong Answer.")
            


    
