# 1. Napisz funkcję, która wypisuje z pierwszej listy imiona i nazwiska
# wszystkich adminów, po jednym adminie na linijkę
def print_admins_names(names):
    for name in names:
        print(name)


# 2. Napisz funkcję, która sprawdza czy w drugiej strukturze jest
# Ervin Howell i czy nie ma Johna Smitha
def check_one_exist_and_one_not(data, name1, name2):
    if name1 in data and name2 not in data:
        return True
    return False


# 3.Napisz funkcję, która zwróci listę długości geograficznych
# każdego z adminów
def get_admins_geo_length(data):
    lengths = []
    for item in data:
        lengths.append(item.get("address").get("geo").get("lng"))
    return lengths


admin_names = [
    "Leanne Graham",
    "Ervin Howell",
    "Clementine Bauch",
    "Patricia Lebsack",
    "Chelsey Dietrich",
    "Mrs. Dennis Schulist",
    "Kurtis Weissnat",
    "Nicholas Runolfsdottir V",
    "Glenna Reichert",
    "Clementina DuBuque",
]

admin_sites = {
    'Chelsey Dietrich': 'demarco.info',
    'Clementina DuBuque': 'ambrose.net',
    'Clementine Bauch': 'ramiro.info',
    'Ervin Howell': 'anastasia.net',
    'Glenna Reichert': 'conrad.com',
    'Kurtis Weissnat': 'elvis.io',
    'Leanne Graham': 'hildegard.org',
    'Mrs. Dennis Schulist': 'ola.org',
    'Nicholas Runolfsdottir V': 'jacynthe.com',
    'Patricia Lebsack': 'kale.biz'
}


admins_min = [
    {"Leanne Graham": "hildegard.org"},
    {"Ervin Howell": "anastasia.net"},
    {"Clementine Bauch": "ramiro.info"},
    {"Patricia Lebsack": "kale.biz"},
    {"Chelsey Dietrich": "demarco.info"},
    {"Mrs. Dennis Schulist": "ola.org"},
    {"Kurtis Weissnat": "elvis.io"},
    {"Nicholas Runolfsdottir V": "jacynthe.com"},
    {"Glenna Reichert": "conrad.com"},
    {"Clementina DuBuque": "ambrose.net"},
]

admins_full = [
    {
        "name": "Leanne Graham",
        "website": "hildegard.org",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {"lat": "-37.3159", "lng": "81.1496"},
        },
    },
    {
        "name": "Ervin Howell",
        "website": "anastasia.net",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {"lat": "-43.9509", "lng": "-34.4618"},
        },
    },
    {
        "name": "Clementine Bauch",
        "website": "ramiro.info",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {"lat": "-68.6102", "lng": "-47.0653"},
        },
    },
    {
        "name": "Patricia Lebsack",
        "website": "kale.biz",
        "address": {
            "street": "Hoeger Mall",
            "suite": "Apt. 692",
            "city": "South Elvis",
            "zipcode": "53919-4257",
            "geo": {"lat": "29.4572", "lng": "-164.2990"},
        },
    },
    {
        "name": "Chelsey Dietrich",
        "website": "demarco.info",
        "address": {
            "street": "Skiles Walks",
            "suite": "Suite 351",
            "city": "Roscoeview",
            "zipcode": "33263",
            "geo": {"lat": "-31.8129", "lng": "62.5342"},
        },
    },
    {
        "name": "Mrs. Dennis Schulist",
        "website": "ola.org",
        "address": {
            "street": "Norberto Crossing",
            "suite": "Apt. 950",
            "city": "South Christy",
            "zipcode": "23505-1337",
            "geo": {"lat": "-71.4197", "lng": "71.7478"},
        },
    },
    {
        "name": "Kurtis Weissnat",
        "website": "elvis.io",
        "address": {
            "street": "Rex Trail",
            "suite": "Suite 280",
            "city": "Howemouth",
            "zipcode": "58804-1099",
            "geo": {"lat": "24.8918", "lng": "21.8984"},
        },
    },
    {
        "name": "Nicholas Runolfsdottir V",
        "website": "jacynthe.com",
        "address": {
            "street": "Ellsworth Summit",
            "suite": "Suite 729",
            "city": "Aliyaview",
            "zipcode": "45169",
            "geo": {"lat": "-14.3990", "lng": "-120.7677"},
        },
    },
    {
        "name": "Glenna Reichert",
        "website": "conrad.com",
        "address": {
            "street": "Dayna Park",
            "suite": "Suite 449",
            "city": "Bartholomebury",
            "zipcode": "76495-3109",
            "geo": {"lat": "24.6463", "lng": "-168.8889"},
        },
    },
    {
        "name": "Clementina DuBuque",
        "website": "ambrose.net",
        "address": {
            "street": "Kattie Turnpike",
            "suite": "Suite 198",
            "city": "Lebsackbury",
            "zipcode": "31428-2261",
            "geo": {"lat": "-38.2386", "lng": "57.2232"},
        },
    },
]


print_admins_names(admin_names)

print(check_one_exist_and_one_not(admin_sites, "Ervin Howell", "John Smith"))

print(get_admins_geo_length(admins_full))
