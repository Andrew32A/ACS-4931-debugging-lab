"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# Expected Output: The program should find and print the largest difference between consecutive numbers in the list [5, 3, 1, 2, 6, 4].
# Actual Output: The code is incomplete and will raise an error.
# Error Message: IndexError: list index out of range
# Line Number Causing the Error: line 31, in find_largest_diff diff = abs(list_of_nums[i] - list_of_nums[i+1])
# Cause of the Error: The code does not handle the last element of the list properly, which will result in an "IndexError" when trying to access list_of_nums[i+1] for the last element.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# The code assumes that the list always contains at least two elements for calculating the difference and should be changed to stop at the second to last index.

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)): # fix by stopping at second to last index with: for i in range(len(list_of_nums) - 1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)

# - Expected vs. Actual Output: The program should find and print the largest difference between consecutive numbers in the list [5, 3, 1, 2, 6, 4]. The code is incomplete and will raise an error.
# - Error Message: IndexError: list index out of range
# - Line Number Causing the Error: line 31, in find_largest_diff diff = abs(list_of_nums[i] - list_of_nums[i+1])
# - Developer Assumptions: The code does not handle the last element of the list properly, which will result in an "IndexError" when trying to access list_of_nums[i+1] for the last element.