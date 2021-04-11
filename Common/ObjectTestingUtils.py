import timeit

from Common.Leetcode import ListNode, TreeNode
from Common.ListUtils import build_list, list_to_string, lists_equal


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
    for j, test in enumerate(tests):
        methods = test[0]
        arguments = test[1]
        expected = test[2]
        n = len(methods)
        # object = OrderedStream(arguments[0][0])
        obj = create_object(methods[0], *arguments[0])
        fail = False
        for i in range(1, n):
            output = call_method(obj, methods[i], *arguments[i])
            if not compare_values(output, expected[i]):
                fail = True
                print("FAIL: " + str(output) + " != " + str(expected[i]) + ": Test " + str(j) + ", step " + str(i))
                break
        if not fail:
            print("PASS")


def to_string(v) -> str:
    if type(v) is ListNode:
        return list_to_string(v)
    else:
        return str(v)


def compare_floats(v1, v2, eps=1e-5):
    return abs(v1 - v2) < eps


def compare_values(v1, v2) -> bool:
    if type(v1) is ListNode:
        return lists_equal(v1, v2)
    elif type(v1) is float:
        return compare_floats(v1, v2)
    else:
        return v1 == v2


def count_tree_nodes(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + count_tree_nodes(root.left) + count_tree_nodes(root.right)


def run_functional_tests(function, tests, **kwargs):
    if "custom_check" in kwargs:
        custom_check = kwargs["custom_check"]
    else:
        custom_check = None
    if "input_metric" in kwargs:
        input_metric = kwargs["input_metric"]
    else:
        if type(tests[0][0]) is TreeNode:
            input_metric = lambda test: count_tree_nodes(test[0])
        else:
            input_metric = lambda test: len(test[0])
    n = len(tests)
    nfail = 0
    i = 0
    for test in tests:
        i += 1
        start = timeit.default_timer()
        result = function(*test[:-1])
        stop = timeit.default_timer()
        expected = test[-1]

        duration = stop - start
        input_size = input_metric(test)

        if custom_check:
            comparison_result = custom_check(test, result)
        else:
            comparison_result = compare_values(result, expected)

        if comparison_result:
            print(str(i) + ") PASS, took: " + str(duration) + " on size="+str(input_size))
        else:
            if type(expected) is str and type(result) is str:
                print(str(i) + ") FAIL - expected '" + expected + "', got '" + result + "'")
            else:
                print(str(i) + ") FAIL - expected " + to_string(expected), ", got " + to_string(result))
            nfail += 1
    status = "OVERALL: " + ("SUCCESS" if nfail == 0 else "FAILED")
    print(status + ", " + str(nfail) + " failed of " + str(n))


def convert_test_params_to_lists(tests, indexes):
    for test in tests:
        for i in indexes:
            test[i] = build_list(test[i])
    return tests
