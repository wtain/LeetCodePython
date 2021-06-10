
def compareSets(test, result) -> bool:
    expected = test[-1]
    if len(expected) != len(result):
        return False
    return sorted(expected) == sorted(result)