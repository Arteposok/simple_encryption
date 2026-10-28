import random as rnd


def encode_chars(str_in):
    str_out = map(
        lambda x: ((lambda r: f"{ord(x) + r}-{r}")(rnd.randint(50, 200))),
        str_in,
    )
    return "-".join(str_out)


def decode_chars(str_in):
    str_in_inner = [(str_in[i], str_in[i + 1]) for i in range(0, len(str_in) - 1, 2)]
    str_out = map(
        lambda x: f"{chr(int(x[0]) - int(x[1]))}",
        str_in_inner,
    )
    return "".join(str_out)


def main():
    pass_n = int(input("Enter pass number > "))
    while True:
        encode_state = input("Encoding (y/N) > ") != "N"
        if encode_state:
            text = encode_chars(input("Enter plaintext > "))
            for x in range(pass_n-1):
                text = encode_chars(text)
            print(text)
            continue
        stage = decode_chars(input("Copy cyphertext > ").split("-"))
        for x in range(pass_n-1):
            stage = decode_chars(stage.split("-"))
        print(stage)


main()
