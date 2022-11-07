import time

nombre=str(input("Pokemaniatico ingresa tu nombre para empezar: "))


print("""
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.      
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
      """)

time.sleep(2)
print("                 ☆☆☆☆☆☆☆☆☆PokeMenu Interactivo☆☆☆☆☆☆☆☆☆")
print("                             Bienvenido "+nombre+"!!")
while True:
    print("""
        ░█▀▀▄░░░░░░░░░░░▄▀▀█        
        ░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
        ░░▀▄░░░▀░░░░░▀░░░▄▀         Elije una opción para listar Pokemones!!!
        ░░░░▌░▄▄░░░▄▄░▐▀▀
        ░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█         1) Generación
        ░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
        ▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█         2) Forma
        █░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
        ░▀▄░░▀░░▀▀▀░░▀░░░▄█▀            3) Habilidad
        ░░░█░░░░░░░░░░░▄▀▄░▀▄
        ░░░█░░░░░░░░░▄▀█░░█░░█          4) Habitat
        ░░░█░░░░░░░░░░░█▄█░░▄▀
        ░░░█░░░░░░░░░░░████▀            5) Tipo
        ░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀                                                          
    """)
    opc = input("Para continuar ingresa una opcion: ")
    
    time.sleep(1)

    if opc =="1":
        
        import requests

        url_api = 'https://pokeapi.co/api/v2/pokemon/'
        response = requests.get(url_api)
        data = response.json()

        #Quizás puedo aumentarle números al final del url hasta alcanzar el límite de la gen??
        #Del 1 al 151 son gen 1
        
        d = [
                ["1:► ","1ra Generación"],
                ["2:► ","2da Generación"],
                ["3:► ","3ra Generación"],
                ["4:► ","4ta Generación"],
                ["5:► ","5ta Generación"],
                ["6:► ","6ta Generación"],
                ["7:► ","7ma Generación"],
                ["8:► ","8va Generación"],
            ]
     
        print ("{:<0} {:<10}".format('Generación','de Pokemon a Elegir:'))
        


        for v in d:
            col1, col2 = v
            print ("{:<0} {:<10}".format( col1, col2))

        #Generación 1
        def gen_uno():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 151}

            for offfset in range(0, 152, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 2
        def gen_dos():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 100}

            for offfset in range(151, 251, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 3
        def gen_tres():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 135}

            for offfset in range(251, 386, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 4
        def gen_cuatro():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 107}

            for offfset in range(386, 493, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 5
        def gen_cinco():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 156}

            for offfset in range(493, 649, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 6
        def gen_seis():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 72}

            for offfset in range(649, 721, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 7
        def gen_siete():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 88}

            for offfset in range(721, 809, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        #Generación 8
        def gen_ocho():
            url_api = 'https://pokeapi.co/api/v2/pokemon/'
            params = {'limit': 96}

            for offfset in range(809, 905, 200):
                params['offset'] = offfset
                response = requests.get(url_api, params=params)

                if response.status_code != 200:
                    print(response.text)
                else:
                    data = response.json()
                    for item in data['results']:
                        print(item['name'])

        opcion_1 = input('Ingresa el número de la generación a listar: ')
        if int(opcion_1) == 1:
            gen_uno()
        elif int(opcion_1) ==2:
            gen_dos()
        elif int(opcion_1) == 3:
            gen_tres()
        elif int(opcion_1) == 4:
            gen_cuatro()
        elif int(opcion_1) == 5:
            gen_cinco()
        elif int(opcion_1) == 6:
            gen_seis()
        elif int(opcion_1) == 7:
            gen_siete()
        elif int(opcion_1) == 8:
            gen_ocho()
        else:
            print('Opción incorrecta.')
            
    time.sleep(1)

    if opc=="2":
        
        import requests

        url_api = 'https://pokeapi.co/api/v2/pokemon/'
        response = requests.get(url_api)
        data = response.json()
        
        import requests
        d = [
                ["☆ Pichu          ", "☆ Unown"],
                ["☆ Burmy          ", "☆ Cherrym"],
                ["☆ Shellos        ", "☆ Gastrodon"],
                ["☆ Arceus         ", "☆ Deerling"],
                ["☆ Sawsbuck       ", "☆ Genesect"],
                ["☆ Vivillon       ", "☆ Flabebe"],
                ["☆ Floette        ", "☆ Furfou"],
                ["☆ Xerneas        ", "☆ Silvally"],
                ["☆ Sinistea       ", "☆ Polteageist"],
                ["☆ Alcremie       ",""],
            ]
     
        print ("{:<8} {:<30}".format('Formas','de Pokemon a Elegir:'))

        for v in d:
            col1, col2 = v
            print ("{:<8} {:<30}".format( col1, col2))

        #FORM PICHU
        def formar_pichu():
            pokemon_numbers = []
            for i in range(171, 173):
                pokemon_numbers.append(i)
            for id in pokemon_numbers:
                url_api = f'https://pokeapi.co/api/v2/pokemon/{id}/'
                response = requests.get(url_api)    
                if response.status_code != 200:
                        print(response.text)
                else:
                    data = response.json()        
                    if len(data['forms']) >= 2:
                        for item in data['forms']:
                            print(data['name'], item)
                        
        #FORM UNOWN
        def formar_unown():
            url_api = 'https://pokeapi.co/api/v2/pokemon/201/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        # #FORM BURMY
        def formar_burmy():
            url_api = 'https://pokeapi.co/api/v2/pokemon/412/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM CHERRIM
        def formar_cherrim():
            url_api = 'https://pokeapi.co/api/v2/pokemon/421/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM SHELLOS
        def formar_shellos():
            url_api = 'https://pokeapi.co/api/v2/pokemon/422/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM GASTRODON
        def formar_gastrodon():
            url_api = 'https://pokeapi.co/api/v2/pokemon/423/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM ARCEUS
        def formar_arceus():
            url_api = 'https://pokeapi.co/api/v2/pokemon/493/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM DEERLING
        def formar_deerling():
            url_api = 'https://pokeapi.co/api/v2/pokemon/585/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM SAWSBUCK
        def formar_sawsbuck():
            url_api = f'https://pokeapi.co/api/v2/pokemon/586/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM GENESECT
        def formar_genesect():
            url_api = 'https://pokeapi.co/api/v2/pokemon/649/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM VIVILLON
        def formar_vivillon():
            url_api = 'https://pokeapi.co/api/v2/pokemon/666/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM FLABEBE
        def formar_flabebe():
            url_api = 'https://pokeapi.co/api/v2/pokemon/669/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM FLOETTE
        def formar_floette():
            url_api = 'https://pokeapi.co/api/v2/pokemon/670/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM FLORGES
        def formar_florges():
            url_api = 'https://pokeapi.co/api/v2/pokemon/671/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM FURFROU
        def formar_furfrou():
            url_api = 'https://pokeapi.co/api/v2/pokemon/676/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM XERNEAS
        def formar_xerneas():
            url_api = 'https://pokeapi.co/api/v2/pokemon/716/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM SILVALLY
        def formar_silvally():
            url_api = 'https://pokeapi.co/api/v2/pokemon/773/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM SINISTEA
        def formar_sinistea():
            url_api = 'https://pokeapi.co/api/v2/pokemon/854/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM POLTEAGEIST
        def formar_polteageist():
            url_api = 'https://pokeapi.co/api/v2/pokemon/855/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        #FORM ALCREMIE
        def formar_alcremie():
            url_api = 'https://pokeapi.co/api/v2/pokemon/869/'
            response = requests.get(url_api)    
            if response.status_code != 200:
                print(response.text)
            else:
                data = response.json()        
                if len(data['forms']) >= 2:
                    for item in data['forms']:
                        print(data['name'], item)

        opcion_2 = input('Ingresa el nombre de la forma a listar: ').lower()

        if opcion_2.lower() == 'pichu':
            formar_pichu()
        elif opcion_2.lower() == 'unown':
            formar_unown()
        elif opcion_2.lower() == 'burmy':
            formar_burmy()
        elif opcion_2.lower() == 'cherrim':
            formar_cherrim()
        elif opcion_2.lower() == 'shellos':
            formar_shellos()
        elif opcion_2.lower() == 'gastrodon':
            formar_gastrodon()
        elif opcion_2.lower() == 'arceus':
            formar_arceus()
        elif opcion_2.lower() == 'deerling':
            formar_deerling()
        elif opcion_2.lower() == 'sawsbuck':
            formar_sawsbuck()
        elif opcion_2.lower() == 'genesect':
            formar_genesect()
        elif opcion_2.lower() == 'vivillon':
            formar_vivillon()
        elif opcion_2.lower() == 'flabebe':
            formar_flabebe()
        elif opcion_2.lower() == 'floette':
            formar_floette()
        elif opcion_2.lower() == 'florges':
            formar_florges()
        elif opcion_2.lower() == 'furfrou':
            formar_furfrou()
        elif opcion_2.lower() == 'xerneas':
            formar_xerneas()
        elif opcion_2.lower() == 'silvally':
            formar_silvally()
        elif opcion_2.lower() == 'sinistea':
            formar_sinistea()
        elif opcion_2.lower() == 'polteageist':
            formar_polteageist()
        elif opcion_2.lower() == 'alcremie':
            formar_alcremie()
        else:
            print('Opción incorrecta.')
            
    time.sleep(1)

    if opc =="3":
        
        url_api_3 = "https://pokeapi.co/api/v2/ability/"
        
        import requests

        d = [
                ["⭐  stench              ", "⭐ sturdy"],
                ["⭐ drizzle              ", "⭐ damp"],
                ["⭐ speed-boost          ", "⭐ limber"],
                ["⭐ battle-armor         ", "⭐ sand-veil"],
                ["⭐ static               ", "⭐ volt-absorb"],
                ["⭐ water-absorb         ", "⭐ oblivious"],
                ["⭐ intimidate           ", "⭐ trace"]      
            ]
     
        print ("{:<8} {:<30}".format('Habilidades','de Pokemon a Elegir:'))

        for v in d:
            col1, col2 = v
            print ("{:<8} {:<30}".format( col1, col2))


        def habilidades_0(ability_name):
            response = requests.get(url_api_3+ ability_name)
            
            data = response.json()

            #lista de habilidades de pokemones
            
            habilidades_pokemones = [habilidad['pokemon']['name']for habilidad in data['pokemon']]

            for i in range(len(habilidades_pokemones)):
                print("Pokemon: {}".format(habilidades_pokemones[i]))

        opcion_3 = input('Ingresa la habilidad del pokemon a listar: ').lower()
        if str(opcion_3) == "stench":
            habilidades_0("stench")
        elif str(opcion_3) == "drizzle":
            habilidades_0("drizzle")
        elif str(opcion_3) == "speed-boost":
            habilidades_0("speed-boost")
        elif str(opcion_3) == "battle-armor":
            habilidades_0("battle-armor")
        elif str(opcion_3) == "sturdy":
            habilidades_0("sturdy")
        elif str(opcion_3) == "damp":
            habilidades_0("damp")
        elif str(opcion_3) == "limber":
            habilidades_0("limber")
        elif str(opcion_3) == "sand-veil":
            habilidades_0("sand-veil")
        elif str(opcion_3) == "static":
            habilidades_0("volt-absorb")
        elif str(opcion_3) == "water-absorb":
            habilidades_0("water-absorb")
        elif str(opcion_3) == "oblivious":
            habilidades_0("oblivious")
        elif str(opcion_3) == "intimidate":
            habilidades_0("intimidate")
        elif str(opcion_3) == "trace":
            habilidades_0("trace")
        else:
            print('Habitat Incorrecto, elige otro por favor.')       
    
    time.sleep(1)
            
    if opc=="4":
        url_api_4 = "https://pokeapi.co/api/v2/pokemon-habitat/"

        import requests
        
        d = [
                ["🚀 Cave          ", "🚀 Forest"],
                ["🚀 Grassland     ", "🚀 Mounstain"],
                ["🚀 Rare          ", "🚀 Rough-Terrain"],
                ["🚀 ea            ", "🚀 Urban"],
                ["🚀 Waters-Edge   ", ""]
            ]
     
        print ("{:<8} {:<30}".format('Habitat','de Pokemon a Elegir:'))

        for v in d:
            col1, col2 = v
            print ("{:<8} {:<30}".format( col1, col2))


        def habitat(habitat_name):
            response = requests.get(url_api_4+ habitat_name)
            
            data = response.json()
            
            #lista de pokemones en habitat
            
            lista_pokemones = [pokemones['name']for pokemones in data['pokemon_species']]
            
            for i in range(len(lista_pokemones)):
                print("pokemon: {}".format(lista_pokemones[i]))
    
        opcion_4 = input('Ingresa el nombre del Habitat a listar: ').lower()
        if str(opcion_4) == "cave":
            habitat("cave")
        elif str(opcion_4) == "forest":
            habitat("forest")
        elif str(opcion_4) == "grassland":
            habitat("grassland")
        elif str(opcion_4) == "mountain":
            habitat("mountain")
        elif str(opcion_4) == "rare":
            habitat("rare")
        elif str(opcion_4) == "rough-terrain":
            habitat("rough-terrain")
        elif str(opcion_4) == "sea":
            habitat("sea")
        elif str(opcion_4) == "urban":
            habitat("urban")
        elif str(opcion_4) == "waters-edge":
            habitat("waters-edge")
        else:
            print('Habitat Incorrecto, elige otro por favor.')
    
    time.sleep(1)
    
    if opc =="5":
        url_api_5 = "https://pokeapi.co/api/v2/type/"

        import requests
        d = [
                ["🧬 Normal       ", "🧬 Fighting"],
                ["🧬 Poison       ", "🧬 Ground"],
                ["🧬 Rock         ", "🧬 Bug"],
                ["🧬 Ghost        ", "🧬 Steel"],
                ["🧬 Fire         ", "🧬 Water"],
                ["🧬 Grass        ", "🧬 Electric"],
                ["🧬 Psychic      ", "🧬 Ice"],
                ["🧬 Dragon       ", "🧬 Dark"],
                ["🧬 Fairy        ", "🧬 Unknown"],
                ["🧬 Shadow       ",""],
            ]
     
        print ("{:<8} {:<30}".format('Tipos','de Pokemon a Elegir:'))

        for v in d:
            col1, col2 = v
            print ("{:<8} {:<30}".format( col1, col2))


        def type_0(type_name):
            response = requests.get(url_api_5+ type_name)
            
            data = response.json()
            
            #lista de tipo de pokemones
            
            type_pokemones = [tipo['pokemon']['name']for tipo in data['pokemon']]

            for i in range(len(type_pokemones)):
                print("Pokemon: {}".format(type_pokemones[i]))
                
                    
        opcion_5 = input('Ingresa el tipo del pokemon a listar: ').lower()
        if str(opcion_5) == "normal":
            type_0("normal")
        elif str(opcion_5) == "fighting":
            type_0("fighting")
        elif str(opcion_5) == "flying":
            type_0("flying")
        elif str(opcion_5) == "poison":
            type_0("poison")
        elif str(opcion_5) == "ground":
            type_0("ground")
        elif str(opcion_5) == "rock":
            type_0("rock")
        elif str(opcion_5) == "bug":
            type_0("bug")
        elif str(opcion_5) == "ghost":
            type_0("ghost")
        elif str(opcion_5) == "steel":
            type_0("steel")
        elif str(opcion_5) == "fire":
            type_0("fire")
        elif str(opcion_5) == "water":
            type_0("water")
        elif str(opcion_5) == "grass":
            type_0("grass")
        elif str(opcion_5) == "electric":
            type_0("electric")
        elif str(opcion_5) == "psychic":
            type_0("psychic")
        elif str(opcion_5) == "ice":
            type_0("ice")
        elif str(opcion_5) == "dragon":
            type_0("dragon")
        elif str(opcion_5) == "dark":
            type_0("dark")
        elif str(opcion_5) == "fairy":
            type_0("fairy")
        elif str(opcion_5) == "unknown":
            type_0("unknown")
        elif str(opcion_5) == "shadow":
            type_0("shadow")
        else:
            print('Tipo Incorrecto, elige otro por favor.')
