from flask import Blueprint, render_template, session, redirect, url_for, request
from engine import get_engine_move
bp = Blueprint("index", __name__, url_prefix="/")

@bp.route('/naive', methods = ['GET','POST'])
def naive():
    # req = request.get_json()
    # fen = req["fen"]
    # print(fen)
    return "does work or not"

@bp.route('/engine', methods = ['GET','POST'])
def engine():
    req = request.get_json()
    res = {'move' : str(get_engine_move(req["fen"]))}
    
    return res