import chess, random
from chess_ai import *

# board1 = chess.Board()
# board1.push_san("e4")
# board1.remove_piece_at(0)
# legal_moves = list(board1.legal_moves)

# print(board1.unicode())
# print(legal_moves)

# board1.push(legal_moves[0])
# print(board1.unicode())

# print(board1.is_checkmate)


# Reset the board and game.
mainBoard = chess.Board()
player1, player2 = ['white', 'black']
turn = 'player1'
print('The ' + turn + ' will go first.')

while True:
    if turn == 'player1':
        #Player 1's turn
        print(mainBoard.unicode())
        input('Press Enter to see the Player 1\'s move.')
        #Player 1 gets it's moves based on the highest score
        moves = getValidMoves(mainBoard)
        random.shuffle(moves)
        mainBoard.push(moves[0])
        if mainBoard.is_checkmate():
            break
        else:
            turn = 'player2'

    else:
        #Player 2's turn
        print(mainBoard.unicode())
        input('Press Enter to see the Player 2\'s move.')
        #Player 2 gets it's moves based on the highest score
        move = getMoveMinimax(mainBoard, player2)
        mainBoard.push(move)
        if mainBoard.is_checkmate():
            break
        else:
            turn = 'player1'
