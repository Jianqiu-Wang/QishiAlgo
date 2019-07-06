class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = [x[0]**2+x[1]**2 for x in points]
        idx = sorted(range(len(distance)), key=lambda k: distance[k])
        n = len(distance)
        res = []
        for i in idx[:K]:
            res.append([points[i][0], points[i][1]])
        return res
       