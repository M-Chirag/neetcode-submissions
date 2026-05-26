class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = 1
            else:
                map_s[s[i]]+=1
            if t[i] not in map_t:
                map_t[t[i]] = 1
            else:
                map_t[t[i]]+=1
        
        for k,v in map_s.items():
            if k not in map_t:
                return False
            if map_t[k]!= v:
                return False
        
        return True 
        