'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    max_window = []
    if len(nums) < k:
        return -1
    # while left_side<k:
    for index in range(0, len(nums)-k+1):
        left_side = index
        right_side = index + k
        max_window.append(max(nums[left_side:right_side]))

    return max_window

# for i in rage(0,len(nums)-k+1):
#     new_window_right=i+k
#     new_window_left= i
#     window_max.append(max(nums[new_window_left:new_window_right]))
    #     if largest_index<left_side:
    #         largest_index=left_side
    #     if nums[index]>nums[largest_index]:
    #         largest_index=index
    # print(nums[largest_index])


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
