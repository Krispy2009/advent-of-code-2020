example_card_pub_key = 5_764_801
example_door_pub_key = 17_807_724
card_pub_key = 8_987_316
door_pub_key = 14_681_524


def find_loop_size(pub_key):
    value = 1
    subject_number = 7
    for i in range(1, 10_000_000):
        value = value * subject_number
        value = value % 20_201_227
        if value == pub_key:
            return i


def calc_encryption_key(pub_key, loop_size):
    value = 1
    subject_number = pub_key
    for _ in range(loop_size):
        value = value * subject_number
        value = value % 20_201_227
    return value


if __name__ == "__main__":
    card_loop_size = find_loop_size(card_pub_key)
    door_loop_size = find_loop_size(door_pub_key)

    print(f"Card Loop size: {card_loop_size}")
    print(f"Door Loop size: {door_loop_size}")

    enc_key = calc_encryption_key(card_pub_key, door_loop_size)
    print(f"ENC KEY: {enc_key}")

