class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start, end = 0, len(tokens)-1
        maxScore = 0
        score = 0
        while start <= end:
            if tokens[start] <= power:
                score+=1
                power-=tokens[start]
                start+=1
            elif score > 0:
                power += tokens[end]
                end-=1
                score-=1
            else:
                break
            maxScore = max(score,maxScore)
 
        return maxScore