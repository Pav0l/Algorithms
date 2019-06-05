#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = -1
    if len(recipe) > len(ingredients):
        return 0
    # loop through recipe dict and for every key
    for rec in recipe:
        # loop throught ingredients dict to see if we have enough ingredients
        for ing in ingredients:
            # find the matching ingredient
            if rec == ing:
                # if you find an ingredient that we have enough off,
                if recipe[rec] <= ingredients[ing]:
                    # calculate how many times more we have and save it in an variable
                    how_many = ingredients[ing] // recipe[rec]
                    # if this value is less than previously saved value, save lower one instead
                    # (the lowest value is limiting factor)
                    if batches == -1 or how_many < batches:
                        batches = how_many

                # else you find an ingredient that we won't have enough off, stop both loops
                elif recipe[rec] > ingredients[ing]:
                    batches = 0
                    break

    return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 10}
    ingredients = {'milk': 198, 'butter': 52, 'flour': 10}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
