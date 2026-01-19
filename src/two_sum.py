class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
            When the processing is N(O)^2 and storage is N(1), there is a possibility
            of making processing N(O) and storage N(O)
            
            In this case we use the dictionary to solve the problem
        """
        num_dict = {}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if num_dict.get(other_num) is not None:
                return (i, num_dict[other_num])
            else:
                # just remember their positions
                num_dict[nums[i]] = i
        #If nothing is found
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