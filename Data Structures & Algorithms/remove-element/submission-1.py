class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmpt=[]
        for num in nums:
            if num == val:
                continue
            tmpt.append(num)
        for i in range(len(tmpt)):
            nums[i]=tmpt[i]
        return len(tmpt)

        