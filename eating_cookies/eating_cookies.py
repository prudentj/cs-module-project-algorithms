'''
Input: an integer
Returns: an integer
'''
# If cookie monster could eat any number of cookies
# def eating_cookies(n):
#     # Your code here
#     # In the end the number of branches that terminate 
#     # Is what matters
#     if n==0:
#         print(f"{n} is the end!")
#         return 1
#     #Should never trigger
#     elif n<0:
#         return 0
#     ends=0
#     for el in range(1, n+1):
#         # print(f"{n} cookies but I eat {el} so I have {n-el} left")
#         print (el)
#         ends+=eating_cookies(n-el)
#     # print(f"Returning: {ends}")
#     return ends
# Since cookie monster could only eat 3 cookies max
def eating_cookies(n):
    #   Your code here
    # In the end the number of branches that terminate 
    # Is what matters
    if n==0:
        # print(f"{n} is the end!")
        return 1
    #Should never trigger
    elif n<0:
        return 0
    ends=0
    for el in range(1, 4):
        # print(f"{n} cookies but I eat {el} so I have {n-el} left")
        # print (el)
        ends+=eating_cookies(n-el)
    # print(f"Returning: {ends}")
    return ends#

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
