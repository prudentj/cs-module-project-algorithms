'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # newArr holds the products of all other numbers except the one at the
    # indx in the arr
    newArr = []
    # We walk through the array
    for index, item in enumerate(arr):
        # We make an array that contains all numbers except the one at the current index
        other_nums = [x for i, x in enumerate(arr) if i != index]
        product = 1
        # we then multiply all of them together
        for n in other_nums:
            product = product * n
        # We append that to the output array
        newArr.append(product)
    return newArr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
