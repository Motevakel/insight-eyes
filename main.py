import chess
import argparse
from movegeneration import next_move

def start():
    board = chess.Board()
    user_side = (
        chess.WHITE if input("Start as a [b]lack bead or [w]hite bead?\n") == "w" else chess.BLACK
    )

    if user_side == chess.WHITE:
        print(render(board))
        board.push(get_move(board))

    while not board.is_game_over():
        board.push(next_move(get_depth(), board, debug=False))
        print(render(board))
        board.push(get_move(board))

    print(f"\nResult: [w] {board.result()} [b]")


def render(board: chess.Board) -> str:
    board_string = list(str(board))
    uni_pieces = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }
    for idx, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[idx] = uni_pieces[char]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")
    if board.turn == chess.BLACK:
        display.reverse()
    display.append("    a b c d e f g h")
    return "\n" + "\n".join(display)

def get_move(board: chess.Board) -> chess.Move:
    move = input(f"\nYour move (Like: {list(board.legal_moves)[0]}):\n")

    for legal_move in board.legal_moves:
        if move == str(legal_move):
            return legal_move
    return get_move(board)

def get_depth() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", default=3, help="Provide an integer (Default: 3)")
    args = parser.parse_args()
    return max([1, int(args.depth)])

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        pass
