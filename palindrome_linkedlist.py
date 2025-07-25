def can_form_palindrome(arr):
    from collections import Counter
    count = Counter(arr)
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    if len(arr) % 2 == 0:
        return odd_count == 0
    else:
        return odd_count == 1

def main():
    n = int(input().strip())
    arr = [int(input().strip()) for _ in range(n)]
    if can_form_palindrome(arr):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
