#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        else:
            result = [0]*len(s)
            result[0] = 1
        for index in range(1, len(s)):
            if s[index] == "0":
                if s[index-1] in ["1", "2"]:
                    if index-2 < 0:
                        result[index] = 1
                    else:
                        result[index] = result[index-2]
                else:
                    return 0
            else:
                if int(s[index-1]+s[index]) in range(1, 27) and s[index-1] != "0":
                    if index-2 < 0:
                        result[index] = result[index-1]+1
                    else:
                        result[index] = result[index-1]+result[index-2]
                else:
                    result[index] = result[index-1]
            # print(result)
        return result[-1]
        # @lc code=end
