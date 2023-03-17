class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        people = [0]*k
        unfairnes = float("inf")
        def backtrack(indx,people):
            nonlocal unfairnes
            if indx >= len(cookies):
                unfairnes = min(unfairnes, max(people))
                return unfairnes
            if max(people) > unfairnes:
                return 
            for i in range(k):
                people[i]+=cookies[indx]
                backtrack(indx+1,people)
                people[i]-=cookies[indx]
            return unfairnes
        return backtrack(0,people)