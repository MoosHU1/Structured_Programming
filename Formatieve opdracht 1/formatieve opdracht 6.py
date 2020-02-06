def gem(lst):
    totaal = 0
    for item in lst:
        totaal += int(item)

    return totaal/len(lst)

def gem_2(lst):
    print("")

input_items = input("Geef je items gescheiden door komma: ")
lst = input_items.split(",")

print(gem(lst))
