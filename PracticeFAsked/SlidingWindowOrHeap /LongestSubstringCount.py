import string


class Solution(object):
    def lengthOfLongestSubstring(self, s: string) -> int:
        last_seen = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_length = max(max_length, right - left + 1)
            print(last_seen, left)

        return max_length        

input = "pwwkew"

solution = Solution()

print(solution.lengthOfLongestSubstring(input))
