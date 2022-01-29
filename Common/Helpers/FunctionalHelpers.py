import copy


def make_inplace(function):
    def inner(args):
        arg0 = args
        arg0 = copy.deepcopy(arg0)
        function(arg0)
        return arg0

    return inner