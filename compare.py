import server
import argparse


__TOTAL_TESTS = 100

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Othello server.")
    parser.add_argument("players", metavar="player", type=str, nargs=2, help="Path to player directory")

    args = parser.parse_args()
    p1, p2 = args.players

    p1_wins = 0
    p2_wins = 0

    half_tests = int(__TOTAL_TESTS / 2)

    for i in range(0, half_tests):
        s = server.Server(p1, p2, 5.0, "history.txt", "results.xml")
        s.run()
        if s.board.piece_count["B"] > s.board.piece_count["W"]:
            p1_wins += 1
        else:
            p2_wins += 1

    for i in range(0, half_tests):
        s = server.Server(p2, p1, 5.0, "history.txt", "results.xml")
        s.run()
        if s.board.piece_count["B"] > s.board.piece_count["W"]:
            p2_wins += 1
        else:
            p1_wins += 1

    total_plays = half_tests * 2

    p1_win_rate = (p1_wins * 100) / total_plays
    p2_win_rate = (p2_wins * 100) / total_plays
    print(f"Win rate ({p1}): {p1_win_rate}")
    print(f"Win rate ({p2}): {p2_win_rate}")
