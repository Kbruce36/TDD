# test slightly bigger equation


def circle_area(radius):
    return 3.142 * radius**2


def test_area():
    assert circle_area(4) == 50.272
