import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quicksort(less) + equal + randomized_quicksort(greater)

if __name__ == "__main__":
    arr = [10, 5, 2, 3, 3, 8, 1]
    print("Original:", arr)
    sorted_arr = randomized_quicksort(arr)
    print("Sorted:", sorted_arr)

