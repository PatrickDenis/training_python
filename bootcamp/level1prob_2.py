def master_yoda(word):
    words = word.split(" ")

    result = " ".join(reversed(words))
    print(result)
    return result

master_yoda("Holla le fou")
