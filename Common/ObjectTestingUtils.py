import copy
import random
import timeit
import traceback

from Common.Helpers.ConsoleHelpers import FAIL, PASS, FATAL, ERROR, SUCCESS, CRASH, FAILED
from Common.Helpers.CompareHelpers import compare_values, compare_result_and_expected
from Common.Helpers.MetricsHelpers import get_input_mertic
from Common.Helpers.ObjectHelpers import declare_class, create_object, call_method
from Common.Helpers.ToStringHelpers import to_string
from Common.DataTypes.Leetcode import TreeNode
from Common.TreeUtils import printTree


def run_object_tests(tests, **kwargs):
    if "cls" in kwargs:
        declare_class(kwargs["cls"])
    if "rndseed" in kwargs:
        random.seed(kwargs["rndseed"])
    if "run_tests" in kwargs:
        run_tests = kwargs["run_tests"]
        if type(run_tests) is int:
            run_tests = [run_tests]
    else:
        run_tests = None
    debug = "debug" in kwargs and kwargs["debug"]
    overall = True
    for j, test in enumerate(tests):
        if run_tests and (j+1) not in run_tests:
            continue
        methods, arguments, expected = test[0:3]
        n = len(methods)
        obj = create_object(methods[0], *arguments[0])
        fail = False
        for i in range(1, n):
            args = arguments[i]
            if not args:
                args = []
            if debug:
                print(f"{methods[i]}({','.join(map(str, args))})")
            output = call_method(obj, methods[i], *args)
            if not compare_values(output, expected[i]):
                fail, overall = True, False
                print(str(j + 1) + f") {FAIL}: " + str(output) + " != " + str(expected[i]) + ": Test " + str(j) + ", step " + str(i) + ', arguments: ' + str(args))
                break
        if not fail:
            print(str(j + 1) + f") {PASS} ({n} steps)")
    print(f"Overall status: {PASS if overall else FAIL}")


def get_result_instance(tests):
    result_instance = None
    for test in tests:
        result_instance = test[0]
        if result_instance:
            break
    return result_instance


def run_functional_tests(function, tests, **kwargs):
    if not tests:
        print(f"** {FATAL} {ERROR}: No found")
        return
    custom_check, input_metric, run_tests, tostring_func = parse_params(kwargs, tests)

    n, failed_tests, i = len(tests), [], 0
    for test in tests:
        i += 1
        if run_tests and i not in run_tests:
            continue
        input_size = input_metric(test)
        start = timeit.default_timer()
        parameters = test[:-1]
        try:
            params = copy.deepcopy(parameters)
            result = function(*params)
            stop = timeit.default_timer()
            expected = test[-1]

            duration = stop - start

            comparison_result = compare_result_and_expected(custom_check, expected, result, test)

            if comparison_result:
                print(str(i) + f") {PASS}, took: " + "{:.6f}".format(duration) + " on size=" + str(input_size))
            else:
                if type(expected) is str and type(result) is str:
                    print(str(i) + f") {FAIL} - expected '" + expected + "', got '" + result + "', params: " + str(parameters))
                elif type(expected) is TreeNode or type(result) is TreeNode:
                    print(str(i) + f") {FAIL} - Expected:")
                    printTree(expected)
                    print("Got:")
                    printTree(result)
                elif type(expected) is list and expected and type(expected[0]) is TreeNode or type(result) is list and result and type(result[0]) is TreeNode:
                    print("Expected:")
                    for exp in expected:
                        printTree(exp)
                    print("Got:")
                    for res in result:
                        printTree(res)
                else:
                    print(str(i) + f") {FAIL} - expected " + tostring_func(expected), ", got " + tostring_func(result), "; took {:.6f}".format(duration) + ", params: " + str(parameters))
                failed_tests.append(i)
        except Exception as e:
            print(str(i) + f") {FAIL} - {CRASH}, params: " + str(parameters))
            print(e, traceback.format_exc())
            failed_tests.append(i)
    nfail = len(failed_tests)
    is_success = nfail == 0
    status = "OVERALL: " + (SUCCESS if is_success else FAILED)
    if is_success:
        print(status)
    else:
        print(status + ", " + str(nfail) + " failed of " + str(n))
        print("Failed tests: " + str(failed_tests))


def parse_params(kwargs, tests):
    if "custom_check" in kwargs:
        custom_check = kwargs["custom_check"]
    else:
        custom_check = None
    if "custom_tostring" in kwargs:
        tostring_func = kwargs["custom_tostring"]
    else:
        tostring_func = to_string
    if "run_tests" in kwargs:
        run_tests = kwargs["run_tests"]
        if type(run_tests) is int:
            run_tests = [run_tests]
    else:
        run_tests = None
    if "input_metric" in kwargs:
        input_metric = kwargs["input_metric"]
    else:
        result_instance = get_result_instance(tests)
        input_metric = get_input_mertic(result_instance)
    return custom_check, input_metric, run_tests, tostring_func
