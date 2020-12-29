def meme1():
    return str(
        bytes(
            list(
                map(
                    lambda i: i + 48,
                    [
                        int("49"),
                        int("3c", 16),
                        int("60"),
                        int(str(-16)),
                        int("38", 16),
                        int("41", 12),
                        int("1l", 36),
                        int("2020", 3),
                        int("-100", 4),
                        int("30", 21),
                        int("1o", 26),
                        int("3h", 18),
                        int("2j", 25),
                        int("29", 31),
                        int(str(63), int("1011", 2)),
                    ],
                )
            )
        ),
        "".join(map(lambda c: chr(ord(c) + 12), list("ihZ,"))),
    )
