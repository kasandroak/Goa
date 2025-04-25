#codewars 1.
def hero(bullets, dragons): return bullets >= dragons * 2


#codewars 2.
import codewars_test as test

def fake_bin(s):
    return ''.join('0' if int(d) < 5 else '1' for d in s)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]
        
        for exp, inp in tests:
            test.assert_equals(fake_bin(inp), exp)




#codewars 3.
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)