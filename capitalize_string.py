def convert_string(s):
    # Case 1: CamelCase → snake_case
    if "_" not in s:
        result = ""
        for ch in s:
            if ch.isupper():
                result += "_" + ch.lower()
            else:
                result += ch
        return result

    # Case 2: snake_case → CamelCase
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


# Examples
print(convert_string("visulaVasics"))     # visual_vasic
print(convert_string("visual_vasics"))    # visualVasic
