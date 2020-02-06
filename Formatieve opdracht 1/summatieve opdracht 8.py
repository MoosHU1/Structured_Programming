f = open("bestand.txt", "r")
lines = f.readlines()
print(lines)

lines_new = []

for item in lines:
    lines_new.append(str.strip(item))

print(lines_new)
new_file = open("bestand_new.txt", "w")

for item in lines_new:
    new_file.write(item)

