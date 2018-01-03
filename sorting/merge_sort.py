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
