class HighScores:

    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(scores)

    def latest(self):
        length = len(scores)
        return scores[length-1]

    def personal_top_three(self):
        self.scores.sort(reverse=True)
        x = 0
        top_three = []
        while x != 3:
            try:
                top_three.append(self.scores[x])
            except:
                pass
            x += 1
        return(top_three)


scores = [100, 0, 90, 30]
print(HighScores(scores).latest())



