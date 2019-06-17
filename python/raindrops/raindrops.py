def raindrops(number):
    factors = {3:'Pling',5:"Plang",7:'Plong'}
    communicate = ''
    for key in factors:
        if number % key == 0:
            communicate += factors[key]
        else:
            pass
    if communicate:
        return communicate
    else:
        return str(number)

raindrops(1)

