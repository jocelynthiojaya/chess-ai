

import chess

board = chess.Board()
board.push_san("e4")
board.remove_piece_at(0)
print(board.unicode())

def getScore():
    score_white = 0
    score_black = 0
    for row in range(0,8):
        for col in range(0,8):
            squareIndex = row*8 + col
            square = chess.SQUARES[squareIndex]
            
            #to get the color of the piece
            piece_color = board.color_at(square)
            
           #to get the type of piece
            piece = board.piece_type_at(square)
           
            #True means the color is white 
            if piece_color is True:
              score_white = score_white + piece
            
            #False means the color is black
            elif piece_color is False:
                score_black = score_black + piece
            
            #if there is no piece in the square
            else: 
                piece = 0 
    return ("white's score: ", score_white, "black's score", score_black)
            
#pawn = 1 ; knight = 2 ; bishop = 3 ; rook = 4 ; queen = 5; king = 6 

print(getScore())
