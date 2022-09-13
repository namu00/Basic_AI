def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result
pickup_even([3, 4, 5, 6, 7, 8])