#1st codewars
def is_uppercase(s):
    return s == s.upper()


#2nd codewars
def monkey_count(n):
    return list(range(1, n + 1))


#3rd codewars
def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]


#4th codewars
def human_years_cat_years_dog_years(humanYears):
    if humanYears == 1:
        return [1, 15, 15]
    elif humanYears == 2:
        return [2, 24, 24]
    else:
        catYears = 24 + (humanYears - 2) * 4
        dogYears = 24 + (humanYears - 2) * 5
        return [humanYears, catYears, dogYears]


#5th codewars
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None  # optional: covers empty or single-element arrays
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None




