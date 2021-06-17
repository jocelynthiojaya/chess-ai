from flask import Blueprint, render_template, session, redirect, url_for, request

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route('/naive', methods = ['GET','POST'])
def naive():
    # req = request.get_json()
    # fen = req["fen"]
    # print(fen)
    return "does work or not"

@bp.route('/engine', methods = ['GET','POST'])
def engine():
    return "whatever"