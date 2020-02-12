'''Zwart is goed op de goede plek, wit is goed op de verkeerde plek'''
import random

colors = {'w': 'Wit',
           'z': 'Zwart',
           'b': 'Blauw',
           'g': 'Groen',
           'r': 'Rood',
           'o': 'oranje'
           }

def player_guess():
    cpu_colors = random.choice(colors)
    print(cpu_colors)


# def cpu_guess():
#
#
#





def start():
    a = input("Wil je raden of  kleuren keizen [R/K]: ")

    if a == "R" or "r":
        player_guess()
    if a == "K" or "k":
        cpu_guess()


start()