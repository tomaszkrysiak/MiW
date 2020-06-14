#4
zmienna_typu_string = "TomaszKrysiak"

#print(dir(zmienna_typu_string))
#help(zmienna_typu_string.lower)

#5
s='Tomasz Krysiak'
print(s[::-1])

#6
lista = [0,1,2,3,4,5,6,7,8,9]
lista_2 = lista[5:]
lista = lista[:5]

#7
lista = lista + lista_2
lista = [0] + lista

lista_kopia = lista
lista_kopia.reverse()
print(lista_kopia)
print(lista[::-1])

#8
studenci = [(111111,'Jan Kowalski'), (222222, 'Jan Nowak'), ('Adam Małysz')]

#9

studenci_slownik = {}

for student in studenci:
    klucz = student[0]
    wartosc = student[1]
    studenci_slownik[klucz] = wartosc

print(studenci_slownik)

wiek_slownik = {1: 22, 2: 23, 3: 19}
adres_slownik = {1: 'address 1', 2: 'address 2', 3: 'address 3'}
email_slownik = {1: 'email@1.com', 2: 'email@2.com', 3: 'email@3.com'}
rok_slownik = {1: 1998, 2: 1997, 3: 2001}

#10
tels = ['12345', '67890', '12345', '67890']
tels = set(tels)
print(tels)

#11
for x in range(1, 11):
    print(x)

#12
for x in range(100, 19, -5):
    print(x)

#13
lista_slownikow = [{1:'Andrzej', 2:'Marcin', 3:'Piotr', 4:'Marek', 5:'Krzysztof'}, {1:25, 2:34, 3:12, 4:87, 5:63},
                   {1:'Zamość', 2:'Warszawa', 3:'Kraków', 4:'Wrocław', 5:'Olsztyn'}, {1:500400300, 2: 100200300, 3:200300400,
                                                                            4:400500600, 5:500600700}]
print('Osoba o imieniu {a}, mieszka w {b}. Jej numer telefonu to {c}.'\
      'Ma {d} lat.'.format(a = lista_slownikow[0][1], b = lista_slownikow[2][1],
                           c = lista_slownikow[3][1], d= lista_slownikow[1][1]))
