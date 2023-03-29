class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for number in range(0, len(nums) - 1):
            number_in_list = nums[number]
            for number in range(nums.index(number_in_list) + 1, len(nums)):
                if nums[number] + number_in_list == target:
                    index_list.append(nums.index(number_in_list))
                    index_list.append(number)
                    return index_list
                else:
                    continue
