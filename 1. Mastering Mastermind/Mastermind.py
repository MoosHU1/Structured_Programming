''''
Bron 1: https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index

Eerste algoritme: 2.1 A simple strategy http://www.philos.rug.nl/~barteld/master.pdf
Tweede algoritme: Eigen algoritme
Derde algoritme: Statisch algoritme, één na laatste alinea http://140.177.205.23/Mastermind.html.
                 Het verwijderen van niet mogelijke opties zoals bij algoritme 1 geeft niet altijd
                 een oplossing in 7 beurten. Ik kon ook geen pseudocode of andere code vinden die
                 dit algoritme gebruikt, dus ik heb zelf wat dingen bijgevoegd.
'''
import random
from algoritmes import *

colors = ['Wit', 'Zwart', 'Blauw', 'Groen', 'Rood', 'Oranje']


def random_color(): # Kies een willekeurige kleur
    return random.choice(colors)


def input_colors(): # Gok van speler opvragen of kleuren van speler opvragen
    guess_list = []
    input_user_list = []

    input_user = input("Geef 4 kleuren op (Wit, Zwart, Blauw, Groen, Rood, Oranje) gescheiden door een komma:")
    list_colors = input_user.split(",")
    for item in list_colors:
        temp = (item.title()).strip()   # Haalt spaties weg en maakt de eerste letter een hoofdletter
        if temp[0] == 'w' or temp[0] == 'W':
            temp = 'Wit'
        if temp[0] == 'z' or temp[0] == 'Z':
            temp = 'Zwart'
        if temp[0] == 'b' or temp[0] == 'B':
            temp = 'Blauw'
        if temp[0] == 'g' or temp[0] == 'G':
            temp = 'Groen'
        if temp[0] == 'r' or temp[0] == 'R':
            temp = 'Rood'
        if temp[0] == 'o' or temp[0] == 'O':
            temp = 'Oranje'
        input_user_list.append(temp)

    return input_user_list


def player_guess(): # Speler raadt door pc gekozen kleuren
    cpu_colors = [random_color(), random_color(), random_color(), random_color()]

    beurt = 0

    while True:
        if beurt == 12:
            print("Je beurten zijn op")
            break

        guess = input_colors()
        print(guess)
        if guess == cpu_colors:
            print("Je hebt gewonnen!")
            break

        black_pin = (check(guess, cpu_colors))[0]
        white_pin = (check(guess, cpu_colors))[1]
        print("{} Goede kleur en goede plek\n{} Goede kleur en verkeerde plek".format(black_pin, white_pin))
        beurt += 1


def cpu_guess(algoritme_nummer):    # Pc raadt door speler gekozen kleuren
    player_colors = input_colors()
    beurt = 1

    while True:
        if beurt == 12:
            print("Jij hebt gewonnen")
            print("\n")
            start()

        if algoritme_nummer == 1: # Algoritme nummer 1
            if beurt == 1:
                guess = ['Wit', "Wit", "Blauw", "Blauw"]
            else:
                guess = algoritme_1(last_guess, black_pin, white_pin)

        elif algoritme_nummer == 2: # Algoritme nummer 2
            if beurt == 1:
                guess = ["Wit", "Wit", "Zwart", "Zwart"]
            else:
                guess = algoritme_2(last_guess, black_pin, white_pin, beurt)

        elif algoritme_nummer == 3: # Algoritme nummer 3
            if beurt == 1:
                guess = ["Wit", "Zwart", "Zwart", "Wit"]
            else:
                guess = algoritme_3(last_guess, black_pin, white_pin, beurt)

        else: # Random
            guess = [random_color(), random_color(), random_color(), random_color()]

        last_guess = guess

        if player_colors == guess:
            print("Ik gok {}".format(guess))
            print("Ik heb gewonnen! In {} beurten".format(beurt))
            print("\n")
            start()

        black_pin = (check(guess, player_colors))[0]
        white_pin = (check(guess, player_colors))[1]
        print("Ik gok {}\n{} Goede kleur en goede plek\n{} "
              "Goede kleur en verkeerde plek\n".format(guess, black_pin, white_pin))
        input()

        beurt += 1


def start():
    create_all_options_list()
    while True:
        try:
            a = input("Wil je codemaker of codebreaker spelen [M/B]?: ")
        except:
            print("Ongeldige invoer, probeer opnieuw\n")
        else:
            if a == "M" or a == "m":
                while True:
                    try:
                        algoritme_nummer = int(input("Welk algoritme wil je dat ik gebruik?(1,2,3):"))
                    except:
                        print("Dat is geen getal, probeer opnieuw")
                    else:
                        if algoritme_nummer > 3 or algoritme_nummer < 1:
                            print("Ongeldig getal, probeer opnieuw")
                        else:
                            break
                cpu_guess(algoritme_nummer)
            elif a == "B" or a == "b":
                player_guess()
            else:
                print("Ongeldige invoer, probeer opnieuw\n")

def explanation():
    print("Welkom bij deze mastermind applicatie")
    print("Je kan straks de optie kiezen om codebreaker of codemaker te spelen.")
    print("Als codebreaker probeer je de kleurencombinatie van de computer te raden.")
    print("Als codemaker kies je een kleurencombinatie die de computer gaat raden dmv een algoritme.")
    print("Bij het invoeren van kleuren kan je ook alleen de eerst letter invoeren. Bv. 'w' i.p.v. 'wit'.")
    print("Druk bij elke gok van de computer op enter om naar de volgende gok te gaan.\n\n")
    start()


explanation()

