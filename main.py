import chess, random
from chess_ai import *

# board1 = chess.Board()
# print(board1.turn) 
# # True is white's turn
# # False is black's turn
# board1.push_san("f3")
# board1.push_san("e5")
# board1.push_san("g4")
# board1.push_san("Qh4#")
# #board1.remove_piece_at(0)
# #legal_moves = list(board1.legal_moves)

# print(board1.unicode())

# if board1.is_checkmate():
#     print("checkmate")
# print(board1.turn)

def getBestMove(fen):
    board = chess.Board(fen)
    color = fen.split()[1]
    return getMoveMinimax(board, color)

# Reset the board and game.
mainBoard = chess.Board()
mainBoard.reset_board()
player1, player2 = ['white', 'black']
turn = 'player1'
print('The ' + turn + ' will go first.')
print(player2)

while True:
    if turn == 'player1':
        #Player 1's turn
        print(mainBoard.unicode())
        #input('Press Enter to see the Player 1\'s move.')
        print('Player 1\'s move.')
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
        #input('Press Enter to see the Player 2\'s move.')
        print('Player 2\'s move.')
        #Player 2 gets it's moves based on the highest score
        move = getMoveMinimax(mainBoard, player2)
        mainBoard.push(move)
        if mainBoard.is_checkmate():
            break
        else:
            turn = 'player1'
