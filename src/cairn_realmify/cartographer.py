from .territory import Territory


def realmify(territory: Territory, width: int, height: int, filler_char=" "):

    representation = [filler_char] * height
    for i in range(0, height):
        representation[i] = [filler_char] * width

    for k, v in territory.landmarks.items():
        vertical_ix = round(v[1][0] * height)
        horizontal_ix = round(v[1][1] * width)

        representation[vertical_ix][horizontal_ix] = k

    render = "\n".join(
        "".join(line)
        for line in representation
    )
    return render
