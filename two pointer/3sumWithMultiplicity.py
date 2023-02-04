class Solution(object):
    def threeSumMulti(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = 0
        for num1 in range(n-2):
            tot = target - arr[num1]
            num2 = num1+1
            num3=len(arr)-1
            while num2 < num3:
                if arr[num2] + arr[num3] > tot:
                    num3-=1
                elif arr[num2] + arr[num3] < tot:
                    num2+=1
                elif arr[num2] != arr[num3]:
                    count1 = count2 = 1
                    while num2 + 1 < num3 and arr[num2] == arr[num2+1]:
                        count1+=1
                        num2+=1
                    while num3 > num2 + 1  and arr[num3] == arr[num3-1]:
                        count2+=1
                        num3-=1
                    ans += (count1 * count2)
                    num2+=1
                    num3-=1
                else:
                    length = num3-num2+1
                    ans += length * (length - 1) // 2
                    break
                
        return ans % (10**9 + 7)
