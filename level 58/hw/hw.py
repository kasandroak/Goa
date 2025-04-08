#1st codewars
def who_is_paying(name):
    # If the name has 2 or fewer characters, return the name itself
    if len(name) <= 2:
        return [name]
    # Otherwise, return the full name and the first 2 characters as a list
    return [name, name[:2]]
