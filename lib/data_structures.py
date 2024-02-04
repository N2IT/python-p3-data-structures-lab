spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [ n['name'] for n in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [ heat for heat in spicy_foods if heat['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    # print([ food['name'] + " " + "(" + food['cuisine'] + ")" +  " | " + "Heat Level: " + "🌶" * food['heat_level'] for food in spicy_foods])

    for food in spicy_foods:
        print(
            food['name'] + " " + "(" +
            (food['cuisine']) + ")" + " " + "|" +
            " Heat Level: " + 
            "🌶" * food['heat_level']
            )


def get_spicy_food_by_cuisine(typspicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
