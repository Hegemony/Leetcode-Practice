class Solution:
    def fizzBuzz(self, n: int):
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 != 0:
                res.append('Fizz')
            elif i % 5 == 0 and i % 3 != 0:
                res.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            else:
                res.append(str(i))

        return res


print(Solution().fizzBuzz(1))
