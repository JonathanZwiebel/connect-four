from connect_four import ConnectFourGame
from human_agent import human_agent
from random_agent import random_agent

import random
import time

def play_connect_four_game(first_agent, second_agent):
    game = ConnectFourGame(board_size = (6, 7), match_length = 4)
    print("New Game")
    state = game.start_state()

    while True:
        game.print_state(state)
        action = first_agent(game, state)
        state = game.successor(state, action)
        if game.is_end(state)[0]:
            break
        game.print_state(state)
        action = second_agent(game, state)
        state = game.successor(state, action)
        if game.is_end(state)[0]:
            break

    game.print_board(state[0])
    result = game.is_end(state)[1]
    if result == 0:
        print("Tie Game")
    elif result == 1:
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")

def test_connect_four_game():
    game = ConnectFourGame(board_size = (6, 7), match_length = 4)
    win_count = [0, 0, 0]

    start_time = time.time()
    games = 100

    for i in range(games):
        state = game.start_state()

        while True:
            input("Enter to continue")
            print(game.print_state(state))
            actions = game.actions(state)   
            print("Current Actions: " + str(actions))
            chosen_action = random.choice(actions)
            chosen_action = int(input("Choose an Action: "))
            print("Chosen Action: " + str(chosen_action))
            state = game.successor(state, chosen_action)
            if game.is_end(state)[0]:
                break
        print("Current State:")
        game.print_state(state)
        print(game.is_end(state))
        win_count[game.is_end(state)[1]] += 1
    end_time = time.time()

    print(win_count)
    print("Took " + str(end_time - start_time) + " seconds to play " + str(games) + " games")
    time_per_game = (end_time - start_time) / games
    print("Took " + str(time_per_game * 1000) + " ms per game")
    time_per_move = time_per_game / (game.num_cols * game.num_rows)
    print("Took ~" + str(time_per_move * 1000) + " ms per move")

play_connect_four_game(human_agent, human_agent)