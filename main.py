from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                pos = i
                break
        
        m = n-1
        maxchange = nums[n-1]
        for i in range(n-1,pos,-1):
            if nums[i]>nums[pos] and nums[i] <  maxchange:
                maxchange = nums[i]
                m = i
        nums[pos],nums[m] = nums[m],nums[pos]
        nums[pos+1:]=sorted(nums[pos+1:])
        
if __name__ == "__main__":
    nums = [2,3,1]
    b = [[1],[2]]
    a = b[:]  # Shallow copy of b
    b[0][0] = 10
    # a[0]  =10
    print(a)  # Output: [1, 2, 3]
    # Solution().nextPermutation(nums)
    # print(nums)