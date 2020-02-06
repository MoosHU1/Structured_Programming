str1 = input("Geef je string: ")
str2 = input("Geef je string: ")

for index in range(max(len(str1), len(str(2)))):
    if str1[index] != str2[index]:
        print("Het verschil zit bij index "+str(index))
        break

