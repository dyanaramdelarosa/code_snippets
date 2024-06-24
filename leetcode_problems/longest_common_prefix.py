# Problem link: https://leetcode.com/problems/longest-common-prefix/
# Author: Dyanara Dela Rosa
# Date: June 15, 2024

class Solution:
    def get_lcp(self, current_lcp: List[str], word: str):
        lcp_len = min(len(current_lcp), len(word))
        for i in range(lcp_len):
            if current_lcp[i] != word[i]:
                return current_lcp[:i]
        return current_lcp[:lcp_len]


    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for word in strs[1:]:
            lcp = self.get_lcp(lcp, word)
            if not lcp:
                break
        return lcp

