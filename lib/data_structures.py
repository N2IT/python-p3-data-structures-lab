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
        sp = " "
        print(
            food['name'] + sp + "(" +
            (food['cuisine']) + ")" + sp + "|" +
            " Heat Level: " + 
            "🌶" * food['heat_level']
            )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
        cuisine_to_food_map = {
            "American": spicy_foods[1],
            "Thai": spicy_foods[0],
            "Sichuan": spicy_foods[2]
        }
        return cuisine_to_food_map[cuisine]

    
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            sp = " "
            print(
                food['name'] + sp + "(" +
                (food['cuisine']) + ")" + sp + "|" +
                " Heat Level: " + 
                "🌶" * food['heat_level']
                )

def get_average_heat_level(spicy_foods):
    # calculate total heat_levels and divide by spicy_foods length
    length = len(spicy_foods)
    return sum([h['heat_level'] for h in spicy_foods]) / length
    

def create_spicy_food(spicy_foods, spicy_food):

    spicy_foods.append(spicy_food)
    return spicy_foods
