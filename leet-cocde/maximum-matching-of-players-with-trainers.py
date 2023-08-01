class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p1 = 0
        p2 = 0
        res = 0
        while p1 < len(players) and p2 < len(trainers):
            while p2 < len(trainers) and trainers[p2] < players[p1]:
                p2 += 1
            if p2 < len(trainers):
                res += 1
            p1 += 1
            p2 += 1
        return res