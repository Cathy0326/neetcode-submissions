class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def get_subsets(i,cur,total):
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i == len(candidates):
                return
            cur.append(candidates[i])
            get_subsets(i+1,cur,total+candidates[i])
            cur.pop()
            get_subsets(i+1,cur,total)
        get_subsets(0,[],0)
        return [list(combination) for combination in res]
        