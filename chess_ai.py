import chess

# board1 = chess.Board()
# board1.push_san("e4")
# board1.remove_piece_at(0)
# print(board1.unicode())

def getScoreOfBoard(board):
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
    return {'white':score_white, 'black':score_black}

def getValidMoves(board):
    return list(board.legal_moves)

def getMoveMinimax(board, color):
    # Given a board and the winner color, determine where to
    # move and return that move.
    possibleMoves = getValidMoves(board)

    bestScore = -10000
    bestMove = []
    for move in possibleMoves:
        dupeBoard = chess.Board(board.fen())
        dupeBoard.push(move)
        score = minimax(dupeBoard, 4, True, -10000, 10000, color)
        if score > bestScore:
            bestMove = move
            bestScore = score
    #if bestMove == []:
    #    bestMove = possibleMoves[0]

    return bestMove

def minimax(board, depth, isMaximizing, alpha, beta, color):
    if board.is_checkmate() == True or depth == 0:
        score = getScoreOfBoard(board)[color]
        return score
    
    if isMaximizing:
        maxVal = -10000
        for child in getValidMoves(board):
            val = minimax(board, depth-1, False, alpha, beta, color)
            maxVal = max(maxVal, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return maxVal
    
    else: 
        minVal = 10000
        for child in getValidMoves(board):
            val = minimax(board, depth-1, True, alpha, beta, color)
            minVal = min(minVal, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return minVal
