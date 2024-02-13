# Zad. 1
# sito erastotenesa ale zwraca liczby pierwsze, których suma cyfr też jest liczbą pierwszą.

def sito(a,b):
    tab = [True]*(b+1) #wszystkie liczby od 2 do danej liczby
    tab[0] = tab[1] = False # bez 0 i 1
    for i in range (2, int(b**0.5)+1): # do pierwiastka
        if tab[i] == True:
            j = 2*i
            while j<=b:
                tab[j] = False #wielokrotnosci false
                j+=i
    liczbypierwsze = []
    for i in range(a, b + 1):
        if tab[i] == True:
            liczbypierwsze.append(i)
    return liczbypierwsze


def sumacyfr(i): # licze sume liczb
    suma = 0
    for cyfra in str(i):
        suma += int(cyfra)
    return suma

wynik = sito(20,200)
a = int(input("początek przedziału: "))
b = int(input("koniec przedziału: ")) # tak to naprawilam lol

wynik = sito(a, b)

# sprawdzanie czy suma cyfr sama w sobie jest liczbą pierwszą:
for liczba in wynik:
    suma = sumacyfr(liczba)
    suma_pierwsza = True
    for x in range(2, suma):
        if suma % x == 0: # jezeli suma nie
            suma_pierwsza = False
            break
    if suma_pierwsza:
        print("Liczba pierwsza:", liczba, "suma jej cyfr, która też jest pierwsza (sprawdzilam):", suma)

# zad 2
def nwd(a, b):
    def rozklad(n):
        czynniki = []
        dzielnik = 2
        while n > 1:
            while n % dzielnik == 0:
                czynniki.append(dzielnik)
                n //= dzielnik
            dzielnik += 1
        return czynniki

    czynnikia = rozklad(a)
    czynnikib = rozklad(b)
    wspolne = []

    for czynnik in czynnikia:
        if czynnik in czynnikib:
            wspolne.append(czynnik)
            czynnikib.remove(czynnik) # usuwam, bo bierze sobie a

    if len(wspolne) == 0:
        return 1 # jak nie ma wspolnych dzielnikow, to zwracam jedynke bo ona jedyna dzieli a i b na 100%
    else:
        iloczyn = 1
        for czynnik in wspolne:
            iloczyn *= czynnik
        return iloczyn

print(nwd(42, 84))

# zad 3
# def bisekcja(a, b):
#     if f(a)*f(b)>0:
#         return None # nie ma zerowego
#     c = (a+b)/2
#     d = (a+b)/3
#     eps = 0.001
#     while b-a >= eps:
#         c = (a+b)/2
#         d = (a+b)/3 # uhh
#         if f(c) == 0.0:
#             return c
#         if f(a)*f(c) < 0:
#             b = c
#         else:
#             a = c
#             return c
# # uhhhhhh
#         if f(d) == 0.0:
#             return d
#         if f(a)*f(d) < 0:
#             b = d
#         else:
#             a = d
#             return d
# dobra to cale jest źle, chcialam zupelnie co innego zrobic (w sensie: pododawac ifów do jednego dzielenia na 3 i usunac to dzielenie na 2)

# def bisekcja(a, b):
#     if f(a)*f(b)>0:
#         return None # nie ma zerowego
#     d = (a+b)/3
#     eps = 0.001
#     while b-a >= eps:
#         d = (a+b)/3 # uhh
#         if f(d) == 0.0:
#             return d
#         if f(a)*f(d) < 0:
#             b = d
#         else:
#             a = d
#             return d

        #o jakos tak(???)
#zad 4

#rekur
def rekurencja(n):
    if n == 0:
        return 0
    if n == 1 or n == 2: # trzy pierwsze elementy ciągu
        return 1
    return rekurencja(n-1)+rekurencja(n-2)+rekurencja((n-3))
print(rekurencja(10))
n = 10
print("elementy: ")
for i in range(n):
    print(rekurencja(i))

#iter
def iteracja(n):
    if n == 0:
        return 0
    if n == 1 or n==2:
        return 1
    previous, prevvious, prevvvious, current, = 1, 1, 0, 0 # current - zaczynamy od trzeciego elementu rownego 1, ta cala reszta to poprzednie elementy w fibbonaccim
    for i in range(3, n+1): # od 3 do n powiekszonego o 1
        current = previous + prevvious + prevvvious
        prevvvious = prevvious
        prevvious = previous
        previous = current

    return current

print(iteracja(7))
n = 7
print("elementy: ")
for i in range(n):
    print(iteracja(i))

# zad. 5
def anagramy(a, b):
    slowoa = set(a) # sety
    slowob = set(b)

    return slowoa == slowob

print(anagramy('aabbccdd', 'dcba'))
print(anagramy('abcdddee', 'abcd'))   # tu e nie ma