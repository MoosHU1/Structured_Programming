def move(ch, n):
    new = []

    if n > 0:
        for index in range(-1, (-len(ch))-1, -1):
            new.append(ch[index+n])
    print(new)



ch = input("Geef een byte: ")
n = int(input("Hoeveel moet die verplaatst worden: "))

move(ch, n)