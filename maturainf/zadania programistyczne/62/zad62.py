osemkowe = []
dziesietne = []
wynik2 = []

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

#zad.2 najdluzszy niemalejacy ciag (jeden wiersz pod drugim, rosnąco)
with open ("liczby2.txt") as file:
    for line in file:
        dziesietne.append(int(line))
w2=[]
import copy
for i in range(len(dziesietne)-1):
    if dziesietne[i] <= dziesietne[i+1]:
        w2.append(dziesietne[i+1])
    else:
        if len(w2) > len(wynik2):
            # wynik2 = w2 # typ referencyjny - odwolouje do pamieci programu (bezposrednio do ramu)
            wynik2 = w2.copy()
        w2 = []
        w2.append(dziesietne[i+1])
print(wynik2)

print(wynik2[0])
print(len(wynik2))

with open("wyniki62.txt", "a") as file:
    file.write("Zad.2 \n")
    file.write(str(wynik2[0]) + "\n")
    file.write(str(len(wynik2)) + "\n")
# lista = [1,2,3]
# listaabc = [10,20,30]
# print(lista, listaabc)
# listaabc = lista
# lista.append(4)
# print(listaabc)
#
# z=5
# y=10
# print(z,y)
# y=z
# z=15
# print(y)


