__author__ = 'hai'

"""
Input: given an array of numbers
Output: shift all the ZERO elements to the right (or left)


Strategy for shift right: we have 2 index running: one (i) is for traverse array from left to right
the other (Count) is the number of elements DIFFERENT to zero
each time we meet a ZERO:
    1/ the different between 2 index increase by 1. Count will stay if meets a ZERO
    2/ if there's different between i and count:
        2.1/ copy the element back to the zero on the left.
        2.2/ increase count
By the end, all the non-ZERO elements have been copied to the left.
Override the rest elements into ZERO


For push left, just do a reverse work by traversing the array from right to left
"""

def push_zero_right(a):
    count = 0

    for i in range(len(a)):
        if a[i] != 0:
            a[count] = a[i]
            count += 1

    while count < len(a):
        a[count] = 0
        count += 1

    for aa in a: print aa,

def push_zero_left(a):
    l = len(a) - 1
    count = l
    for i in reversed(range(l)):
        if a[i] != 0:
            a[count] = a[i]
            count -= 1

    while count >= 0:
         a[count] = 0
         count -= 1

    for aa in a: print aa,




"""
This algorithm is very much shorter using different strategy
traverse from left -> right, if there's a zero then swap it with the first non-zero element from the top
Also needs 2 index:
    count: the number of zero elements, started from -1 (first match will swap with a[0]
    i: traverse inside the array
"""
def push_zero_left2(a):
    l = len(a)
    count = -1
    for i in range(l):
        if a[i] == 0:
            count += 1
            # swap a[i] and a[count]
            temp = a[i]
            a[i] = a[count]
            a[count] = temp

    for aa in a: print aa,


# TEST
a = [1, 5, 0 , 7 , 0, 8, 0, 9, 0]
push_zero_right(a)
# 1 5 7 8 9 0 0 0 0


print
push_zero_left2(a)
# 0 0 0 0 1 5 7 8 9
