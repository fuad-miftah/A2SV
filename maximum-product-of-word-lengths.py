class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_format = []
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - 97)
            bit_format.append(mask)

        res = 0
        
        for i in range(len(bit_format)-1):
            for j in range(i+1,len(bit_format)):
                if bit_format[i] & bit_format[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]) )

        return res