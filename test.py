def TestFail(RuntimeError):
    pass

def check(result, expected) -> None:
    if result == expected:
        print("PASS")
    else:
        raise TestFail("Failed got: %s expected: %s", result, expected)
