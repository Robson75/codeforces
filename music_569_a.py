class Music:

    pass


if __name__ == '__main__':
    in_params = list(map(int, input().split()))
    song_duration = in_params[0]
    downloaded = in_params[1]
    q = in_params[2]
    d = float(q - 1)/q
    replays = 1
    x = downloaded * d / (1 - d)
    rounding_error = 0.000001
    while downloaded + x < song_duration - rounding_error:
        replays += 1
        downloaded += x
        x = downloaded * d / (1 - d)
    print(replays)


