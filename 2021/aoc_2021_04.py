# Advent of Code 2021 - Day 4
# https://adventofcode.com/2021/day/4

#f = open('./2021/input/04_sample.txt')
f = open('./2021/input/04.txt')
lines = f.read().splitlines() 
f.close()

def handle_input(lines): # returns moves and boards
    moves = lines[0].split(',')
    lines = lines[1:]
    nboards = len(lines) // 6
    boards = []
    for i in range(nboards):
        boards.append([])
        for r in range(5):
            boards[i].append(lines[i*6+r+1].split())
    return moves, boards

def checkwin(board):
    for i in range(5):
        hwin = True
        vwin = True
        for j in range(5):
            if board[i][j] != 'x':
                hwin = False
            if board[j][i] != 'x':
                vwin = False
        if vwin or hwin:
            return True
    return False

def boardsum(board):
    result = 0
    for r in board:
        for c in r:
            if c != 'x':
                result += int(c)
    return result

def playboard(board, moves):
    for num_moves, m in enumerate(moves):
        for r in range(5):
            for c in range(5):
                if board[r][c] == m:
                    board[r][c] = 'x'
        if checkwin(board):
            return (num_moves, boardsum(board) * int(m))
    return ((1000001, 1))


moves, boards = handle_input(lines)

bestmoves = 1000000
bestscore = []

worstmoves = 0
worstscore = []

for b in boards:
    num_moves, score = playboard(b, moves)

    if num_moves < bestmoves:
        bestmoves = num_moves
        bestscore = [score]
    elif num_moves == bestmoves:
        bestscore.append(score)

    if num_moves > worstmoves:
        worstmoves = num_moves
        worstscore = [score]
    elif num_moves == worstmoves:
        worstscore.append(score)

print('Part 1', bestmoves, bestscore)
print('Part 2', worstmoves, worstscore)