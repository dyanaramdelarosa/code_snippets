# Problem Link: https://www.hackerrank.com/challenges/balanced-brackets/problem
# Author: Dyanara Dela Rosa
# Date: January 2024

# Problem Definition: Identify whether an input string is "balanced".
# It is balanced if the string contains no unmatched brackets and if the subset of brackets
# enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Output YES if input string is balanced, else output NO.

# Similar Problem with better solution: leetcode/valid_parenthesis.py

def is_balanced(str_input):
    """
    Function that identifies if a string is "balanced" or not
    Parameter:
        str_input (str): string to be classified if it's balanced or not
    Returns:
        str: YES if string is balanced; otherwise returns NO
    """
    stack = []
    opening_chars = '{[('   # contains all valid opening characters
    closing_chars = '}])'   # contains all valid closing characters
    # ordering for opening_chars and closing_chars are significant because it shows which
    # character matches e.g. first character in opening_chars matches with
    # first character in closing_chars

    for character in s:
        if character in opening_chars:
            stack.append(character)     # add character to the stack if it's an opening character
        else:
            try:
                tos_character = stack.pop()
                char_index = opening_chars.find(tos_character)  # get the index of the character
                if closing_chars[char_index] != character:  # check if the pair of tos character matches
                    return "NO"
            except IndexError as exc:   # handler for empty stack
                return "NO"

    if stack:   # handler for stack not empty i.e. there were unmatched characters
        return "NO"
    return "YES"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = is_balanced(s)
        print(result)
