import random

getal = random.randrange(1,11)

while True:
    gok = int(input("Gok een getal tussen 1 en 10: "))
    if gok == getal:
        print("Goedzo")
        break
    else:
        print("Incorrect, probeer opnieuw")