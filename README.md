# zjprog

[Originated from](https://github.com/emilybache/Tennis-Refactoring-Kata/tree/master/python)


Imagine you work for a consultancy company, and one of your colleagues has been doing some work for the Tennis Society. The contract is for 10 hours billable work, and your colleague has spent 8.5 hours working on it. Unfortunately he has now fallen ill. He says he has completed the work, and the tests all pass. Your boss has asked you to take over from him. She wants you to spend an hour or so on the code so she can bill the client for the full 10 hours. She instructs you to tidy up the code a little and perhaps make some notes so you can give your colleague some feedback on his chosen design. You should also prepare to talk to your boss about the value of this refactoring work, over and above the extra billable hours.

1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "Love", "Fifteen", "Thirty", and "Forty" respectively.
3. If at least three points have been scored by each player, and the scores are equal, the score is "Deuce".
4. If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "Advantage" for the player in the lead.

[Original file](https://github.com/ksazon/tennis_kata/blob/master/tennis.py)

Metryki. (obrazek wkleić?)

[First step](https://github.com/ksazon/tennis_kata/blob/master/tennis_v2.py)
```
class Player:

    def __init__(self, playerName, playerScore):
        self.name = playerName
        self.score = playerScore
```
Metryki.

[TennisGame v3](https://github.com/ksazon/tennis_kata/blob/master/tennis_v3.py)
```
class Score(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __iter__(self):
        return self

    @staticmethod
    def get_constant_value(self, value):
        dictionary = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty"
        }
        return dictionary.get(value)

class Tie(Score):
    def __init__(self, player1, player2):
        super(Tie, self).__init__(player1, player2)

    def is_current_score(self):
        return self.player1.score == self.player2.score

    def get_score(self):
        if(self.player1.score > 2):
            return "Deuce"
        else:
            return Score.get_constant_value(self, self.player1.score) + "-All"
```
Metryki.

[TennisGame v4](https://github.com/ksazon/tennis_kata/blob/master/tennis_v4.py)

```
class Win(Score):
    def __init__(self, player1, player2):
        super(Win, self).__init__(player1, player2)

    def is_current_score(self):
        return abs(self.player1.score - self.player2.score) >= 2 and (self.player1.score >= 4 or self.player2.score >= 4)

    def get_score(self):
        return "Win for " + self.player1.name if self.player1.score > self.player2.score else "Win for " + self.player2.name
```

[Refactor result](https://github.com/ksazon/tennis_kata/blob/master/tennis_v5.py)

Metryki. 
