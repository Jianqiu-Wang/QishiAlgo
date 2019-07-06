class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        
        def backtrack(combination, index, target):
            if target == 0:
                if combination not in res:
                    res.append(combination)
                return
            if index < len(candidates) and target < candidates[index]:
                return
            for i in range(index, len(candidates)):
                backtrack(combination + [candidates[i]], i+1, target-candidates[i])
        backtrack([], 0, target)
        return res