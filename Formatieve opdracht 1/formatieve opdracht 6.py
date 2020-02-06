def gem(lst):
    totaal = 0
    for item in lst:
        totaal += int(item)

    return totaal/len(lst)

def gem_multiple(lst):
    averages = []
    for sub in lst:
        averages.append(gem(sub))

    return averages

#input_items = input("Geef je items gescheiden door komma: ")
#lst = input_items.split(",")

# eerste functie is met user input, 2de hardcoded.
sublists = [[3, 4, 5], [8, 9, 10], [1, 2, 3]]

print(gem_multiple(sublists))
