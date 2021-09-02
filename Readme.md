# Servidor de Othello

Este arquivo contem instruções simples para execução do servidor e do jogador 'random'.

## Requisitos
O servidor foi testado em uma máquina GNU/Linux (Ubuntu, mais precisamente) com
o interpretador python 3.7.7

## Instruções

Para iniciar uma partida de Othello, digite no terminal:

python server.py [-h] [-d delay] [-l log-history] player1 player2

Onde 'player(1 ou 2)' são os diretórios onde estão os agent.py dos jogadores.
Os argumentos entre colchetes são opcionais, seu significado é descrito a seguir:

-h, --help            Mensagem de ajuda
-d delay, --delay delay
                    Tempo alocado para os jogadores realizarem a jogada (default=5s)
-l log-history, --log-history log-history
                    Arquivo que conterá registro simples de jogadas (default=history.txt)
-o output-file, --output-file output-file
                    Arquivo que conterá detalhes do jogo (incluindo registro de jogadas)

## Jogador random
O jogador 'random' se localiza no diretório randomplayer. Para jogar uma partida com ele,
basta substituir diretorio_player1 e/ou 2 por randomplayer. Como exemplo, inicie
uma partida random vs. random para ver o servidor funcionando:

python server.py randomplayer randomplayer

Você verá o tabuleiro se preenchendo quase instantaneamente porque o jogador random é muito rápido (e muito incompetente).

## Funcionamento

Iniciando pelo player1, que jogará com as peças pretas, o servidor cria o objeto Board e chama o make_move do agent.py dentro do diretório do player 1.

O make_move deve retornar as coordenadas x, y da jogada. O servidor as recebe, processa, e repete o procedimento para o próximo jogador, com o estado atualizado.

# Notas
* O servidor checa a legalidade das jogadas antes de efetivá-las. 
* Você pode usar as funções da classe Board como auxílio para obter as jogadas válidas, além de outras facilidades.
* Jogadas ilegais repetidas vezes resultam em desqualificação.
* Timeout resulta em perda da vez (o que é uma desvantagem no jogo)
* Em caso de problemas com o servidor, por favor avise via moodle ou discord.
"# ia-trab2" 
