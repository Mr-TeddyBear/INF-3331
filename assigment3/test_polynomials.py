"""

"""
from polynomials import Polynomial
def test_polynomial():
    """ Testing if a Polynomial assetion at a given point is correct"""
    tol = 1e-8
    poly1 = Polynomial([1,2,2])
    evaluation_at_4,expected_value_4 = poly1(4),41
    msg_value = "Expected value at x=%g: %f, Calcualted value at x=%g: %f" % (4,expected_value_4,4,evaluation_at_4)
    assert (abs(evaluation_at_4-expected_value_4) < tol), msg_value

    """Testing function for adding and subtracting two Polynomials"""
    poly2 = Polynomial([2,5])
    expected_new_poly_sum = [3,7,2]
    expected_new_poly_sub = [-1,-3,2]
    sum_poly = (poly1+poly2)
    sub_poly = (poly1-poly2)
    msg_sum_poly = "Expected new polynom sum: %s, Calculated new polynom sum: %s" % (expected_new_poly_sum,sum_poly)
    msg_sub_poly = "Expected new polynom subtraction: %s, Calculated new polynom subtraction: %s" % (expected_new_poly_sub,sub_poly)
    assert (expected_new_poly_sum == sum_poly), msg_sum_poly
    assert (expected_new_poly_sub == sub_poly), msg_sub_poly

    """ Testing if the class returns the corrct degree of the polynom"""
    expected_degree = 2
    poly1 = Polynomial([1,2,3,0])
    returned_degree = poly1.degree()
    msg_degree = "Returned degree %i Expected Degree: %i" % (returned_degree,expected_degree)
    assert (expected_degree == returned_degree), msg_degree

    """ Testing if __repr__ works correctly"""
    expected_string = "1 + 2x + 3x^2"
    print_msg = "Retuned string do nat match expected string"
    assert (poly1.__repr__() == expected_string), print_msg

    """ Testing __mul__ method"""
    expected_new_poly_mul = [2,4,6,0]
    poly1 = Polynomial([1,2,3,0])
    new_mul_pol = poly1*2
    msg_mul = "Multiplaction did not return the expected polynimal. Expected: ",expected_new_poly_mul," Calculated: ", new_mul_pol
    assert (expected_new_poly_mul == new_mul_pol), msg_mul


test_polynomial()
