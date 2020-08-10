from typing import List, Tuple, Dict


def get_ingredients(ingredient: str, count: int, book: Dict[str, Dict[str, int]]):
    if ingredient not in book:
        return {ingredient: count}

    next_ings = {}

    recept = book[ingredient]
    for inner_ingre in recept:
        inner_count = recept[inner_ingre]
        next_ings[inner_ingre] = inner_count * count

    res = {}
    for name in next_ings:
        ings = get_ingredients(name, next_ings[name], book)
        for n in ings:
            if res.get(n) is None:
                res[n] = ings[n]
            else:
                res[n] += ings[n]

    return res


def build_list(
    bludos: Dict[str, int],
    book: Dict[str, Dict[str, int]],
    inventory: Dict[str, int]
) -> List[Tuple[str, int]]:
    book['__COOK__'] = bludos

    ingredients = get_ingredients('__COOK__', 1, book)

    for name in inventory:
        if name in ingredients:
            ingredients[name] -= inventory[name]
            if ingredients[name] < 0:
                ingredients[name] = 0
    ingredients = {name: ingredients[name]
                   for name in ingredients if ingredients[name] > 0}

    ingredients = [(name, ingredients[name]) for name in ingredients]
    ingredients = sorted(ingredients, key=lambda el: el[0])

    return ingredients


def main():
    x = int(input())
    for _ in range(x):
        n, k, f = map(lambda x: int(x), input().split(" "))
        bludos = {}
        for _ in range(n):
            bludo, count = input().split(" ")
            count = int(count)
            bludos[bludo] = count

        book = {}
        for _ in range(k):
            name, r = input().split(" ")
            r = int(r)
            book[name] = {}
            for _ in range(r):
                ingredient, count = input().split(" ")
                count = int(count)
                book[name][ingredient] = count

        inventory = {}
        for _ in range(f):
            name, count = input().split(" ")
            count = int(count)
            inventory[name] = count

        res = build_list(bludos, book, inventory)
        for name, count in res:
            print(f"{name} {count}")


if __name__ == "__main__":
    main()
