import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        cum_time = 0
        for t, end_date in sorted(courses, key=lambda courses:courses[1]):
            cum_time += t
            heapq.heappush(pq, -t)
            while cum_time > end_date:
                cum_time += heapq.heappop(pq)
        return len(pq)
        