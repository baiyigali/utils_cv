from unittest import TestCase

from utils_cv import utils_box


class Test_get_area(TestCase):
    def test_is_equal(self):
        area = utils_box.get_area([0, 0, 1, 1])
        self.assertEqual(area, 4)


class Test_box2poly(TestCase):
    def test_is_equal(self):
        poly = utils_box.box2poly([0, 0, 1, 1])
        self.assertEqual(poly, [0, 0, 1, 0, 1, 1, 0, 1])


class Test_boxes2bbox(TestCase):
    def test_is_equal(self):
        bbox = utils_box.boxes2bbox([[0, 0, 1, 1], [1, 0, 2, 1]])
        self.assertEqual(bbox.tolist(), [0, 0, 2, 1])
