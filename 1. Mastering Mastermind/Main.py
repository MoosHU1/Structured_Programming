'''
Bron 1: https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary-in-python
Bron 2: https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index

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
        temp = (item.title()).strip()
        input_user_list.append(temp)

    return input_user_list


def check(guess, color_code): #Checkt de gok op zwarte en blauwe pinnen
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
        return(all_options[0])


def cpu_guess():    # Pc raadt door speler gekozen kleuren
    player_colors = input_colors()
    beurt = 1

    algoritme_nummer = 2

    while True:
        if beurt == 10000:
            print("Jij hebt gewonnen")
            break

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

        else: # Random
            guess = [random_color(), random_color(), random_color(), random_color()]

        last_guess = guess

        if player_colors == guess:
            print("Ik gok {}".format(guess))
            print("Ik heb gewonnen!")
            break

        black_pin = (check(guess, player_colors))[0]
        white_pin = (check(guess, player_colors))[1]
        print("Ik gok {}\n{} Goede kleur en goede plek\n{} "
              "Goede kleur en verkeerde plek\n".format(guess, black_pin, white_pin))

        beurt += 1


def start():
    a = input("Wil je raden of  kleuren keizen [R/K]: ")

    if a == "R" or a == "r":
        player_guess()
    if a == "K" or a == "k":
        cpu_guess()



create_all_options_list()
start()