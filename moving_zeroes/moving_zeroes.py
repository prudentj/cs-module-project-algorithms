'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    arr1 = []
    numZeros = 0
    test = [0, 3, 1, 0, -2]
    # We walk through arr and check if it is a zero
    # If it is we add it to our output arr1.
    for item in arr:
        if item == 0:
            numZeros += 1
        else:
            arr1.append(item)
    while numZeros != 0:
        numZeros -= 1
        arr1.append(0)
    return arr1


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# test = [0, 3, 1, 0, -2]

# moving_zeroes(test)
