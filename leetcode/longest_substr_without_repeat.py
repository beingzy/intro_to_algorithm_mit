"""challenge: https://goo.gl/MFyoRw
   given a string, find the longest substring with no repeats
   and ouput its length
"""

def all_unique(s):
    """
    """
    return len(set(s)) == len(s)


def return_longest_substr_len(s):
    chars = list(s)
    s_len = len(s)
    max_substr = 0

    if s_len < 2:
        return s_len

    for ii in range(s_len-1):
        substr = {chars[ii]}

        for jj in range(ii+1, s_len):
            new_char  = chars[jj]
            if new_char in substr:
                if max_substr < len(substr):
                    max_substr = len(substr)
                    pass
            else:
                substr.add(new_char)
                if jj == s_len:
                    if max_substr < len(substr):
                        max_substr = len(substr)
                        #break

    print("".join(list(substr)))
    return max_substr


if __name__ == '__main__':
    assert return_longest_substr_len('abcabcbb') == 3

    #assert return_longest_substr_len('bbbbb') == 1

    #assert return_longest_substr_len('pwwkew') == 3

    #assert return_longest_substr_len('au') == 2
