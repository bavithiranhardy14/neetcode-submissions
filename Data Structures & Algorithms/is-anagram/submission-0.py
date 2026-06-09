class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        value1 = "".join(s.lower())
        value2 = "".join(t.lower())

        return Counter(value1) == Counter(value2)
        