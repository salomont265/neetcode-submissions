class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for index,cord in enumerate(points):
            true_dis = math.sqrt(cord[0]**2 + cord[1]**2)
            distance.append([true_dis,index])
        distance.sort()
        res = []
        for i in range(k):
            index = distance[i][1]
            res.append(points[index])
        return (res)


        