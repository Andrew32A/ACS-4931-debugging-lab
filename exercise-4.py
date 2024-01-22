"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# Expected Output: The program is expected to perform a binary search on the sorted list [1, 2, 4, 5, 7] to find the index of the element 7. The expected output is the index 4.
# Actual Output: IndentationError: unindent does not match any outer indentation level and RecursionError: maximum recursion depth exceeded in comparison
# Line Number Causing the Error: line 28, 43, and 47
# Cause of the Error: The code likely contains a logical issue that prevents it from performing the binary search correctly.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

# The code assumes that the input list arr is sorted in ascending order. The code also assumes that the element is always in the list. Docscring is also indented incorrectly.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search.""" # fix by moving the extra space to the left
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid) # should be return binary_search(arr, element, low, mid - 1)

    else: 
        return binary_search(arr, element, mid, high) # should be return binary_search(arr, element, mid + 1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)

# - Expected vs. Actual Output: Expected to perform a binary search on the sorted list [1, 2, 4, 5, 7] to find the index of the element 7. The expected output is the index 4 but is returning an IndentationError and RecursionError.
# - Error Message: RecursionError: maximum recursion depth exceeded in comparison.
# - Line Number Causing the Error: lines 28, 43, and 47
# - Developer Assumptions: Docstring is one indent too far to the right. The recursion issue is because the developer doesn't account if the element is on the left or right side of the middle element. Should add a +1 or -1 to mid on the last 2 conditionals to fix this.