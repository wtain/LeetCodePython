from Common.Leetcode import ListNode
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
    for test in tests:
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
                print("FAIL: " + str(output) + " != " + str(expected[i]))
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


def run_functional_tests(function, tests, **kwargs):
    if "custom_check" in kwargs:
        custom_check = kwargs["custom_check"]
    else:
        custom_check = None
    n = len(tests)
    nfail = 0
    i = 0
    for test in tests:
        i += 1
        result = function(*test[:-1])
        expected = test[-1]

        if custom_check:
            comparison_result = custom_check(test, result)
        else:
            comparison_result = compare_values(result, expected)

        if comparison_result:
            print(str(i) + ") PASS")
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
