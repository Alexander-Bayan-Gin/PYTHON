def same_by(characteristic, objects):
    result = list(map(characteristic, objects))
    return all([i == result[0] for i in result])

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
