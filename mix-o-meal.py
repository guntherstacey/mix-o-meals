def read_file(text_file):
  if ".txt" in text_file:
    recipe_options = open(text_file)
    opened_recipe_options = (recipe_options.read())
    return opened_recipe_options
  else:
    print ("Invalid Input: Not a .txt file")

def user_preferences():
    meal_plan_preferences = []
    print("Welcome to Mix-O-Meals!")
    print("-------------")
    print("This wonderful meal-planning assistant allows you to choose the number and type of meals you would like.")
    print("You can also specify if you would like side dishes, desserts, and/or a bonus dish included with your meal plan.")
    print("Please answer the following:")
    print("-------------")
    while True:
        food_type_preference = input("What kind of meals would you like?  Italian, Mexican, Indian, Korean, Thai, or Combination?").lower()
        if food_type_preference == "italian":
            print("Grazi!  Italian sounds great!")
            meal_plan_preferences.append(food_type_preference)
            break
        elif food_type_preference == "mexican":
            print("Gracias!  I like Mexican too!")
            meal_plan_preferences.append(food_type_preference)
            break
        elif food_type_preference == "indian":
            print("Awesome!  Indian cooking has amazing spices!")
            meal_plan_preferences.append(food_type_preference)
            break
        elif food_type_preference == "korean":
            print("Delicious!  Kimchi makes everything taste better!")
            meal_plan_preferences.append(food_type_preference)
            break
        elif food_type_preference == "thai":
            print("Yum!  Thai curry is one of my favorites!")
            meal_plan_preferences.append(food_type_preference)
            break
        elif food_type_preference == "combination":
            print("Great!  A combination of foods can be a great way to try new dishes!")
            meal_plan_preferences.append(food_type_preference)
            break
        else:
            print("Please choose one of the above food types.")
    print("-------------")
    while True:
        side_dish_preference = input("Would you like side dish ideas to go with your meals?").lower()
        if side_dish_preference == "yes":
            print("Awesome!  Side dishes are a great addition!")
            meal_plan_preferences.append(side_dish_preference)
            break
        elif side_dish_preference == "no":
            print("Ok.  These dishes stand really well on their own too!")
            meal_plan_preferences.append(side_dish_preference)
            break
        else:
            print("Please answer yes or no.")
    print("-------------")
    while True:
        dessert_preference = input("How about dessert?").lower()
        if dessert_preference == "yes":
            print("Yummy!  Dessert is the best part of the meal!")
            meal_plan_preferences.append(dessert_preference)
            break
        elif dessert_preference == "no":
            print("Ok.  Cutting out the sweets can be good sometimes!")
            meal_plan_preferences.append(dessert_preference)
            break
        else:
            print("Please answer yes or no.")
    print("-------------")
    while True:
        bonus_preference = input("And what about that bonus dish?").lower()
        if bonus_preference == "yes":
            print("Ooh...A bonus mystery dish!  How exciting!")
            meal_plan_preferences.append(bonus_preference)
            break
        elif bonus_preference == "no":
            print("Ok.  Maybe next time.")
            meal_plan_preferences.append(bonus_preference)
            break
        else:
            print("Please answer yes or no.")
    print("-------------")
    while True:
        meal_number_preference = input("And finally, how many meals would you like for your meal plan?  You can choose between 1 and 10 meals.")
        if int(meal_number_preference) >= 1 and int(meal_number_preference) <= 10:
            print("Sounds like a good number to me!")
            meal_plan_preferences.append(str(meal_number_preference))
            break
        else:
            print("Please enter a number between 1 and 10")
    print("-------------")
    print("Awesome!  Now that we have your meal plan preferences, let's put together a meal plan for you!")
    print("-------------")
    return meal_plan_preferences

def choose_file(meal_plan_preferences):
    if meal_plan_preferences[0] == "italian":
        meal_plan_file = read_file("italian-recipes.txt")
    elif meal_plan_preferences[0] == "mexican":
        meal_plan_file = read_file("mexican-recipes.txt")
    elif meal_plan_preferences[0] == "indian":
        meal_plan_file = read_file("indian-recipes.txt")
    elif meal_plan_preferences[0] == "korean":
        meal_plan_file = read_file("korean-recipes.txt")
    elif meal_plan_preferences[0] == "thai":
        meal_plan_file = read_file("thai-recipes.txt")
    elif meal_plan_preferences[0] == "combination":
        meal_plan_file = read_file("combination-recipes.txt")
    else:
        print("Food preference not recognized")
    return meal_plan_file

import random
    
def meal_planner(meal_plan_file, meal_plan_preferences):
    meal_plan_file = meal_plan_file.splitlines()
    mealPlan = []
    number_of_meals = int(meal_plan_preferences[-1])
    mainDishes = meal_plan_file[meal_plan_file.index("mainDishes") + 1:meal_plan_file.index("sideDishes")]
    mainDishes = random.sample(mainDishes, number_of_meals)
    mealPlan.append(mainDishes)
    if meal_plan_preferences[1] == "yes":
        sideDishes = meal_plan_file[meal_plan_file.index("sideDishes") + 1:meal_plan_file.index("desserts")]
        sideDishes = random.sample(sideDishes, number_of_meals)
        mealPlan.append(sideDishes)
    if meal_plan_preferences[2] == "yes": 
        desserts = meal_plan_file[meal_plan_file.index("desserts") + 1:meal_plan_file.index("extras")]
        desserts = random.sample(desserts, number_of_meals)
        mealPlan.append(desserts)
    if meal_plan_preferences[3] == "yes":
        extras = meal_plan_file[meal_plan_file.index("extras") + 1:]
        extras = [random.choice(extras)]
        mealPlan.append(extras)
    return mealPlan
def meal_plan_dictionary(mealPlan):
    meal_plan_dictionary = {"Main Dishes" : "", "Side Dishes" : "", "Desserts" : "", "Bonus Dish" : ""}
    meal_plan_dictionary["Main Dishes"] = mealPlan[0]
    meal_plan_dictionary["Side Dishes"] = mealPlan[1]
    meal_plan_dictionary["Desserts"] = mealPlan[2]
    meal_plan_dictionary["Bonus Dish"] = mealPlan[3]
    return meal_plan_dictionary


meal_plan_preferences = user_preferences()
meal_plan_file = choose_file(meal_plan_preferences)
mealPlan = meal_planner(meal_plan_file, meal_plan_preferences)
meal_plan_dictionary = meal_plan_dictionary(mealPlan)
print(meal_plan_dictionary)