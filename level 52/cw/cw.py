#codewars

def solution(n):
    if n < 0:
        return 0
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)
 print(solution(10))  # Output: 23
