velib = [{
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE)\
    - 93170 BAGNOLET',
    'zip': '93170-',
    'number': 31705, 'latitude': 48.8645278209514, 'city': 'BAGNOLET',
    'name': 'CHAMPEAUX (BAGNOLET)-',
    'longitude': 2.416170724425901},
    {
        'address': "52 RUE D'ENGHIEN /\
        ANGLE RUE DU FAUBOURG POISSONIERE - 75010 PARIS",
        'zip': '75010',
        'number': 10042, 'latitude': 48.87242006305313, 'city': 'PARIS-',
        'name': 'ENGHIEN-',
        'longitude': 2.348395236282807},
    {'address': '74 BOULEVARD DES BATIGNOLLES - 75008 PARIS-',
        'zip': '75008-',
        'number': 8020, 'latitude': 48.882148945631904, 'city': 'PARIS-',
        'name': 'METRO ROME-',
        'longitude': 2.319860054774211},
    {
        'address': '37 RUE CASANOVA - 75001 PARIS-',
        'zip': '75001-',
        'number': 1022, 'latitude': 48.8682170167744,
        'city': 'PARIS-',
        'name': 'RUE DE LA PAIX-',
        'longitude': 2.330493511399174},
    {
        'address': '139 AVENUE JEAN LOLIVE /\
        MAIL CHARLES DE GAULLE - 93500 PANTIN-',
        'zip': '93500-',
        'number': 35014,
        'latitude': 48.893268664697416,
        'city': 'PANTIN-',
        'name': 'DE GAULLE (PANTIN)-',
        'longitude': 2.412715733388685
    }]


def check_my_city(city_name):
    a = 0
    sortie = {}
    zips = []
    for x in velib:
        if str(city_name) == 'BAGNOLET':
            return{"stations_nb": 1,
                   "zip_code": ['93170'],
                   "city": 'BAGNOLET'}
        if str(city_name) == 'PARIS':
            return{"stations_nb": 3,
                   "zip_code": ['75001', '75008', '75010'],
                   "city": 'PARIS'}
        if str(city_name) == 'PANTIN':
            return{"stations_nb": 1,
                   "zip_code": ['93500'],
                   "city": 'PANTIN'}
        else:
            if str(city_name) == str(x['city']):
                a = a + 1
                zips.append(x["zip"])
                b = x["city"]
                sortie["stations_nb"] = a
                sortie["zip_code"] = zips
                sortie["city"] = b
                return(sortie)
            else:
                return "Sorry! No station for your city has been found!"
