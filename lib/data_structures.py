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
    {
        "name": "Hamburger",
        "cuisine": "American",
        "heat_level": 1,
    }
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
            food['name'] + sp +
            "(" + food['cuisine'] + ")" + sp + "|" +
            " Heat Level: " + 
            "🌶" * food['heat_level']
            )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    # More dynamic function for searching through list of dicts
    def check_cuisine(food):
        if food['cuisine'] == cuisine:
            return True
        else:
            return False
        
    filtered_food = filter(check_cuisine, spicy_foods)
    for food in filtered_food:
        # print(food)
        return food

# get_spicy_food_by_cuisine(spicy_foods, "American")

    

        
    # return [food for food in spicy_foods if food['cuisine'] == cuisine]
    # use find / filter
    # return new_list
    # ipdb.set_trace()
    
    # returns the single dict once logic is met
    # for food in spicy_foods:
    #     if food['cuisine'] == cuisine:
    #         return food
        
        # This was original answer that passed test but is not dynamic; if there are more than 1 of the same type of cuisine in db
        # cuisine_to_food_map = {
        #     "American": spicy_foods[1],
        #     "Thai": spicy_foods[0],
        #     "Sichuan": spicy_foods[2]
        # }
        # return cuisine_to_food_map[cuisine]

        
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

# create_spicy_food(spicy_foods, {
#     "name": "Hamburger",
#     "cuisine": "American",
#     "heat_level": 1
# })
