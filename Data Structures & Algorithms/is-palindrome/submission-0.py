class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join([ch.lower() for ch in s if ch.isalnum()])
        s2 = s1[::-1]

        if s1 == s2 :
            return True
        else:
            return False

        