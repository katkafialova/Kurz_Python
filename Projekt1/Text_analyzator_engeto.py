'''
author = 'Jan Hrabina'
'''
TEXTS = [
    '''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
]

uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
oddelovac = 40 * '-'

# zadani jmena a hesla uzivatele
user = input('username: ')
password = input('password: ')

print(oddelovac)

# kontrola jmena a odpovidajiciho hesla uzivatele, v pripade neshody konec applikace,
# jinak privitani uzivatele
if user in uzivatele.keys() and password == uzivatele.get(user):
    print(f'Welcome to the app,', user)
else:
    print('Wrong login and/or password. Exiting app...')
    exit()

pocet_textu = len(TEXTS)

print(f'We have', pocet_textu, 'texts to be analyzed.')
print(oddelovac)

if not pocet_textu:
    print('No text to analyze, exiting app...')
    exit()

# vyber textu k analyze
cislo_textu = input('Enter a number btw. 1 and ' + str(pocet_textu) + ' to select: ')

if not cislo_textu.isnumeric():
    print('Wrong input, exiting app...')
    exit()
elif int(cislo_textu) not in range(1, pocet_textu + 1):
    print('Wrong input, exiting app...')
    exit()

print(oddelovac)


# rozsekani vybraneho textu na slova, orezani interpunkce,
# pocitani title, upper, lower, numstrings, souctu
text = TEXTS[int(cislo_textu) - 1]
slova = text.split()

titlecase = 0
uppercase = 0
lowercase = 0
numstr = 0
soucet = 0

for index in range(len(slova)):
    slova[index] = slova[index].strip('.,;:!?')

    if slova[index][0].isupper():
        titlecase += 1

    if slova[index].isupper() and slova[index].isalpha():
        uppercase += 1
        continue

    if slova[index].islower() and slova[index].isalpha():
        lowercase += 1
        continue

    if slova[index].isnumeric():
        numstr += 1
        soucet += int(slova[index])

# tisk vysledku prvni casti
print('There are', len(slova), 'words in the selected text.')
print('There are', titlecase, 'titlecase words.')
print('There are', uppercase, 'uppercase words.')
print('There are', lowercase, 'lowercase words.')
print('There are', numstr, 'numeric strings.')
print('The sum of all the numbers is:', soucet)
print(oddelovac)

# pocitani a naformatovany tisk delek slov
delky = {}
for slovo in slova:
    if len(slovo) not in delky:
        delky[len(slovo)] = 1
    else:
        delky[len(slovo)] += 1

print('LEN | OCCURENCES       | NR.')
print(oddelovac)

for index in range(1, len(delky) + 1):
    pocet = delky.get(index)
    if pocet:
        print('{:>3} | {:<17}  {:<12}'.format(index, pocet * '*', pocet))