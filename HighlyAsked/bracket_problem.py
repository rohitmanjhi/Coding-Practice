mapping = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def is_valid(s):
    stack = []
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if not stack or mapping[stack.pop()] != char:
                return False
    return not stack

print(is_valid("([{}])"))
# print(is_valid("(]"))
