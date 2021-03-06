'''
author = Kateřina Fialová
'''
TEXTS = ['''
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

oddelovac = "-" * 40

registr = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'lize' : 'pass123'}
username = input('Username: ')
password = input('Password: ')
print(oddelovac)

if registr.get(username) == password:
    print('Welcome to the app, ', username, '\nWe have 3 texts to be analyzed.')
    print(oddelovac)
else:
    print('You are not a registered user.')
    exit()

number= input('Enter a number btw. 1 and 3 to select: ')
print(oddelovac)

if not number.isnumeric():
    print('Not a number')
    exit()
elif not int(number) in range(1, 4):
    print('We have only 3 texts')
    exit()

odstavec = TEXTS[int(number) - 1]
odstavec = odstavec.replace(",", "")
odstavec = odstavec.replace(".", "")
odstavec=odstavec.split()

pocet_slov = len(odstavec)

pocet_tittlecase, pocet_uppercase, pocet_lowercase, pocet_numeric, suma_numeric = 0, 0, 0, 0, 0

for slovo in range(len(odstavec)):
    odstavec[slovo] = odstavec[slovo].strip(".,:?!;")
    if odstavec[slovo].istitle():
        pocet_tittlecase += 1
    elif odstavec[slovo].isupper():
        pocet_uppercase += 1
    elif odstavec[slovo].islower():
        pocet_lowercase += 1
    elif odstavec[slovo].isnumeric():
        pocet_numeric += 1
        suma_numeric += int(odstavec[slovo])


print('There are', pocet_slov, 'words in the selected text.')
print('There are', pocet_tittlecase, 'titlecase words.')
print('There are', pocet_uppercase, 'uppercase words.')
print('There are', pocet_lowercase, 'lowercase words.')
print('There are', pocet_numeric, 'numeric strings.')
print('The sum of all the numbers is:', suma_numeric)
print(oddelovac)

f = '{:5}|{:20}|{:3}'
print(f.format('LEN', 'OCCURRENCES', 'NR.'))
print(oddelovac)

graf = {}
for slovo in odstavec:
    if len(slovo) not in graf:
        graf[len(slovo)] = 1
    else:
        graf[len(slovo)] += 1

graf = sorted(graf.items())
for a, b in graf:
    print(f.format(a, b * '*', b))
