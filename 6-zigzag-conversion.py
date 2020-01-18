#Submitted-1, runtime error division by zero
#Submitted-2, 268ms ** bad runtime **, Fix runtime error division by zero and fix some case

import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return ""
        if numRows - 2 < 0:
            nCharUp = 0
        else:
            nCharUp = numRows - 2
        nCharPerCollect = numRows + nCharUp
        nCollect = int(len(s) / nCharPerCollect)
        nColPerCollect = nCharUp + 1
        fractChars = len(s) - nCharPerCollect * nCollect
        fractCol = 1 if fractChars - numRows < 0 else fractChars - numRows + 1
        nCol = (nColPerCollect * nCollect + fractCol)
        arr = [[""] * nCol for i in range(numRows)]
        row = 0
        col = 0
        isUp = False
        for char in s:
            arr[row][col] = char
            if row == numRows - 1 :
                isUp = True
            if row == 0 and numRows - 1 != 0:
                isUp = False
            if isUp:
                col += 1
                if row != 0:
                    row -= 1
            else:
                row += 1
        return "".join([c for cc in arr for c in cc])