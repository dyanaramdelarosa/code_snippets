# Problem Link: https://leetcode.com/problems/validate-ip-address/
# Author: Dyanara Dela Rosa
# Date: June 10, 2024


import re

class Solution:
    def is_IPv4(self, queryIP):
        # ip_tokens = queryIP.split(".")
        # if len(ip_tokens) != 4: return False
        # pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")

        # for token in ip_tokens:
        #     if not pattern.search(token):
        #         return False
        # return True
        # pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
        # if pattern.search(queryIP):
        #     return True
        # return False

        ip_tokens = queryIP.split(".")
        if len(ip_tokens) != 4:
            return False

        for token in ip_tokens:
            int_token = int(token)
            if token == str(int_token) and int_token <= 255 and int_token >= 0:
                print(token)


    def is_IPv6(self, queryIP):
        # ip_tokens = queryIP.split(":")
        # if len(ip_tokens) != 8: return False
        # pattern = re.compile("^[a-f0-9]{1,4}$", re.IGNORECASE)
        # for token in ip_tokens:
        #     if not pattern.search(token):
        #         return False
        # return True
        # pattern = re.compile(r"^([a-f0-9]{1,4}:){7}([a-f0-9]{1,4})$", re.I)
        # if pattern.search(queryIP):
        #     return True
        # return False

        ip_tokens = queryIP.split(":")
        if len(ip_tokens) != 8:
            return False
        for token in ip_tokens:
            if len(token) !=4:
                return False
            for char_token in token.lower():
                if char_token >= 'a' and char_token <= 'z':
                   continue
                elif char_token >= 0 and char_token <= 9:
                    continue
                else:
                    return False

    def validIPAddress(self, queryIP: str) -> str:
        if self.is_IPv4(queryIP):
            return "IPv4"
        if self.is_IPv6(queryIP):
            return "IPv6"
        return "Neither"

