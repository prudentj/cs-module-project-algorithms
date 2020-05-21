'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# We know it will only contain numbers


def single_number(arr):
    # Any number without a mate goes here
    unmatched_numbers = []
    for n in arr:
        # If the number has a mate in unmatched numbers this
        # found is set to true telling us to remove it
        found = False
        # iterating through our array of unmatched to see if it matches n
        for index, item in enumerate(unmatched_numbers):
            # is the item has a mate we remove it from unmatched numbers
            # we declare it found
            if item == n:
                unmatched_numbers.pop(index)
                found = True
                break
        # if it wasn't found we add it to unmatched numbers
        if not found:
            unmatched_numbers.append(n)
    # we are only returning the first element in the array because specs say there
    # will only be one
    return unmatched_numbers[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
