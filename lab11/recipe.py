import requests
import json
import plotter


def get_recipes(query, url, app_id, app_key):
    # @TODO request for the recipe with a given query. Try curl to figure out what is the structure
    list_of_recipes_objects = requests.get(f"{url}/search?q={query}&app_id={app_id}&app_key={app_key}").json()
    return list_of_recipes_objects


class Recipe:
    def __init__(self, data):
        self._name = data["label"]
        self._ingredients = data["ingredientLines"]
        self._kcal = data["calories"]
        self._portions = data["yield"]

    def get_kcal_per_portion(self):
        # @TODO compute the portion kcal per portion

        return self._kcal / self._portions

    def __str__(self):
        return self._name


class Menu:
    def __init__(self, recipes=None):
        self.recipes = recipes if recipes is not None else []

    def add_recipe(self, recipe):
        # @TODO add new recipe to the menu
        self.recipes.append(recipe)
        return None

    def get_menu_list(self):
        output_string = ""
        for idx, recipe in enumerate(self.recipes):
            output_string += f"{idx}. {recipe}\n"
        return output_string

    def get_num_dishes(self):
        return len(self.recipes)

    def __str__(self):
        return str(self.get_menu_list())


def main():
    # @TODO read url, id, key from json file
    with open("secrets.json") as file:
        lines = ""
        for i in file:
            lines += i.rstrip()
        data = json.loads(lines)
        url = data["url"]
        app_id = data["app_id"]
        app_key = data["app_key"]
    menu = Menu()
    n_dishes = 3
    while n_dishes > 0:
        print("What would You like to eat?")
        query = input()
        tmp_menu = Menu(get_recipes(query, url, app_id, app_key))
        if tmp_menu.get_num_dishes() == 0:
            print("No recipe with given name")
            continue
        print(tmp_menu)
        # @TODO write dish selection from the given list of recipes

        selection = int(input())
        menu.add_recipe(tmp_menu.recipes[selection])
        n_dishes -= 1

    print("Final menu:")
    print(menu)
    plotter.plot_menu(menu)


if __name__ == "__main__":
    main()
