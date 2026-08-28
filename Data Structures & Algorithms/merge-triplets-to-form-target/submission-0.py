class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        find = set()

        for c in triplets:
            if c[0] >target[0] or c[1] >target[1] or c[2] >target[2]:
                continue
            for i, v in enumerate(c):
                if v == target[i]: 
                    find.add(i)
        return len(find) ==3

        