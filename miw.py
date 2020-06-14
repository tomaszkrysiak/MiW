#1
zmienna = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz ' \
       'pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków ' \
       'później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował ' \
       'się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ' \
       'ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na ' \
       'komputerach osobistych, jak Aldus PageMaker'

#2
name = 'Tomasz'
surname = 'Krysiak'

litera_1 = name[1]
litera_2 = surname[2]

litera_1_ile = zmienna.count(litera_1)
litera_2_ile = zmienna.count(litera_2)

print('W tekście jest {a} liter {b} oraz {c} liter {d}'.format(a = litera_1_ile, b = litera_1, c = litera_2_ile, d = litera_2))

