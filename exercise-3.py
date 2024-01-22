"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# The program is expected to sort the list [5, 2, 3, 1, 6] using the Insertion Sort algorithm and print the sorted list.
# Actual Output: IndexError: list index out of range.
# Line Number Causing the Error: line 34 and 26.
# Cause of the Error: The code likely contains a logical issue that prevents it from sorting the list correctly.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

# Needs to check for j >= 0 in the while loop and key < arr[j] to prevent the IndexError.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] : # should be while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

