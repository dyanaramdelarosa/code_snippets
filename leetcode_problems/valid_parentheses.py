# Problem link: https://leetcode.com/problems/valid-parentheses/
# Author: Dyanara Dela Rosa
# Date: June 15, 2024

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack: list[str] = []
        for character in s:
            if character in pairs:
                stack.append(character)
            else:
                try:
                    tos = stack.pop()
                    if pairs[tos] != character:
                        return False
                except IndexError:
                    print("Stack is empty.")
                    return False
        if stack:
            return False
        return True


## no stack implementation

class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            print(f"{s=}")
            if "()" in s:
                s=s.replace("()", "")
            elif "{}" in s:
                s=s.replace("{}", "")
            elif "[]" in s:
                s=s.replace("[]", "")
            else:
                return not s
