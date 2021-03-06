from src.util import *

lines = parse_string_list_from_file(INPUT)

ingredients = set()
allergens = set()
orig_ingred = {}
orig_aller = {}
count_ingred = {}
count_aller = {}
all_aller = {}
all_ingred = {}
pos_aller = {}
pos_ingred = {}
for line in lines:
    [in_list, aller_list] = line.split("(")
    ingredients_list = in_list.strip().split(" ")
    allergens_list = aller_list[9:-1].split(",")
    for ingred in ingredients_list:
        ingredients.add(ingred)
        count_ingred.setdefault(ingred, 0)
        count_ingred[ingred] += 1
        orig_ingred.setdefault(ingred, []).append([a.strip() for a in allergens_list])
        for aller in allergens_list:
            aller = aller.strip()
            all_aller.setdefault(ingred, []).append(aller)
            pos_aller.setdefault(ingred, set()).add(aller)
    for aller in allergens_list:
        aller = aller.strip()
        allergens.add(aller)
        orig_aller.setdefault(aller, []).append([i.strip() for i in ingredients_list])
        count_aller.setdefault(aller, 0)
        count_aller[aller] += 1
        for ingred in ingredients_list:
            all_ingred.setdefault(aller, []).append(ingred)
            pos_ingred.setdefault(aller, set()).add(ingred)


print("ingredients:", ingredients)
print("allergens:", allergens)
print("orig_ingred:", orig_ingred)
print("orig_aller:", orig_aller)
print("count_ingred:", count_ingred)
print("count_aller:", count_aller)
print("all_ingred:", all_ingred)
print("all_aller:", all_aller)
print("pos_ingred:", pos_ingred)
print("pos_aller:", pos_aller)
print("")

non_aller_ingreds = []
for ingred in ingredients:
    rem_from_allers = []
    for aller in pos_aller[ingred]:
        for ings in orig_aller[aller]:
            if not ingred in ings:
                rem_from_allers.append(aller)
    for rem_from_aller in rem_from_allers:
        if rem_from_aller in pos_aller[ingred]:
            pos_aller[ingred].remove(rem_from_aller)

print("pos_aller:", pos_aller)
print("")

non_allers = [a for a in pos_aller.keys() if len(pos_aller[a]) == 0]

summed = sum(len(orig_ingred[a]) for a in non_allers)
print(summed)