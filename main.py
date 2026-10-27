import random as rnd

while True:
    encode_state = input("encode (y/N) > ") != "N"
    x = input("Enter input > ")
    if encode_state:
        print(
            " ".join(
                [
                    str(x)
                    for x in (
                        lambda s: [
                            y
                            for x in [
                                (lambda c, n: [(ord(c) + n), n])(c, rnd.randint(1, 255))
                                for c in s
                            ]
                            for y in x
                        ]
                    )(x)
                ]
            )
        )
        continue
    print(
        "".join(
            (
                lambda s: (lambda c: [chr(x[0] - x[1]) for x in c])(
                    [[int(s[i]), int(s[i + 1])] for i in range(0, len(s) - 1, 2)]
                )
            )(x.split(" "))
        )
    )
