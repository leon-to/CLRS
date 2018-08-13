def quicksort(A, p, r):
    if (p < r):
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def quicksort_iterative(A, p, r):
    stack = []
    stack.append ((p, r))
    while (stack):
        pos = stack.pop()
        left, right = pos[0], pos[1]
        print (right, left)
        pivot = partition(A, p, r)
        if (pivot > left):
            stack.append((left, pivot))
        if (pivot < right):
            stack.append((pivot, right))


def partition(A, p, r):
    x = A[r]
    i = p-1
    # from the book: for j in range(p, r-1)
    # the book is wrong
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            exchange(A, i, j)
    exchange(A, i+1, r) 
    # print (x, p, r, i+1, A)
    return  i+1

def exchange(A, a, b):
    temp = A[a] 
    A[a] = A[b]
    A[b] = temp

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
# quicksort(A, 0, len(A)-1)
quicksort_iterative (A, 0, len(A)-1)

print (A)