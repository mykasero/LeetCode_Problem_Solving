# LeetCode Problem Name: Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer=[]
        for i in range((len(nums)-1)):
            for j in range(i+1,(len(nums))):
                if (nums[i] + nums[j]) == target:
                    answer.insert(0,i)
                    answer.insert(1,j)
                    break
                
        return answer
