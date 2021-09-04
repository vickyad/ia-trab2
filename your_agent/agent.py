import copy
import board
import sys

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def minimax_alphabeta(original_state, current_board: board.Board, color: str, depth: int, alpha, beta, min_moves=0, max_moves=0, is_max_turn=True):
    global move
    print('Entrei na função minimax')
    print(f'Profundidade: {depth}')
    print('Board atual:')
    current_board.print_board()

    if current_board.is_terminal_state() or depth == 0:
        print('Hora da decisão')
        print(f'Depth: {depth} // Estado terminal? {current_board.is_terminal_state()}')
        # return mobility_heuristic(min_moves, max_moves)
        return corners_heuristic(max_moves, min_moves)
    successors = current_board.legal_moves(color)
    print(f'Sucessores {successors}')
    if is_max_turn:
        # max_moves += len(successors)
        print('Vez do MAX')
        for s in successors:
            print(f'Avaliando: {s}')
            current_board.process_move(s, color)
            max_moves = calculate_corners(current_board.tiles, color)
            current_board.print_board()
            v = minimax_alphabeta(original_state, current_board, current_board.opponent(color), depth - 1, alpha, beta, min_moves, max_moves, False)
            print(f'New_v: {v} do {s}')
            if v > alpha:
                alpha = v
                move = s
            print(f'V: {alpha} do {s}')
            if beta <= alpha:
                break
        return alpha
    else:
        # min_moves += len(successors)
        print('Vez do MIN')
        for s in successors:
            print(f'Avaliando: {s}')
            current_board.process_move(s, color)
            min_moves = calculate_corners(current_board.tiles, color)
            current_board.print_board()
            v = minimax_alphabeta(original_state, current_board, current_board.opponent(color), depth - 1, alpha, beta, min_moves, max_moves, True)
            print(f'New_v: {v} do {s}')

            if v < beta:
                beta = v
                move = s
            print(f'V: {beta} do {s}')
            if alpha >= beta:
                break
        return beta


def mobility_heuristic(min_moves, max_moves):
    if min_moves + max_moves == 0:
        return 0
    return 100 * (max_moves - min_moves)/ (max_moves + min_moves)


def calculate_corners(current_board_tiles, color):
    player_corner = 0
    if current_board_tiles[0][0] == color:
        player_corner += 1
    if current_board_tiles[0][7] == color:
        player_corner += 1
    if current_board_tiles[7][0] == color:
        player_corner += 1
    if current_board_tiles[7][7] == color:
        player_corner += 1
    return player_corner


def corners_heuristic(max_corners, min_corners):
    if max_corners + min_corners == 0:
        return 0
    return 100 * (max_corners - min_corners) / (max_corners + min_corners)


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    if not the_board.legal_moves(color):
        return -1, -1
    original_state = {'board': copy.deepcopy(the_board.tiles), 'player': color}
    alpha = - sys.maxunicode
    beta = sys.maxunicode
    minimax_alphabeta(original_state, the_board, color, 100, alpha, beta)
    return move
