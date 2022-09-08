import pprint

with open('cooking_recipes.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()


def create_dict(read_file):
    cook_book = {}
    n = 0
    for i in range(len(read_file)):
        if i == n:
            dish_name = read_file[i].replace('\n','')
            cook_book[dish_name] = []
            n += int(read_file[i+1]) + 3
        else:
            str_replace = read_file[i].replace('\n','')
            if len(str_replace) > 1:
                str_split = str_replace.split('|')
                cook_book[dish_name].append({
                    'ingredient_name': str_split[0],
                    'quantity': str_split[1],
                    'measure': str_split[2]
                })
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for dish in dishes:
        ingredients = create_dict(content).get(dish)
        for ingredient in ingredients:
            ingredient_name = ingredient.get('ingredient_name')
            if ingredient_name not in ingredient_dict.keys():
                ingredient_dict.setdefault(ingredient_name, {
                    'measure': ingredient.get('measure'),
                    'quantity': int(ingredient.get('quantity')) * person_count
                })
            else:
                quantity = int(ingredient_dict.get(ingredient_name).get('quantity')) + \
                           int(ingredient.get('quantity')) * person_count
                ingredient_dict[ingredient_name] = {
                    'measure': ingredient.get('measure'),
                    'quantity': quantity}
    return ingredient_dict

pprint.pprint(get_shop_list_by_dishes(['Омлет','Фахитос'], 1))