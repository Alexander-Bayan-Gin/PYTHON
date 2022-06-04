numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# массив нечетных чисел
odd = []
# массив четных чисел
even = []
for number in numbers:
   if number % 2 == 0:
       # если делится на 2 без остатка добавляем в четные
       even.append(number)
   else:
       # если делится на 2 с остатком добавляем в нечетные
       odd.append(number)
# смотрим результат
print(odd)
print(even)
