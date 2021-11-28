from plancia import plancia_metro, plancia_bus, plancia_taxi, plancia_taxi_bus, plancia_taxi_bus_metro


# Implemento il grafo del campo da gioco
# Creo 3 grafi: -Taxi
#               -Bus
#               -Metro
metro = plancia_metro()
bus = plancia_bus()
taxi = plancia_taxi()


# Chiedo le posizioni dei detective e ritorna l'insieme delle posizioni
def posizioni_detective():
    while True:
        posizioni_str = input('Dove sono i detective?\n ')
        posizioni_set = {el for el in posizioni_str.split(' ') if el != ''}
        if False not in {el.isnumeric() for el in posizioni_set} and len(posizioni_set) > 0:
            return {int(el) for el in posizioni_set}


# Simulazione del gioco
def track():
    tipo = 'TAXI'
    kbus = set(bus.keys())
    kmetro = set(metro.keys())
    contatore = 0
    possibili_posti = set(plancia_taxi().keys())
    while True:
        # Un turno ogni 5 MrX deve rivelare la propria posizione
        if contatore % 5 == 0:
            while True:
                start_mrx = int(input('Dove è Mr.X?\n '))
                if start_mrx in possibili_posti:
                    break
            percorsi = {(start_mrx,)}
            # Stampa dei possibili percorsi fatti dal precedente punto di rivelazione
            if contatore != 0:
                contatore = 0
                path = sorted(
                    (pth for pth in percorsi_futuri if pth[-1] == start_mrx))
                print('I possibili percorsi fatti sono',
                      len(path), ':')
                for percorso in path:
                    print(percorso)
            possibili_posti = {start_mrx}
        # Chiedo dove sono i detective e escludo i loro nodi dai posti possibili
        posti_detective = posizioni_detective()
        # Escludo i posti e i percorsi che hanno come posto finale quello dei detective
        possibili_posti -= posti_detective
        percorsi = {strada for strada in percorsi
                    if strada[-1] not in posti_detective}
        if len(possibili_posti) == 0 or len(percorsi) == 0:
            print('I detective hanno trovato Mr.X!!!')
            return ''
        contatore = contatore + 1
        # Chiedo con che mezzo si sta spostando MrX controllando se sia un mezzo possibile o meno
        while True:
            print('Con cosa si muove Mr.X? [Taxi/Bus/Metro/Unknown]')
            tipo = input()
            if tipo.upper() not in {'M', 'B', 'T', 'U', 'METRO', 'BUS', 'TAXI', 'UNKNOWN'}:
                print('\nFINE GIOCO\n')
                return ''
            # controllo sul mezzo usato
            elif (tipo.upper() in {'BUS', 'B'} and len(possibili_posti & kbus) == 0) or (tipo.upper() in {'METRO', 'M'} and len(possibili_posti & kmetro) == 0):
                continue
            else:
                break
        percorsi_futuri = set()
        # Aggiornamento dei percorsi possibili usati da MrX e delle possibili posizioni in cui potrebbe essere
        if tipo.upper() in {'TAXI', 'T'}:
            for passato in percorsi:
                for futuro in taxi[passato[-1]]:
                    if futuro not in posti_detective:
                        percorsi_futuri.add(passato + (futuro,))
        elif tipo.upper() in {'BUS', 'B'}:
            for passato in percorsi:
                if passato[-1] in kbus:
                    for futuro in bus[passato[-1]]:
                        if futuro not in posti_detective:
                            percorsi_futuri.add(passato + (futuro,))
        elif tipo.upper() in {'METRO', 'M'}:
            for passato in percorsi:
                if passato[-1] in kmetro:
                    for futuro in metro[passato[-1]]:
                        if futuro not in posti_detective:
                            percorsi_futuri.add(passato + (futuro,))
        elif tipo.upper() in {'UNKNOWN', 'U'}:
            for passato in percorsi:
                futuri = plancia_taxi_bus_metro()[passato[-1]]
                for futuro in futuri:
                    if futuro not in posti_detective:
                        percorsi_futuri.add(passato + (futuro,))
        percorsi = percorsi_futuri
        possibili_posti = {percorso[-1] for percorso in percorsi}
        if len(possibili_posti) == 0 or len(percorsi) == 0:
            print('I detective hanno trovato Mr.X!!!')
            return ''
        print('\nMr.X è in uno di questi ', len(possibili_posti), ' posti:\n',
              sorted(possibili_posti))


track()
