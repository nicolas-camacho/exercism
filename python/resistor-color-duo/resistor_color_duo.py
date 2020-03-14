COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    return int(''.join(
        str(COLORS.index(color[1])) for color in zip(range(2), colors)
        ))
