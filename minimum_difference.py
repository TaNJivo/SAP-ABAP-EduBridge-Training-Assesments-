def find_min_diff_index(arr):
   
    n = len(arr)
    mean = sum(arr) / n
    min_diff = float('inf')
    min_index = -1

    for i, val in enumerate(arr):
        diff = abs(val - mean)
        if diff < min_diff:
            min_diff = diff
            min_index = i
    return min_index


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = find_min_diff_index(arr)
    print(result)
