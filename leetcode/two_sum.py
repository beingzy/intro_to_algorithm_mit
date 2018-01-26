"""url: https://leetcode.com/problems/two-sum/description/

   description:
   Given an array of integers, return indices of the two numbers such that
   they add up to a specific target. You may assume that each input would have
   exactly one solution, and you may not use the same element twice.

   example:
   Given nums = [2, 7, 11, 15], target = 9,
   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1].
"""
def search_value(x, start, val):
    """
    """
    for i in range(start, len(x)):
        if x[i] == val:
            return i
    return None

def find_twosum(x, target_val):
    ans = []
    for i in range(len(x)):
        diff = target_val - x[i]
        j = search_value(x, i+1, diff)
        if j is not None:
            return [i, j]


if __name__ == "__main__":
    x = [2, 7, 11, 15]
    ans = find_twosum(x, 9)
    assert ans == [0, 1]

    x = [3, 2, 3]
    ans = find_twosum(x, 6)
    assert ans == [0, 2]
