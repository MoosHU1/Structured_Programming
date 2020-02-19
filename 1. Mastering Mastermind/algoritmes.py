colors = ['Wit', 'Zwart', 'Blauw', 'Groen', 'Rood', 'Oranje']


def check(guess, color_code):   # Checkt de gok op zwarte en blauwe pinnen
    black_pin = 0
    white_pin = 0

    for i in range(0, 4):
        if color_code[i] == guess[i]:
            black_pin += 1

        elif color_code[i] in guess:
            white_pin += 1

    return [black_pin, white_pin]


def create_all_options_list():
    global all_options
    all_options = []
    for color_1 in colors:  # Stop alle opties in de lijst
        for color_2 in colors:
            for color_3 in colors:
                for color_4 in colors:
                    all_options.append([color_1, color_2, color_3, color_4])


def algoritme_1(last_guess, black_pin, white_pin):
    all_options.remove(last_guess)

    for item in all_options:    # Verwijdert alle opties die niet mogelijk zijn
        if check(last_guess, item) != [black_pin, white_pin]:
            all_options.remove(item)

    else:
        return all_options[0]


def algoritme_2(last_guess, black_pin, white_pin, beurt):   # Eigen algoritme
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
    for item in all_options:    # Verwijdert alle opties die niet mogelijk zijn
        if check(last_guess, item) != [black_pin, white_pin]:
            all_options.remove(item)

    if white_pin == 4:
        for color in last_guess:
            for item in all_options:
                if color not in item:
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
        return all_options[0]
