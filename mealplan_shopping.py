import json
import ada_io

shopping_list = {}
meals_type = ["breakfast", "lunch"]  # shorter version for testing purposes
week_days = ["Saturday", "Sunday"]  # shorter version for testing purposes
# meal_basis = ["meat"] #shorter version for testing purposes
#week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# meals_type = ["breakfast", "lunch", "dinner"]
meal_basis = {"1": "meat", "2": "vege", "3": "fish"}
# meal_breakfast = {"1": {"name": "yoghurt and nuts", "ingredients": {"yoghurt": 100, "nuts": 50, "cinnamon": 3}}, "2": {"name": "fruits and nuts", "ingredients": {"kiwi": 1, "banana": 1, "pear": 1, "nuts": 50}}}
meal_breakfast = {"1": "yoghurt and nuts", "2": "fruits and nuts", "3": "carrot and nuts", "4": "grapefruit and rolls",
                  "5": "buckwheat porridge", "6": "millet porridge", "7": "strudel", "8": "poppy pasta"}
# meal_MEAT = {"1": {"name":"egg with bryndza", "ingredients": {"egg": 2, "bryndza": 50} } , "2": {"name": "turkey with celery", "ingredients":{ "turkey meat": 150, "celery": 200 }}}
meal_MEAT = {"1": "egg with bryndza", "2": "turkey with celery", "3": "meat balls and veggie", "4": "sausages",
             "5": "carbonara", "6": "chicken and veggie"}
meal_VEGE = {"1": "zucchini with cheese", "2": "broccoli with cheese or egg", "3": "beetroot", "4": "vegetable soup",
             "5": "pasta and kohlrabi", "6": "carrot goulash", "7": "cous-cous", "8": "poppy pasta"}
meal_FISH = {"1": "cod with frozen vege", "2": "salmon with vege"}
chosen_meals = []
chosen_dish = 0
# ingredients loaded from JSON
ingredients = {}


##ingredients written in PyCharm
# ingredients = { meal_breakfast["1"]: {"yoghurt": 100, "nuts": 50, "cinnamon": 3}, meal_breakfast["2"]: {"kiwi": 1, "banana": 1, "pear": 1, "nuts": 50}, meal_MEAT["1"]: {"egg": 2, "bryndza": 50}, meal_MEAT["2"]: {"turkey meat": 150, "celery": 200}, meal_VEGE["1"]: {"zucchini": 0.5, "cheese": 100}, meal_VEGE["2"]:{"broccoli": 300, "cheese": 100} , meal_FISH["1"]: {"cod": 200, "vege": 200}, meal_FISH["2"]: {"salmon": 150, "vege": 250} }

def make_shopping_list():
    shopping_list = {"a": 100}
    print(shopping_list)


def choose_basis():
    for meal_basis_no in meal_basis:
        print(f"{meal_basis_no}: {meal_basis[meal_basis_no]}")
    basis = input(f"Choose number: ")
    if basis == "1":
        meal_basis_chosen = meal_MEAT
    elif basis == "2":
        meal_basis_chosen = meal_VEGE
    elif basis == "3":
        meal_basis_chosen = meal_FISH
    else:
        print("Try again")
        choose_basis()
    return meal_basis_chosen


def get_meal_plan():
    print("\nYour mealplan is: ")
    for i in chosen_meals:
        print(i)


def read_ingredients():
    #   Reading recipes from file
    with open("aux_files/recipe_book.json", "r", encoding="utf-8") as file:
        recipe_book = json.load(file)
    return recipe_book


ingredients = read_ingredients()
chosen_dish
print("Let's get this over with!")
persons = input("How many persons will eat?")
for day in week_days:
    for meal in meals_type:
        print(f"\n What would you like for a {day}'s {meal} ?")
        if meal != "breakfast":
            meal_basis_chosen = choose_basis()
            chosen_dish = 0  # for program to enter "while not" the "chosen_dish" has to be something out of "meal_basis_chosen"'s range
            while not chosen_dish in meal_basis_chosen:
                print(f"\nChoose dish for {day}:")
                for meal in meal_basis_chosen:
                    print(f'{meal} : {meal_basis_chosen[meal]}')
                chosen_dish = input(f"Choose one: ")  # before ingredients were part of meals
                # chosen_dish = input( f"Choose one number: " ) #ingredients added to meal list
            chosen_meals.append(meal_basis_chosen[chosen_dish])
        else:
            for breakfast in meal_breakfast:
                print(f'{breakfast} : {meal_breakfast[breakfast]}')
            chosen_meals.append(meal_breakfast[input("Number: ")])  # before ingredients were in "meal_breakfast"
            # chosen_meals.append( meal_breakfast[ input(f"Number of breakfast choice: ") ]["name"] ) #ingredients in "meal_breakfast
print("\n----------------------------------------")
print("Your needed ingredients are:")
chosen_meals_SET = set(chosen_meals)
for current_meal in chosen_meals_SET:
    print(f"\n{current_meal} for {chosen_meals.count(current_meal)} times")
    for current_ingredient in ingredients[current_meal]:
        if ingredients[current_meal][current_ingredient] < 10:
            unit = "pcs"
        else:
            unit = "g"
        print(
            f"{current_ingredient} :{ingredients[current_meal][current_ingredient] * chosen_meals.count(current_meal) * int(persons)} {unit}")
        ada_io.shop_upload(
            f"{current_ingredient}:{ingredients[current_meal][current_ingredient] * chosen_meals.count(current_meal) * int(persons)}")
