import sys
import chess
import argparse
from movegeneration import next_move

def talk():
    board = chess.Board()
    depth = get_depth()

    while True:
        msg = input()
        command(depth, board, msg)

def command(depth: int, board: chess.Board, msg: str):
    msg = msg.strip()
    tokens = msg.split(" ")
    while "" in tokens:
        tokens.remove("")

    if msg == "quit":
        sys.exit()

    if msg == "uci":
        print("ID name dotOnion")
        print("ID author dotOnion")
        print("uciok")
        return

    if msg == "isready":
        print("readyok")
        return

    if msg == "ucinewgame":
        return

    if msg.startswith("position"):
        if len(tokens) < 2:
            return

        if tokens[1] == "startpos":
            board.reset()
            moves_start = 2
        elif tokens[1] == "fen":
            fen = " ".join(tokens[2:8])
            board.set_fen(fen)
            moves_start = 8
        else:
            return

        if len(tokens) <= moves_start or tokens[moves_start] != "moves":
            return

        for move in tokens[(moves_start+1):]:
            board.push_uci(move)

    if msg == "d":
        print(board)
        print(board.fen())

    if msg[0:2] == "go":
        _move = next_move(depth, board)
        print(f"bestmove {_move}")
        return

def get_depth() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", default=3, help="provide an integer (default: 3)")
    args = parser.parse_args()
    return max([1, int(args.depth)])
