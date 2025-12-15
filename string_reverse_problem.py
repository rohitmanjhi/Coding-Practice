# Q-   R@hi#t => t@hi#R


name = "R@hi#t"

chars = list(name)
i, j = 0, len(chars) - 1

while i < j:
    if not chars[i].isalpha():
        i += 1
    elif not chars[j].isalpha():
        j -= 1
    else:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1

output = "".join(chars)
print(output)   # t@hi#R
