
def compareSets(test, result) -> bool:
    expected = test[-1]
    if len(expected) != len(result):
        return False
    return sorted(expected) == sorted(result)


def compareSetsOfSets(test, result) -> bool:
    expected = test[-1]
    if len(expected) != len(result):
        return False

    def canonize(s):
        return sorted(sorted(v) for v in s)

    return canonize(expected) == canonize(result)
