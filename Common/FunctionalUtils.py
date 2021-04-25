import copy


def in_place_to_function(function):

    def wrapper(inarg):
        inarg_copy = copy.deepcopy(inarg)
        function(inarg_copy)
        return inarg_copy

    return wrapper
