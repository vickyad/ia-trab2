import copy
import board
import math

__BLACK = "B"
__WHITE = "W"
__MAX_DEPTH = 5


def __bigger_or_equal_than(a: int, b: int) -> bool:
    return a >= b


def __smaller_or_equal_than(a: int, b: int) -> bool:
    return a <= b


def __minmax_alphabeta(board: board.Board, player_color: str, depth: int, last_better_value: int, is_max_turn=True):
    if __is_terminal_state(board, depth):
        return (None, __eval_result(board, player_color))

    new_depth = depth + 1

    if is_max_turn:
        current_color = player_color
        better_value = -math.inf
        isBetter = __bigger_or_equal_than
    else:
        current_color = __get_enemy_color(player_color)
        better_value = math.inf
        isBetter = __smaller_or_equal_than

    better_move = None

    possible_moves = board.legal_moves(current_color)

    for possible_move in possible_moves:
        possible_board = copy.deepcopy(board)
        possible_board.process_move(possible_move, current_color)
        minmax_result = __minmax_alphabeta(possible_board, player_color, new_depth, better_value, not is_max_turn)
        possible_value = minmax_result[1]
        if isBetter(possible_value, better_value):
            better_value = possible_value
            better_move = possible_move
            if isBetter(better_value, last_better_value):
                break

    return (better_move, better_value)


def __is_terminal_state(board: board.Board, depth: int) -> bool:
    return depth >= __MAX_DEPTH or board.is_terminal_state()


def __get_enemy_color(player_color: str) -> str:
    return __WHITE if player_color == __BLACK else __BLACK


def __eval_result(board: board.Board, player_color: str) -> int:
    return __simple_points(board, player_color)


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    result = __minmax_alphabeta(the_board, color, 1, math.inf, True)
    return result[0]


# region Heuristic
def __simple_points(board: board.Board, player_color: str) -> int:
    black_count = 0
    white_count = 0
    for tile in board.tiles:
        for piece in tile:
            if piece == __BLACK:
                black_count += 1
            elif piece == __WHITE:
                white_count += 1

    result = black_count - white_count

    return result if player_color == __BLACK else -result


def __mobility_heuristic(min_moves, max_moves):
    if min_moves + max_moves == 0:
        return 0
    return 100 * (max_moves - min_moves) / (max_moves + min_moves)


def __calculate_corners(current_board_tiles, color):
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


def __corners_heuristic(max_corners, min_corners):
    if max_corners + min_corners == 0:
        return 0
    return 100 * (max_corners - min_corners) / (max_corners + min_corners)


# endregion
