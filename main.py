def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here

    # Verification
    # for i in arr:
    #     print(i)

    # BRUTE FORCE
    # largest_sum = 0
    # curr_sum = 0
    # arr_size = len(arr)
    #
    # for subarray_idx in range(arr_size-k+1):
    #     print("subarray_idx:", subarray_idx)
    #
    #     for element in range(subarray_idx, subarray_idx + k):
    #         #print("element:", element)
    #
    #         curr_sum += arr[element]
    #         print("curr sum:", curr_sum)
    #
    #     if curr_sum > largest_sum:
    #         largest_sum = curr_sum
    #
    #     print("largest_sum sum:", largest_sum)
    #
    #     curr_sum = 0

    # BETTER METHOD

    largest_sum = 0
    curr_sum = 0
    arr_size = len(arr)

    for element in range(arr_size - 1):
        print("element:", element)
        curr_sum += arr[element]

        if element >= k - 1:
            print("entered curr sum:", curr_sum)
            largest_sum = max(largest_sum, curr_sum)

            curr_sum -= arr[element - (k-1)]    # Suggested to create variable "window_start" to keep track of the index element to be popped off
            #curr_sum += arr[element + 1]

        print("curr sum:", curr_sum)
        print("large sum:", largest_sum)

    return 0

max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]);
