class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cero, uno, dos = [], [], []

        for i in range(len(nums)):
            if nums[i] == 0:
                cero.append(0)
            elif nums[i] == 1:
                uno.append(1)
            elif nums[i] == 2:
                dos.append(2)
        
        nums[:] = cero + uno + dos