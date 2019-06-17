def two_fer(name=''):
    if name:
        x = name
    else:
        x = 'you'
    return "One for {}, one for me.".format(x)


two_fer()

