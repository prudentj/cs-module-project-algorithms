'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# We know it will only contain numbers

def single_number(arr):
    # Your code here
    # I would make this ordered for speed if I could
    # But lets do it quick and dirty first
    unmatched_numbers = []
    for n in arr:
        found=False
        for index, item in enumerate(unmatched_numbers):
            if item == n:
                unmatched_numbers.pop(index)
                found= True
                break
        if not found:
            unmatched_numbers.append(n)
    return unmatched_numbers[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")