import threading, random, bubblesort

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Create threads for merge sort on left and right halves
        left_thread = threading.Thread(target=merge_sort, args=(left_half,))
        right_thread = threading.Thread(target=merge_sort, args=(right_half,))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to divide list into parts of 10,000 elements each and apply bubble sort with threads
def parallel_bubble_sort(arr):
    threads = []
    chunk_size = 10000

    # Divide the list into chunks of size 10,000 and apply bubble sort with individual threads
    for i in range(0, len(arr), chunk_size):
        thread = threading.Thread(target=bubblesort.bubblesort, args=(arr[i:i+chunk_size],))
        threads.append(thread)
        thread.start()

    print("All threads created")

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Done with bubble sort")

    # Merge the sorted parts using merge sort with threads
    merge_sort(arr)

daten = [random.randint(1000, 10000) for _ in range(100000)]

parallel_bubble_sort(daten)
print(daten)