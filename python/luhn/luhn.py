from string import punctuation, ascii_letters


class Luhn(object):

    def __init__(self, card_num):
        self.card_num = list(card_num.replace(' ', ''))

    def valid(self):
        if len(self.card_num) < 2 or any(char in punctuation or char in ascii_letters for char in self.card_num):
            return False
        new_card_num = [int(char) for char in self.card_num]
        for i in range(len(new_card_num) -2, -1, -2):
            new_card_num[i] = new_card_num[i] * 2
            if new_card_num[i] > 9:
                new_card_num[i] -= 9
        return sum(new_card_num) % 10 == 0
