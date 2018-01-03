"""
"""


def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result


def mergesort(alist):
	if len(alist) < 2:
		return alist

	middle = len(alist) // 2
	left = mergesort(alist[:middle])
	right = mergesort(alist[middle:])

	return merge(left, right)


if __name__ == "__main__":
    x = [9, 8, 5, 2, 3, 1, 4, 0, 7, 6]
    assert mergesort(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('test is exeecuted successfully!')
