def transformation(x):
    return x + 5


def simple_map(transformation, values):
    return [transformation(x) for x in values]


lst = [1, 3, 1, 5, 7]
print(*simple_map(transformation, lst))

