d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    try:
        return d[word]

    except KeyError:
        return ("That word doesn't exist!")

word = input("Enter word: ")

print(vocabulary(word))
