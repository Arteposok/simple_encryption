import random as rnd


def encode_chars(str_in, sep):
    str_out = map(
        lambda x: (
            (lambda r: f"{hex(ord(x) + r)[2:]}{sep}{hex(r)[2:]}")(rnd.randint(50, 200))
        ),
        str_in,
    )
    return sep.join(str_out)


def decode_chars(str_in):
    str_in_inner = [(str_in[i], str_in[i + 1]) for i in range(0, len(str_in) - 1, 2)]
    str_out = map(
        lambda x: f"{chr(int(x[0], 16) - int(x[1], 16))}",
        str_in_inner,
    )
    return "".join(str_out)


def main():
    pass_n = int(input("Enter pass number > "))
    sep = input("Enter separator > ")
    while True:
        encode_state = input("Encoding (y/N) > ") != "N"
        if encode_state:
            text = encode_chars(input("Enter plaintext > "), sep)
            for x in range(pass_n - 1):
                text = encode_chars(text, sep)
            print(text)
            continue
        stage = decode_chars(input("Copy cyphertext > ").split(sep))
        for x in range(pass_n - 1):
            stage = decode_chars(stage.split(sep))
        print(stage)


main()
