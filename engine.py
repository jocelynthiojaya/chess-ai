import chess
import chess.engine

PIECE_VALUE = {}
PIECE_VALUE[1] = 1
PIECE_VALUE[2] = 3
PIECE_VALUE[3] = 3
PIECE_VALUE[4] = 5
PIECE_VALUE[5] = 9
PIECE_VALUE[6] = 0

def minimax(board, depth):
    if depth == 0 or board.is_checkmate() or board.is_stalemate():
        boardEvaluation = evaluate_naive(board)
        return (boardEvaluation, None)
    else:
        # print("here")
        if board.turn:
            best_score = -10000
            best_move = None
            legal_moves = list(board.legal_moves)
            for move in legal_moves:
                board.push(move)
                new_board = board
                score = minimax(new_board, depth - 1)[0]
                new_board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move
        else:
            best_score = 10000
            best_move = None
            legal_moves = list(board.legal_moves)
            for move in legal_moves:
                board.push(move)
                new_board = board
                score = minimax(new_board, depth - 1)[0]
                new_board.pop()
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_score, best_move

def alphabeta(board, depth, alpha = -10000, beta = 10000):
    if depth == 0 or board.is_checkmate() or board.is_stalemate():
        boardEvaluation = evaluate_naive(board)
        return (boardEvaluation, None)
    else:
        # print("here")
        if board.turn:
            best_move = None
            legal_moves = list(board.legal_moves)
            for move in legal_moves:
                board.push(move)
                new_board = board
                score = alphabeta(new_board, depth - 1, alpha, beta)[0]
                new_board.pop()
                if score > alpha:
                    alpha = score
                    best_move = move
                    if alpha >= beta:
                        break
            return alpha, best_move
        else:
            best_move = None
            legal_moves = list(board.legal_moves)
            for move in legal_moves:
                board.push(move)
                new_board = board
                score = alphabeta(new_board, depth - 1, alpha, beta)[0]
                new_board.pop()
                if score < beta:
                    beta = score
                    best_move = move
                    if alpha >= beta:
                        break
            return beta, best_move

def evaluate_naive(board):
    score_white = 0
    score_black = 0
    total = 0
    for i in range(64):
        square = chess.SQUARES[i]
        piece_color = board.color_at(square)
        
        #to get the type of piece
        piece = board.piece_type_at(square)
        #True means the color is white 
        if piece_color == True:
            score_white += PIECE_VALUE[piece]
            total += 1
        #False means the color is black
        elif piece_color == False:
            score_black += PIECE_VALUE[piece]
            total += 1
    # print("total : ", total)
    return score_white - score_black

def get_engine_move(fen):
    board = chess.Board(fen)
    engine = chess.engine.SimpleEngine.popen_uci('stockfish_13_win_x64')
    result = engine.play(board, chess.engine.Limit(time=5, depth=15))
    engine.quit()
    return result.move

def engine_evaluation(board):
    print(board.fen())
    result = engine.analyse(board, chess.engine.Limit(time=0.01, depth=10))

    return result['score'].relative.score(mate_score=100)

# engine = chess.engine.SimpleEngine.popen_uci('stockfish_13_win_x64')
# evaluate = engine_evaluation

# test = chess.Board()
# print(test.fen())
# algo = alphabeta(test, 4)
# print(algo)
# test.push(algo[1])
# print(test.unicode())
# print(engine_evaluation(chess.Board()))