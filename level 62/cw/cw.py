#codewars 1
def final_grade(exam: int, projects: int) -> int:
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    

#codewars 2
def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, a + b * c, (a + b) * c, a * (b + c))


#codewars 3
def sum_str(a: str, b: str) -> str:
    return str(int(a or 0) + int(b or 0))