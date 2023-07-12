class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #[2,7,11,15] target:9 
        for i in range(len(nums)): #range 0 1 2 3 
            for j in range(i + 1, len(nums)): #como en la primera iteracion i=0 seria del 1 al 3
                if nums[j] == target - nums[i]: #7 == 9 - 2
                    return [i, j] # return indeces