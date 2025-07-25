def greatest_first_sort(arr):
    from collections import Counter
    freq = Counter(arr)
    first_occurrence = {}
    for i, val in enumerate(arr):
        if val not in first_occurrence:
            first_occurrence[val] = i
    arr.sort(key=lambda x: (-freq[x], first_occurrence[x]))
    return arr

def main():
    arr = list(map(int, input().strip().split()))
    result = greatest_first_sort(arr)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
