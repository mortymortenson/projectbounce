def check(result, expected):
    if result == expected:
        print("PASS")
    else:
        raise Exception("Failed got: %s expected: %s", result, expected)
