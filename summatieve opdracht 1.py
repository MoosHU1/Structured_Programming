grootte = int(input("Hoe groot is de piramide"))

def for_loop(grootte):
    for x in range(grootte):
        print(x*("*"))

    for x in range(grootte, 0, -1):
        print(x*("*"))


#for_loop(grootte)

def while_loop(grootte):
    x = grootte
    y = 1

    while y != grootte:
        print(y*"*")
        y += 1

    while x != 0:
        print(x*"*")
        x = x-1

#while_loop(grootte)


def for_loop_andersom(grootte):
    def for_loop(grootte):
        pass
    for x in range(grootte):
        print(('{:>'+str(grootte)+'}').format(x *("*")))

    for x in range(grootte, 0, -1):
        print(('{:>'+str(grootte)+'}').format(x *("*")))

for_loop_andersom(grootte)