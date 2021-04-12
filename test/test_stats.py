import unittest
from assault.stats import Results


class TestStats(unittest.TestCase):
    def setUp(self):
        self.results_1 = Results(0, [])
        self.results_2 = Results(0, [{"time": 0, "status": 0}])
        self.results_3 = Results(0, [{"time": 0.0, "status": 0}])
        self.results_4 = Results(0, [{"time": 0.0000000, "status": 0}])
        self.results_5 = Results(
            1.0,
            [
                {"time": 1.0, "status": 200},
                {"time": 0, "status": 200},
                {"time": 0, "status": 200},
                {"time": 0, "status": 200},
            ],
        )
        self.results_6 = Results(
            8,
            [
                {"time": 1, "status": 200},
                {"time": 2, "status": 403},
                {"time": 2, "status": 300},
                {"time": 3, "status": 199},
            ],
        )
        self.results_7 = Results(
            59024.39,
            [
                {"time": 1000, "status": 200},
                {"time": 25000.88, "status": 299},
                {"time": 0.35, "status": 201},
                {"time": 33023.16, "status": 200},
            ],
        )
        self.results_8 = Results(
            0.01,
            [{"time": 0.005, "status": 200}, {"time": 0.005, "status": 200}],
        )

    def test_average(self):
        self.assertEqual(self.results_1.average(), 0)
        self.assertEqual(self.results_2.average(), 0)
        self.assertEqual(self.results_3.average(), 0)
        self.assertEqual(self.results_4.average(), 0)
        self.assertEqual(self.results_5.average(), 0.25)
        self.assertEqual(self.results_6.average(), 2)
        self.assertEqual(self.results_7.average(), 14756.097500000002)
        self.assertEqual(self.results_8.average(), 0.005)

    def test_slowest(self):
        self.assertEqual(self.results_1.slowest(), 0)
        self.assertEqual(self.results_2.slowest(), 0)
        self.assertEqual(self.results_3.slowest(), 0)
        self.assertEqual(self.results_4.slowest(), 0)
        self.assertEqual(self.results_5.slowest(), 1)
        self.assertEqual(self.results_6.slowest(), 3)
        self.assertEqual(self.results_7.slowest(), 33023.16)
        self.assertEqual(self.results_8.slowest(), 0.005)

    def test_fastest(self):
        self.assertEqual(self.results_1.fastest(), 0)
        self.assertEqual(self.results_2.fastest(), 0)
        self.assertEqual(self.results_3.fastest(), 0)
        self.assertEqual(self.results_4.fastest(), 0)
        self.assertEqual(self.results_5.fastest(), 0)
        self.assertEqual(self.results_6.fastest(), 1)
        self.assertEqual(self.results_7.fastest(), 0.35)
        self.assertEqual(self.results_8.fastest(), 0.005)

    def test_successful(self):
        self.assertEqual(self.results_1.successful(), 0)
        self.assertEqual(self.results_2.successful(), 0)
        self.assertEqual(self.results_3.successful(), 0)
        self.assertEqual(self.results_4.successful(), 0)
        self.assertEqual(self.results_5.successful(), 4)
        self.assertEqual(self.results_6.successful(), 1)
        self.assertEqual(self.results_7.successful(), 4)
        self.assertEqual(self.results_8.successful(), 2)

    def test_requests_per_minute(self):
        self.assertEqual(self.results_1.requests_per_minute(), 0)
        self.assertEqual(self.results_2.requests_per_minute(), 0)
        self.assertEqual(self.results_3.requests_per_minute(), 0)
        self.assertEqual(self.results_4.requests_per_minute(), 0)
        self.assertEqual(self.results_5.requests_per_minute(), 240)
        self.assertEqual(self.results_6.requests_per_minute(), 30)
        self.assertEqual(self.results_7.requests_per_minute(), 0)
        self.assertEqual(self.results_8.requests_per_minute(), 12000)

    def test_requests_per_second(self):
        self.assertEqual(self.results_1.requests_per_second(), 0)
        self.assertEqual(self.results_2.requests_per_second(), 0)
        self.assertEqual(self.results_3.requests_per_second(), 0)
        self.assertEqual(self.results_4.requests_per_second(), 0)
        self.assertEqual(self.results_5.requests_per_second(), 4)
        self.assertEqual(self.results_6.requests_per_second(), 0)
        self.assertEqual(self.results_7.requests_per_second(), 0)
        self.assertEqual(self.results_8.requests_per_second(), 200)


if __name__ == "__main__":
    unittest.main()
