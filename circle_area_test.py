import geometry

def test_circle_area_one():
    print('Circle Area 3:')
    assert geometry.getCircleArea(3) == 28.27

def test_circle_area_two():
    print('Circle Area 12:')
    assert geometry.getCircleArea(12) == 452.39

def test_circle_area_three():
    print('Circle Area 27:')
    assert geometry.getCircleArea(27) == 2290.22

def test_circle_area_four():
    print('Circle Area 89:')
    assert geometry.getCircleArea(89) == 24884.56

def test_circle_area_five():
    print('Circle Area 91:')
    assert geometry.getCircleArea(91) == 26015.53