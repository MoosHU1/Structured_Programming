'''Zwart is goed op de goede plek, wit is goed op de verkeerde plek'''
from termcolor import


def player_guess():




def cpu_guess():








def start():
    a = input("Wil je raden of  kleuren keizen [R/K]: ")

    if a == "R" or "r":
        player_guess()
    if a == "K" or "k":
        cpu_guess()

