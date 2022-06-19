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

        for i in range(k):
            curr_sum +=
        print("curr sum:", curr_sum)

        # for element in range(subarray_idx, subarray_idx + k):
        #     # print("element:", element)
        #
        #     curr_sum += arr[element]
        #     print("curr sum:", curr_sum)
        #
        # if curr_sum > largest_sum:
        #     largest_sum = curr_sum
        #
        # print("largest_sum sum:", largest_sum)
        #
        # curr_sum = 0


    return 0

max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]);
