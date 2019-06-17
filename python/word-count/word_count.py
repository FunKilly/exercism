def word_count(phrase):
    import re
    phrase = re.findall(r"([\da-zA-Z]+[']?[\da-zA-Z]+|[\da-zA-Z]+)", phrase.lower())
    set_list = {word for word in phrase}
    counter = {word: phrase.count(word) for word in set_list }
    return counter
    pass

print(word_count('sdasda., \nasdas'))