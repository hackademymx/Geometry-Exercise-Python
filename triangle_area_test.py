import geometry

def test_triangle_area_one():
    print('Triangle Area 3,2:')
    assert geometry.getTriangleArea(3,2) == 3

def test_triangle_area_two():
    print('Triangle Area 5,4:')
    assert geometry.getTriangleArea(5,4) == 10

def test_triangle_area_three():
    print('Triangle Area 10,10:')
    assert geometry.getTriangleArea(10,10) == 50

def test_triangle_area_four():
    print('Triangle Area 0,60:')
    assert geometry.getTriangleArea(0,60) == 0

def test_triangle_area_five():
    print('Triangle Area 12,11:')
    assert geometry.getTriangleArea(12,11) == 66