class Solution:
    def binary_search(self, nums: List[int], target: int, left: int, right: int):
        if left > right:
            return -1

        mid = (left+right)//2
        if nums[mid] == target:
            return mid

        if nums[left] < nums[mid] and target >= nums[left] and target < nums[mid]:
            return self.binary_search(nums, target, left, mid-1)
        elif nums[right] > nums[mid] and target <= nums[right] and target > nums[mid]:
            return self.binary_search(nums, target, mid+1, right)
        elif nums[left] > nums[mid] and (target >= nums[left] or target < nums[mid]):
            return self.binary_search(nums, target, left, mid-1)
        elif nums[right] < nums[mid] and (target <= nums[right] or target > nums[mid]):
            return self.binary_search(nums, target, mid+1, right)
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)