#codewars homework:

def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

import codewars_test as test

@test.describe("rock paper scissors")
def basic_tests():
    @test.it("Player 1 wins")
    def player_1():
        test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
    
    @test.it("Player 2 wins")
    def player_2():
        test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
    
    @test.it("Draw")
    def draw():
        test.assert_equals(rps('rock', 'rock'), 'Draw!')