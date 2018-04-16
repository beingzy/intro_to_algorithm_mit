"""detect string cotaining only "(", "{", "[", ")", "}" and "]"

   author: Yi Zhang <beingzy@gmail.com>
   date: 2018-04-15
"""
def is_valid_parentheses(s):
    """general solution to deal with string containing non-parenthese charactor
    """
    open_p = set(("(", "[", "{"))
    close_p = set((")", "]", "}"))
    mapping = {")": "(", "]": "[", "}": "{"}

    opens = []

    for i in range(len(s)):
        if s[i] in open_p:
            opens.append(s[i])
        if s[i] in close_p:
            if len(opens) > 0:
                if opens[-1] == mapping[s[i]]:
                    _ = opens.pop()
                else:
                    return False
            else:
                return False

    return True if len(opens) == 0 else False


def test_case_01():
    assert is_valid_parentheses("()") == True


def test_case_02():
    assert is_valid_parentheses("()[]{}") == True


def test_case_03():
    assert is_valid_parentheses("[({})]") == True


def test_case_04():
    assert is_valid_parentheses("[({)]") == False


def test_case_05():
    assert is_valid_parentheses("[1+2] + (23-1)") == True


def test_case_06():
    assert is_valid_parentheses("}{") == False

if __name__ == "__main__":
    test_case_01()
    test_case_02()
    test_case_03()
    test_case_04()
    test_case_05()
    test_case_06()
