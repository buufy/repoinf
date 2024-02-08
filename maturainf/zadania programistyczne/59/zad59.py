liczby = []

with open ("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))

#
# def rozkladfast2(n):
#     czynniki = []
#     while n%2 == 0:
#         n//=2
#         czynniki.append(2)
#     k=3
#     while n>1:
#         while n%k == 0:
#             n//=k
#             czynniki.append(k)
#         k+=1
#     return czynniki

def factorize_efficient_list(number: int) -> list:
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    factor = 3
    while factor * factor <= number:
        while number % factor == 0:
            factors.append(factor)
            number //= factor
        factor += 2
    if number > 1:
        factors.append(number)
    return factors


#Zad.1
ile1 = 0
for l in liczby:
    print(l)
    czynniki = factorize_efficient_list(l)
    # print(czynniki)
    czynniki = set(czynniki) # set usuwa duplikaty :)
    # print(czynniki)
    flaga = True
    for n in czynniki:
        if n == 2:
            flaga = False
            break
    if len(czynniki) == 3 and flaga:
        ile1 += 1
print(ile1)

with open ("wyniki59.txt", "w") as file:
    file.write("Zad.1 \n")
    file.write(str(ile1) +"\n")

#Zad.2
def palindrom(n):
    return n == n[::-1]
def odwrotnosc(n):
    return n[::-1]

dodane = 0
for l in liczby:
    #obliczyć odwrotność
    g = str(l)
    g = odwrotnosc(g)
    g = int(g)

    #obliczyć sumę
    suma = l + g
    suma = str(suma)
    # sprawdzic palindrom, jezeli palindrom to plus jeden
    if palindrom(suma):
        dodane += 1

with open ("wyniki59.txt", "a") as file:
    file.write("Zad.2 \n")
    file.write(str(dodane) +"\n")

#zad.3

def iloczyn(n):
    wynik = 1
    n = str(n)
    for i in n:
        x = int(i)
        wynik *= x
    return wynik
tab = 9*[0]
mini = 999999
maxi = 0

for l in liczby:
    x = l
    moc = 0
    while l > 9:
        il = iloczyn(l)
        moc += 1
        l = il # WOW wylicza moc :)
    tab[moc]+=1
    if moc == 1:
        if mini > x:
            mini = x
        if maxi < x:
            maxi = x
print(tab)
print(mini, maxi)

with open ("wyniki59.txt", "a") as file:
    file.write("Zad.3 \n")
    for i in range (1,9):
        file.write(str(i)+": "+str(tab[i]) +"\n")
    file.write("mini: "+str(mini)+"\n")
    file.write("maxi: " + str(maxi) + "\n")