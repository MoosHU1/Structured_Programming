def sort(lst):
    for index in range(len(lst)):
        minimum_index = lst.index(min(lst[index:]))
        lst[index], lst[minimum_index] = lst[minimum_index], lst[index]
    return lst

input_items = input("Geef je items gescheiden door komma: ")
lst = input_items.split(",")

print(sort(lst))