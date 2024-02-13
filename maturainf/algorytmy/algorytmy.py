# 1: CZY PIERWSZA


# szukanie czy liczba jest pierwsza


def czypierwsza(n):
    if n <= 1: #ujemne NIE
        return False 
    for x in range(2, n): # bedzie dzielić do n-1
        if n % x == 0:  # sprawdza czy dzieli bez reszty
            return False
    return True
# print(czypierwsza(9))
# print(czypierwsza(12))
# print(czypierwsza(7))
# print(czypierwsza(11))

# 1.1: czypierwsza ale sprawdza do pierwiastka

def czypierwsza2(n):
    if n <= 1:  
        return False
    for x in range(2, int(n**0.5)+1): # bedzie dzielić do pierwiastka drugiego stopnia (0.5)
        if n % x == 0:  # sprawdza czy dzieli bez reszty
            return False
    return True
# print(czypierwsza2(9))
# print(czypierwsza2(12))
# print(czypierwsza2(7))
# print(czypierwsza2(11))
#
#1.2: algorytm osobno sprawdzający liczby parzyste
def czypierwsza3(n):
    if n <= 1:  
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2): # 1 argument start, 2 koniec, 3 krok (co ile)
        if n % x == 0:  # sprawdza czy dzieli bez reszty
            return False
    return True
# print(czypierwsza3(9))
# print(czypierwsza3(12))
# print(czypierwsza3(7))
# print(czypierwsza3(11))



# 2: SITO ERASTOTENESA znajdź liczby pierwsze z przedzialu miedzy a,b

def sito(a,b):
    tab = (b+1)*[True]
    tab[1]= False
    tab[0]= False # wykluczasz 0, 1 recznie
    for i in range(2, int(b**0.5)+1):
        if tab[i] == True:                     
            j = 2*i
            while j<=b:           
                tab[j]= False # jako False musimy oznaczyć wszystkie wielokrotności i wartości większe od liczby i (są złożone)
                j+=i # zwiekszamy j o i
    for i in range(a,b+1):
        if tab[i] == True:
            print(i, "jest liczba pierwsza.")
sito(20,200)


 # Wersja ze zwracaniem listy            
def sito2(a,b):
    wyniki=[]
    tab = (b+1)*[True]
    tab[1]= False
    tab[0]= False # wykluczasz 0, 1 r�cznie
    for i in range(2, int(b**0.5)+1):
        if tab[i] == True:                     
            j = 2*i
            while j<=b:           
                tab[j]= False         
                j+=i # zwiekszamy j o i
    for i in range(a,b+1):
        if tab[i] == True:
            wyniki.append(i)
    return wyniki
print (sito2(20,200))

# 3: SPRAWDZENIE, CZY LICZBA JEST DOSKONAŁA (2*x = suma dzielnikow x)

def liczbadoskonala(x):
    suma = 0
    for i in range (1, int(x**0.5)+1):
        if x % i == 0:
            suma+=i
            suma+=x//i
        if x==i*i: # sprawdzam czy x jest kwadratem i, jak tak to odejmuje jedno i od sumy bo już było dwukrotnie (x//i)
            suma-=i
    #print(suma) # Sprawdzam przypadek kiedy pierwiastek ca�kowity z x jest liczb� ca�kowit�
    if suma==2*x: # sprawdzam samo w sobie założenie
        return True
    return False
print(liczbadoskonala(6))
print(liczbadoskonala(28))
print(liczbadoskonala(15))
print(liczbadoskonala(9))

    # 4: ROZKŁAD NA CZYNNIKI PIERWSZE

def rozklad(n):
    k = 2
    while n>1:
        while n%k == 0:
            n//=k
            print(k, end = ", ")
        k+=1
    print()
rozklad(24)
rozklad(30)

# 4.1 w formie listy

def rozklad2(n):
    czynniki = []
    k = 2
    while n>1:
        while n%k == 0:
            n//=k
            czynniki.append(k)
        k+=1
    return czynniki
print(rozklad2(24))
print(rozklad2(30))

# 4.2 szybciej z printem

def rozkladfast1(n):
    while n%2 == 0:
        n//=2
        print(2, end = ", ")
    k=3
    while n>1:
        while n%k == 0:
            n//=k
            print(k, end = ", ")
        k+=2
    print()
rozkladfast1(24)
rozkladfast1(30)

# 4.3 szybciej z listami

def rozkladfast2(n):
    czynniki = []
    while n%2 == 0:
        n//=2
        czynniki.append(2)
    k=3
    while n>1:
        while n%k == 0:
            n//=k
            czynniki.append(k)
        k+=1
    return czynniki
print(rozkladfast2(24))
print(rozkladfast2(30))

#4.4 rozklad z sitem 

def rozkladzsitem(n):
    k = sito2(2,n)
    czynniki = []
    j = 0
    while n > 1:
        while n % k[j] == 0:        #procent - modulo (oblicza resztę z dzielenia)
            n//=k[j]
            czynniki.append(k[j])
        j+=1
    return czynniki
print(rozkladzsitem(24))
print(rozkladzsitem(30))

#4.5 TEN NAJLEPSZY
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

# 5: SUMA ITERACYJNIE - z u�yciem p�tli

def sumaiter(n):
    if n < 0:
        return -1  # - 1 jest uniwersalne na b��d :)))))
    suma = 0
    for i in range (1, n+1):
        suma += i
    return suma
print(sumaiter(-5))
print(sumaiter(10))

# 5.5: SUMA REKURENCYJNIE - z u�yciem odwo�ania do funkcji

def sumarekur(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    return n + sumarekur(n-1)
print(sumarekur(-5))
print(sumarekur(10))
        
 # 6:  ILOCZYN ITERACYJNIE

def iloczyniter(n):
    if n < 0:
        return -1  # - 1 jest uniwersalne na b��d :)))))
    iloczyn = 1
    for i in range (1, n+1):
        iloczyn *= i
    return iloczyn
print(iloczyniter(-5))
print(iloczyniter(10))

 # 6.5: ILOCZYN REKURENCYJNIE

def iloczynrekur(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    return n * iloczynrekur(n-1)
print(iloczynrekur(-5))
print(iloczynrekur(10))

  # 7: NWD ITERACYJNIE
def nwd(a, b):
   while b:
       a, b = b, a%b
   return a
print(nwd(28, 24))

# 7.5 NWD REKURENCYJNIE
def nwdrek(a, b):
    if b > 0:
        return nwdrek(b, a%b)
    return a
print(nwdrek(28, 24))

# 8: NWW ITERACYJNIE
def nww(a, b):
    return a*b//nwd(a,b)
print(nww(28, 24))

# 9: FIBONACCI REKURENCJA
def fibrek(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibrek(n-1)+fibrek(n-2)
print(fibrek(10))

# 9.5: FIBONACCI ITERACJA
def fibiter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    pop, ob = 0, 1
    for i in range(n-1):
        pop, ob = ob, pop+ob
    return ob
print(fibiter(10))
        
 # rakieta 
print(fibiter(100)) 

 # 10: LICZENIE RESZTY: metoda zach�anna
def reszta(n, nom):
    lista = []
    for i in nom:
        while i <= n:
            lista.append(i)
            n -= i
    return lista
print(reszta(43, [500, 200, 100, 50, 20, 10, 5, 2 , 1]))
print(reszta(58, [20, 19, 1]))
    
  # 11: KT�RA NAJWI�KSZA, KT�RA NAJMNIEJSZA
def maxmin(tab):
    mini = tab[0]
    maxi = tab[0]
    for i in tab:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return (mini,maxi)
print(maxmin([84, 374, 82, 33, 83]))
print(min([84, 374, 82, 33, 83])) #ban
print(max([84, 374, 82, 33, 83])) #ban

# ALGORYTMY GEOMETRYCZNE

# 12: ALGORYTM NEWTONA RAPHSONA
def pierwiastek(p):
    a = 1
    eps = 0.0001
    b = p
    while abs(a-b) > eps: #abs = wartosc bezwzgledna
        a = (a+b)/2
        b = p/a
        
    return (a+b)/2
print(pierwiastek(3))
print(pierwiastek(4))

# 13: Znajdowanie miejsc zerowych funkcji ITERACYJNIE

# METODĄ BISEKCJI

# 13.1 WERSJA ITERACYJNA

def f(x: float) -> float:
    return 2*x*x*x - 2*x - 8    #1.7963
    # return x-2
def bisekcja(a, b): # a, b = początek i koniec przedziału
    if f(a)*f(b)>0: # sprawdzam, czy jest tu w ogole miejsce zerowe
        return None
    c = (a+b)/2
    eps = 0.001 # eps = dokladnosc
    while b-a >= eps:
        c = (a+b)/2
        if f(c) == 0.0:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c
# print(bisekcja(1.99999, 2.00001))

# 13.2 WERSJA REKURENCYJNA

def bisekcja2(a, b):
    eps = 0.001
    if f(a)*f(b)>0: # sprawdzam, czy jest tu w ogole miejsce zerowe
        return None
    if (b - a) < eps:
        return (a+b)/2
    c = (a+b)/2
    if f(c) == 0.0:
        return c
    if f(a) * f(c) < 0:
        return bisekcja2(a, c)
    return bisekcja2(c, b)
# print(bisekcja2(0, 5))

# 14. PALINDROM

def palindrom(slowo):
    return slowo == slowo[::-1]
# print(palindrom('mama'))

# 15. ANNAGRAM

def anagram(slowo1, slowo2):
    return sorted(slowo1)==sorted(slowo2)
# print(anagram('matura', 'trauma'))

# 15.1 PALINDROM NA ŻÓŁTĄ KARTKĘ :D
def palindromzk(slowo):
    i = 0
    j = len(slowo)-1
    for x in slowo:
        if slowo[i] != slowo[j]:
            return False
        if i >= j:
            return True
        i = i+1
        j = j-1
# print(palindromzk('kajak'))
# print(palindromzk('potop'))
# print(palindromzk('mama'))

# 15.2 REKURENCYJNIE
def palindromzkrekur(slowo, i, j):
    if i >= j:
        return True
    if slowo[i] != slowo[j]:
        return False
    return palindromzkrekur(slowo,i+1,j-1)
# print(palindromzkrekur('kajak', 0,4))
# print(palindromzkrekur('potop', 0,4))
# print(palindromzkrekur('mama', 0,3))

def palindrom_rek(string: str, i: int, j: int) -> bool:
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return palindrom_rek(string, i+1, j-1)
# print(palindrom_rek("kajak", 0, len("kajak") - 1))
# print(palindrom_rek("ebe", 0, len("ebe") - 1))
# print(palindrom_rek("konrad", 0, len("konrad") - 1))

# 15.3 JESZCZE JEDNA BEZ ZK BAN

def palindromrekurturbo(slowo):
    if len(slowo) <= 1:
        return True
    if slowo[0] != slowo[-1]: #pierwsza od konca
        return False
    return palindromrekurturbo(slowo[1:-1])
# print(palindromrekurturbo('kajak'))


# ZAD DOM

def palindromdom(slowo):
    k = ""
    for i in range(len(slowo)):
        if ord(slowo[i]) >= 65 and ord(slowo[i]) <= 90: # przedzial ascii
            k = k + chr(ord(slowo[i]) + 32) # jesli jest w przedziale to znaczy ze litera jest duza
        else:
            k = k + slowo[i] # jak juz jest mala to po prostu ja dodajemy
            # = wszystko juz jest na male :like:
    i = 0
    j = len(k)-1
    for x in k:
        if k[i] != k[j]:
            return False
        if i >= j:
            return True
        i = i+1
        j = j-1
# print(palindromdom('aDa'))

# litery na liczby - ord() w ascii
# liczby na litery - chr() w ascii
# != - is not equal to

# 16. Annagram Zliczanie

def annagramzliczanie(slowo1, slowo2):
    tab = [0] * 128
    if len(slowo1) != len(slowo2):
        return False
    for litera in slowo1:
        k = ord(litera) # do nowej zmienniej przypisuje nową wartość, więć od razu -> k =
        tab[k] = tab[k]+1 # nie tworze nowej wartości, a zmieniam wartość (dodaję w tym przypadku) czyli tab od k = tab od k plus coś tam
    for litera in slowo2:
        k = ord(litera)
        tab[k] = tab[k]-1
    for k in range(128):
        if tab[k] != 0:
            return False
    return True
# print(annagramzliczanie('matura', 'trauma'))

# 17. Wzorzec TURBO

def wzorzec(tekst, wzor):
    return wzor in tekst
# print(wzorzec('lokomotywa', 'motyw'))

# 17.1 Wzorzec ZK
def wzorzeczk(tekst, wzor):
    for i in range(len(tekst)):
        j = 0
        while j < len(wzor) and i+j < len(tekst) and tekst[i+j] == wzor[j]:
            j += 1
        if j == len(wzor):
            return True
    return False
# print(wzorzeczk('lokomotywa','motyw'))

# 18. czy da sie zbudować trójkąt

def trojkat(a,b,c):
    return a+b>c and a+c>b and b+c>a
# print(trojkat(4,5,3))

def anagramcase(slowo1, slowo2):
    return sorted(slowo1.lower())==sorted(slowo2.lower())
print(anagramcase('Matura', 'Trauma'))

# 19. WYSZUKIWANIE BINARNE

def wysz_bin_iter(lista,x):
    lewy_koniec = 0
    prawy_koniec = len(lista)-1
    while lewy_koniec <= prawy_koniec:
        srodek = (lewy_koniec + prawy_koniec)//2 # Oblicz środek listy
        if lista[srodek] == x: # Jeśli element w środku jest równy x, zwróć jego inkex
            return srodek
        if lista[srodek] < x:
            lewy_koniec = srodek+1 # jesli elemen mniejszy od x, zaaktualizuj lewy koniec
        else:
            prawy_koniec = srodek-1 # analogicznie prawy
    return -1

# kiedy dzielisz przedziały na połówki zawsze masz złożoność logarytmiczną

# print(wysz_bin_iter([2.2, 3.3, 4.5, 4.7, 5.11, 5.55, 6.12, 6.7, 7.5, 8.1], 8.1))
# print(wysz_bin_iter([2.2, 3.3, 4.5, 4.7, 5.11, 5.55, 6.12, 6.7, 7.5, 8.1], 5.55))
# print(wysz_bin_iter([2.2, 3.3, 4.5, 4.7, 5.11, 5.55, 6.12, 6.7, 7.5, 8.1], 2.5))

# 19.1 REKURENCJA

def wysz_bin_rekur(lista, x, lewy_koniec, prawy_koniec):
    srodek = (lewy_koniec + prawy_koniec)//2
    if lewy_koniec > prawy_koniec:
        return -1
    if lista[srodek] == x:
        return srodek
    if lista[srodek] < x:
        return wysz_bin_rekur(lista, x, srodek+1, prawy_koniec)
    if lista[srodek] > x:
        return wysz_bin_rekur(lista, x, lewy_koniec, srodek-1)

print(wysz_bin_rekur([2.2, 3.3, 4.5, 4.7, 5.11, 5.55, 6.12, 6.7, 7.5, 8.1], 8.1, 0, 9))
print(wysz_bin_rekur([2.2, 3.3, 4.5, 4.7, 5.11, 5.55, 6.12, 6.7, 7.5, 8.1], 5.55, 0,9))
print(wysz_bin_rekur([2.2, 3.3, 4.5, 4.7, 5.11, 5.55, 6.12, 6.7, 7.5, 8.1], 2.5, 0, 9))

# Warunek stopu w rekurencji jest przeciwny do warunku kontunuacji while'a w iteracji
# np. w wyszukiwaniu binarnym w iteracji - while lewy_koniec <= prawy_koniec, a w rekur. musi być na odwrót, czyli if lewy_koniec > prawy_koniec.
# analogicznie jest np. w Bisekcji

# 20. POTĘGOWANIE SZYBKIE ITERACYJNE

def potegowanie_iter(x, n): # x ** n (do potęgi)
    wynik = 1
    while n > 0:
        if n%2 == 1:
            wynik = wynik*x
        n = n//2
        x = x*x
    return wynik
print(potegowanie_iter(2, 10))
print(2**10)
print(potegowanie_iter(3, 5))
print(3**5)

# 20.1 POTĘGOWANIE SZYBKIE 2

def potegowanie_2(x, n):
    wynik = x
    y = x
    x = bin(n)[3:] # wypisuje od 3 znaku
    for i in x:
        wynik = wynik**2
        if i == '1':
            wynik = wynik*y
    return wynik

print(potegowanie_2(2, 13))

# powtórka :)
# funkcja, która w danym zakresie policzy sumę liczb pierwszych

def sumapierwszych(a,b):
    tab = (b+1)*[True]
    wynik = []
    tab[0] = False
    tab[1] = False
    for i in range(2, int(b**0.5)+ 1):
        if tab[i]:
            for j in range(i*2, b+1, i): # od pierwszej wielokrotności
                tab[j] = False
    for i in range(a, b+1):
        if tab[i] == True:
            wynik.append(i)
    return sum(wynik)
# print(sumapierwszych(20,50))


def sumapierwszych(a, b):
    tab = (b + 1) * [True]  # Tworzymy tablicę o długości (b+1) z wartościami True.
    wynik = []  # Inicjalizujemy pustą listę, w której będziemy przechowywać liczby pierwsze.
    tab[0] = False
    tab[1] = False  # 0 i 1 nie są liczbami pierwszymi, więc oznaczamy je jako False.

    # Algorytm sita Eratostenesa: Oznaczamy wielokrotności liczb pierwszych jako False.
    for i in range(2, int(b ** 0.5) + 1):
        if tab[i]:
            for j in range(i * 2, b + 1, i):
                tab[j] = False

    # Tworzymy listę wynikową, zawierającą tylko liczby pierwsze w zakresie od a do b.
    for i in range(a, b + 1):
        if tab[i] == True:
            wynik.append(i)

    return sum(wynik)  # Zwracamy sumę liczb pierwszych.

# suma dzielników danej liczby, w najgorszym razie ma działać w złożoności pierwiastkowej
def sumdzielnikow(n):
    suma = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            if i != n//i:
                suma += n//i
    return suma
# print(sumdzielnikow(12))

# Algorytm szukający liczby narcystycznej (liczby armstronga)
# Na przykład, 153 to liczba Armstronga, ponieważ 1^3 + 5^3 + 3^3 = 153.

def narcystyczna(n):
    # zamiana liczby na liste cyfr
    tab = []
    n = str(n)
    for x in n:
        tab.append(int(x))
    # podniesienie do potegi
    suma = 0
    for x in tab:
        suma += x**len(tab)
    return suma==int(n)
# print(narcystyczna(1634))

 # zadanie z podatkami - kwota podatku
def podatki(x):
    kwotawolna = 30000
    prog = 120000
    dochod = x

    if dochod <= kwotawolna:
        return 0
    if dochod <= prog:
        podatek =  0.17 * (dochod - kwotawolna)
    else:
        podatek = 0.17 * (prog - kwotawolna) + 0.32 * (dochod - prog)


    return podatek
# x = float(input("Podaj dochod: "))

# print(podatki(x))

# inny sposob :D
# x = float(input("Podaj dochod: "))

def podatki2(x):
    kwotawolna = 30000
    prog = 120000

    if x <= 30000:
        return 0
    if x <= 120000:
        return (x - kwotawolna) * 0.17
    return (prog - kwotawolna) * 0.17 + 0.32 * (x - prog)

# print(podatki2(x))

def roz(x):
    czynniki = []
    k = 2
    while x>1:
        while x%k == 0:
            x//=k
            czynniki.append(k)
        k += 1
    return czynniki
# print(roz(120))
def roz2(x):
    czynniki = []
    k = 2
    while x%k == 0:
        x//=k
        czynniki.append(2)
    k = 3
    while x > 1:
        while x%k == 0:
            x//=k
            czynniki.append(k)
        k += 2
    return czynniki

# print(roz2(120))

# napisz funkcje, która sumuje cyfry w liczby
def suma(x):
    x = str(x)
    suma = 0
    for cyfra in x[::-1]:
        suma += int(cyfra)

    return suma
# print(suma(268))

# mnoży cyfry liczby
def ilocz(x):
    x = str(x)
    wynik = 1
    for cyfra in x[::-1]:
        wynik *= int(cyfra)

    return wynik
# print(ilocz(268))

# 21. STORTOWANIE BĄBELKOWE
x = [3, 9, 2, 8, 1, 28, 19, 7, 0]
def sortowanie(x):
    for i in range(len(x)):
        for n in range(len(x)-i-1):
            if x[n] > x[n+1]:
                x[n], x[n+1] = x[n+1], x[n]
    return x
# print(sortowanie(x))

# 22. KONWERSJA NA DZIESIĄTKOWY
# def kon(l, x):
#     l = str(l) # Konwertuje liczbę na tekst, aby można było iterować po jej cyfrach
#     pot = len(l)-1 # Potęga, zaczynając od najwyższej potęgi liczby
#     suma = 0 # przechowywanie sumy
#
#     for i in l:
#         suma+=int(i)*x**pot  # Dodawanie do sumy iloczynu cyfry i potęgi x
#         pot -=1 # Zmniejszenie potęgi
#
#     return suma
# print(kon(2301,5))




#zad dom:

#POWTORZYC WSZYSTKO ;) (ok man)

#ZASTANOWIĆ SIĘ JAK PRZEKONWERTOWAĆ SYSTEMY WIĘKSZE OD DZIESIĄTKOWEGO NA DZIESIĄTKOWY(Z LITERKAMI) (HEHE DZIALA)
#ZASTANOWIĆ SIĘ JAK KONWERTOWAĆ Z DZIESIĄTKOWEGO NA INNE (...uuuuh kinda..?)

def konkoks(l, x, ref): # ref - referencja dla programu czym jakie dany system ma znaczki ;)
    l = str(l)
    pot = len(l)-1
    suma = 0

    for i in l:
        if i in ref:
            suma += ref[i] * x ** pot  # Dodawanie do sumy iloczynu cyfry i potęgi x
        else:
            raise ValueError(f"Nieznany znak '{i}' w systemie liczbowym")
        pot -= 1

    return suma
ref16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
ref30 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29}
ref2 = {'0': 0, '1': 1}
# try:
#     print('wyniki konwersji systemow hihi: ')
#
#     print(konkoks("A82", 30, ref30))
#     print(konkoks("100111010", 2, ref2))
#     print(konkoks("E11", 16, ref16))
# except ValueError as error:
#     print(error)
# ogolnie to jest mega glupie, bo jak jeden print ma faila to kolejnych juz nie pokazuje. glupie.

naszeprinty = [
    ("A82", 30, ref30),
    ("100111010", 2, ref2),   #  <-- no i tutaj teraz byśmy wpisywali to co chcemy sprawdzić :)
    ("B11", 12, ref16)
]

print('Wyniki konwersji systemów: ')

for dane in naszeprinty:
    try:
        wynik = konkoks(*dane)
        print(f"Wynik dla danych {dane}: {wynik}")
    except ValueError as error:
        print(f"Błąd dla danych {dane}: {error}") # z tego co rozumiem pętla erroru bierze tu kazdy intiger do zewaluowania(??) ZAPYTAĆ

# skomplikowane, i szczerze mozna byloby to juz zrobić fajniej ale z wpisywanymi danymi przez uzytkownika,
# bez problemu przerywania programu itd itp ale sie uparłam.

# zapytać konrada o to jak zrobić value error dla nieprawidłowo podanego ref ;w; -> ogarnelam to sama bo pętla erroru postanowila byc mila(chyba)

#z dziesiątkowego na dowolne inne (2, 16) do czwartku

# 23. SZYFR CEZARA 65 + 32 (do małej) (literek jest 26) (0 - 48)
def szyfrcezara(text, shift):
    wynik = ''
    for znak in text:
        if 'A' <= znak and znak <= 'Z':
            wynik += chr((ord(znak) - 65 + shift) % 26 + 65)  # 26 możliwości, powinno mi sie skojarzyc z operatorem... % :D
        elif 'a' <= znak and znak <= 'z':
            wynik += chr((ord(znak) - 97 + shift) % 26 + 97)
        else:
            wynik += znak
    return wynik
# print(szyfrcezara("Ala Ma Kota",3))
# print(szyfrcezara("abcABCxyzXYZ",3))
# print(szyfrcezara("abcABCxyzXYZ",29)) # przesuwam całą tasiemkę alfabetu (26) wracam do 2 printa

# 23.1 SZYFR CEZARA (ODKODUJ)
def CezarOdkoduj(text, shift):
    wynik = ''
    for znak in text:
        if 'A' <= znak and znak <= 'Z':
            wynik += chr((ord(znak) - 65 - shift) % 26 + 65)  # ODEJMUJEMY przesunięcie
        elif 'a' <= znak and znak <= 'z':
            wynik += chr((ord(znak) - 97 - shift) % 26 + 97)
        else:
            wynik += znak
    return wynik
print(szyfrcezara("ABCXYZabcxyz Ala ma^psa, a Konrad:)ma kota", -3))
print(szyfrcezara("ABCXYZabcxyz Ala ma^psa, a Konrad:)ma kota", -29))
print(szyfrcezara("ABCXYZabcxyz Ala ma^psa, a Konrad:)ma kota", 3))
print(szyfrcezara("ABCXYZabcxyz Ala ma^psa, a Konrad:)ma kota", 29))
print(CezarOdkoduj("XYZUVWxyzuvw Xix jx^mpx, x Hlkoxa:)jx hlqx", -3))
print(CezarOdkoduj("XYZUVWxyzuvw Xix jx^mpx, x Hlkoxa:)jx hlqx", -29))
print(CezarOdkoduj("DEFABCdefabc Dod pd^svd, d Nrqudg:)pd nrwd", 3))
print(CezarOdkoduj("DEFABCdefabc Dod pd^svd, d Nrqudg:)pd nrwd", 29))

# 22.1 Konwersja z dziesiątkowego na inne wybrane systemy:
def konreverse(l, x):
    reszty = []

    while l > 0:
        reszta = l % x
        if reszta >= 10:  # Jeśli reszta jest większa lub równa 10, zamień ją na odpowiadającą literę
            reszta = chr(ord('A') + reszta - 10)
        reszty.insert(0, str(reszta))  # Wstawienie reszty na początek listy
        l = l // x

    wynik = "".join(reszty)
    return wynik

print(konreverse(909,36))
