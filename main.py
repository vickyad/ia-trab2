import copy

import your_agent.agent as nha
import board

if __name__ == '__main__':
    initial_board = board.Board()
    print(nha.make_move(initial_board, 'B'))
