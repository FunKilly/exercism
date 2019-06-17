def is_isogram(string):
    string = string.lower()
    for letter in string:
        if letter.isalpha():
            for l in string:
                if letter == l:
                    value += 1
