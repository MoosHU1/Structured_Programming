'''Hoofdletters ook omzetten was niet gelukt'''

import string
def rotate(tekst, n):
    tekst_list = []
    alfabet = list(string.ascii_letters)
    cipher_list = []

    for i in range(0, len(tekst)):
        tekst_list.append(tekst[i])

    for i in range(0, len(tekst_list)):

        if tekst_list[i] not in alfabet:
            cipher_list.append(tekst_list[i])
        else:
            letter_index = alfabet.index(tekst_list[i])
            cipher_letter_index = (letter_index + n)

            if cipher_letter_index > 26:
                cipher_letter_index = - 26

            cipher_list.append(alfabet[cipher_letter_index])

    return ''.join(cipher_list)

tekst = input("Geef je tekst: ")
n = int(input("Hoeveel verplaatsen?: "))

print(rotate(tekst, n))