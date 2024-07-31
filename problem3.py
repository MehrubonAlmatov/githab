class Solution(object):
    def shuffle(self, nums, n):
        lst = []

        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[i+n])
        return lst