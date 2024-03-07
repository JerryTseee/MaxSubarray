def find_maximum_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start_index = 0
    end_index = 0

    for i in range(1, len(arr)):#starting from the second element is because we already let the max_sum and current_sum = arr[0], we should not repeat
        current_sum += arr[i]

        if current_sum < arr[i]:#situation that when we add the negative number, which may leads to the decrease of sum, so we restart the index again in new position
            current_sum = arr[i]
            start_index = i

        if current_sum > max_sum:#keep adding when is continueing increasing
            max_sum = current_sum
            end_index = i

    return max_sum, start_index, end_index

a=(1,2,4)
print(find_maximum_subarray(a))
#the time complexity is O(n)