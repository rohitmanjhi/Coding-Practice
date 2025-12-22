from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    # if its empty s or t
    if not s or not t:
        return ""

    # count of letter t count
    need = Counter(t)
    required = len(need) 

    # How many letters count done
    window = defaultdict(int)
    formed = 0

    # Answer tracking
    min_len = float('inf')
    ans_left = 0

    left = 0

    # Right pointer sa window badao
    for right in range(len(s)):
        char = s[right]
        window[char] = +1

        # Agar current char ka required count poora ho gaya
        if char in need and window[char] == need[char]:
            formed += 1

        # jab sare letter mil jye tab
        while formed == required:
            # chota answer mila to save karo
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                ans_left = left

            # left sa ek letter htao
            left_char = s[left]
            window[left_char] -= 1

            # Agar koi required letter kam ho gaya
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1     # window chhoti karo
    # Step 5: Answer return karo
    if min_len == float("inf"):
        return ""    

    return s[ans_left: ans_left + min_len]      

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))


