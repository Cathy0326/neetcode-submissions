class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]
        count=len(intervals)-2
        for i in range(1,len(intervals)):
            if intervals[i][1] < intervals[-1][1]:
                res[-1][1]=max(res[-1][1],intervals[i][1])
                count -= 1
            else:
                res.append(intervals[i])
        return count
