class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1

        return k
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(Solution, nums))
