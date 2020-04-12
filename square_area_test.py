import geometry

def test_square_area_one():
    print('Square Area 3:')
    assert geometry.getSquareArea(3) == 9

def test_square_area_two():
    print('Square Area 12:')
    assert geometry.getSquareArea(12) == 144

def test_square_area_three():
    print('Square Area 27:')
    assert geometry.getSquareArea(27) == 729

def test_square_area_four():
    print('Square Area 89:')
    assert geometry.getSquareArea(89) == 7921

def test_square_area_five():
    print('Square Area 91:')
    assert geometry.getSquareArea(91) == 8281