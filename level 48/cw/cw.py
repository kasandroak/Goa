#1st codewars
def solution(s):
    return s[::-1]


#2nd codewars
def accum(s):
    return '-'.join((c.upper() + c.lower() * i) for i, c in enumerate(s))

# Examples
print(accum("abcd"))      # "A-Bb-Ccc-Dddd"
print(accum("RqaEzty"))   # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))      # "C-Ww-Aaa-Tttt"


#3rd codewars
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

# Example usage:
n = 5
m = 5
print(paperwork(n, m))  # Output: 25

n = -5
m = 5
print(paperwork(n, m))  # Output: 0
