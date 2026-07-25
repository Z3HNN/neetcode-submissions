class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        i = 0
        s_letter_monster = []
        while i<len(s):
            s_letter_monster.append(s[i])
            i += 1
        print(s_letter_monster)


        i = 0
        t_letter_monster = []
        while i<len(t):
            t_letter_monster.append(t[i])
            i += 1
        print(t_letter_monster)

        t_letter_monster.sort()
        s_letter_monster.sort()

        return(t_letter_monster == s_letter_monster)
        
