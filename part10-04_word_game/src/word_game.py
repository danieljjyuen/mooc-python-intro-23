# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word:str, player2_word:str):
        if len(player1_word) == len(player2_word):
            pass
        elif len(player1_word) > len(player2_word):
            return 1
        else:
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)

    def round_winner(self, player1_word:str, player2_word:str):
        p1 = 0
        p2 = 0
        p1lower = player1_word.lower()
        p2lower = player2_word.lower()
        p1 += p1lower.count("a")
        p2 += p2lower.count("a")
        p1 += p1lower.count("e")
        p2 += p2lower.count("e")
        p1 += p1lower.count("i")
        p2 += p2lower.count("i")
        p1 += p1lower.count("o")
        p2 += p2lower.count("o")
        p1 += p1lower.count("u")
        p2 += p2lower.count("u")
        if p1 == p2:
            pass
        elif p1 > p2:
            return 1
        else: 
            return 2   

class RockPaperScissors(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        valid = ["rock", "scissors", "paper"]
        if player1_word not in valid and player2_word not in valid:
            return 3
        elif player1_word not in valid and player2_word in valid:
            return 2
        elif player1_word in valid and player2_word not in valid:
            return 1
        
        
        if player1_word == player2_word:
            return 3
        if player1_word == "rock":
            if player2_word == "scissors":
                return 1
            else:
                return 2
        if player1_word == "scissors":
            if player2_word == "paper":
                return 1
            else:
                return 2
        if player1_word == "paper":
            if player2_word == "rock":
                return 1
            else:
                return 2