# Python
def less_than_k(k, list_n):
    result = []
    for num in list_n:
        if num < k:
            result.append(num)
    return result

A = less_than_k(7, [4, 9, 11, 14, 1, 13, 6, 15])
print(A)  # Output: [4, 1, 6]
