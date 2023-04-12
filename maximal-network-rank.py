class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adl = defaultdict(set)
        if roads == [] : return 0
        indx = []
        for i in range(len(roads)):
            if (roads[i][0] == 15 and roads[i][1] == 7) or (roads[i][0] == 7 and roads[i][1] == 15):
                indx.append(i)
            adl[roads[i][0]].add(roads[i][1])
            adl[roads[i][1]].add(roads[i][0])

        maxnode = roads[0][0]
        count = 0
        for i in adl:
            if len(adl[i]) > len(adl[maxnode]):
                maxnode = i

        maxcount = [maxnode]
        for i in adl:
            if len(adl[i]) == len(adl[maxnode]) and i != maxnode:
                maxcount.append(i)
        allconn = True
        
        if len(maxcount) > 2:
            for i in range(len(maxcount)):
                newList = maxcount[:]
                newList.remove(maxcount[i])
                if (all(value in adl[maxcount[i]] for value in newList)):
                    allcon = True
                else:
                    allcon = False
                    break
            if allcon:
                return len(adl[maxnode]) * 2 - 1
            else:
                return len(adl[maxnode]) * 2

        if roads[0][0] != maxnode:
            secondmax = roads[0][0]
        else:
            secondmax = roads[0][1]
        for i in adl:
            if (len(adl[i]) > len(adl[secondmax]) or len(adl[i]) == len(adl[secondmax]) and maxnode in adl[secondmax]) and i != maxnode:    
                secondmax = i

        if maxnode in adl[secondmax]:
            count = len(adl[maxnode]) + len(adl[secondmax]) - 1
        else:
            count = len(adl[maxnode]) + len(adl[secondmax])

        return count