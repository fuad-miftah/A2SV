class Solution:
     
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isvalid(ip):
            if (ip[0]=="0" and len(ip)>1) or int(ip)>255:
                return False
            return True

        res=[]
        def backtrack(i,ip,r):
            if i==len(s) and r==0:
                res.append(ip[:-1])
                return
            if i+1<=len(s) and isvalid(s[i:i+1]):
                backtrack(i+1,ip+s[i:i+1]+".",r-1)
            if i+2<=len(s) and isvalid(s[i:i+2]):
                backtrack(i+2,ip+s[i:i+2]+".",r-1)
            if i+3<=len(s) and isvalid(s[i:i+3]):
                backtrack(i+3,ip+s[i:i+3]+".",r-1)
            return res
        return backtrack(0,"",4)