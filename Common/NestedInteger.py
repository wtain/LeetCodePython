def CreateNestedInteger(arg):
    return NestedInteger(arg)
    # if type(arg) is int:
    #     return NestedInteger(arg)
    # return [ NestedInteger(argi) for argi in arg ]


def CreateNestedList(arg):
    return [CreateNestedInteger(arg)]


def ConvertToList(it):
    result = []
    while it.hasNext():
        result.append(it.next())
    return result


class NestedInteger:

    def __init__(self, arg = []):
        if arg is None:
            arg = []
        if type(arg) is int:
            self.value = arg
            self.type = "int"
        elif type(arg) is list:
            self.type = "list"
            self.value = []
            for v in arg:
                self.value.append(CreateNestedInteger(v))
        # elif type(arg) is NestedInteger:
        #     self.type = arg.type
        #     self.value = arg.value
        else:
            raise Exception("Unexpected type")

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.type == "int"

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.value

    def getList(self):  # -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.value

    ### NEW METHODS

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.value.append(elem)


def compareNestedIntegers(test, result: NestedInteger) -> bool:
    expected: NestedInteger = test[-1]
    return nestedIntegersEqual(expected, result)


def nestedIntegersEqual(expected: NestedInteger, result: NestedInteger) -> bool:
    if result is None and expected is None:
        return True
    if result is None or expected is None:
        return False
    if result.isInteger() and expected.isInteger():
        return result.getInteger() == expected.getInteger()
    if result.isInteger() or expected.isInteger():
        return False
    result_list = result.getList()
    expected_list = expected.getList()
    if len(result_list) != len(expected_list):
        return False
    n = len(result_list)
    for i in range(n):
        if not nestedIntegersEqual(expected_list[i], result_list[i]):
            return False
    return True


def nestedIntegerToString(ni: NestedInteger) -> str:
    if not ni:
        return "[NONE]"
    else:
        if ni.isInteger():
            return str(ni.getInteger())
        else:
            return "[" + ",".join(map(lambda v: nestedIntegerToString(v), ni.getList())) + "]"
