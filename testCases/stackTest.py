import unittest
from dataStructures import stack


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack_obj = stack.Stack()
        self.assertEqual(stack_obj.is_empty(), True)  # add assertion here
        stack_obj.add_item(1)
        stack_obj.add_item(2)
        stack_obj.add_item(3)
        stack_obj.add_item(4)
        print(stack_obj.__repr__())
        print(stack_obj.__doc__)
        self.assertEqual(stack_obj.get_stack(), [1,2,3,4])
        self.assertEqual(stack_obj.length(), 4)
        self.assertEqual(stack_obj.peek(), 4)
        stack_obj.remove_item()
        self.assertEqual(stack_obj.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
