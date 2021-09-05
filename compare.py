import server
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Othello server.")
    parser.add_argument("players", metavar="player", type=str, nargs=2, help="Path to player directory")

    parser.add_argument(
        "-t",
        "--test",
        type=int,
        dest="test",
        default=100,
        metavar="test",
        help="Total of tests.",
    )

    args = parser.parse_args()
    p1, p2 = args.players

    p1_wins = 0
    p2_wins = 0

    half_tests = int(args.test / 2)

    for i in range(0, half_tests):
        print(f"turn 1, play {i}")
        s = server.Server(p1, p2, 5.0, "history.txt", "results.xml")
        s.run()
        if s.board.piece_count["B"] > s.board.piece_count["W"]:
            p1_wins += 1
            print(f"winner {p1}")
        else:
            p2_wins += 1
            print(f"winner {p2}")

    for i in range(0, half_tests):
        print(f"turn 2, play {i}")
        s = server.Server(p2, p1, 5.0, "history.txt", "results.xml")
        s.run()
        if s.board.piece_count["B"] > s.board.piece_count["W"]:
            p2_wins += 1
            print(f"winner {p2}")
        else:
            p1_wins += 1
            print(f"winner {p1}")

    total_plays = half_tests * 2

    p1_win_rate = (p1_wins * 100) / total_plays
    p2_win_rate = (p2_wins * 100) / total_plays
    print(f"Wins ({p1}): {p1_wins}")
    print(f"Win rate ({p1}): {p1_win_rate}")
    print(f"Wins ({p2}): {p2_wins}")
    print(f"Win rate ({p2}): {p2_win_rate}")
