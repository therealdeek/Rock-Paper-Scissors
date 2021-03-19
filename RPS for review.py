#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Player:

    my_move = random.choice(moves)
    their_move = random.choice(moves)
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):

    def move(self):
        decision = random.choice(moves)
        return(decision)

class HumanPlayer(Player):
    def move(self):
        selection = input('What is your move? Rock, Paper, or Scissors: ')

        while True:
            human_move = input(str(moves))
            if human_move == input(str(moves)):
                return human_move
            else:
                print("incorrect choice, please try again")
            return (human_move.lower())
        return human_move

class ReflectPlayer(Player):

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move

class CyclePlayer(Player):

    def move(self):
        index = moves.index(self.my.move) + 1
        return moves[index % len(moves)]

    def learn(self, my_move, their_move):
        self.their_move = their_move

class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f" Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score_p1 +=1
            print("Player 1 wins, check out the score! ")
        elif beats(move2, move1):
            self.score_p2 +=1
            print("Player 2 wins, watch out now! ")
        else:
            move1 == move2
            print("No winners, because, it's a Tie! ")
            print(f'Player 1 score: {self.score_p1}', f'Player 2 score: {self.score_p2}')

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print('Come back to play again!')
            if self.score_p1 > self.score_p2:
                print('Player 1 wins as usual, step your game up Player 2! ')
            elif self.score_p2 > self.score_p1:
                print("Player 2 won this time, Player 1 you are off, aren't you!?!?!? ")
        else:
            print("The game is not fun anymore because it's a TIE...Bogus!")
            print("Game over!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

