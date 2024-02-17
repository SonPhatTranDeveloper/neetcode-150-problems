"""
The encoding is [string_length][space][string_itself]
Author: Son Phat Tran
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Create a string
        string = ""

        # Add the length of the string + the string itself
        for s in strs:
            string += str(len(s))
            string += " "
            string += s

        # Return the string
        return string

    def decode(self, s: str) -> List[str]:
        # Create the result
        results = []

        # Get the strings one by one
        index = 0

        while index < len(s):
            # Get the length
            length = ""
            while s[index] != " ":
                length += s[index]
                index += 1
            length = int(length)
            index += 1

            # Get the remaining characters
            current_string = ""
            for _ in range(length):
                current_string += s[index]
                index += 1

            # Add to results
            results.append(current_string)

        return results


if __name__ == "__main__":
    strings = ["we", "say", ":", "yes", "!@#$%^&*()"]
    sol = Solution()
    encode_result = sol.encode(strings)
    print(encode_result)
    decode_result = sol.decode(encode_result)
    print(decode_result)
