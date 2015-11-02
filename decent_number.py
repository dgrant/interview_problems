import unittest

def decent(n):
    if n % 3 == 0:
        return int('5' * n)
    else:
        num_fives = n
        while num_fives >= 0:
            print('trying num_fives=', num_fives)
            if num_fives % 3 == 0:
                num_threes = n - num_fives
                print('trying num_threes=', num_threes)
                if num_threes % 5 == 0:
                    break
            num_fives -= 1
        else:
            return -1
        return int('5' * num_fives + '3' * num_threes)



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decent(3), 555)

    def test2(self):
        self.assertEqual(decent(5), 33333)

    def test3(self):
        self.assertEqual(decent(11), 55555533333)

    def test4(self):
        self.assertEqual(decent(1), -1)

    def testOneToTen(self):
        inputs = (1,2,3,4,5,6,7,8,9,10,)
        outputs = (-1, -1, 555, -1, 33333, 555555, -1, 55533333, 555555555, 3333333333)
        for i, o in zip(inputs, outputs):
            self.assertEqual(decent(i), o, 'failed i={0}, o={1}'.format(i, o))

    def testOneHundred(self):
        self.assertEqual(decent(100), 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553333333333)

if __name__ == '__main__':
    unittest.main()
