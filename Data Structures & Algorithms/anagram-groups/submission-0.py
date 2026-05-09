class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for words in strs:
            key=''.join(sorted(words))
            if key in dict1:
                dict1[key].append(words)
            else:
                dict1[key]=[words]
        return list(dict1.values())
            
        
        