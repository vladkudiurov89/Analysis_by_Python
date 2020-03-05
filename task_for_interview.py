def get_check_string(string):
    """Check string for open or closed brackets
    :param: string
    :return: True or False
    """
    check_stack = []
    first_brackets = ('(', '[', '{')
    last_brackets = (')', ']', '}')
    for bracket in string:
        if bracket in first_brackets:
            check_stack.append(bracket)
        if bracket in last_brackets:
            if len(check_stack) == 0:
                return False
            act = last_brackets.index(bracket)
            act_bracket = first_brackets[act]
            if check_stack[-1] == act_bracket:
                check_stack = check_stack[:-1]
            else:
                return False
    return not check_stack


string_1 = '([])'
string_2 = '{[(]}'
print(get_check_string(string_1))  # True
print(get_check_string(string_2))  # False

