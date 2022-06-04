from math import ceil

cities = ['Братислава Словакия 625167',
          'Брюссель Бельгия 1154635',
          'Будапешт Венгрия 1757618',
          'Белград Сербия 1233796',
          'Прага Чехия 1267449',
          'София Болгария 1286383',
          'Тбилиси Грузия 1118035']

popul = {}

for x in cities:
    city, _, pop = x.split()
    pop = int(ceil(int(pop) / 100000)) * 100
    popul[pop] = popul.get(pop, []) + [city]

popul = sorted(popul.items())

for k, v in popul:
        s = ','.join(sorted(v))
        print(int(k) - 100, '-',  str(k) + ':',  s)
