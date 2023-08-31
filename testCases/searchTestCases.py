import unittest
from algorithms import linearSearch, binarySearch

test_cases = [
    # query occurs exactly in the middle
    {'input': {'search_space': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    # query occurs somewhere in the middle
    {'input': {'search_space': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    # query is the first element
    {'input': {'search_space': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    # query is the last element
    {'input': {'search_space': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    # search space contains just one element, query
    {'input': {'search_space': [6], 'query': 6}, 'output': 0},
    # search space does not contain query
    {'input': {'search_space': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    # search space is empty
    {'input': {'search_space': [], 'query': 7}, 'output': -1},
    # numbers can repeat in search space
    {'input': {'search_space': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    # query occurs multiple times
    {'input': {'search_space': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
]


class MyTestCase(unittest.TestCase):

    def test_linear_search(self):
        for case in test_cases:
            try:
                self.assertEqual(linearSearch.LinearSearch(**case['input']), case['output'])  # add assertion here
            except Exception as e:
                print(e, case['input'], 'LinearSearch')

    def test_binary_search(self):
        for case in test_cases:
            try:
                self.assertEqual(binarySearch.BinarySearch(**case['input']), case['output'])  # add assertion here
            except Exception as e:
                print(e, case['input'], 'BinarySearch')


if __name__ == '__main__':
    unittest.main()
