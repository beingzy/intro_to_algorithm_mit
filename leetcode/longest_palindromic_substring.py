"""challenge: https://leetcode.com/problems/longest-palindromic-substring/description/

   palindromic string:
   forward-traversing a string = backward-traversing a string

   author: Yi Zhang <beingzy@gmail.com>
   date: 2018/04/14
"""


def expand_around_center(s, left, right):
    """return length of substring[left:right] if it is
       palindromic
    """
    while (left >= 0) & (right < len(s)):
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break
    return s[(left+1):right]


def find_longest_palindrome(s):
    """
    """
    start, end = 0, 0
    max_str = ''
    for i in range(len(s)):
        str1 = expand_around_center(s, i, i)
        str2 = expand_around_center(s, i, i+1)

        if len(str1) > len(max_str):
            max_str = str1
        if len(str2) > len(max_str):
            max_str = str2

    return max_str


def test_case01():
    assert find_longest_palindrome('abacdfgdcaba') == 'aba'

def test_case02():
    assert find_longest_palindrome('babad') == 'bab'

def test_case03():
    assert find_longest_palindrome('cbbd') == 'bb'


if __name__ == "__main__":
    print('running test cases!')
    test_case01()
    test_case02()
    test_case03()
    print('SUCCESS: test passed!')
