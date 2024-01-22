"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# Expected Output: The program should return true if the list contains 3 consecutive numbers each increasing by 1.
# Actual Output: The code is returning false with the list [4, 1, 2, 3] when it should return true.
# Line Number Causing the Error: line 31.
# Cause of the Error: The code is stopping too early and returning false due to the else on line 27, it can be fixed by removing the else statement and returning false after the for loop.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# Code is stopping to early and returning false due to the else on line 27, it can be fixed by removing the else statement and returning false after the for loop.

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else: # fix by removing else statement and returning false after for loop
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True