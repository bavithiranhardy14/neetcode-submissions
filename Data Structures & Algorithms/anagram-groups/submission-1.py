class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for ch in strs:
            key = "".join(sorted(ch))
            group[key].append(ch)

        result = list(group.values())

        for gr in result:
            gr.sort()
        
        result.sort(key = lambda x : (len(x) , x[0] ))

        return result


        