from libraries import numeric

def test_gcd():
    assert(numeric.gcd(874, 1406) == 38)

def test_lcm():
    assert(numeric.lcm([330, 225]) == 4950)
    assert(numeric.lcm([330, 75, 450, 11, 37]) == 183150)

def test_number_of_divisors():
    assert(numeric.number_of_divisors(220) == 12)
