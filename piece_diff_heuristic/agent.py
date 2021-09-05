import copy
import board
import sys

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def minimax_alphabeta(
    original_state, current_board: board.Board, color: str, depth: int, alpha, beta, is_max_turn=True
):
    global move
    current_board.print_board()

    if current_board.is_terminal_state() or depth == 0:
        return pieces_diff(original_state["board"], current_board.tiles, original_state["player"])
    successors = current_board.legal_moves(color)

    if is_max_turn:
        for s in successors:
            new_board = copy.deepcopy(current_board)
            new_board.process_move(s, color)
            v = minimax_alphabeta(original_state, new_board, new_board.opponent(color), depth - 1, alpha, beta, False)
            if v > alpha:
                alpha = v
                move = s
            if beta <= alpha:
                break
        return alpha
    else:
        for s in successors:
            new_board = copy.deepcopy(current_board)
            new_board.process_move(s, color)
            v = minimax_alphabeta(original_state, new_board, new_board.opponent(color), depth - 1, alpha, beta, True)

            if v < beta:
                beta = v
                move = s

            if alpha >= beta:
                break
        return beta


def pieces_diff(original_board_tiles, current_board_tiles, color):
    ob_tile_count = 0
    for line in original_board_tiles:
        ob_tile_count += line.count(color)
    cb_tile_count = 0
    for line in current_board_tiles:
        cb_tile_count += line.count(color)

    return ob_tile_count - cb_tile_count


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    if not the_board.legal_moves(color):
        return -1, -1
    original_state = {"board": copy.deepcopy(the_board.tiles), "player": color}
    alpha = -sys.maxunicode
    beta = sys.maxunicode
    minimax_alphabeta(original_state, the_board, color, 100, alpha, beta)
    return move
