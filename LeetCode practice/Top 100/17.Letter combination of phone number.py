def letterCombinations(digits):
    if not digits:
        return []
    digit2chars = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = [i for i in digit2chars[digits[0]]]

    for i in digits[1:]:
        result = []
        for m in res:
            for n in digit2chars[i]:
                result.append(m+n)
            res = result
            print(result)
    return result

print(letterCombinations('234'))

