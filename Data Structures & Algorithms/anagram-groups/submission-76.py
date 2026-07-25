class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        fingerprint_dict = {}

        for word in strs:
            fingerprint = ''.join(sorted(word))

            if fingerprint not in fingerprint_dict:
                fingerprint_dict[fingerprint] = []
            fingerprint_dict[fingerprint].append(word)

        return(list(fingerprint_dict.values()))
    
