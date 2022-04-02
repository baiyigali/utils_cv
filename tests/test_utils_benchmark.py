from unittest import TestCase

from utils_cv import utils_benchmark
import pandas as pd


class Test_end2end(TestCase):
    def test_is_init_ok(self):
        from utils_cv.utils_benchmark import end2end

        df = pd.DataFrame(
            {
                "texts_gt": [["good", "good2"]],
                "texts_pd": [["good", "good2"]],
                "boxes_gt": [[[0, 0, 1, 1], [0, 0, 1, 1]]],
                "boxes_pd": [[[0, 0, 1, 1], [0, 0, 1, 1]]],
            }
        )
        p, r, f, df = end2end.benchmark(df)


class Test_text_detection(TestCase):
    def test_is_init_ok(self):
        from utils_cv.utils_benchmark import text_detection

        df = pd.DataFrame({"boxes_gt": [[0, 0, 1, 1]], "boxes_pd": [[0, 0, 1, 1]]})
        p, r, f, df = text_detection.benchmark(df)
