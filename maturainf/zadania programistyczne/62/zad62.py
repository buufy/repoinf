osemkowe = []

with open ("liczby1.txt") as file:
    for line in file:
        osemkowe.append(int(line))

#zad 1 wypisz najwieksza i najmniejsza w osemkowym:

print(min(osemkowe))
print(max(osemkowe))

with open("wyniki62.txt", "w") as file:
    file.write("Zad.1 \n")
    file.write(str(min(osemkowe)) + "\n")
    file.write(str(max(osemkowe)) + "\n")

#zad.2