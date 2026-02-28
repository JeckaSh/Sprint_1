world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

for key, value in world_champions.items():
    print(key, '-', value)

country = 'Италия'

for key, value in world_champions.items():
    if country in value:
        print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
    else:
        print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
    