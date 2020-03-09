#Given 2 sorted arrays A and B with n and m elements respectively.
#A has enough space at the end of the array to fit in all elements of B.
#Write an algorithm to merge the elements of A and B ensuring the resultant A is sorted as well.
#The code cannot use an extra array.
#Input: A = 1 3 5 6 8 - - -
#B = 0 2 10
#Output: A = 0 1 2 3 5 6 8 10

#Algorithm
# Let first array be mPlusN[] and other array be N[]
# 1) Move m elements of mPlusN[] to end.
# 2) Start from nth element of mPlusN[] and 0th
# element of N[] and merge them into mPlusN[].


NA = -1

def moveToEnd(mPlusN, size):
    i = 0
    j = size - 1
    for i in range(size - 1, -1, -1):
        if (mPlusN[i] != NA):
            mPlusN[j] = mPlusN[i]
            j -= 1

def merge(mPlusN, N, m, n):
    i = n
    j = 0
    k = 0
    while (k < (m + n)):

        # Take an element from mPlusN[] if
        # a) value of the picked
        # element is smaller and we have
        # not reached end of it
        # b) We have reached end of N[] */
        if ((i < (m + n) and mPlusN[i] <= N[j]) or (j == n)):

            mPlusN[k] = mPlusN[i]
            k += 1
            i += 1

        else:  # Otherwise take element from N[]

            mPlusN[k] = N[j]
            k += 1
            j += 1

def printArray(arr, size):
    for i in range(size):
        print(arr[i], " ", end="")

    print()

mPlusN = [2, 8, NA, NA, NA, 13, NA, 15, 20]
N = [5, 7, 9, 25]
n = len(N)

m = len(mPlusN) - n
moveToEnd(mPlusN, m + n)
merge(mPlusN, N, m, n)
printArray(mPlusN, m + n)

