#codewars homework!
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test cases
import codewars_test as test

@test.describe("Example tests")
def example_tests():
    
    @test.it('even_or_odd(1) should return "Odd"')
    def test_positive_odd():
        test.assert_equals(even_or_odd(1), "Odd")
        
    @test.it('even_or_odd(2) should return "Even"')
    def test_positive_even():
        test.assert_equals(even_or_odd(2), "Even")

    @test.it('even_or_odd(-1) should return "Odd"')
    def test_negative_odd():
        test.assert_equals(even_or_odd(-1), "Odd")
        
    @test.it('even_or_odd(-2) should return "Even"')
    def test_negative_even():
        test.assert_equals(even_or_odd(-2), "Even")
        
    @test.it('even_or_odd(0) should return "Even"')
    def test_zero():
        test.assert_equals(even_or_odd(0), "Even")

# To run the tests
if __name__ == "__main__":
    test.run()
