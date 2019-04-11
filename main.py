import random

countries={
    "Albania":"Tirana",
    "Andorra":"Andorra la Vella",
    "Armenia":"Yerevan",
    "Austria":"Vienna",
    "Azerbaijan":"Baku",
    "Belarus":"Minsk",
    "Belgium":"Brussels",
    "Bosnia and Herzegovina":"Sarajevo",
    "Bulgaria":"Sofia",
    "Croatia":"Zagreb",
    "Cyprus":"Nicosia",
    "Czechia":"Prague",
    "Denmark":"Copenhagen",
    "Estonia":"Tallinn",
    "Finland":"Helsinki",
    "France":"Paris",
    "Georgia":"Tbilisi",
    "Germany":"Berlin",
    "Greece":"Athens",
    "Hungary":"Budapest",
    "Iceland":"Reykjavik",
    "Ireland":"Dublin",
    "Italy":"Rome",
    "Kazakhstan":"Nur-Sultan",
    "Kosovo":"Pristina",
    "Latvia":"Riga",
    "Liechtenstein":"Vaduz",
    "Lithuania":"Vilnius",
    "Luxembourg":"Luxembourg",
    "Malta":"Valletta",
    "Moldova":"Chisinau",
    "Monaco":"Monaco",
    "Montenegro":"Podgorica",
    "Netherlands":"Amsterdam",
    "North Macedonia":"Skopje",
    "Norway":"Oslo",
    "Poland":"Warsaw",
    "Portugal":"Lisbon",
    "Romania":"Bucharest",
    "Russia":"Moscow",
    "San Marino":"San Marino",
    "Serbia":"Belgrade",
    "Slovakia":"Bratislava",
    "Slovenia":"Ljubljana",
    "Spain":"Madrid",
    "Sweden":"Stockholm",
    "Switzerland":"Bern",
    "Turkey":"Ankara",
    "Ukraine":"Kiev",
    "United Kingdom":"London",
    "Vatican City (Holy See)":"Vatican"
}

user=""
inputas=""
country_list=[]
capital_list=[]


def fun_data_generator():
    for name, answer in countries.items():
        country_list.append(name)
        capital_list.append(answer)


def fun_compare(sk, value):
    if capital_list[sk]==value:
        print("Teisingai! Pelnote 1 taska")
        print("******")
        return True
    print("Deja, neteisingai, teisingas variantas buvo: ",capital_list[sk])
    return False


def fun_game_mode(x,sk):
    result=False
    if "1" in x or "be" in x:
        guess=input(inputas)
    elif "2" in x or "su" in x:
        counter=1
        options=[]
        options.append(capital_list[sk])
        while not(counter==4):
            rand = random.randint(0,len(capital_list)-1)
            if not(capital_list[rand] in options):
                options.append(capital_list[rand])
                counter=len(options)
        options.sort()
        print('Galimi variantai')
        for var in options:
            print(var)
        guess=input(inputas)

    result=fun_compare(sk=sk,value=guess)
    return result
    


def fun_game(mode):
    counter=0
    condition=True
    while condition:
        sk = random.randint(0,len(countries)-1)
        print(' Salis: ',country_list[sk])
        condition = fun_game_mode(x=mode, sk=sk)
        if condition==True:
            counter=counter+1
        else:
            break
    fun_zaidimo_pabaiga(counter)
        
       

def fun_zaidimo_pabaiga(points):
    print("Zaidimas baigesi")
    print("Surinkote tasku: ",points)
    print("-------------------------")
    
    
def fun_menu():
    print("**********************************************")
    print("Zaidimas: Labas,",user,", pasirinkite žaidimo rezima:")
    print("1. Spelioti be variantu")
    print("2. Spelioti su variantais")
    mode = input(inputas)
    print("**********************************************")
    fun_game(mode)

while True:
    user = input("Zaidimas: Kas busite?:")
    inputas = user+":"
    fun_data_generator()
    fun_menu()
