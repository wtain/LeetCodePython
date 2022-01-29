from Common.ListUtils import build_list
from Common.TreeUtils import build_tree_from_list


def convert_test_params(tests, function, **kwargs):
    if "indexes" in kwargs and kwargs["indexes"]:
        indexes = kwargs["indexes"]
    else:
        indexes = range(len(tests[0]))
    for test in tests:
        for i in indexes:
            test[i] = function(test[i])
    return tests


def convert_test_params_to_lists(tests, indexes=None):
    return convert_test_params(tests, build_list, indexes=indexes)


def convert_test_params_to_trees(tests, indexes):
    return convert_test_params(tests, build_tree_from_list, indexes=indexes)