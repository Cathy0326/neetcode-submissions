class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
         
            res = num 
            maxCount=max(maxCount,count[num])
        return res

       
        