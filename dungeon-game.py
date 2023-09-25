class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dungeon[-1][-1] = 1 if 1 - dungeon[-1][-1] < 1 else 1 - dungeon[-1][-1]
        for i in range(len(dungeon)-2,-1,-1):
            dungeon[i][-1] = 1 if dungeon[i+1][-1] - dungeon[i][-1] < 1 else dungeon[i+1][-1] - dungeon[i][-1]
        for i in range(len(dungeon[0])-2,-1,-1):
            dungeon[-1][i] = 1 if dungeon[-1][i+1] - dungeon[-1][i] < 1 else dungeon[-1][i+1] - dungeon[-1][i]
        for i in range(len(dungeon)-2,-1,-1):
            for j in range(len(dungeon[0])-2,-1,-1):
                r = 1 if j + 1 >= len(dungeon[0]) else dungeon[i][j+1]
                b = 1 if i + 1 >= len(dungeon) else dungeon[i+1][j]
                cur = 1 if min(b,r) - dungeon[i][j] < 1 else min(b,r) - dungeon[i][j]
                dungeon[i][j] = cur
        return dungeon[0][0]