message = None


def print_without_duplicates(string):
    global message
    if string != message:
        print(string)
    message = string
