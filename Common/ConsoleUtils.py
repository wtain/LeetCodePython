
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;192;192;192m".format(r, g, b, text)


SUCCESS = colored(0, 255, 0, "SUCCESS")
PASS = colored(0, 255, 0, "PASS")
FAILED = colored(255, 0, 0, "FAILED")
FAIL = colored(255, 0, 0, "FAIL")
FATAL = colored(255, 0, 0, "FATAL")
ERROR = colored(255, 0, 0, "ERROR")
CRASH = colored(255, 0, 0, "CRASH")
