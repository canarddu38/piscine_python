#!/usr/bin/env python3

import sys


def main():
    """Main function"""
    scores = []
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py \
    <score1> <score2> ...")
    else:
        i = 0
        try:
            for arg in sys.argv:
                if i > 0:
                    scores.append(int(arg))
                i += 1
            print(f"Scores processed: {scores}")
            print(f"Total players: {i - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {int(sum(scores) * 100 / (i - 1)) / 100}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError:
            print(f"Invalid input '{arg}'")


if __name__ == "__main__":
    main()
