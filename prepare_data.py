from itertools import product


def cartesian_prod(sets) -> set:
    return set(product(*sets))


if __name__ == '__main__':
    somelists = [
        [1, 2, 3],
        ['a', 'b'],
        [4, 5]
    ]
    print(cartesian_prod(somelists))
