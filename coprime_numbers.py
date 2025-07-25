import math

def are_coprime(a, b):
    return math.gcd(a, b) == 1

def find_coprime_pairs(limit):
    coprime_pairs = []
    for i in range(1, limit + 1):
        for j in range(i + 1, limit + 1):
            if are_coprime(i, j):
                coprime_pairs.append((i, j))
    return coprime_pairs

def main():
    limit = int(input("Enter the max limit to find co-prime pairs: "))
    pairs = find_coprime_pairs(limit)
    print(f"Co-prime pairs up to {limit}:")
    for pair in pairs:
        print(pair)

if __name__ == "__main__":
    main()
