# Problem Link: https://leetcode.com/problems/word-pattern/
# Author: Dyanara Dela Rosa
# Date: Jul 24, 2025


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        character_word_mapping = {}
        word_character_mapping = {}
        pattern = list(pattern)
        s = s.split()

        if len(pattern) != len(s):
            return False

        for word, character in zip(s, pattern):
            if (
                character not in character_word_mapping and
                word not in word_character_mapping
            ):
                character_word_mapping[character] = word
                word_character_mapping[word] = character
                continue
            if word != character_word_mapping.get(character, ""):
                return False
            if character != word_character_mapping.get(word, ""):
                return False
        return True