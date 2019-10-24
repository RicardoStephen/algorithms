"""14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string \"\".

Example:

  Input: ["flower","flow","flight"]
  Output: "fl"

Example:

  Input: ["dog","racecar","car"]
  Output: ""
  Explanation: There is no common prefix among the input strings.


https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        template = strs[0]
        tail = len(strs[0])
        if not tail:
            return ""
        strsit = iter(strs)
        next(strsit)
        for s in strsit:
            tail = min(tail, len(s))
            for idx in range(tail):
                if template[idx] != s[idx]:
                    tail = idx
                    break
            if not tail:
                return ""
        return template[:tail]


if __name__ == '__main__':
    solution = Solution()
    cases = [["flower","flow","flight"],
             ["dog","racecar","car"]]
    solutions = ["fl", ""]
    results = [solution.longestCommonPrefix(strs) for strs in cases]
    print(results)
    assert(results == solutions)
