class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count = Counter(deck)
        if len(count) > 1:
            gcds = count[deck[0]]
            for i in count:
                gcds = gcd(gcds,count[i])
            if gcds > 1:
                return True
            else:
                return False
        elif len(deck) > 1:
            return True
        else:
            return False