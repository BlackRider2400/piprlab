from matplotlib import pyplot as plt
import recipe


def sort_recipes(calories, labels):
    # @TODO write function to sort dishes according to their calories

    dictionary = dict(zip(calories, labels))

    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

    return sorted_dict.keys(), sorted_dict.values()


def plot_menu(menu):
    labels = []
    calories = []
    for _recipe in menu.recipes:
        labels.append(str(_recipe))
        calories.append(_recipe.get_kcal_per_portion())
    calories, labels = sort_recipes(calories, labels)
    # @TODO Prepare a Pie chart with calories from different dishes
    plt.figure(figsize=(8, 8))
    plt.pie(calories, labels=labels, autopct='%1.1f%%', startangle=140)
    title = f"Wigilijne kalorie: {sum(calories)}"
    plt.title(title, fontdict={"fontsize": 'xx-large'})
    plt.show()


if __name__ == "__main__":
    test_recipes = [
        recipe.Recipe({"label": "Kapusta",
                       "ingredientLines": "Kapusta",
                       "calories": 100,
                       "yield": 5}),
        recipe.Recipe({"label": "Pierogi",
                       "ingredientLines": "maka, woda, farsz",
                       "calories": 400,
                       "yield": 2}),
        recipe.Recipe({"label": "Barszcz",
                       "ingredientLines": "buraki, woda, uszka",
                       "calories": 500,
                       "yield": 5})
    ]
    test_menu = recipe.Menu(test_recipes)
    plot_menu(test_menu)
