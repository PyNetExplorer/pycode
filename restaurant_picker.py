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

    count = 0
    while count < 3:
        # Randomly choose a restaurant
        chosen_restaurant = random.choice(restaurants)
    
        print("Welcome to the Tacoma Restaurant Chooser!")
        answer=input("Are you hungry? (yes/no)\n> ").lower()

        if answer == "yes":
            print("I suggest you try", chosen_restaurant)
            choice=input("Do you like this choice? (yes/no)\n> ").lower()
            if choice == "yes":
                print("Enjoy!")
                break
            elif choice == "no":
                count += 1
                if count < 3:
                    print("Really?? Well, than...")
                    continue
                else:
                    print("Sorry, choose it yourself then.")
                    break
            else:
                print("Type yes or no.")
        elif answer == "no":
            print("Well, come back when you are hungry!")
            break
        else:
            print("K, bye..")
            break

    
# Run the restaurant chooser app
choose_restaurant()
