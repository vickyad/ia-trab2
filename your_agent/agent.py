import board
import random
import sys


# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.
def minimax_alphabeta(original_state, current_board: board.Board, color: str, depth: int, is_max_turn=True):
    if current_board.is_terminal_state() or depth == 0:
        return pieces_diff(original_state['board'], current_board.tiles, original_state['player'])
    successors = current_board.legal_moves(color)
    if is_max_turn:
        v = - sys.maxunicode
        for s in successors:
            current_board.process_move(s, color)
            new_v = minimax_alphabeta(original_state, current_board, current_board.opponent(color), depth - 1, False)
            v = max(v, new_v)
        return v
    else:
        v = sys.maxunicode
        for s in successors:
            current_board.process_move(s, color)
            new_v = minimax_alphabeta(original_state, current_board, current_board.opponent(color), depth - 1, True)
            v = min(v, new_v)


def pieces_diff(original_board_tiles, current_board_tiles, color):
    return original_board_tiles.count(color) - current_board_tiles.count(color)


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])

