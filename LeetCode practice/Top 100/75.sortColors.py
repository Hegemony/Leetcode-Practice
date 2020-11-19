class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quick_sort(array, left, right):
            if left >= right:
                return
            low = left
            high = right
            key = array[low]
            while left < right:
                while left < right and array[right] > key:
                    right -= 1
                array[left] = array[right]

                while left < right and array[left] <= key:
                    left += 1
                array[right] = array[left]

            array[right] = key
            quick_sort(array, low, right - 1)
            quick_sort(array, left + 1, high)

        quick_sort(nums, 0, len(nums) - 1)


"""
快速排序模板
"""


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        # 如果right与left未重合，right(右边)指向的元素大于等于基准元素，则right向左移动
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        # 走到此位置时right指向一个比基准元素小的元素,将right指向的元素放到left的位置上,此时right指向的位置空着,接下来移动left找到符合条件的元素放在此处
        # 如果left与right未重合，left指向的元素比基准元素小，则left向右移动
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
        # 此时left指向一个比基准元素大的元素,将left指向的元素放到right空着的位置上,此时left指向的位置空着,之后进行下一次循环,将right找到符合条件的元素填到此处

    # 退出循环后，left与right重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    array[right] = key  # 将基准元素放到该位置,
    quick_sort(array, low, left - 1)  # 对基准元素左边的子序列进行快速排序
    quick_sort(array, left + 1, high)  # 对基准元素右边的子序列进行快速排序


a = [2, 3, 5, 1, 4, 0]
quick_sort(a, 0, len(a) - 1)


"""
循环不变量
"""
class Solution1:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2

        zero = 0
        two = len(nums) - 1
        if len(nums) < 2:
            return

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        i = 0
        while i <= two:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, two)
                two -= 1
        print(nums)


print(Solution1().sortColors([1, 0]))
