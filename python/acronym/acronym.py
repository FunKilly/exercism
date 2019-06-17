def abbreviate(words):
    import re
    words = re.findall(r"([\da-zA-Z]+[']?[\da-zA-Z]+|[\da-zA-Z]+)", words.upper())
    return ''.join(word[0] for word in words)
    pass

