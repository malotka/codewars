def cakes(recipe, available):
    # variable to check how many times you can cook a pie
    pie = []
    #jesli nie ma skladnikow - zwroc 0
    if len(available) == 0:
        print("No ingredients - No cake!")
        return 0
    # jesli w przepisie jest wiecej skladnikow niz dostepnych - zwroc 0
    elif len(recipe) > len(available):
        print("U no have ingredients - No cake!")
        return 0
    # jesli jest wiecej dostepnych to porownaj dostepne i przepis
    else:
        for value in available.keys():
            for key in recipe.keys():

                if value == key:
                    pie.append(available[value] // recipe[key])
        print("You can bake ", min(pie), " cakes today!")
    return min(pie)



if __name__ == '__main__':

    recipe = {'flour': 400, 'eggs': 4, 'sugar': 150}
    available = {'flour': 1200, 'eggs': 3}

    cakes(recipe, available)

