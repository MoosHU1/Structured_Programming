'''
Bron 1: https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index

Eerste algoritme: 2.1 A simple strategy http://www.philos.rug.nl/~barteld/master.pdf
Tweede algoritme: Eigen algoritme
Derde algoritme: Statisch algoritme, één na laatste alinea http://140.177.205.23/Mastermind.html.
                 Om niet mogelijke combinaties te elimineren heb ik gebruik gemaakt van hetzelfde
                 principe als bij algoritme 1.

'''
import random

# colors = {'Wit': 'w',
#            'Zwart': 'z',
#            'Blauw': 'b',
#            'Groen': 'g',
#            'Rood': 'r',
#            'Oranje': 'o'
#            }

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


def check(guess, color_code):   # Checkt de gok op zwarte en blauwe pinnen
    black_pin = 0
    white_pin = 0

    for i in range(0, 4):
        if color_code[i] == guess[i]:
            black_pin += 1

        elif color_code[i] in guess:
            white_pin += 1

    return [black_pin, white_pin]


def player_guess(): # Speler raadt door pc gekozen kleuren
    cpu_colors = [random_color(), random_color(), random_color(), random_color()]
    print(cpu_colors)

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


def create_all_options_list():
    global all_options
    all_options = []
    for color_1 in colors:  # Stop alle opties in de lijst
        for color_2 in colors:
            for color_3 in colors:
                for color_4 in colors:
                    all_options.append([color_1, color_2, color_3, color_4])


def algoritme_1(last_guess, black_pin, white_pin):

    len_before = len(all_options)

    for item in all_options:
        if check(last_guess, item) != [black_pin, white_pin]:
            all_options.remove(item)

    len_after = len(all_options)
    
    if len_before == len_after:
        return all_options[(all_options.index(last_guess))+1] # Gaat de hele lijst af als de lijst niet meer verandert
    else:
        return all_options[0]


def algoritme_2(last_guess, black_pin, white_pin, beurt): # Eigen algoritme

    all_options.remove(last_guess)
    if [black_pin, white_pin] == [0, 0]:
        for a in range(4):
            for item in all_options:
                if last_guess[a] in item:
                    all_options.remove(item)

    if beurt == 2:
        return ["Blauw", "Blauw", "Groen", "Groen"]

    elif beurt == 3:
        return ["Rood", "Rood", "Oranje", "Oranje"]

    else:
        return all_options[0]


def algoritme_3(last_guess, black_pin, white_pin, beurt):   # Statisch algoritme

    for item in all_options:
        if check(last_guess, item) != [black_pin, white_pin]:
            all_options.remove(item)

    if beurt == 2:
        return ["Zwart", "Blauw", "Rood", "Groen"]

    elif beurt == 3:
        return ["Blauw", "Blauw", "Wit", "Wit"]

    elif beurt == 4:
        return ["Groen", "Rood", "Zwart", "Groen"]

    elif beurt == 5:
        return ["Rood", "Oranje", "Rood", "Oranje"]

    elif beurt == 6:
        return ["Oranje", "Oranje", "Groen", "Blauw"]

    else:
        return(all_options[0])


def cpu_guess():    # Pc raadt door speler gekozen kleuren
    player_colors = input_colors()
    beurt = 1

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
    while True:
        try:
            a = input("Wil je codemaker of codebreaker spelen [M/B]?: ")
        except:
            print("Ongeldige invoer, probeer opnieuw\n")
        else:
            if a == "M" or a == "m":
                cpu_guess()
            elif a == "B" or a == "b":
                player_guess()
            else:
                print("Ongeldige invoer, probeer opnieuw\n")

def explanation():
    print("Welkom bij deze mastermind applicatie")
    print("Je kan straks de optie kiezen om codebreaker of codemaker te spelen.")
    print("Als codebreaker probeer je de kleurencombinatie van de computer te raden.")
    print("Als codemaker kies je een kleurencombinatie die de computer gaat raden dmv een algoritme.")
    print("Bij het invoeren van kleuren kan je ook alleen de eerst letter invoeren. Bv. 'w' i.p.v. 'wit'\n\n")
    start()

create_all_options_list()
explanation()