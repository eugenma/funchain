from funchain import Chain


def test_islice_stop_only():
    actual = list(Chain(range(10)).islice(4))

    assert actual == list(range(4))


def test_islice_full():
    actual = list(Chain(range(10)).islice(0, 7, 2))

    assert actual == list(range(0, 7, 2))
