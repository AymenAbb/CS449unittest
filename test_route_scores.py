import trains
import unittest


class TestRouteScores(unittest.TestCase):

    def test_3_trains_should_return_4_points(self):
        score = trains.get_route_score(3)
        self.assertEqual(score, 4)

    def test_5_trains_should_return_double_points(self):
        score = trains.get_route_score(5)
        self.assertEqual(score, 10)
