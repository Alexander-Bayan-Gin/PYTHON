def main():

    p = float(input("Введите p: "))
    q = float(input("Введите q: "))

    def discriminant(a, b, c):

        discriminant_var = b ** 2 - 4 * a * c

        if discriminant_var <= 0:
            discriminant_var = -(discriminant_var)

        return discriminant_var

    def larger_root(b, c):

        return (- b + discriminant(1, b, c) ** 0.5) / 2

    def smaller_root(b, c):
        return (- b - discriminant(1, b, c) ** 0.5) / 2

    print(discriminant(1, p, q))
    print(larger_root(p, q), smaller_root(p, q))


main()