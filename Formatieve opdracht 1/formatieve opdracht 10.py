'''Ik heb hiervoor het internet gebruikt, maar ik snap hem eerlijk gezegd nog steeds niet.
Bron: https://www.programiz.com/python-programming/examples/fibonacci-recursion'''

def fibonacci(index):
    if index <= 1:
        return index

    return fibonacci(index-1) + fibonacci(index-2)


index = int(input("Geef een index van de fibonacci reeks: "))
fibonacci(index)

print(fibonacci(index))
