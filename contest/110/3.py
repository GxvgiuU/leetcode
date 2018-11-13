class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        xset, yset = defaultdict(int), defaultdict(int)
        for p in points:
            xset[p[0]] += 1
            yset[p[1]] += 1
        pset = set()
        for p in points:
            if xset[p[0]] >= 2 and yset[p[1]] >= 2:
                pset.add(tuple(p))
        areas = []
        points_ = list(pset)
        n = len(points_)
        for i in range(n):
            for j in range(i + 1, n):
                if points_[i][0] == points_[j][0] or points_[i][1] == points_[j][1]:
                    continue
                if (points_[i][0], points_[j][1]) in pset and (points_[j][0], points_[i][1]) in pset:
                    areas.append(abs((points_[i][0] - points_[j][0]) * (points_[i][1] - points_[j][1])))
        if not areas:
            return 0
        return min(areas)


s = Solution()
# print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
# print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(s.minAreaRect([[19926,6265],[5763,23757],[21517,6265],[19926,28133],[21517,13382],[37526,26633],[36066,7139],[19926,13382],[32016,9742],[37526,34209],[5763,37795],[35370,23825],[20667,23757],[25466,5866],[7285,13382],[36066,9742],[7285,23757],[3013,4341],[20667,15162],[25466,15162],[5763,30144],[9190,4341],[6129,6265],[25819,30144],[19926,6036],[5763,9742],[7285,30144],[13468,38640],[16345,28133],[9190,30144],[7285,5866],[25861,34209],[36488,28133],[17305,39863],[25861,26633],[36488,37795],[6129,21029],[1094,5866],[36488,5866],[36488,38640],[13468,6265],[37526,30144],[20667,16878],[3013,5866],[35370,23757],[20667,6265],[1094,6036],[17305,17876],[21517,5866],[5763,21029],[32016,21029],[36758,23757],[25861,23825],[36758,23825],[5763,34209],[6129,34209],[5763,26633],[3013,13382],[1094,9742],[37526,37795],[25819,34209],[13468,23825],[5763,17876],[36488,15162],[23076,23825],[37526,21029],[9190,17876],[36758,34209],[5763,23825],[36066,15162],[36488,39863],[23076,15162],[17305,13382],[6129,4341],[32016,15162],[16345,6036],[32016,16878],[35370,15414],[5763,34116],[5763,16878],[25861,37795],[16345,5866],[36488,7139],[23076,37795],[21517,16878],[1094,30144],[19926,16878],[25819,34116],[36758,13382],[6129,38640],[36758,16878],[25466,9742],[36758,34116],[35370,9742],[17305,4341],[20667,39863],[3013,28133],[25861,16878],[16345,9742],[35370,6036],[35370,15162],[35370,37795],[36758,30144],[37526,7139],[19926,17876],[32016,38640],[16345,21029],[5763,4341],[20667,23825],[16345,26633],[13468,28133],[23076,28133],[23076,15414],[13468,15162],[6129,23825],[21517,9742],[1094,4341],[19926,9742],[1094,17876],[25466,21029],[25466,34116],[6129,15162],[25466,23757],[1094,15162],[35370,17876],[21517,34209],[7285,6036],[20667,34209],[7285,15162],[21517,7139],[25819,5866],[32016,30144],[37526,6036],[36758,39863],[16345,34116],[5763,15162],[19926,23825],[21517,30144],[20667,30144],[32016,13382],[1094,26633],[9190,34116],[32016,7139],[9190,6036],[35370,4341],[1094,15414],[35370,7139],[7285,9742],[17305,6265],[25861,6036],[7285,21029],[16345,17876],[23076,6036],[5763,28133],[19926,23757],[6129,30144],[25819,6265],[13468,17876],[20667,13382],[25819,28133],[36066,21029],[20667,15414],[21517,15414],[5763,6265],[37526,15162],[7285,34116],[20667,38640],[32016,4341],[7285,28133],[32016,17876],[23076,5866],[1094,23825],[5763,15414],[21517,37795],[25861,23757],[23076,38640],[9190,15162],[13468,5866],[9190,5866],[17305,16878],[36488,13382],[25861,7139],[25861,5866],[37526,15414],[32016,26633],[32016,37795],[23076,34116],[21517,21029],[16345,6265],[1094,7139],[21517,23825],[36758,26633],[6129,17876],[1094,16878],[25861,15414],[9190,28133],[35370,28133],[13468,26633],[35370,6265],[13468,30144],[3013,34209],[36488,21029],[3013,34116],[5763,7139],[37526,28133],[19926,26633],[17305,9742],[13468,9742],[16345,4341],[7285,23825],[25819,7139],[19926,39863],[25819,4341],[17305,21029],[13468,7139],[25861,9742],[17305,34209],[23076,7139],[17305,26633],[6129,34116],[25861,21029],[13468,39863],[19926,21029],[25466,23825],[23076,13382],[35370,34116],[35370,5866],[36066,6036],[32016,39863],[36488,6036],[25466,28133],[20667,28133],[16345,39863],[1094,34209],[19926,38640],[32016,34209],[19926,5866],[25466,15414],[9190,23825],[20667,26633],[21517,4341],[1094,21029],[23076,30144],[13468,21029],[6129,28133],[25861,34116],[25466,6036],[36488,15414],[36488,26633],[1094,6265],[6129,9742],[25819,37795],[37526,4341],[25819,15162],[32016,34116],[13468,37795],[17305,23757],[3013,30144],[17305,37795],[3013,26633],[36758,28133],[25819,23757],[16345,15162],[25819,6036],[25466,6265],[9190,16878],[17305,15162],[7285,34209],[13468,15414],[6129,6036],[17305,30144],[1094,39863],[25861,4341],[20667,7139],[25819,15414],[7285,39863],[37526,16878],[13468,4341],[37526,34116],[36066,15414],[35370,30144],[36758,5866],[25819,17876],[5763,39863],[9190,37795],[16345,16878],[36066,6265],[21517,6036],[1094,28133],[3013,7139],[7285,17876],[36488,23757],[25819,23825],[35370,34209],[32016,6265],[36066,28133],[16345,15414],[1094,38640],[9190,21029],[37526,17876],[13468,34209],[20667,21029],[25861,39863],[23076,34209],[23076,21029],[3013,23757],[21517,38640],[25819,26633],[36488,9742],[37526,39863],[7285,37795],[20667,5866],[3013,15162],[19926,4341],[20667,37795],[1094,34116],[20667,6036],[25466,17876],[36488,34209],[13468,6036],[9190,39863],[35370,39863],[19926,30144],[17305,34116],[9190,7139],[13468,16878],[32016,6036],[13468,23757],[13468,13382],[36066,38640],[32016,28133],[7285,4341],[25861,38640],[25819,13382],[36066,5866],[32016,15414],[6129,37795],[9190,23757],[17305,38640],[16345,23825],[7285,15414],[36066,4341],[36488,4341],[36758,9742],[25466,13382],[6129,26633],[37526,23757],[5763,5866],[36488,30144],[3013,16878],[5763,38640],[36758,37795],[36758,17876],[17305,7139],[25861,6265],[25466,30144],[19926,15162],[16345,13382],[7285,7139],[16345,23757],[17305,6036],[21517,17876],[32016,23825],[36488,16878],[36758,15414],[25466,37795],[36758,38640],[23076,23757],[36066,16878],[36066,34116],[9190,13382],[35370,38640],[25861,17876],[6129,5866],[16345,30144],[35370,16878],[20667,34116],[6129,39863],[36066,23825],[37526,6265],[20667,9742],[19926,15414],[21517,34116],[19926,34116],[6129,7139],[6129,15414],[37526,13382],[36488,23825],[25466,38640],[19926,34209],[19926,7139],[7285,6265],[23076,17876],[36066,17876],[36488,17876],[1094,23757],[6129,23757],[6129,16878],[25466,4341],[21517,39863],[20667,17876],[36066,26633],[20667,4341],[3013,23825],[36066,34209],[7285,38640],[17305,15414],[36758,7139],[17305,28133],[9190,6265],[37526,9742],[36066,39863],[16345,34209],[16345,7139],[36488,34116],[25466,16878],[23076,26633],[21517,28133],[25819,21029],[3013,15414],[1094,37795],[35370,21029],[25466,34209],[25466,7139],[23076,9742],[23076,4341],[21517,26633],[9190,9742],[7285,16878],[25861,28133],[1094,13382],[25466,39863],[37526,38640],[36066,30144],[37526,5866],[36758,4341],[19926,37795],[36758,6036],[21517,15162],[3013,6036],[3013,9742],[9190,15414],[32016,23757],[9190,38640],[13468,34116],[3013,21029],[23076,16878],[36066,23757],[36066,37795],[16345,38640],[17305,23825],[25819,9742],[36758,21029],[35370,13382],[7285,26633],[25861,15162],[5763,13382],[16345,37795],[17305,5866],[25819,16878],[36758,6265],[25819,38640],[3013,6265],[6129,13382],[21517,23757],[36758,15162],[5763,6036],[23076,39863],[25466,26633],[3013,39863],[36488,6265],[32016,5866],[3013,38640],[25861,13382],[37526,23825],[23076,6265],[35370,26633],[9190,26633],[36066,13382],[25819,39863],[9190,34209],[3013,17876],[25861,30144],[3013,37795]]))
