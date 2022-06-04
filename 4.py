number_items = 0
number_receipt = 0
all_items_name_and_cost = ""
total_cost = 0


def print_receipt():

    global number_items

    if number_items == 0:
        pass
    else:
        global number_receipt
        global total_cost
        global all_items_name_and_cost

        number_receipt += 1
        print("Чек", number_receipt, ". ", "Всего предметов: ", number_items)

        while all_items_name_and_cost.find("*"):

            items_name_and_cost = all_items_name_and_cost[0:all_items_name_and_cost.find("*")]
            all_items_name_and_cost = all_items_name_and_cost[all_items_name_and_cost.find("*"):len(all_items_name_and_cost)]
            all_items_name_and_cost = all_items_name_and_cost.replace("*", "", 1)

            print(items_name_and_cost)

            if len(all_items_name_and_cost) == 0:
                break

        print("Итого: ", total_cost)
        print("-----")

        number_items = 0
        all_items_name_and_cost = ""
        total_cost = 0


def add_item(item_name, item_cost):

    global number_items
    global all_items_name_and_cost
    global total_cost

    number_items += 1
    total_cost += item_cost
    all_items_name_and_cost += item_name + " - " + str(item_cost) + "*"


def cancel():

    global number_items
    global all_items_name_and_cost
    global total_cost

    number_items = 0
    all_items_name_and_cost = ""
    total_cost = 0


add_item("Блокнот", 100)
print_receipt()

add_item("Ручка", 70)
print_receipt()
print_receipt()

add_item("Булочка", 15)
add_item("Булочка", 15)
add_item("Чай", 5)
print_receipt()

add_item("Булочка", 20)
add_item("Булочка", 20)
cancel()