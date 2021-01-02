class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        l = len(flowerbed)
        cnt = 0
        if l == 1:
            if flowerbed[0] == 0:
                cnt += 1
                return True if cnt >= n else False
            else:
                return True if cnt >= n else False

        for i in range(l - 1):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                cnt += 1

            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1:
                flowerbed[i] = 1
                cnt += 1

        if flowerbed[l - 1] == 0 and flowerbed[l - 2] == 0:
            flowerbed[l - 1] = 1
            cnt += 1

        return True if cnt >= n else False


print(Solution().canPlaceFlowers([0, 0], 2))
