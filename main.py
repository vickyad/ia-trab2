import copy

import mixed_heuristic.agent as nha
import board

if __name__ == "__main__":
    initial_board = board.Board()
    print(f'Retorno: {nha.make_move(initial_board, "B")}')
