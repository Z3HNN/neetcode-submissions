from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Frequency = Counter(nums)

        print(Frequency.most_common(k))
        
        frequency_answer = []
        for each_set in (Frequency.most_common(k)):
            number, frequency = each_set
            print(number)
            print(frequency)
            frequency_answer.append(number)

        return(frequency_answer)
    

        
            
        
        