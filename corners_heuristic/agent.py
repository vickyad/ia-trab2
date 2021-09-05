import copy
import board
import math

BLACK = "B"
WHITE = "W"
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
    return __corners_heuristic(state)


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
def __corners_heuristic(state: GameState):
    player_corners = __calculate_corners(state.board.tiles, state.player_color)
    enemy_corners = __calculate_corners(state.board.tiles, state.enemy_color)
    if player_corners + enemy_corners == 0:
        return 0
    return 100 * (player_corners - enemy_corners) / (player_corners + enemy_corners)


def __calculate_corners(board_tiles: list[list[str]], color: str) -> int:
    dominated_corners = 0
    if board_tiles[0][0] == color:
        dominated_corners += 1
    if board_tiles[0][7] == color:
        dominated_corners += 1
    if board_tiles[7][0] == color:
        dominated_corners += 1
    if board_tiles[7][7] == color:
        dominated_corners += 1
    return dominated_corners


# endregion
