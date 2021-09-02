import your_agent.agent as nha
import board

if __name__ == '__main__':
    initial_board = board.Board()
    print(nha.minimax_alphabeta({'board': initial_board.tiles, 'player': 'B'}, initial_board, 'B', 4))
