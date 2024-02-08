liczby = []
mniejsze = []
zapisaneliczby = []
zapisanedzielniki = []
with open ("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))

def dzielenie(x):
    ugabuga = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            ugabuga.append(i)
            ugabuga.append(x//i)
        if x==i*i:
            ugabuga.pop()
    if len(ugabuga) == 18:
        return (True, ugabuga) # krotka(tuple)
    return False




# zad.1
# Odpowiedź: dwie ostatnie najmniejsze + ilość <1000
for i in liczby:
    if i < 1000:
        mniejsze.append(int(i))
elementy = len(mniejsze)

print(elementy)
print(mniejsze[-1])

with open ("wyniki60.txt","w") as file:
    file.write("Zad.1 \n")
    file.write(str(mniejsze[-1]) +"\n")
    file.write(str(mniejsze[-2]) + "\n")
    file.write("Ilosc elementow: " + str(elementy) +"\n")
# Zad. 2
# Odpowiedź: Liczby, które mają dokładnie 18 dzielników + lista tych dzielników posortowana rosnąco
for i in liczby:
    if dzielenie(i):
        zapisaneliczby.append(i)
        zapisanedzielniki.append(dzielenie(i)[1]) # wyciagam z krotki ugabuga z zapisanymi dzielnikami
for i in range(len(zapisaneliczby)):
    print(zapisaneliczby[i])
    print(sorted(zapisanedzielniki[i]))

with open ("wyniki60.txt","a") as file:
    file.write("Zad.2 \n")
    for i in range(len(zapisaneliczby)):
        file.write(str(zapisaneliczby[i]) +"\n")
        file.write((str(sorted(zapisanedzielniki[i])) +"\n"))

#Zad. 3
# znaleźć największą liczbę, która ze wszystkimi pozostałymi nie dzieli się przez więcej niż 1
def nwd(a,b):
    if b > 0:
        return nwd(b,a%b)
    return a
najwieksza = 0
for i in liczby:
    for j in liczby:
        if nwd(i,j) != 1 and i != j: # i nie moze byc takie samo jak j bo wywali 0
            break
    else:
        if i > najwieksza:
            najwieksza = i
print(najwieksza)

with open("wyniki60.txt", "a") as file:
    file.write("Zad.3 \n")
    file.write(str(najwieksza))




