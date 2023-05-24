class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        for num in bills:
            if num == 5:
                dic[5] += 1
            elif num == 10:
                if dic[5] > 0:
                    dic[5] -= 1
                    dic[10] += 1
                else:
                    return False
            else:
                if dic[10] > 0 and dic[5] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] > 2:
                    dic[5] -= 3
                else:
                    return False
        return True