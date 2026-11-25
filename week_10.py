import random

def make_case(n):

    return random.sample(range(n), n)

def swap_if_needed(seq, i, j):
    if (i < j and seq[j] < seq[i]) or (i > j and seq[j] > seq[i]):
         seq[i], seq[j] = seq[j], seq[i]  # clever python 1 line swap.
         return True
    return False



def bubble_sort_1(seq): # will go to the end every single time. 0(n^2)
    for j in range(len(seq) - 1):
        for i in range(0, len(seq) - 1):
            swap_if_needed(seq, i, i + 1)

def bubble_sort_2(seq): # after each pass it skips the last element ( in this case the largest number. ) 0(n^2)
    for j in range(len(seq) - 1, 1, -1):
        for i in range(0, j):
            swap_if_needed(seq, i, i + 1)


def bubble_sort_3(seq):
    for j in range(len(seq) - 1, 1, -1):
        did_swap = False
        for i in range(0, j):
            if swap_if_needed(seq, i, i + 1):
                did_swap = True
        if not did_swap:
            return 
        # This sort basically a variation of bubblesort 2 but if did_Swap is still false it will exil the function and do no more sweeps.
lst = make_case(40)
print(lst)
bubble_sort_3(lst)
print(lst)





