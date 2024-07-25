
def balanced_brackets(my_string: str):
    my_string = "".join(ch for ch in my_string if ch in "[]()")
    if len(my_string) == 0:
        return True
    first = my_string[0] 
    last = my_string[-1]

    if first == '(':
        if last != ')':
            return False
    elif first == '[':
        if last != ']':
            return False
    elif first == ']':
        return False
    elif first == ')':
        return False
    # remove first and last character
    return balanced_brackets(my_string[1:-1])
