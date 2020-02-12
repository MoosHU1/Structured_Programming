'''Zwart is goed op de goede plek, wit is goed op de verkeerde plek
Bron 1: https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary-in-python


'''
import random

colors = {'w': 'Wit',
           'z': 'Zwart',
           'b': 'Blauw',
           'g': 'Groen',
           'r': 'Rood',
           'o': 'oranje'
           }


def random_color():
    return random.choice(list(colors.keys()))


def player_guess():
    cpu_colors = [random_color(), random_color(), random_color(), random_color()]
    print(cpu_colors)


# def cpu_guess():
#
#
#





def start():
    a = input("Wil je raden of  kleuren keizen [R/K]: ")

    if a == "R" or a == "r":
        player_guess()
    if a == "K" or a == "k":
        cpu_guess

start()