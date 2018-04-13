"""challenge: https://goo.gl/MFyoRw
   given a string, find the longest substring with no repeats
   and ouput its length
"""

def get_max_uniq_str_length(s):
    """
    """
    def find_max(astring, num):
        return num if num > len(astring) else len(astring)

    max_len = 0
    cur_str = ''
    for _, char in enumerate(s):
        c_idx = cur_str.find(char)
        if c_idx == -1:
            cur_str += char
        else:
            max_len = find_max(cur_str, max_len)
            cur_str = cur_str[(c_idx+1):] + char

    return find_max(cur_str, max_len)


def test_case01():
    assert get_max_uniq_str_length('abcabcbb') == 3


def test_case02():
    assert get_max_uniq_str_length('bbbbb') == 1


def test_case03():
    assert get_max_uniq_str_length('pwwkew') == 3


if __name__ == "__name__":
    test_case01()
    test_case02()
    test_case03()
