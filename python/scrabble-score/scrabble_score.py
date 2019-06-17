def score(word):
    Punctation = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):1,('D', 'G' ):2,('B', 'C', 'M', 'P'):3,
                  ('F', 'H', 'V', 'W', 'Y' ):4,'K':5,('J','X'):8,('Q','Z'):10 }
    score_sum = 0
    for l in word:
        l = l.upper()
        score_sum += sum(Punctation[key] for key in Punctation if l in key)
    return score_sum
