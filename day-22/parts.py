from os import read


def read_input(filename):
    player1 = []
    player2 = []
    load_player1 = True
    with open(filename) as f:
        for line in f.read().splitlines():
            if load_player1:
                if line == "Player 1:" or line == "":
                    continue
                if line == "Player 2:":
                    load_player1 = False
                    continue
                player1.append(int(line))
            else:
                player2.append(int(line))

    return player1, player2


def play_game(player1, player2):
    winner = None
    while len(player1) and len(player2):
        card_1 = player1.pop(0)
        card_2 = player2.pop(0)

        if card_1 > card_2:
            player1.append(card_1)
            player1.append(card_2)
            # print("Player1 wins")
            winner = player1
        else:
            player2.append(card_2)
            player2.append(card_1)
            # print("Player2 wins")
            winner = player2

        # print(f"Player 1: {player1}")
        # print(f"Player 2: {player2}")

    calculate_score(winner)


def calculate_score(winner):
    total = 0
    for idx, i in enumerate(range(len(winner), 0, -1)):
        total += winner[idx] * i

    print(f"Total Score: {total}")


if __name__ == "__main__":
    player1, player2 = read_input("input.txt")
    play_game(player1, player2)
