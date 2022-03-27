from unittest import TestCase

from utils_cv import utils_benchmark
from utils_cv.utils_benchmark import end2end
import pandas as pd


class Test_end2end(TestCase):
    def test_is_init_ok(self):
        df = pd.DataFrame(
            {"texts_gt": [["good", "good2"]], "texts_pd": [["good", "good2"]]}
        )
        p, r, f, df = end2end.benchmark(df)
