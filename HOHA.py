import math
def is_perfect_number(n: int) -> bool:
    if n <= 1:
        return False

    sum_divisors = 1

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i

    return sum_divisors == n

if __name__ == "__main__":
    n = int(input().strip())
    print("YES" if is_perfect_number(n) else "NO")