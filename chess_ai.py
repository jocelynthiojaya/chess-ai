import chess

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
              score_white = score_white + (piece * 10)
            
            #False means the color is black
            elif piece_color is False:
                score_black = score_black + (piece * 10)
            
            #if there is no piece in the square
            else: 
                piece = 0 
    return {'white':score_white-score_black, 'black':score_black-score_white}

def getEvaluationBoard(board, color):
    score_white = 0
    score_black = 0
    pawn_points = [0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,1,1,2,3,3,2,1,1,0.5,0.5,1,2.5,2.5,1,0.5,0.5,0,0,0,2,2,0,0,0,0,5,-0.5,-1,0,0,-1,-0.5,0.5,0.5,1,1,-2,-2,1,1,0.5,0,0,0,0,0,0,0]
    knight_points = [-5,-4,-3,-3,-3,-3,-4,-5, -4,-2,  0,  0,  0,  0,-2,-4, -3,  0, 1, 1.5, 1.5, 1,  0,-3, -3,  0.5, 1.5, 2, 2, 1.5,  0.5,-3, -3,  0, 1.5, 2, 2, 1.5,  0,-3, -3,  0.5, 1, 1.5, 1.5, 1,  0.5,-3, -4,-2,  0,  0.5,  0.5,  0,-2,-4, -5,-4,-3,-3,-3,-3,-4,-5]
    bishop_points = [-2,-1,-1,-1,-1,-1,-1,-2, -1,  0,  0,  0,  0,  0,  0,-1, -1,  0,  0.5, 1, 1,  0.5,  0,-1, -1,  0.5,  0.5, 1, 1,  0.5,  5,-1, -1,  0, 1, 1, 1, 1,  0,-1, -1, 1, 1, 1, 1, 1, 1,-1, -1,  0.5,  0,  0,  0,  0,  0.5,-1, -2,-1,-1,-1,-1,-1,-1,-2]
    rooks_points = [ 0,  0,  0,  0,  0,  0,  0,  0, 0.5, 1, 1, 1, 1, 1, 1,  0.5, -0.5,  0,  0,  0,  0,  0,  0, -0.5, -0.5,  0,  0,  0,  0,  0,  0, -0.5, -0.5,  0,  0,  0,  0,  0,  0, -0.5, -0.5,  0,  0,  0,  0,  0,  0, -0.5, -0.5,  0,  0,  0,  0,  0,  0, -0.5, 0,  0,  0,  0.5,  0.5,  0,  0,  0]
    queen_points = [-2,-1,-1,-0.5,-0.5,-1,-1,-2,-1,0,0,0,0,0,0,-1,-1,0,0.5,0.5,0.5,0.5,0,-1,-0.5,  0,  0.5, 0.5,  0.5,  0.5,  0, -0.5, 0,  0,  0.5,  0.5,  0.5,0.5,0, -0.5,-1,0.5,0.5,0.5,0.5,0.5,0,-1,-1,0,0.5,0,0,0,0,-1,-2,-1,-1,-0.5,-0.5,-1,-1,-2]
    king_points = [-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-2,-3,-3,-4,-4,-3,-3,-2,-1,-2,-2,-2,-2,-2,-2,-1,2,2,0,0,0,0,2,2,2,3,1,0,0,1,3,2]
    for row in range(0,8):
        for col in range(0,8):
            squareIndex = row*8 + col
            square = chess.SQUARES[squareIndex]
            
            #to get the color of the piece
            piece_color = board.color_at(square)
            
           #to get the type of piece
            piece = board.piece_type_at(square)
            if piece == 1:
                if piece_color is True:
                    score_white += pawn_points[-square]
                elif piece_color is False:
                   score_black += pawn_points[square]
            elif piece == 2:
                if piece_color is True:
                    score_white += knight_points[-square]
                elif piece_color is False:
                   score_black += knight_points[square]
            elif piece == 3:
                if piece_color is True:
                    score_white += bishop_points[-square]
                elif piece_color is False:
                   score_black += bishop_points[square]
            elif piece == 4:
                if piece_color is True:
                    score_white += rooks_points[-square]
                elif piece_color is False:
                   score_black += rooks_points[square]
            elif piece == 5:
                if piece_color is True:
                    score_white += queen_points[-square]
                elif piece_color is False:
                   score_black += queen_points[square]
            elif piece == 6:
                if piece_color is True:
                    score_white += king_points[-square]
                elif piece_color is False:
                   score_black += king_points[square]     

    piece_white = getScoreOfBoard(board)['white']
    piece_black = getScoreOfBoard(board)['black']

    if color == 'white':
        if board.is_checkmate() == True and board.turn == False:
            score_white += 100
    elif color == 'black':
        if board.is_checkmate() == True and board.turn == True:
            score_black += 100

    return {'white':score_white+piece_white, 'black':score_black+piece_black}

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
    if winCondition(board, color) == True or depth == 0:
        score = getEvaluationBoard(board, color)[color]
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

def winCondition(board, color):
    if color == 'white':
        if board.is_checkmate() == True and board.turn == False:
            return True
    elif color == 'black':
        if board.is_checkmate() == True and board.turn == True:
            return True







