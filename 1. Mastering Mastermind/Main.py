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

def random_color():
    return random.choice(colors)

def input_guess():
    guess_list = []
    input_user_list = []

    input_user = input("Geef 4 kleuren op (Wit, Zwart, Blauw, Groen, Rood, Oranje) gescheiden door een komma:")
    list_colors = input_user.split(",")
    for item in list_colors:
        temp = (item.title()).strip()
        input_user_list.append(temp)

    return input_user_list


def player_guess():
    cpu_colors = [random_color(), random_color(), random_color(), random_color()]
    #print(cpu_colors)

    beurt = 0

    while True:
        if beurt == 12:
            print("Je beurten zijn op")
            break

        black_pin = 0   # Goed op de goede plek
        white_pin = 0   # Goed op de verkeerde plek
        guess = input_guess()
        print(guess)
        if guess == cpu_colors:
            print("Je hebt gewonnen!")
            break

        for i in range(0, 3):
            if guess[i] == cpu_colors[i]:
                black_pin += 1

            elif guess[i] in cpu_colors:
                white_pin += 1

        print("{} Goede kleur en goede plek\n{} Goede kleur en verkeerde plek".format(black_pin, white_pin))
        beurt += 1


#def cpu_guess():








def start():
    a = input("Wil je raden of  kleuren keizen [R/K]: ")

    if a == "R" or a == "r":
        player_guess()
    if a == "K" or a == "k":
        cpu_guess

start()