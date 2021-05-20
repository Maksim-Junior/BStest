# Task 3(b)
# function that returns the first repeating element from some list
def first_repeating_element(some_list: list):
    repeating_elements = [item for item in set(some_list) if some_list.count(item) > 1]
    result = repeating_elements[0] if repeating_elements else None
    return result
