from typing import List


# Incomplete solution
class Solution:
    # [-1,0,1,2,-1,-4]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for index, num in enumerate(nums):
            second, third = self.__two_sum(nums, num, index)

            if second is None or third is None:
                continue

            if num + second + third == 0:
                result.append([num, second, third])

        return result

    def __two_sum(self, nums, target, index):
        complements = set()

        for index in range(index + 1, len(nums)):
            no = nums[index]
            complement = abs(target) - no

            if complement in complements:
                return no, complement
            else:
                complements.add(no)


def test_two_unique_pairs():
    nums = [-1, 0, 1, 2, -1, -4]
    output = [[-1, -1, 2], [-1, 0, 1]]
    solution = Solution()
    assert solution.threeSum(nums) == output
