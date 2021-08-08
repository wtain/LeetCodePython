import copy
import timeit
from typing import List

from Common.Leetcode import ListNode, TreeNode
from Common.ListUtils import build_list, list_to_string, lists_equal, list_length
from Common.NAryTree import Node
from Common.NestedInteger import NestedInteger, nestedIntegerToString
from Common.TreeUtils import compareTrees, printTree


def call_method(o, name, *args, **kwargs):
    # print("*** Calling " + name + " with " + str(args) + " and " + str(kwargs))
    return getattr(o, name)(*args, **kwargs)


def create_object(class_name, *args, **kwargs):
    return globals()[class_name](*args, **kwargs)


def declare_class(CLASS):
    globals()[CLASS.__name__] = CLASS


def run_object_tests(tests, **kwargs):
    if "cls" in kwargs:
        declare_class(kwargs["cls"])
    overall = True
    for j, test in enumerate(tests):
        methods = test[0]
        arguments = test[1]
        expected = test[2]
        n = len(methods)
        obj = create_object(methods[0], *arguments[0])
        fail = False
        for i in range(1, n):
            args = arguments[i]
            if not args:
                args = []
            output = call_method(obj, methods[i], *args)
            if not compare_values(output, expected[i]):
                fail = True
                overall = False
                print(str(j+1) + ") FAIL: " + str(output) + " != " + str(expected[i]) + ": Test " + str(j) + ", step " + str(i))
                break
        if not fail:
            print(str(j+1) + ") PASS")
    if overall:
        print("Overall status: PASS")
    else:
        print("Overall status: FAIL")


def to_string(v) -> str:
    if type(v) is ListNode:
        return list_to_string(v)
    elif type(v) is NestedInteger:
        return nestedIntegerToString(v)
    else:
        return str(v)


def compare_floats(v1, v2, eps=1e-5):
    return abs(v1 - v2) < eps


def compare_values(v1, v2) -> bool:
    if type(v1) is ListNode:
        return lists_equal(v1, v2)
    elif type(v1) is TreeNode:
        return compareTrees(v1, v2)
    elif type(v1) is float:
        return compare_floats(v1, v2)
    else:
        return v1 == v2


def count_tree_nodes(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + count_tree_nodes(root.left) + count_tree_nodes(root.right)


def count_nary_tree_nodes(root: Node) -> int:
    if not root:
        return 0
    result = 1
    if root.children:
        for child in root.children:
            result += count_nary_tree_nodes(child)
    return result


# todo: recursive calc_size, e.g. List of Lists
# def calc_size(obj) -> int:

def make_inplace(function):

    def inner(args):
        arg0 = args
        arg0 = copy.deepcopy(arg0)
        function(arg0)
        return arg0

    return inner


def run_functional_tests(function, tests, **kwargs):
    if "custom_check" in kwargs:
        custom_check = kwargs["custom_check"]
    else:
        custom_check = None
    if "run_tests" in kwargs:
        run_tests = kwargs["run_tests"]
    else:
        run_tests = None
    if "input_metric" in kwargs:
        input_metric = kwargs["input_metric"]
    else:
        if type(tests[0][0]) is TreeNode:
            input_metric = lambda test: count_tree_nodes(test[0])
        elif type(tests[0][0]) is Node:
            input_metric = lambda test: count_nary_tree_nodes(test[0])
        elif type(tests[0][0]) is ListNode:
            input_metric = lambda test: list_length(test[0])
        elif type(tests[0][0]) is int:
            input_metric = lambda test: test[0]
        else:
            input_metric = lambda test: len(test[0])
    n = len(tests)
    nfail = 0
    i = 0
    for test in tests:
        i += 1
        if run_tests and i not in run_tests:
            continue
        input_size = input_metric(test)
        start = timeit.default_timer()
        parameters = test[:-1]
        try:
            result = function(*parameters)
            stop = timeit.default_timer()
            expected = test[-1]

            duration = stop - start

            if custom_check:
                comparison_result = custom_check(test, result)
            else:
                comparison_result = compare_values(result, expected)

            if comparison_result:
                print(str(i) + ") PASS, took: " + "{:.3f}".format(duration) + " on size=" + str(input_size))
            else:
                if type(expected) is str and type(result) is str:
                    print(str(i) + ") FAIL - expected '" + expected + "', got '" + result + "', params: " + str(parameters))
                elif type(expected) is TreeNode or type(result) is TreeNode:
                    print("Expected:")
                    printTree(expected)
                    print("Got:")
                    printTree(result)
                else:
                    print(str(i) + ") FAIL - expected " + to_string(expected), ", got " + to_string(result), "; took {:.3f}".format(duration) + ", params: " + str(parameters))
                nfail += 1
        except Exception as e:
            print(str(i) + ") FAIL - CRASH, params: " + str(parameters))
            print(e)
            nfail += 1
    is_success = nfail == 0
    status = "OVERALL: " + ("SUCCESS" if is_success else "FAILED")
    if is_success:
        print(status)
    else:
        print(status + ", " + str(nfail) + " failed of " + str(n))


def convert_test_params(tests, function, **kwargs):
    if "indexes" in kwargs:
        indexes = kwargs["indexes"]
    else:
        indexes = range(len(tests[0]))
    for test in tests:
        for i in indexes:
            test[i] = function(test[i])
    return tests


def convert_test_params_to_lists(tests, indexes):
    return convert_test_params(tests, build_list, indexes=indexes)
