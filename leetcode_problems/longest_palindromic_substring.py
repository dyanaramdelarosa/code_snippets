# Problem Link: https://leetcode.com/problems/longest-palindromic-substring/
# Author: Dyanara Dela Rosa
# Date: June 3, 2024

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     longest_instance = ""
    #     longest_instance_len = 0
    #
    #     for i in range(len(s)):
    #         for j in range(i+1, len(s)+1):
    #             substr = s[i:j]
    #             rev_substr = s[i:j][::-1]
    #             if substr == rev_substr and len(substr) > longest_instance_len:
    #                 longest_instance = substr
    #                 longest_instance_len = len(substr)
    #
    #     return longest_instance

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            print(f"{left=}")
            print(f"{right=}")
            print(f"{s[left:right]=}")
            print(f"{s[left+1:right]=}")
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                print(f"{s[left:right]=}")
                print(f"{s[left+1:right]=}")
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            print(f"center: {s[i]=}")
            odd = expand_from_center(i, i)
            print(f"{odd=}")
            even = expand_from_center(i, i + 1)
            print(f"{even=}")
            print("============================")

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

solution = Solution()
print(solution.longestPalindrome(input()))
