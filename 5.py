a = 0
name = None


def polite_input(info):
    global a
    global name
    if a == 0:
        name = str(input("Как вас зовут?\n")) + ","
        a += 1

    print(name, info)
    return input()


age = polite_input("укажите возраст")
school_number = polite_input("укажите номер школы")
class_num = polite_input("укажите полный номер класса")