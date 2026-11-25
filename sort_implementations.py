def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]



def selection_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]



def insertion_sort(seq):

    n = len(seq)
    for i in range(1, n):
        key = seq[i]
        j = i - 1

        while j >= 0 and seq[j] > key:
            seq[j + 1]  = seq[j]
            j -= 1

        seq [j + 1] = key

        

