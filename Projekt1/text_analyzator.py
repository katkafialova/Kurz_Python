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

registr = {'bob' : '13', 'ann' : 'pass123', 'mike' : 'password123', 'lize' : 'pass123'}
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

odstavec = TEXTS[int(number) - 1].split()

pocet_slov = len(odstavec)
pocet_tittlecase, pocet_uppercase, pocet_lowercase, pocet_numeric, suma_numeric = 0, 0, 0, 0, 0

for slovo in odstavec:
    slovo = slovo.strip(".,:?!;")
    if slovo.istitle():
        pocet_tittlecase += 1
    elif slovo.isupper():
        pocet_uppercase += 1
    elif slovo.islower():
        pocet_lowercase += 1
    elif slovo.isnumeric():
        pocet_numeric += 1
        suma_numeric += int(slovo)


print('There are', pocet_slov, 'words in the selected text.')
print('There are', pocet_tittlecase, 'titlecase words.')
print('There are', pocet_uppercase, 'uppercase words.')
print('There are', pocet_lowercase, 'lowercase words.')
print('There are', pocet_numeric, 'numeric strings.')
print('The sum of all the numbers is:', suma_numeric)
print(oddelovac)

graf = {}
for slovo in odstavec:
    if len(slovo) not in graf:
        graf[len(slovo)] = 1
    else:
        graf[len(slovo)] += 1

print('LEN | OCCURENCES       | NR.')
print(oddelovac)

#graf = {}
#for slovo in odstavec:
  #  if len(slovo) not in
  #  graf[len(slovo)] = graf.get(len(slovo), 0) + 1

#graf = sorted(graf.items())

print("LEN | OCCURENCES | Nr.")
f = "{:5}|{:20}|{:5}"
#for a in graf:
    #print(neco[0], "|", "*" * int(neco[1]), "|", neco[1])
 #   print(f.format(a[0], int(a[1]) * '*', a[1]))

for index in range(1, len(graf) + 1):
    pocet = graf.get(index)
    if pocet:
        print('{:>3} | {:<17}  {:<12}'.format(index, pocet * '*', pocet))







