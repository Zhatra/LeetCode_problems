class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            #nuestro contador de palabras repetidas
            count[n] = 1 + count.get(n, 0) 
        for n,c in count.items():
            #count is the index
            #n occurs c number of times
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res