import copy
import board
import math

BLACK = "B"
WHITE = "W"
EMPTY = "."
__MAX_DEPTH = 4


class GameState:
    def __init__(self, board: board.Board, player_color: str):
        # Armazena o board atual
        self.board = board
        # Armazena a cor do jogador
        self.player_color = player_color
        # Armazena a cor do inimigo
        self.enemy_color = WHITE if player_color == BLACK else BLACK
        # Conta se a jogada atual é do jogador ou do inimigo
        self.is_player_turn = True
        # Armazena a profundidade atual da análise de jogada
        self.depth = 0
        # Armazena a quantidade atual (ou da jogada anterior) de movimentos possíveis do inimigo
        self.enemy_possible_moves_count = 0
        # Armazena a quantidade atual (ou da jogada anterior) de movimentos possíveis do jogador
        self.player_possible_moves_count = 0

    def apply_move(self, move):
        """
        Aplica um movimento ao board, mudando seu estado atual, o jogador atual
        e a profundidade da jogada em relação ao inicio
        """
        color = self.player_color if self.is_player_turn else self.enemy_color
        self.depth += 1
        self.is_player_turn = not self.is_player_turn
        self.board.process_move(move, color)

    def calc_possible_moves(self):
        """
        Calcula os movimentos possíveis e atualiza a informação quanto a quantidade de possíveis
        movimentos do jogador ou do seu inimigo
        """
        color = self.player_color if self.is_player_turn else self.enemy_color
        possible_moves = self.board.legal_moves(color)
        possible_moves_count = len(possible_moves)
        if self.is_player_turn:
            self.player_possible_moves_count = possible_moves_count
        else:
            self.enemy_possible_moves_count = possible_moves_count
        return possible_moves


def __minmax_alphabeta(state: GameState, last_better_value: int):
    if state.is_player_turn:
        better_value = -math.inf
        is_better_value = __bigger_or_equal_than
    else:
        better_value = math.inf
        is_better_value = __smaller_or_equal_than

    better_move = None
    possible_moves = state.calc_possible_moves()

    if __is_terminal_state(state):
        return (None, __eval_result(state))

    for possible_move in possible_moves:
        possible_state = copy.deepcopy(state)
        possible_state.apply_move(possible_move)
        possible_value = __minmax_alphabeta(possible_state, better_value)[1]
        if is_better_value(possible_value, better_value):
            better_value = possible_value
            better_move = possible_move
            if is_better_value(better_value, last_better_value):
                break

    return (better_move, better_value)


def make_move(the_board: board.Board, player_color: str):
    """
    Retorna um movimento para o jogo Othello
    :param the_board: board do jogo no estado atual
    :param color: cor do jogador
    :return: (int, int) tupla de coordenadas da jogada (atenção: 0 é a primeira linha/coluna)
    """
    result = __minmax_alphabeta(GameState(the_board, player_color), math.inf)
    return result[0]


# region Helpers
def __is_terminal_state(state: GameState) -> bool:
    return state.depth >= __MAX_DEPTH or state.board.is_terminal_state()


def __eval_result(state: GameState) -> int:
    return __mixed_heuristic(state)


def __bigger_or_equal_than(a: int, b: int) -> bool:
    """
    Aplica >= em dois inteiros
    """
    return a >= b


def __smaller_or_equal_than(a: int, b: int) -> bool:
    """
    Aplica <= em dois inteiros
    """
    return a <= b


# endregion

# region Heuristic
def __simple_points_heuristic(state: GameState) -> int:
    """
    Cálcula a heuristíca simplesmente pela quantidade de peças do jogador
    contra a quantidade de peças do inimigo.
    """
    black_count = 0
    white_count = 0
    for tile in state.board.tiles:
        for piece in tile:
            if piece == BLACK:
                black_count += 1
            elif piece == WHITE:
                white_count += 1

    result = black_count - white_count

    return result if state.player_color == BLACK else -result


def __mobility_heuristic(state: GameState):
    if state.enemy_possible_moves_count + state.player_possible_moves_count == 0:
        return 0
    return (
        100
        * (state.player_possible_moves_count - state.enemy_possible_moves_count)
        / (state.player_possible_moves_count + state.enemy_possible_moves_count)
    )


__POINT_MAP = [
    [120, -20, 20, 5, 5, 20, -20, 120],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [120, -20, 20, 5, 5, 20, -20, 120],
]


def __point_map_heuristic(state: GameState):
    player_points = 0
    enemy_points = 0
    for x, tile in enumerate(state.board.tiles):
        for y, piece in enumerate(tile):
            if piece == state.player_color:
                player_points += __POINT_MAP[x][y]
            elif piece == state.enemy_color:
                enemy_points += __POINT_MAP[x][y]

    return player_points - enemy_points


def __mixed_heuristic(state: GameState) -> int:
    if __is_last_move(state):
        return __simple_points_heuristic(state)

    point_map_heuristic_result = __point_map_heuristic(state)
    mobility_heuristic_result = __mobility_heuristic(state)
    return point_map_heuristic_result * 0.4 + mobility_heuristic_result * 0.6


def __count_empty_values(state: GameState):
    empty_points = 0
    for tile in state.board.tiles:
        for piece in tile:
            if piece == EMPTY:
                empty_points += 1
    return empty_points


def __is_last_move(state: GameState):
    return __count_empty_values(state) <= 2


# endregion
