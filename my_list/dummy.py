def mergesort(l):

    def merge(left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result



    if len(l) <= 1:
        return l
    middle = len(l) // 2
    left = mergesort(l[:middle])
    right = mergesort(l[middle:])
    return merge(left, right)








s = ["Die", "Katze", "tritt", "die", "Treppe", "krumm"]



s = mergesort(s)
print(s)