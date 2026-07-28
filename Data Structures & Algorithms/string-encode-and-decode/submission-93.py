class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted_string = []
        for j, word in enumerate(strs):
            if len(word) == 0:
                letter = (f"hygnllhsd{j}***")
                encrypted_string.append(letter)
            else:
                for i in range(len(word)):
                    letter = word[i]
                    letter = (f"hyg{letter}hsd{j}***")
                    encrypted_string.append(letter)
        
        return "".join(encrypted_string)
        

    def decode(self, s: str) -> List[str]:
        decrypted_text = []
        decrypted_letters = s.split("***")
        for letter in decrypted_letters:
            if "nll" in letter:
                decrypted_text.append("")
            else:
                if not letter or len(letter) < 8:
                    continue
                letters = letter[3]
                j = int(letter[7:])
            
                while len(decrypted_text) <= j:
                    decrypted_text.append("")
                
                decrypted_text[j] = decrypted_text[j] + letters
        return (decrypted_text)
        
        


        