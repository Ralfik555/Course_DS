
import urllib.request 
import re
import logging

####----------------------- Zadanie 1 -----------------------------------------------
kraj = 'Polska'

def country_info(kraj:str):
    kraj_parse = urllib.parse.quote(kraj)
    #kraj_parse = kraj ## --------------- jezeli chcemy uzyć funkcji sprawdzajacej return_errors
    html = 0
    try:
        with urllib.request.urlopen('https://pl.wikipedia.org/wiki/'+kraj_parse) as response: 
            html = response.read().decode('utf-8') 
    except:
        logging.error('Błąd pobierania adresu url')
        return(0)
    
    if html:
        html = html.replace("\r","")
        html = html.replace("\n","")
        
        pattern_cap = r'title="Stolica".{0,70}title="(.{0,30})">'
        pattern_phone = r'title="Telefoniczny kod kraju".{0,70}(\+[0-9 \-]{0,6})'
        
        
        cap_search =  re.search(pattern_cap,html)
        if cap_search:
            cap = cap_search.groups()
        
        phone_search = re.search(pattern_phone,html)
        if phone_search:
            phone = phone_search.groups()
        
        if not cap_search and not phone_search:
            logging.warning('Nie znaleziono informacji o wskazanm kraju, bądź wskazano artykuł nie dotyczący państwa')
            return(0)
        elif not cap_search:
            out = 'Panstwo:{}, Stolica:{}, kod telefoniczny:{}'.format(kraj,'Nie znaleziono',phone[0])
        elif not phone_search:
            out = 'Panstwo:{}, Stolica:{}, kod telefoniczny:{}'.format(kraj,cap[0],'Nie znaleziono')
        else:
            out = 'Panstwo:{}, Stolica:{}, kod telefoniczny:{}'.format(kraj,cap[0],phone[0])
        print(out)
        return(out)
            
    
###--------------- Przykłady wywołania -------------------------   

country_info('Barbados')  
country_info('Saint_Vincent_i_Grenadyny')  
country_info('Wyspy_Marshalla')  
country_info('Nepal')  
country_info('Unia_Europejska')  
country_info('Warszawa')  
country_info('test1')  

#####-------------------- funkcja sprawdzająca ------------------------------------------------------



countries = ['Afganistan',
'Albania',
'Algieria',
'Andora',
'Angola',
'Antigua i Barbuda',
'Arabia Saudyjska',
'Argentyna',
'Armenia',
'Australia',
'Austria',
'Azerbejdżan',
'Bahamy',
'Bahrajn',
'Bangladesz',
'Barbados',
'Belgia',
'Belize',
'Benin',
'Bhutan',
'Białoruś',
'Boliwia',
'Bośnia i Hercegowina',
'Botswana',
'Brazylia',
'Brunei',
'Bułgaria',
'Burkina Faso',
'Burundi',
'Chile',
'Chiny',
'Chorwacja',
'Cypr',
'Czad',
'Czarnogóra',
'Czechy',
'Dania',
'Demokratyczna Republika Konga',
'Dominika',
'Dominikana',
'Dżibuti',
'Egipt',
'Ekwador',
'Erytrea',
'Estonia',
'Etiopia',
'Fidżi',
'Filipiny',
'Finlandia',
'Francja',
'Gabon',
'Gambia',
'Ghana',
'Grecja',
'Grenada',
'Gruzja',
'Gujana',
'Gwatemala',
'Gwinea',
'Gwinea Bissau',
'Gwinea Równikowa',
'Haiti',
'Hiszpania',
'Holandia',
'Honduras',
'Indie',
'Indonezja',
'Irak',
'Iran',
'Irlandia',
'Islandia',
'Izrael',
'Jamajka',
'Japonia',
'Jemen',
'Jordania',
'Kambodża',
'Kamerun',
'Kanada',
'Katar',
'Kazachstan',
'Kenia',
'Kirgistan',
'Kiribati',
'Kolumbia',
'Komory',
'Kongo',
'Korea Południowa',
'Korea Północna',
'Kostaryka',
'Kuba',
'Kuwejt',
'Laos',
'Lesotho',
'Liban',
'Liberia',
'Libia',
'Liechtenstein',
'Litwa',
'Luksemburg',
'Łotwa',
'Macedonia',
'Madagaskar',
'Malawi',
'Malediwy',
'Malezja',
'Mali',
'Malta',
'Maroko',
'Mauretania',
'Mauritius',
'Meksyk',
'Mikronezja',
'Mjanma',
'Mołdawia',
'Monako',
'Mongolia',
'Mozambik',
'Namibia',
'Nauru',
'Nepal',
'Niemcy',
'Niger',
'Nigeria',
'Nikaragua',
'Norwegia',
'Nowa Zelandia',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua-Nowa Gwinea',
'Paragwaj',
'Peru',
'Polska',
'Portugalia',
'Południowa Afryka',
'Republika Środkowoafrykańska',
'Republika Zielonego Przylądka',
'Rosja',
'Rumunia',
'Rwanda',
'Saint Kitts i Nevis',
'Saint Lucia',
'Saint Vincent i Grenadyny',
'Salwador',
'Samoa',
'San Marino',
'Senegal',
'Serbia',
'Seszele',
'Sierra Leone',
'Singapur',
'Słowacja',
'Słowenia',
'Somalia',
'Sri Lanka',
'Stany Zjednoczone',
'Eswatini',
'Sudan',
'Sudan Południowy',
'Surinam',
'Syria',
'Szwajcaria',
'Szwecja',
'Tadżykistan',
'Tajlandia',
'Tanzania',
'Timor Wschodni',
'Togo',
'Tonga',
'Trynidad i Tobago',
'Tunezja',
'Turcja',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraina',
'Urugwaj',
'Uzbekistan',
'Vanuatu',
'Watykan',
'Wenezuela',
'Węgry',
'Wielka Brytania',
'Wietnam',
'Włochy',
'Wybrzeże Kości Słoniowej',
'Wyspy Marshalla',
'Wyspy Salomona',
'Wyspy Świętego Tomasza i Książęca',
'Zambia',
'Zimbabwe',
'Zjednoczone Emiraty Arabskie']


countries_new = []
for c in countries:
    countries_new.append(urllib.parse.quote(c, safe='/', encoding=None, errors=None))

def return_errors(function_info):
    error_list = []
    for i in range(len(countries)):
        check = function_info(countries_new[i])
        if not check:
            if countries[i] !='Chiny':
                error_list.append(countries[i])
    return(error_list)


errors = return_errors(country_info)

####----------------------- Zadanie 2 -----------------------------------------------
    
import csv
import json
import logging

def adresy_fast_food(ff_name:str,file_path='Datafiniti_Fast_Food_Restaurants.csv'):
    try:
        with open(file_path ,encoding="utf8") as file:
            data = csv.reader(file) 
            if data:
                ff_list = []
                idx = {'address': 0,'latitude':0,'longitude':0,'name':0,
                'city':0,'province': 0} 
                
                for line in data:
                    for i in idx:
                        if not idx[i]:
                            idx[i] = line.index(i)
                            
                    if ff_name in line[idx['name']]:
                        key_name = '{0} {1} {2}'.format(line[idx['address']],line[idx['city']],line[idx['province']])
                        res ={  \:{'lat':float(line[idx['latitude']]),'long':float(line[idx['longitude']])}}
                        ff_list.append(res)
    except:
        logging.error('Błąd pobrania pliku')        
    if ff_list: 
        js = {ff_name:ff_list}
        json.dump(js, open(ff_name+'.json','w'))
    else:
        logging.warning('Wskazana nazwa nie występuje w pliku')   

####------------------ przykładowe wywołanie i odczyt otrzymanego json -----------

ff = "McDonald's"
adresy_fast_food(ff)
with open (ff+'.json') as j:
    mc = json.load(j)
    print(mc)

ff = "Pizza Hut"
adresy_fast_food(ff)
with open (ff+'.json') as j:
    ph = json.load(j)
    print(ph)
    
adresy_fast_food('test')
