from collections import defaultdict
from pprint import pprint
from functools import reduce


CONFIRMED = {}


def read_input(filename):
    allergens = defaultdict(list)
    all_foods = []
    with open(filename) as f:
        for line in f.read().splitlines():
            food, allergen = line.split(" (contains")
            food = set(food.split(" "))
            all_foods.append(food)
            for a in allergen.replace(")", "").strip().split(", "):
                allergens[a].append(set(list(food)))

    return allergens, all_foods


def get_confirmed_allergen(allergen, foods):
    conf = foods[0]
    for food_group in foods:
        conf &= food_group

    if len(conf) == 1:
        CONFIRMED[allergen] = conf.pop()
    return set(conf)


def find_food_allergens(allergens):

    for allergen, foods in allergens.items():
        conf = get_confirmed_allergen(allergen, foods)
        if len(conf) > 1:
            # print(CONFIRMED.values())
            conf = conf - set(CONFIRMED.values())
            if len(conf) == 1:
                CONFIRMED[allergen] = conf.pop()

    print(CONFIRMED)


def count_non_allergens(all_foods):
    total = 0
    for row in all_foods:
        total += len(row - set(CONFIRMED.values()))

    print(f"TOTAL: {total}")


if __name__ == "__main__":
    allergens, all_foods = read_input("example.txt")
    find_food_allergens(allergens)
    count_non_allergens(all_foods)

