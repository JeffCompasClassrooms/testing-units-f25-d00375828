from circle import *

class TestCircle:
    
    def test_get_radius(self):
        c = Circle(5)
        assert c.getRadius() == 5

    def test_set_radius_zero(self):
        c = Circle(5)
        result = c.setRadius(0)
        assert result is True
        assert c.getRadius() == 0

    def test_set_radius_neg(self):
        c = Circle(10)
        result = c.setRadius(-2)
        assert result is False
        assert c.getRadius() == 10

    def test_set_radius_float(self):
        c = Circle(2)
        result = c.setRadius(7.4)
        assert result is True
        assert c.getRadius() == 7.4

    def test_area_special(self):
        c = Circle(2)
        assert c.getArea() == 0

    def test_area(self):
        c = Circle(3)
        result = math.pi * 3 * 3
        assert round(c.getArea(), 4) == round(result, 4)

    def test_circumference(self):
        c = Circle(2.5)
        result = 2 * math.pi * 2.5
        assert round(c.getCircumference(), 4) == round(result, 4)
        
