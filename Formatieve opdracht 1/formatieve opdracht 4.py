def check(string):
    omgedraad_list = []
    for x in range(len(string)-1, -1, -1):
        omgedraad_list.append(string[x])

    omgedraaid = ''.join(omgedraad_list)

    if omgedraaid == string:
        print("Het is een palindroom")
    else:
        print("Het is geen palindroom")

check(input("Geef string:"))

'''Ik kon geen library vinden die een string omdraait'''