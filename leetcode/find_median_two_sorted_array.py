"""find the median of two sorted arrays:
   median is the number which in the middle number of a sequence of sorted
   numbers (x)
   if len(x) is odd, the median is kth value, k = (len(x) + 1) / 2
   if len(x) is even, the median is (x[len(x)/2] + x[len(x)/2+1]) / 2

   author: Yi Zhang <beingzy@gmail.com>
   date: 2018/04/14
"""


def merge_two_sorted(x, y):
    """assume x and y are both sorted in ascending order
    """
    x, y = x[:], y[:]
    if y[0] > x[-1]:
        return x + y
    elif y[-1] < x[0]:
        return y + x
    else:
        start_idx = 0
        while len(y) > 0:
            for i in range(start_idx, len(x)):
                if y[0] < x[i]:
                    val = y.pop(0)
                    x.insert(i, val)
                    start_idx = i + 1
                elif i == len(x) - 1:
                    return x + y

                if len(y) == 0:
                    break
    return x


def find_median_of_two_sorted(x, y):
    seq = merge_two_sorted(x, y)
    n = len(seq)
    if n % 2 == 1:
        med_idx = int((n+1)/2) - 1
        return seq[med_idx]
    else:
        right_idx = int(n/2)
        left_idx = right_idx - 1
        return (seq[left_idx] + seq[right_idx]) / 2.0


def test_merge_two_sorted_01():
    x = [10, 12, 15, 16]
    y = [9, 13, 17]
    ans = [9, 10, 12, 13, 15, 16, 17]
    res = merge_two_sorted(x, y)
    assert res == ans

def test_merge_two_sorted_02():
    x = [10, 12, 15, 16]
    y = [1, 2]
    ans = [1, 2, 10, 12, 15, 16]
    res = merge_two_sorted(x, y)
    assert res == ans


def test_merge_two_sorted_03():
    x = [10, 12, 15, 16]
    y = [17]
    ans = [10, 12, 15, 16, 17]
    res = merge_two_sorted(x, y)
    assert res == ans


def test_median01():
    x = [5, 8, 10, 11]
    y = [6, 7, 12]
    return find_median_of_two_sorted(x, y) == 10


if __name__ == "__main__":
    test_merge_two_sorted_01()
    test_merge_two_sorted_02()
    test_merge_two_sorted_03()

    test_median01()
