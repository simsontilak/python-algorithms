class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            if (nums[i] > 0 and nums[i] > target) or (nums[i] < o and nums[i] < target):
                continue
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i,j)
        return (None,None)
    
    def twoSum_brute_force(self, nums: list[int], target: int) -> list[int]:
        """
            Given an array of integers nums and an integer target, 
            return indices of the two numbers such that they add up to target.

            You may assume that each input would have exactly 
            one solution, and you may not use the same element twice.

            You can return the answer in any order.
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i,j)
        return (None,None)
            
def main():
    givenList = [2,7,11,15]
    sol = Solution()
    resultList = sol.twoSum(givenList,9)
    print(resultList)
    
if __name__ == "__main__":
    main()