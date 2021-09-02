import copy
import board
import sys

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def minimax_alphabeta(original_state, current_board: board.Board, color: str, depth: int, is_max_turn=True):
    global move
    print('Entrei na função minimax')
    print('Board atual:')
    current_board.print_board()

    if current_board.is_terminal_state() or depth == 0:
        print('Hora da decisão')
        print(f'Depth: {depth} // Estado terminal? {current_board.is_terminal_state()}')
        return pieces_diff(original_state['board'], current_board.tiles, original_state['player'])
    successors = current_board.legal_moves(color)
    print(f'Sucessores {successors}')
    if is_max_turn:
        print('Vez do MAX')
        v = - sys.maxunicode
        for s in successors:
            print(f'Avaliando: {s}')
            current_board.process_move(s, color)
            current_board.print_board()
            new_v = minimax_alphabeta(original_state, current_board, current_board.opponent(color), depth - 1, False)
            print(f'New_v: {new_v} do {s}')
            if new_v > v:
                v = new_v
                move = s
            print(f'V: {v} do {s}')
        return v
    else:
        print('Vez do MIN')
        v = sys.maxunicode
        for s in successors:
            print(f'Avaliando: {s}')
            current_board.process_move(s, color)
            current_board.print_board()
            new_v = minimax_alphabeta(original_state, current_board, current_board.opponent(color), depth - 1, True)
            print(f'New_v: {new_v} do {s}')

            if new_v < v:
                v = new_v
                move = s
            print(f'V: {v} do {s}')
        return v


def pieces_diff(original_board_tiles, current_board_tiles, color):
    print('Fazendo os calculos com')
    print(original_board_tiles)
    print(current_board_tiles)
    ob_tile_count = 0
    for line in original_board_tiles:
        ob_tile_count += line.count(color)
    cb_tile_count = 0
    for line in current_board_tiles:
        cb_tile_count += line.count(color)
    print(f'Quantidade de {color} no original board: {ob_tile_count}')
    print(f'Quantidade de {color} na table atual: {cb_tile_count}')
    return ob_tile_count - cb_tile_count


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
    minimax_alphabeta({'board': copy.deepcopy(the_board.tiles), 'player': color}, the_board, color, 4)
    return move
