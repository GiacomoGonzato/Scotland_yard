# Funzioni che riportano tutte le informazioni di collegamenti della plancia

# Plancia
def plancia_metro():
    return {1: (46,),
            13: (46, 67, 89),
            46: (1, 13, 74, 79),
            67: (13, 79, 89, 111),
            74: (46,),
            79: (46, 67, 93, 111),
            89: (13, 67, 140, 128),
            93: (79,),
            111: (67, 79, 153, 163),
            128: (89, 140, 185),
            140: (89, 128, 153),
            153: (111, 140, 163, 185),
            163: (111, 153),
            185: (153, 128)}


def plancia_bus():
    return {1: (46, 58),
            3: (22, 23),
            7: (42,),
            13: (23, 14, 52),
            14: (13, 15),
            15: (14, 29, 41),
            22: (3, 23, 34, 65),
            23: (3, 13, 22, 67),
            29: (15, 41, 42, 55),
            34: (22, 46, 63),
            41: (15, 29, 52, 87),
            42: (7, 29, 72),
            46: (1, 34, 58, 78),
            52: (13, 41, 67, 86),
            55: (29, 89),
            58: (1, 46, 74, 77),
            63: (34, 65, 79, 100),
            65: (22, 63, 67, 82),
            67: (23, 52, 65, 82, 102),
            72: (42, 105, 107),
            74: (58, 94),
            77: (58, 78, 94, 124),
            78: (46, 77, 79),
            79: (63, 78),
            82: (65, 67, 100, 140),
            86: (52, 87, 102, 116),
            87: (41, 86, 105),
            89: (55, 105),
            93: (94,),
            94: (74, 77, 93),
            100: (63, 82, 111),
            102: (67, 86, 127),
            105: (72, 87, 89, 107, 108),
            107: (72, 105, 161),
            108: (105, 116, 135),
            111: (100, 124),
            116: (86, 108, 127, 142),
            122: (123, 144),
            123: (122, 124, 144, 165),
            124: (77, 111, 123, 153),
            127: (102, 116, 133),
            128: (135, 142, 161, 187, 199),
            133: (127, 140, 157),
            135: (108, 128, 161),
            140: (82, 133, 154, 156),
            142: (116, 128, 157),
            144: (122, 123, 163),
            153: (124, 154, 180, 184),
            154: (140, 153, 156),
            156: (140, 154, 157, 184),
            157: (133, 142, 156, 185),
            161: (107, 128, 135, 199),
            163: (144, 176, 191),
            165: (123, 180, 191),
            176: (163, 190),
            180: (153, 165, 184, 190),
            184: (153, 156, 180, 185),
            185: (157, 184, 187),
            187: (128, 185),
            190: (176, 180, 191),
            191: (163, 165, 190),
            199: (128, 161)}


def plancia_taxi():
    return {1: (8, 9),
            2: (20, 10),
            3: (11, 12, 4),
            4: (3, 13),
            5: (15, 16),
            6: (29, 7),
            7: (6, 17),
            8: (1, 18, 19),
            9: (1, 19, 20),
            10: (2, 21, 34, 11),
            11: (10, 3, 22),
            12: (3, 23),
            13: (4, 23, 24, 14),
            14: (13, 25, 15),
            15: (14, 5, 26, 16, 28),
            16: (5, 15, 28, 29),
            17: (7, 29, 30),
            18: (8, 31, 43),
            19: (8, 9, 32),
            20: (9, 2, 33),
            21: (10, 33),
            22: (11, 34, 35, 23),
            23: (12, 22, 37, 13),
            24: (13, 37, 38),
            25: (14, 38, 39),
            26: (15, 39, 27),
            27: (26, 28, 40),
            28: (15, 16, 27, 41),
            29: (16, 41, 6, 17, 42),
            30: (17, 42),
            31: (18, 43, 44),
            32: (19, 44, 45, 33),
            33: (20, 21, 32, 46),
            34: (47, 10, 22, 48),
            35: (22, 48, 65, 36),
            36: (35, 49, 37),
            37: (36, 23, 50, 24),
            38: (24, 50, 25, 51),
            39: (25, 51, 26, 52),
            40: (27, 52, 53, 41),
            41: (28, 40, 54, 29),
            42: (29, 30, 56, 72),
            43: (18, 31, 57),
            44: (31, 32, 58),
            45: (32, 58, 59, 60, 46),
            46: (33, 45, 47, 61),
            47: (46, 62, 34),
            48: (34, 62, 63, 35),
            49: (36, 50, 66),
            50: (49, 37, 38),
            51: (38, 39, 52, 68, 67),
            52: (51, 39, 40, 69),
            53: (40, 54, 69),
            54: (41, 53, 70, 55),
            55: (54, 71),
            56: (42, 91),
            57: (43, 58, 73),
            58: (75, 57, 44, 45, 59, 74),
            59: (58, 45, 76, 75),
            60: (45, 76, 61),
            61: (46, 62, 76, 60, 78),
            62: (61, 47, 48, 79),
            63: (48, 79, 64, 80),
            64: (63, 81, 65),
            65: (64, 35, 66, 82),
            66: (65, 49, 67, 82),
            67: (51, 68, 84, 66),
            68: (67, 51, 69, 85),
            69: (52, 68, 53, 86),
            70: (54, 71, 87),
            71: (70, 55, 89, 72),
            72: (71, 42, 90, 91),
            73: (57, 74, 92),
            74: (73, 75, 92, 58),
            75: (74, 58, 59, 94),
            76: (59, 60, 61, 77),
            77: (76, 78, 95, 96),
            78: (77, 61, 79, 97),
            79: (62, 78, 98, 63),
            80: (63, 99, 100),
            81: (64, 100, 82),
            82: (65, 66, 81, 101),
            83: (101, 102),
            84: (67, 85),
            85: (68, 84, 103),
            86: (69, 103, 104),
            87: (70, 88),
            88: (87, 89, 117),
            89: (71, 88, 105),
            90: (105, 91, 72),
            91: (90, 72, 56, 107, 105),
            92: (73, 74, 93),
            93: (92, 94),
            94: (93, 75, 95),
            95: (94, 77, 122),
            96: (77, 97, 109),
            97: (96, 78, 98, 109),
            98: (97, 79, 99, 110),
            99: (98, 110, 112, 80),
            100: (80, 112, 113, 101, 81),
            101: (100, 82, 83, 114),
            102: (83, 103, 115),
            103: (102, 85, 86),
            104: (86, 116),
            105: (89, 90, 91, 106, 108),
            106: (105, 107),
            107: (106, 91, 119),
            108: (105, 117, 119),
            109: (96, 97, 110, 124),
            110: (98, 99, 111, 109),
            111: (110, 112, 124),
            112: (111, 99, 100, 125),
            113: (100, 114, 125),
            114: (113, 101, 115, 126, 132, 131),
            115: (114, 102, 126, 127),
            116: (104, 127, 118, 117),
            117: (116, 129, 108, 88),
            118: (116, 129, 134, 142),
            119: (108, 136, 107),
            120: (144, 121),
            121: (120, 145, 122),
            122: (121, 146, 123, 95),
            123: (122, 137, 124, 148, 149),
            124: (123, 109, 111, 130, 138),
            125: (112, 113, 131),
            126: (114, 115, 127, 140),
            127: (126, 115, 116, 134, 133),
            128: (142, 143, 160, 172, 188),
            129: (118, 117, 135, 143, 142),
            130: (124, 131, 139),
            131: (130, 125, 114),
            132: (114, 140),
            133: (140, 127, 141),
            134: (141, 127, 118, 142),
            135: (129, 143, 161, 136),
            136: (135, 119, 162),
            137: (147, 123),
            138: (124, 150, 152),
            139: (130, 153, 154, 140),
            140: (139, 132, 126, 133, 156, 154),
            141: (133, 134, 142, 158),
            142: (141, 134, 118, 129, 143, 128, 158),
            143: (142, 129, 135, 160, 128),
            144: (120, 145, 177),
            145: (144, 121, 146),
            146: (145, 122, 147, 163),
            147: (146, 137, 164),
            148: (164, 123, 149),
            149: (148, 123, 150, 165),
            150: (138, 149, 151),
            151: (150, 152, 166, 165),
            152: (138, 151, 153),
            153: (152, 139, 154, 167, 166),
            154: (153, 139, 140, 155),
            155: (154, 156, 168, 167),
            156: (155, 140, 157, 169),
            157: (156, 158, 170),
            158: (141, 157, 159, 142),
            159: (158, 172, 198, 186, 170),
            160: (143, 161, 173, 128),
            161: (160, 135, 174),
            162: (136, 175),
            163: (146, 177),
            164: (147, 148, 179, 178),
            165: (149, 151, 180, 179),
            166: (151, 153, 183, 181),
            167: (153, 155, 168, 183),
            168: (167, 155, 184),
            169: (156, 184),
            170: (157, 159, 185),
            171: (173, 199, 175),
            172: (128, 159, 187),
            173: (160, 174, 171, 188),
            174: (173, 161, 175),
            175: (174, 162, 171),
            176: (177, 189),
            177: (176, 144, 163),
            178: (164, 191, 189),
            179: (164, 165, 191),
            180: (165, 181, 193),
            181: (180, 166, 182, 193),
            182: (181, 183, 195),
            183: (182, 166, 167, 196),
            184: (168, 169, 185, 197, 196),
            185: (184, 170, 186),
            186: (185, 198, 159),
            187: (172, 188, 198),
            188: (187, 128, 173, 199),
            189: (176, 178, 190),
            190: (189, 191, 192),
            191: (190, 178, 179, 192),
            192: (190, 191, 194),
            193: (180, 181, 194),
            194: (192, 193, 195),
            195: (194, 182, 197),
            196: (183, 184, 197),
            197: (196, 184, 195),
            198: (186, 159, 187, 199),
            199: (188, 171, 198)}


def plancia_taxi_bus_metro():
    grafo = dict()
    for nodo in plancia_taxi().keys():
        if nodo in plancia_metro().keys():
            grafo[nodo] = tuple(sorted(set(
                plancia_taxi()[nodo] + plancia_bus()[nodo] + plancia_metro()[nodo])))
        elif nodo in plancia_bus().keys():
            grafo[nodo] = tuple(sorted(set(
                plancia_taxi()[nodo] + plancia_bus()[nodo])))
        else:
            grafo[nodo] = tuple(sorted(plancia_taxi()[nodo]))
    return grafo


def plancia_taxi_bus():
    grafo = dict()
    for nodo in plancia_taxi().keys():
        if nodo in plancia_bus().keys():
            grafo[nodo] = tuple(
                sorted(set(plancia_taxi()[nodo] + plancia_bus()[nodo])))
        else:
            grafo[nodo] = tuple(sorted(plancia_taxi()[nodo]))
    return grafo


# Controllo consistenza della Plancia
def check_consistency(dizio):
    # dato un dizionario controllo se tutti i collegamenti tra i nodi sono sensati e reciproci
    flag = True
    for numero in dizio.keys():
        for valore in dizio[numero]:
            if not (numero in dizio[valore]):
                flag = False
                print('\nProblema inconsistenza!\n', numero)
                for x in dizio[numero]:
                    print('  ', x)
                print(valore)
                for x in dizio[valore]:
                    print('  ', x)
    if flag:
        print('\nNessun problema di inconsistenza trovato\n')
    return


# Creo la funzione che descrive i percorsi più veloci tra due nodi
# basata sul numero di spostamenti minimi per andare da un nodo A a uno B
# in base al mezzo usato
# Ritorna una lista ordinata di percorsi oppure una tupla contenente -1 in caso di errori
def short_path(start, end, vehicle='M'):
    vehicle = vehicle.upper()
    if vehicle not in {'M', 'B', 'T', 'METRO', 'BUS', 'TAXI'}:
        print('Veicolo di spostamento definito in modo errato!')
        return (-1,)
    if vehicle in {'M', 'METRO'}:
        grafo = plancia_taxi_bus_metro()
    elif vehicle in {'B', 'BUS'}:
        grafo = plancia_taxi_bus()
    else:
        grafo = plancia_taxi()
    if start not in grafo.keys() or end not in grafo.keys():
        print('Punto di partenza o di arrivo non definiti nella Plancia!')
        return (-1,)
    visited = {start}
    distance = dict()
    i = 1
    distance[0] = {(start,)}
    while end not in visited:
        distance[i] = set()
        for path in distance[i-1]:
            for nodo_futuro in set(grafo[path[-1]]) - visited:
                distance[i].add(path + (nodo_futuro,))
        for path in distance[i-1]:
            visited |= {nodo for nodo in grafo[path[-1]]}
        i += 1
    return sorted({cammino for cammino in distance[i-1] if cammino[-1] == end})


# Ritorna un dizionario con chiave la distanza e valore i nodi a tale distanza dal punto
def distance(point, vehicle='M'):
    vehicle = vehicle.upper()
    if vehicle not in {'M', 'B', 'T', 'METRO', 'BUS', 'TAXI'}:
        print('Veicolo di spostamento definito in modo errato!')
        return -1
    if vehicle in {'M', 'METRO'}:
        grafo = plancia_taxi_bus_metro()
    elif vehicle in {'B', 'BUS'}:
        grafo = plancia_taxi_bus()
    else:
        grafo = plancia_taxi()
    if point not in grafo.keys():
        print('Punto di partenza o di arrivo non definiti nella Plancia!')
        return -1
    distanza = dict()
    distanza[0] = {point}
    visited = {point}
    n_posti = len(grafo.keys())
    i = 1
    while len(visited) < n_posti:
        distanza[i] = set()
        for nodo in distanza[i-1]:
            luoghi = {next_posto for next_posto in
                      set(grafo[nodo]) - visited}
            distanza[i] |= luoghi
            visited |= luoghi
        i += 1
    return distanza
