def incentive(N: int) -> int:
   
    incentive_total = 0

    if N > 50:
        incentive_total += (N - 50) * 1000
        N = 50
    if N > 40:
        incentive_total += (N - 40) * 800
        N = 40
    if N > 30:
        incentive_total += (N - 30) * 500
        N = 30

    return incentive_total


if __name__ == "__main__":
    test_cases = [42, 55, 32, 75]
    for days in test_cases:
        print(f"Days worked: {days}, Incentive: {incentive(days)}")
