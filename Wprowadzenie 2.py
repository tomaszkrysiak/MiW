# 1

a_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ab_list = []

def suma(a_list, b_list):
    suma1 = [i for i, j in enumerate(a_list) if i % 2 == 0]
    suma1 += [i for i, j in enumerate(b_list) if i % 2 == 1]
    return print(ab_list)


suma(a_list, b_list)


# 2

def tekst(data_text):
    dlugosc = len(data_text)
    litery = list(data_text)
    d_litery = data_text.upper()
    m_litery = data_text.lower()
    dict = {
        'dlugosc': dlugosc,
        'litery': litery,
        'd_litery': d_litery,
        'm_litery': m_litery
    }
    return print(dict)


tekst('Moto')


# 3

def zad3(text, litera):
    wynik = text.replace(litera, '')
    return print(wynik)


zad3('rabarbar', 'r')


# 4

def zad4(C, jednostka):
    if jednostka == 'Fahrenheit':
        wynik = (C * 9 / 5) + 32
        return print(wynik)
    elif jednostka == 'Rankine':
        wynik = (C * 9 / 5) + 491.67
        return print(wynik)
    elif jednostka == 'Kelvin':
        wynik = C + 273.15
        return print(wynik)
    else:
        return print('Błąd! Proszę podać prawdiłowy typ temperatury')


zad4(12, 'Fahrenheit')
zad4(23, 'Rankine')
zad4(43, 'Kelvin')
zad4(11, 'blad')


# 5

class Calculator:
    def dod(a, b):
        wynik = a + b
        return print(wynik)

    def roznica(a, b):
        wynik = a - b
        return print(wynik)

    def mnoz(a, b):
        wynik = a * b
        return print(wynik)

    def dziel(a, b):
        wynik = a / b
        return print(wynik)


Calculator.dod(1, 1)
Calculator.roznica(6, 2)
Calculator.mnoz(3, 2)
Calculator.dziel(16, 2)


# 6

class ScienceCalculator(Calculator):
    def potega(a, b):
        wynik = a ** b
        return print(wynik)


ScienceCalculator.potega(2, 4)


# 7

def ćw7(tekst):
    tyl = tekst[::-1]
    return print(tyl)

ćw7('Krysiak')



#8

from file_manager import FileManager

plik = FileManager("dokument.txt")

FileManager.read_file(plik)
FileManager.update_file(plik, " fragment tekstu  ")
FileManager.read_file(plik)
