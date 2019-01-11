# tennis_kata

[Originated from](https://github.com/emilybache/Tennis-Refactoring-Kata/tree/master/python)


Imagine you work for a consultancy company, and one of your colleagues has been doing some work for the Tennis Society. The contract is for 10 hours billable work, and your colleague has spent 8.5 hours working on it. Unfortunately he has now fallen ill. He says he has completed the work, and the tests all pass. Your boss has asked you to take over from him. She wants you to spend an hour or so on the code so she can bill the client for the full 10 hours. She instructs you to tidy up the code a little and perhaps make some notes so you can give your colleague some feedback on his chosen design. You should also prepare to talk to your boss about the value of this refactoring work, over and above the extra billable hours.

1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "Love", "Fifteen", "Thirty", and "Forty" respectively.
3. If at least three points have been scored by each player, and the scores are equal, the score is "Deuce".
4. If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "Advantage" for the player in the lead.

![alt text](https://www.thinktocode.com/wp-content/uploads/2018/02/red-green-refactor.png)

## [Original file](https://github.com/ksazon/tennis_kata/blob/measurments/tennis.py)
###### [Tests](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_unittest.py)
###### [Metrics](https://github.com/ksazon/tennis_kata/blob/measurments/measurments/tennis-hal.txt)
```
tennis.py
    M 16:4 TennisGame1.score - B (9)
    C 3:0 TennisGame1 - A (4)
    M 10:4 TennisGame1.won_point - A (2)
    M 4:4 TennisGame1.__init__ - A (1)
```

## [First step](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_v2.py)
###### [Tests](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_unittest_v2.py)
###### [Metrics](https://github.com/ksazon/tennis_kata/blob/measurments/measurments/tennis_v2-hal.txt)
```
class Player:

    def __init__(self, playerName, playerScore):
        self.name = playerName
        self.score = playerScore
```
____________
```
tennis_v2.py
    C 14:0 TennisGame1 - A (5)
    C 4:0 Player - A (1)
    
    M 19:4 TennisGame1.score - B (9)
    M 6:4 Player.__init__ - A (1)
    M 10:4 Player.score_point - A (1)
    M 15:4 TennisGame1.__init__ - A (1)
```

## [TennisGame v3](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_v3.py)
###### [Tests](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_unittest_v3.py)
###### [Metrics](https://github.com/ksazon/tennis_kata/blob/measurments/measurments/tennis_v3-hal.txt)
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
____________
```
tennis_v3.py
    C 45:0 TennisGame1 - A (2)
    C 4:0 Player - A (1)
    C 13:0 Score - A (1)
    C 31:0 Tie - A (1)
    
    M 55:4 TennisGame1.score - A (3)
    M 38:4 Tie.get_score - A (2)
    M 5:4 Player.__init__ - A (1)
    M 9:4 Player.score_point - A (1)
    M 14:4 Score.__init__ - A (1)
    M 18:4 Score.__iter__ - A (1)
    M 21:4 Score.get_constant_value - A (1)
    M 32:4 Tie.__init__ - A (1)
    M 35:4 Tie.is_current_score - A (1)
    M 47:4 TennisGame1.__init__ - A (1)
    M 51:4 TennisGame1.get_possible_scores - A (1)
```

## [TennisGame v4](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_v4.py)
###### [Metrics](https://github.com/ksazon/tennis_kata/blob/measurments/measurments/tennis_v4-hal.txt)

```
class Win(Score):
    def __init__(self, player1, player2):
        super(Win, self).__init__(player1, player2)

    def is_current_score(self):
        return abs(self.player1.score - self.player2.score) >= 2 and (self.player1.score >= 4 or self.player2.score >= 4)

    def get_score(self):
        return "Win for " + self.player1.name if self.player1.score > self.player2.score else "Win for " + self.player2.name
```
____________
```
tennis_v4.py
    C 45:0 Win - A (2)
    C 56:0 TennisGame1 - A (2)
    C 4:0 Player - A (1)
    C 13:0 Score - A (1)
    C 31:0 Tie - A (1)

    M 49:4 Win.is_current_score - A (3)
    M 67:4 TennisGame1.score - A (3)
    M 38:4 Tie.get_score - A (2)
    M 52:4 Win.get_score - A (2)
    M 5:4 Player.__init__ - A (1)
    M 9:4 Player.score_point - A (1)
    M 14:4 Score.__init__ - A (1)
    M 18:4 Score.__iter__ - A (1)
    M 21:4 Score.get_constant_value - A (1)
    M 32:4 Tie.__init__ - A (1)
    M 35:4 Tie.is_current_score - A (1)
    M 46:4 Win.__init__ - A (1)
    M 57:4 TennisGame1.__init__ - A (1)
    M 61:4 TennisGame1.get_possible_scores - A (1)
```

# [Refactor result](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_v5.py)
## [Tennis Classes](https://github.com/ksazon/tennis_kata/blob/measurments/tennis_classes.py)
###### [Metrics](https://github.com/ksazon/tennis_kata/blob/measurments/measurments/tennis_v5-hal.txt)
###### [Classes Metrics](https://github.com/ksazon/tennis_kata/blob/measurments/measurments/tennis_classes-hal.txt)
```
tennis_v5.py
    C 6:0 TennisGame1 - A (2)

    M 19:4 TennisGame1.score - A (3)
    M 7:4 TennisGame1.__init__ - A (1)
    M 11:4 TennisGame1.get_possible_scores - A (1)
```
