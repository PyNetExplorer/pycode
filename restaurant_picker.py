import random

def choose_restaurant():
    # List of restaurants in Tacoma
    restaurants = [
        "Matador",
        "Trapper's",
        "Harvest Buffet",
        "Zen Ramen and Sushi Burrito",
        "Farelli's",
        "Buffalo Wild Wings",
        "iPho",
        "Andale Mexican Restaurant",
        "@ Thai Restaurant",
        "Forbidden City"
    ]

    # Randomly choose a restaurant
    chosen_restaurant = random.choice(restaurants)
    
    print("Welcome to the Tacoma Restaurant Chooser!")
    answer=input("Are you hungry? yes/no\n>").lower()
    if answer == "yes":
        print("I suggest you try:", chosen_restaurant)
    elif answer == "no":
        print("Well, come back when you are hungry!")
    else:
        print("K, bye..")

# Run the restaurant chooser app
choose_restaurant()
