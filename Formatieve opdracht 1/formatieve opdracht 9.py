'''Bron:https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string.'''

def move(ch, n):
    new = []

    if n > 0:# opschuiven naar links
        for i in range(n, len(ch)):# Verplaats alles wat naar het begin moet komen
            new.append(ch[i])
        for i in range(0, n):# Verplaats de rest
            new.append(ch[i])

        return ''.join(new)

    if n < 0:# opschuiven naar rechts
        for i in range(n, 0):# Verplaats alles wat naar het begin moet
            new.append(ch[i])
        for i in range(0, len(ch)+n):# Verplaats de rest
            new.append(ch[i])

        return ''.join(new)

ch = input("Geef een byte: ")
n = int(input("Hoeveel moet die verplaatst worden: "))

print(move(ch, n))