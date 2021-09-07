# Trabalho Prático 1
## Alunos
* 00303397 - João Pedro Silveira e Silva (turma A)
* 00314280 - Rafael Humann Petry (turma A)
* 00302072 - Victória de Avelar Duarte (turma A)

## Função de avaliação
Usamos as heurísticas de estabilidade e de mobilidade em conjunto. 
A proporção utilizada foi:

`0.8 * heuristica_de_estabilidade + 0.2 * heuristica_de_mobilidade`

### Estabilidade
Foi construída uma matriz indicando qual o peso associado a cada posição do
tabuleiro. Os valores positivos são os valores que favorecem o jogador e, os 
negativos, são os que favorecem o oponente.
```
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
```
Os valores foram retirados de https://www.ic.unicamp.br/~rocha/teaching/2011s2/mc906/seminarios/2011s2-mc906-seminario-04.pdf

Com a matriz definida, dado um tabuleiro, calcula-se o valor associado a 
cada jogador com base na posição de cada peça com um somatório

```
pontos_jogador = 0
pontos_oponente = 0

para cada peça dentro de um tabuleiro:
    se jogador:
        pontos_jogador += __POINT_MAP[posição_peça]
    se oponente:
        pontos_oponente += __POINT_MAP[posição_peça]
retorna pontos_jogador - pontos_oponente
```

### Mobilidade
A cada tabuleiro, é calculada todas as possibilidades de movimento para cada 
jogador
```
se movimentos_MAX_player + movimentos_MIN_player == 0:
	heuristica = 0
senão:
	heuristica = 100 * (movimentos_MAX_player - movimentos_MIN_player) / (movimentos_MAX_player + movimentos_MIN_player)
```

## Bibliografia
https://pt.wikipedia.org/wiki/Minimax

https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/

https://www.ic.unicamp.br/~rocha/teaching/2011s2/mc906/seminarios/2011s2-mc906-seminario-04.pdf