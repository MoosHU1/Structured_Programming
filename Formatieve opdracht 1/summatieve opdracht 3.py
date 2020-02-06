input_items = input("Geef je items gescheiden door komma: ")
lijst = input_items.split(",")



def count(lijst, item):
    aantal = 0
    for x in lijst:
        if x == item:
            aantal += 1

    return aantal

def verschil(lijst):
    grootste = 0
    for x in range(0, len(lijst)-1):
        v = int(lijst[x+1]) - int(lijst[x])
        if v > grootste:
            grootste = v

    print(grootste)

def voldoet(lijst):
    if count(lijst, str(1)) > count(lijst, str(0)) and count(lijst, str(0)) <= 12:
        print("Voldoet")
    else:
        print("Voldoet niet")

#count(lijst, str(input("Hoevaak komt dit item voor: ")))
#verschil(lijst)
voldoet(lijst)