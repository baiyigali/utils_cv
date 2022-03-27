from unittest import TestCase

from utils_cv import utils_layout
from utils_cv.utils_layout import TextLineBuilder


class Test_line_builder(TestCase):
    def test_is_init_ok(self):
        utils_layout.TextLineBuilder()
