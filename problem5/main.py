def max_sequence(arr):
    max_sum = -1
    current_max = 0
    min_sum = 1
    current_min = 0

    for i in arr :
        current_max = max(i, current_max+i)
        max_sum = max(max_sum, current_max)
        current_min = min(i, current_min+i)
        min_sum = min(min_sum, current_min)

        # print(current_max, end=" ")
        # print(current_min, end=" ")
        # print(' ')
        # print(max_sum, end= " ")
        # print (min_sum, end= " ")
        # print(' ')

    if max_sum <= 0 :
        return max_sum
    return max(max_sum, sum(arr) - min_sum)

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12)