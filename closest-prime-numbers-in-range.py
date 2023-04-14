class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = [-1,-1]
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False
        i = 2
        while i * i <= right:
            if primes[i]:
                j = i * i
                while j <= right:
                    primes[j] = False
                    j += i
            i += 1
        p1 = left
        while p1 < right and not primes[p1]:
                p1 += 1
        if p1 >= right:
            return res

        p2 = p1 + 1
        while p2 <= right:
            while p2 <= right and not primes[p2]:
                p2 += 1

            if p2 > right:
                return res
            else:
                if res == [-1,-1] or res[1] - res[0] > p2 - p1:
                    res = [p1,p2]
                p1 = p2
                p2 += 1

        return res