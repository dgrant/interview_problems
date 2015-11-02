#!/usr/bin/env python3

def find_smallest_zeroone(n):
    test = n
    while True:
        print(test)
        digit_test = test
        while digit_test > 0:
            if (digit_test % 10) != 0 and (digit_test % 10) != 1:
                break
            digit_test = digit_test // 10
        else:
            return test
        test += n

print(find_smallest_zeroone(109))
