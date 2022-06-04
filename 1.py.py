translated_text = None


def translate(text):
    for lan in text:
        if lan in "УЕАОЭЯЮЫЁИуеаоэяюыёи.,:;'?!-":
            text = text.replace(lan, '')

        elif lan in '"':
            text = text.replace(lan, '')

    for i in range(len(text)):
        if text.find(" ") == 0:
            text = text.replace(" ", "", 1)
        elif text.find(" ") == text.find(" ", text.find(" ")+1)-1:
            text = text.replace(" ", "", 1)
        elif text.find(" ") == len(text) - 1:
            text = text.replace(" ", "", 1)
        else:
            text = text.replace(" ", "_", 1)

    text = text.replace("_", " ")

    global translated_text
    translated_text = text


a = "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать."
b = "А я?"
c = "гдеёж"
translate(a)
print(translated_text)
