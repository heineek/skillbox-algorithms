from unittest import TestCase
from typing import Dict, List


from path import shortest_path_duration


class PathTest(TestCase):
    def test_path_duration(self):
        """Path to princess-frog."""

        cases = [
            # expected hours, plan
            (
                17,
                [
                    [0, 1, 5, 5, 1, 1, 2],
                    [1, 1, 5, 5, 1, 1, 1],
                    [1, 1, 8, 2, 2, 2, 1],
                    [8, 8, 8, 2, 2, 1, 1],
                    [8, 2, 2, 8, 1, 1, 0],
                ],
            ),
            (3, [[0, 1, 1], [1, 1, 1], [1, 1, 0]]),
            (6, [[0, 1, 5], [2, 8, 1], [2, 2, 0]]),
            (
                16,
                [[0, 1, 2], [1, 2, 5], [2, 5, 8], [5, 8, 0]],
            ),
            (
                54,
                [
                    [0, 1, 5, 5, 1, 1, 2, 1, 1, 5, 5, 2, 1, 2, 1, 1, 5, 5, 1, 1, 2],
                    [1, 1, 5, 5, 1, 1, 1, 1, 1, 5, 5, 2, 1, 1, 1, 1, 5, 5, 1, 1, 1],
                    [1, 1, 8, 2, 2, 2, 1, 1, 1, 8, 2, 2, 2, 1, 1, 1, 8, 2, 2, 2, 1],
                    [8, 8, 8, 2, 2, 5, 1, 8, 8, 8, 2, 2, 5, 1, 8, 8, 8, 2, 2, 1, 1],
                    [8, 8, 8, 2, 2, 1, 5, 8, 8, 8, 2, 2, 1, 5, 8, 8, 8, 2, 2, 1, 1],
                    [8, 8, 8, 2, 2, 5, 1, 8, 8, 8, 2, 2, 5, 1, 8, 8, 8, 2, 2, 1, 1],
                    [8, 8, 8, 2, 2, 1, 5, 8, 8, 8, 2, 2, 1, 5, 8, 8, 8, 2, 2, 1, 1],
                    [8, 8, 8, 2, 2, 1, 1, 8, 8, 8, 2, 2, 5, 1, 8, 8, 8, 2, 2, 1, 1],
                    [8, 8, 8, 2, 2, 1, 1, 8, 8, 8, 2, 2, 1, 5, 8, 8, 8, 2, 2, 1, 1],
                    [8, 8, 8, 2, 2, 1, 1, 8, 8, 8, 2, 2, 5, 1, 8, 8, 8, 2, 2, 1, 1],
                    [8, 2, 2, 8, 1, 1, 1, 8, 2, 2, 8, 1, 1, 0, 8, 2, 2, 8, 1, 1, 0],
                ],
            ),
        ]
        for i, (expected_hours, plan) in enumerate(cases):
            with self.subTest(case=i):
                self.assertEqual(shortest_path_duration(plan), expected_hours)
