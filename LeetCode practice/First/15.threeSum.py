class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        if n < 3:
            return []
        for i in range(n - 2):
            if nums[i] > 0:
                return result
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l = i + 1
            r = n - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return result

